#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, sys
from datetime import datetime, timezone
from pathlib import Path

REQUEST_SCHEMA = 'nk.qiita.deployment.request.v1'
RESULT_SCHEMA = 'nk.qiita.publication_result.v1'
ACTIONS = {'publish_new','update_existing'}

def req(ok,msg):
    if not ok: raise ValueError(msg)
def hbytes(b): return hashlib.sha256(b).hexdigest()
def hfile(p): return hbytes(p.read_bytes())
def load(p):
    v=json.loads(Path(p).read_text(encoding='utf-8')); req(isinstance(v,dict),f'JSON root must be object: {p}'); return v
def dump(p,v):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def normpath(s):
    p=Path(s); req(not p.is_absolute() and '..' not in p.parts,'invalid repository-relative path')
    q=p.as_posix(); req(len(p.parts)==2 and p.parts[0]=='public' and q.endswith('.md'),'article.path must be public/<slug>.md'); return q

def splitfm(text):
    t=text.replace('\r\n','\n'); req(t.startswith('---\n'),'missing front matter')
    i=t.find('\n---\n',4); req(i>=0,'front matter not closed'); return t[4:i],t[i+5:]
def parsefm(front):
    out={}; lines=front.splitlines(); i=0
    while i<len(lines):
        line=lines[i]
        if line.startswith('title:'): out['title']=line.split(':',1)[1].strip().strip('"\'')
        elif line.startswith('id:'): out['id']=line.split(':',1)[1].strip().strip('"\'')
        elif line.startswith('private:'): out['private']=line.split(':',1)[1].strip().lower()=='true'
        elif line.startswith('ignorePublish:'): out['ignorePublish']=line.split(':',1)[1].strip().lower()=='true'
        elif line.startswith('tags:'):
            tags=[]; j=i+1
            while j<len(lines) and re.match(r'^\s+-\s+',lines[j]):
                tags.append(re.sub(r'^\s+-\s+','',lines[j]).strip().strip('"\'')); j+=1
            out['tags']=tags; i=j-1
        i+=1
    return out

def info(r):
    a=r.get('article') if isinstance(r.get('article'),dict) else {}; e=r.get('existing_article') if isinstance(r.get('existing_article'),dict) else None
    path=normpath(str(a.get('path','')))
    return {'request_id':r.get('request_id'),'action':r.get('action'),'article_path':path,'article_name':Path(path).stem,'title':a.get('title'),'tags':a.get('tags'),'rendered_file_sha256':a.get('rendered_file_sha256'),'source_body_sha256':a.get('source_body_sha256'),'existing_qiita_item_id':(e or {}).get('qiita_item_id') if e else None}

def validate(request_path,repo_root=Path('.'),changed=None):
    request_path=Path(request_path); repo_root=Path(repo_root); r=load(request_path)
    req(r.get('schema')==REQUEST_SCHEMA,'bad request schema'); rid=r.get('request_id'); req(isinstance(rid,str) and rid and request_path.stem==rid,'request_id mismatch')
    action=r.get('action'); req(action in ACTIONS,'bad action')
    a=r.get('article'); req(isinstance(a,dict),'article required'); path=normpath(str(a.get('path',''))); ap=repo_root/path; req(ap.is_file(),'article missing')
    title=a.get('title'); tags=a.get('tags'); req(isinstance(title,str) and title.strip(),'title required'); req(isinstance(tags,list) and tags and all(isinstance(x,str) and x.strip() for x in tags),'tags required')
    rs=a.get('rendered_file_sha256'); bs=a.get('source_body_sha256'); req(bool(re.fullmatch(r'[0-9a-f]{64}',str(rs))),'bad rendered SHA'); req(bool(re.fullmatch(r'[0-9a-f]{64}',str(bs))),'bad body SHA'); req(hfile(ap)==rs,'rendered SHA mismatch')
    front,body=splitfm(ap.read_text(encoding='utf-8')); fm=parsefm(front); req(fm.get('title')==title,'title mismatch'); req(fm.get('tags')==tags,'tags mismatch'); req(fm.get('private') is False and fm.get('ignorePublish') is False,'article must be public/publishable'); req(hbytes(body.encode())==bs,'body SHA mismatch'); req('{{' not in body and '}}' not in body and '#実質支配国' not in body,'unexpanded/internal placeholder')
    approval=r.get('approval'); req(isinstance(approval,dict) and approval.get('actor_type')=='human' and isinstance(approval.get('actor_id'),str) and approval.get('actor_id') and isinstance(approval.get('approved_at'),str) and approval.get('approved_at'),'human approval required'); req(approval.get('approved_rendered_file_sha256')==rs,'approval hash mismatch')
    d=r.get('deployment'); req(isinstance(d,dict) and d.get('repository')=='umayado17/zenn-content' and d.get('branch')=='main' and d.get('workflow')=='.github/workflows/publish.yml','bad deployment binding')
    e=r.get('existing_article')
    if action=='publish_new': req(e in (None,{}),'publish_new existing_article must be null'); req(not fm.get('id'),'new article id must be empty')
    else:
        req(isinstance(e,dict),'update_existing requires existing_article'); eid=e.get('qiita_item_id'); req(normpath(str(e.get('repository_path','')))==path and isinstance(eid,str) and eid and fm.get('id')==eid,'existing article identity mismatch')
    if changed is not None:
        c={Path(x).as_posix() for x in changed if x}; rp=request_path.relative_to(repo_root).as_posix(); req(path in c and rp in c,'request and article must change together'); req(len([x for x in c if x.startswith('.qiita-gateway/requests/') and x.endswith('.json')])==1,'exactly one request required'); req({x for x in c if x.startswith('public/') and x.endswith('.md')}=={path},'exactly one article markdown may change')
    return info(r)

def select_remote(i,items):
    found=[]
    for x in items:
        if not isinstance(x,dict): continue
        if i.get('existing_qiita_item_id') and x.get('id')!=i['existing_qiita_item_id']: continue
        if x.get('title')!=i['title'] or not isinstance(x.get('body'),str) or hbytes(x['body'].encode())!=i['source_body_sha256']: continue
        if not isinstance(x.get('url'),str) or not x['url'].startswith('https://'): continue
        found.append(x)
    req(len(found)<=1,'ambiguous exact remote match'); return found[0] if found else None

def bind_id(path,item_id):
    p=Path(path); front,body=splitfm(p.read_text(encoding='utf-8')); fm=parsefm(front); cur=fm.get('id') or ''; req(not cur or cur==item_id,'conflicting front matter id')
    lines=front.splitlines(); hit=False
    for n,line in enumerate(lines):
        if line.startswith('id:'): lines[n]=f'id: "{item_id}"'; hit=True; break
    req(hit,'front matter id missing'); p.write_text('---\n'+'\n'.join(lines)+'\n---\n'+body,encoding='utf-8')
def item_id(path): return parsefm(splitfm(Path(path).read_text(encoding='utf-8'))[0]).get('id') or ''

def status_for(i,remote,fmid,cli_rc):
    if remote:
        ok_id=isinstance(remote.get('id'),str) and remote.get('id') and (not i.get('existing_qiita_item_id') or remote['id']==i['existing_qiita_item_id']); ok_title=remote.get('title')==i['title']; ok_body=isinstance(remote.get('body'),str) and hbytes(remote['body'].encode())==i['source_body_sha256']; ok_fm=bool(fmid) and fmid==remote.get('id')
        if ok_id and ok_title and ok_body and ok_fm: return 'PUBLISHED',None
        return 'UNKNOWN',{'code':'REMOTE_MISMATCH','details':{'id':ok_id,'title':ok_title,'body':ok_body,'frontmatter_id':ok_fm,'cli_exit_code':cli_rc}}
    return 'UNKNOWN',{'code':'REMOTE_NOT_CONFIRMED_AFTER_CLI_SUCCESS' if cli_rc==0 else 'PUBLISH_SIDE_EFFECT_UNKNOWN','details':{'cli_exit_code':cli_rc}}

def result_obj(i,status,remote,commit,runid,error,fmid):
    q=None
    if status=='PUBLISHED': q={'item_id':remote['id'],'url':remote['url'],'title':remote['title']}
    return {'schema':RESULT_SCHEMA,'request_id':i['request_id'],'status':status,'observed_at':datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),'source':{'deployment_commit_sha':commit,'workflow_run_id':str(runid),'workflow_conclusion':'success' if status=='PUBLISHED' else 'failure','article_path':i['article_path'],'rendered_file_sha256':i['rendered_file_sha256']},'qiita':q,'verification':{'frontmatter_item_id_present':bool(fmid),'remote_item_confirmed':status=='PUBLISHED','approval_binding_match':True},'error':error}
def outputs(path,values):
    if not path:return
    with open(path,'a',encoding='utf-8') as f:
        for k,v in values.items(): f.write(f'{k}={json.dumps(v,ensure_ascii=False) if isinstance(v,list) else ("" if v is None else v)}\n')

# Compatibility aliases used by tests and the workflow package.
validate_request = validate
select_exact_remote = select_remote
bind_frontmatter_item_id = bind_id
evaluate_remote = status_for
split_front_matter = splitfm
parse_simple_front_matter = parsefm

def main():
    p=argparse.ArgumentParser(); s=p.add_subparsers(dest='cmd',required=True)
    a=s.add_parser('preflight'); a.add_argument('--repo-root',default='.'); a.add_argument('--request',required=True); a.add_argument('--changed-files'); a.add_argument('--github-output')
    a=s.add_parser('select-remote'); a.add_argument('--repo-root',default='.'); a.add_argument('--request',required=True); a.add_argument('--items-json',required=True); a.add_argument('--output')
    a=s.add_parser('bind-item-id'); a.add_argument('--article',required=True); a.add_argument('--item-id',required=True)
    a=s.add_parser('item-id'); a.add_argument('--article',required=True)
    a=s.add_parser('result'); a.add_argument('--repo-root',default='.'); a.add_argument('--request',required=True); a.add_argument('--remote-json'); a.add_argument('--cli-exit-code',type=int,required=True); a.add_argument('--commit-sha',required=True); a.add_argument('--workflow-run-id',required=True); a.add_argument('--github-output')
    x=p.parse_args()
    try:
        if x.cmd=='preflight':
            root=Path(x.repo_root).resolve(); rp=(root/x.request).resolve(); req(str(rp).startswith(str(root)),'request escapes repo'); changed=Path(x.changed_files).read_text().splitlines() if x.changed_files else None; i=validate(rp,root,changed); print(json.dumps(i,ensure_ascii=False)); outputs(x.github_output,i)
        elif x.cmd=='select-remote':
            root=Path(x.repo_root).resolve(); i=validate((root/x.request).resolve(),root); raw=json.loads(Path(x.items_json).read_text()); items=raw if isinstance(raw,list) else [raw]; m=select_remote(i,items)
            if not m:return 1
            dump(x.output,m) if x.output else print(json.dumps(m,ensure_ascii=False))
        elif x.cmd=='bind-item-id': bind_id(x.article,x.item_id)
        elif x.cmd=='item-id': print(item_id(x.article))
        else:
            root=Path(x.repo_root).resolve(); rp=(root/x.request).resolve(); r=load(rp); i=info(r); ap=root/i['article_path']; fmid=item_id(ap); remote=load(x.remote_json) if x.remote_json and Path(x.remote_json).exists() and Path(x.remote_json).stat().st_size else None; st,err=status_for(i,remote,fmid,x.cli_exit_code); obj=result_obj(i,st,remote,x.commit_sha,x.workflow_run_id,err,fmid); out=root/'.qiita-gateway/results'/f"{i['request_id']}.json"; dump(out,obj); vals={'result_path':out.relative_to(root).as_posix(),'publication_status':st}
            if obj['qiita']: vals|={'qiita_item_id':obj['qiita']['item_id'],'qiita_url':obj['qiita']['url'],'qiita_title':obj['qiita']['title']}
            outputs(x.github_output,vals); print(vals['result_path']); print(st)
        return 0
    except Exception as e: print(f'ERROR: {e}',file=sys.stderr); return 2
if __name__=='__main__': raise SystemExit(main())
