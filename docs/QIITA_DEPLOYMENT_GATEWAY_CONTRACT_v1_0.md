# QIITA_DEPLOYMENT_GATEWAY_CONTRACT v1.0

## 0. 位置づけ

本契約は、AIサービス信用調査Projectの **Phase 3（Qiita Writer）で確定した記事を、内容・判定値を再推論せずにQiita公開経路へ引き渡し、実公開結果を確認するための外部インターフェース契約** である。

```text
Phase 3
  ↓
Qiita Deployment Gateway
  ↓
umayado17/zenn-content / public/<slug>.md
  ↓
GitHub Actions / .github/workflows/publish.yml
  ↓
Qiita CLI / Qiita API
  ↓
Qiita
  ↓
.qiita-gateway/results/<request_id>.json
```

本契約はnote向けPhase 4 / Phase 5 Control Planeとは別系統である。

```yaml
schema: nk.qiita.deployment.contract.v1
version: v1.0
status: ready_for_adoption
```

`status: active` への切替は、本契約をProjectの現行INDEXへ登録し、MAIN / Project Instructionsの参照を更新し、GitHub側実装とNK006 current artifactが検証された後に行う。

---

## 1. 責務境界

### Phase 3 Writer

Phase 3は次を確定する。

- Qiita記事本文
- 記事タイトル
- Qiitaタグ
- slug候補
- NK安全性レベル / ラベル / 記事タイプ
- 信用調査判定
- 名目国 / 実質支配国
- 出典

Phase 3はGitHub commit、Qiita CLI/API、公開承認、item ID / URL生成、公開後状態判定を行わない。

### Qiita Deployment Gateway

Gatewayは次だけを担当する。

1. Phase 3成果物validation
2. current articleへの人間公開承認binding
3. deploy-ready front matterの決定論的生成
4. `public/<slug>.md` とrequest artifactのsubmission
5. GitHub Actions観測
6. Qiita remote reconciliation
7. publication result確定

Gatewayは本文、タイトル、タグ、評価値を再推論しない。

### GitHub Actions Publisher

GitHub Actionsはrequest validation、exact target articleのpublish、remote result確認、item ID書戻し、publication result生成、公開後通知だけを担当する。

---

## 2. 不変条件

1. Phase 3確定本文をGatewayが意味編集しない。
2. Phase 3完了は公開承認ではない。
3. current articleへbindingされた所長の明示的Qiita公開承認なしにpublication-triggering requestを作らない。
4. 承認後に本文・タイトル・タグ・action・既存item identityが変わった場合、旧承認は失効する。
5. GitHub Actions成功だけでQiita公開成功と断定しない。
6. Qiita item ID / URLはremote実値だけを使用し、推測しない。
7. remote side effectがUNKNOWNの場合、自動retryしない。
8. request artifactはimmutable / one-shotとする。訂正は新しいrequest IDを使う。
9. `publish_new` と `update_existing` を区別する。
10. note Phase 5のapproval/state/control artifactをQiitaへ流用しない。

---

## 3. Gateway request

標準path:

```text
.qiita-gateway/requests/<request_id>.json
```

標準形:

```json
{
  "schema": "nk.qiita.deployment.request.v1",
  "request_id": "<uuid>",
  "issued_at": "<RFC3339>",
  "action": "publish_new",
  "article": {
    "path": "public/<slug>.md",
    "source_body_sha256": "<sha256>",
    "rendered_file_sha256": "<sha256>",
    "title": "<title>",
    "tags": ["AI", "Security"]
  },
  "existing_article": null,
  "approval": {
    "actor_type": "human",
    "actor_id": "director",
    "approved_at": "<RFC3339>",
    "approved_rendered_file_sha256": "<sha256>"
  },
  "deployment": {
    "repository": "umayado17/zenn-content",
    "branch": "main",
    "workflow": ".github/workflows/publish.yml"
  }
}
```

`update_existing` の場合は `existing_article.repository_path` と `existing_article.qiita_item_id` を必須とし、front matterのcurrent `id` と一致させる。

### Preflight gate

最低限次を検証する。

- request schema / request filename一致
- action許可値
- article pathが `public/<slug>.md`
- title / tags存在
- rendered file SHA-256一致
- body SHA-256一致
- front matter title / tags一致
- `private: false` / `ignorePublish: false`
- `{{...}}`、`#実質支配国` 等の未展開内部値なし
- human approval存在
- approval hashがexact rendered fileへbinding
- repository / branch / workflow binding一致
- 同一commitでexact 1 request + exact 1 article markdownだけがpublication対象
- `publish_new` は既存article pathを上書きしない
- `update_existing` は既存path/item IDと一致

FAIL時はQiita side effectを開始しない。

---

## 4. Human publication approval

Gateway起動前に所長へcurrent articleのタイトル、タグ、新規/更新の別、本文または完成版への明確な参照を提示する。

公開承認として扱える例:

```text
この内容でQiitaに公開して
表示したQiita記事を現在の内容で公開してよい
このQiita記事を公開承認する
```

次は公開承認とみなさない。

```text
続けて
進めて
OK
いいよ
任せる
Phase 3へ進めて
記事を書いて
```

承認は次へbindingする。

```text
rendered file SHA-256
+ body SHA-256
+ title
+ tags
+ action
+ existing Qiita item identity（更新時）
```

---

## 5. GitHub submission

正式publication commitでは最低限次を同時に変更する。

```text
public/<slug>.md
.qiita-gateway/requests/<request_id>.json
```

Gateway modeでは単なる `public/**` pushだけを公開承認とみなさない。requestがないcommitはworkflowが起動してもpublish side effectを行わない。

一つのrequestで複数記事をpublishしない。

---

## 6. GitHub Actions Publisher

### Credential safety

- `QIITA_TOKEN`はGitHub Secretからのみ取得する。
- credentialsファイルやtokenをログ表示しない。
- publication resultへtokenを保存しない。

### Exact publish

requestにbindingされた1記事だけを `qiita publish` の対象とする。asset変更を理由に全記事publishしない。

### Replay protection

同じrequest IDのdurable resultがmainに存在する場合、automatic replayを拒否する。

writeback commitには新規requestを含めず、workflowが起動してもpublish side effectを行わない。

### Side-effect reconciliation

Qiita CLI実行前後にremote itemを確認し、exact title + body hash + expected item identityで既存side effectを検出する。

CLI失敗だけを理由にblind retryしない。

```text
exact remote item確認済み
  → PUBLISHED

remote side effect成立有無を確定できない
  → UNKNOWN
```

`UNKNOWN` は自動retry禁止とする。

---

## 7. Publication result

terminal artifact:

```text
.qiita-gateway/results/<request_id>.json
```

標準形:

```json
{
  "schema": "nk.qiita.publication_result.v1",
  "request_id": "<uuid>",
  "status": "PUBLISHED",
  "observed_at": "<RFC3339>",
  "source": {
    "deployment_commit_sha": "<git sha>",
    "workflow_run_id": "<run id>",
    "workflow_conclusion": "success",
    "article_path": "public/<slug>.md",
    "rendered_file_sha256": "<sha256>"
  },
  "qiita": {
    "item_id": "<observed item id>",
    "url": "<observed remote URL>",
    "title": "<observed title>"
  },
  "verification": {
    "frontmatter_item_id_present": true,
    "remote_item_confirmed": true,
    "approval_binding_match": true
  },
  "error": null
}
```

statusは `PUBLISHED / FAILED / UNKNOWN / CANCELLED` のみを使用する。

`PUBLISHED` は次をすべて満たした場合だけ成立する。

1. preflight PASS
2. exact approved articleだけを対象としている
3. front matterに実item IDが保存されている
4. Qiita remote itemを取得できる
5. remote title/body/item identityがapproval対象と一致
6. 実URLをremote responseから取得できる

GitHub Actionsの `conclusion=success` だけではPUBLISHEDとしない。

---

## 8. Failure / recovery

- validation failure: side effectを開始しない。
- GitHub submission failure: 未submitとして扱う。
- Qiita CLI前のfailure: remote side effectなしを確認できる場合のみFAILED扱い可。
- Qiita CLI開始後のfailure: remote reconciliationを行う。
- 確定不能: UNKNOWN。自動retry禁止。

request本文を修正して再送しない。訂正は新request IDを使用する。

---

## 9. Post-processing

GASその他通知はQiita publication successと分離する。

QiitaがPUBLISHEDで通知だけ失敗した場合、publication resultはPUBLISHEDのままとし、通知失敗をwarningとして扱う。

---

## 10. Core integration gate

本契約をactive化する前に次を満たす。

1. 本実装が `umayado17/zenn-content` mainへmerge済み。
2. Gateway unit tests PASS。
3. requestなしのpushでpublish side effectが発生しないことを確認。
4. preflight negative testがside effect前にFAILすることを確認。
5. NK006完全本文がDrive current artifactとして取得可能。
6. 本ContractをDrive正本へ登録。
7. MAIN / Project Instructions / INDEX新versionを作成・検証。
8. `CORE_CURRENT.yaml`をmaintenance transactionの最後に更新。

---

## 11. Production acceptance

新規Qiita記事1件で次を観測する。

```text
Phase 3確定
→ current article review提示
→ 明示Qiita公開承認
→ request生成
→ exact article + request commit
→ preflight PASS
→ Qiita publish
→ remote reconciliation
→ item ID writeback
→ publication result PUBLISHED
```

以下が一件でもあればacceptance FAILとする。

- 承認前publish
- Gatewayによる記事意味改変
- 別記事の意図しないpublish
- writebackによる再publish loop
- item ID / URL推測
- UNKNOWNへのblind retry
- durable resultなしで成功扱い

---

*Contract version: v1.0 (2026-08-15)*
