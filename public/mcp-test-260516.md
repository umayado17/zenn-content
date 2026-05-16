---
title: Zapier MCP経由commit疎通テスト(260516)
tags:
  - test
  - MCP
  - Claude
  - Zapier
private: true
updated_at: ''
id: ''
organization_url_name: null
slide: false
ignorePublish: true
---

## テスト目的

AI安全性評価プロジェクトにおいて、Claude が Zapier MCP 経由で `umayado17/zenn-content` の `public/` 配下に直接commitし、GitHub Actions の `publish.yml` ワークフローが正常に駆動するかを確認する。

## テスト構成

- commit実行者: Claude(Zapier MCP経由)
- リポジトリ: umayado17/zenn-content
- ブランチ: main
- パス: public/mcp-test-260516.md
- Front matter:
  - `private: true` (下書き相当)
  - `ignorePublish: true` (Qiita publish ステップをスキップ)
  - `id: ''` (新規記事として扱われる)

## 確認項目

1. ✅ commit が main に正常に反映されるか
2. ⏳ GitHub Actions `publish.yml` が起動するか(`public/**` パスフィルタによる)
3. ⏳ `ignorePublish: true` により Qiita publish ステップがスキップされるか
4. ⏳ front matter サニタイズ処理が正常動作するか(`id: null` → `id: ""` 変換等)
5. ⏳ GAS Webhook通知がスキップされるか(Qiita IDなしのため)

## 期待される動作

| ステップ | 期待結果 |
|---------|---------|
| commit反映 | ✅ 成功 |
| GitHub Actions起動 | ✅ 起動する(`public/**` 変更) |
| Sanitize front matter | ✅ 正常実行 |
| Detect changed markdowns | ✅ 本ファイルを検出 |
| Publish changed markdowns | ⚠️ `ignorePublish: true` でスキップ |
| GAS notification | ⚠️ Qiita IDなしのためスキップ |
| Commit & push back | ⚠️ IDなしのため書き戻し不要 |

## メインプロンプトv4.4への組み込み(想定)

Phase 3完了時の標準アクションに以下を追加する想定:

```
Phase 3完了
  ↓
Claude: Qiita CLI形式の.md(front matter付き)を生成
  ↓
Claude: Zapier MCP github_create_or_update_file で commit
        repo: umayado17/zenn-content
        path: public/<slug>-<YYMMDD>.md
        branch: main
  ↓
GitHub Actions (publish.yml): 自動駆動
  - npx qiita publish <basename>
  - Qiita公開、IDをfront matterに書き戻し
  - GAS Webhook通知
```

## 削除予定

テスト完了確認後、所長によりこのファイルは削除する。

---

*テスト実行日: 2026年5月16日*
*実行プロジェクト: AI安全性評価*
