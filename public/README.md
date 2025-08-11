---
title: "Qiita用フォルダ"
tags: ["qiita", "documentation", "readme"]
private: false
updated_at: "2025-08-11T00:00:00Z"
organization_url_name: ""
slide: false
---

# Qiita用フォルダ

このフォルダは、Qiita CLIを使用して記事を管理するためのものです。

## 使用方法

1. 記事ファイルを`public/`フォルダに配置
2. 各記事に適切なfront matterを設定
3. GitHubにpushすると自動的にQiitaに公開

## Front Matterの必須項目

- `title`: 記事のタイトル（文字列）
- `tags`: タグ（配列）
- `private`: 非公開設定（true/false）
- `updated_at`: 更新日時（文字列）
- `organization_url_name`: 組織名（文字列、個人記事の場合は空）
- `slide`: スライドモード（true/false）
