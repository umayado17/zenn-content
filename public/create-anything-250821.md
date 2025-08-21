---
title: '【4: 安全】Anything AI（旧Create.xyz）の安全性調査レポート'
tags:
  - Security
  - AI
  - anything
  - privacy
  - nocode
private: false
updated_at: '2025-08-21T13:16:25+09:00'
id: 5b6d6612e619c33d50a1
organization_url_name: null
slide: false
ignorePublish: false
---

# 【4: 安全】Anything AI（旧Create.xyz）の安全性調査レポート

- 対象AIサービス: Anything（旧Create.xyz）
- 公式URL: https://www.create.xyz/
- 安全性レベル: 4/5（安全）

## エグゼクティブ・サマリー

Anything（旧Create.xyz）は、テキスト指示だけでウェブサイトやモバイルアプリを自動生成できるAIプラットフォームです。Stanford出身の創業者が率いる米国企業で、LinkedIn・Shopifyなどに投資実績を持つBessemer Venture Partnersから$8.5Mを調達している信頼性の高いサービスです。

- **法務判定**: 導入可（条件付き）
- **技術判定**: 安全
- **主要リスク**: 
  - 第三者AIモデルへのデータ共有
  - 企業機密情報の入力リスク
  - 無料プランでの機能制限

## 詳細調査結果

### 技術アーキテクチャ分析

**基盤技術**:
- フロントエンド: React.js自動生成
- バックエンド: PostgreSQLデータベース標準装備
- 外部API統合: Stripe、Google Maps、Slack、Discord等50+サービス
- AIモデル: GPT-4、Claude 3.5 Sonnet、Stable Diffusion等

**データフロー**:
```
ユーザー入力 → Create.xyzプラットフォーム → 第三者AIモデル → 生成結果
                     ↓
              米国サーバーで処理・保存
```

**技術的透明性**: ✅ 高
- 生成されたコードのリアルタイム表示
- ソースコードの編集・ダウンロード可能
- 使用技術スタックの明示

### 法的条項分析

**利用規約の重要条項**:

**セクション3.11（AI Tools）**:
> "By accessing and using the Services, you shall comply with the applicable terms of any Third Party Models and hereby consent and authorize Create to share Customer Data, including Prompts, with one or more Third-Party Models to the minimum extent required to complete your request."

**リスク**: 入力データが第三者AIモデル（OpenAI、Anthropic等）と共有される

**セクション3.12（Ownership of Output）**:
> "You are the owner of Customer Data, and we hereby assign to you all right, title and interest it may have, if any, in and to any Output."

**保護**: 生成されたコードの完全な所有権はユーザーに帰属

**プライバシーポリシー評価**:
- GDPR準拠の包括的なプライバシー保護
- データ削除権・修正権の保障
- 米国での適切なデータ保護措置

### 地政学的リスク評価

**運営企業**: Create, Inc.（米国カリフォルニア州サンフランシスコ）

**創業者背景**:
- **Dhruv Amin**: Stanford University MBA、元YouTube PM（2015-2017）、元Google APM（2014-2016）
- **Marcus Lowe**: 共同CEO
- **Mark Craemer**: 共同創業者

**投資家構成**:
- **リード投資家**: Bessemer Venture Partners（1911年創業の老舗VC）
- **投資実績**: LinkedIn、Shopify、Pinterest、Twilio等への投資
- **調達額**: 総額$8.5M（2025年8月最新ラウンド$5.5M）

**地政学的判定**: ✅ **信頼性極めて高い**
- 西側諸国の企業・投資家
- 透明性の高い経営陣
- 米国の法的管轄下

### 厚黒学的要素の検証

厚黒学的評価チェックリスト（18項目中）:

- [ ] 誇張的キャッチコピー - 実証的な機能説明
- [ ] "無料"条件の隠蔽 - 料金体系明確
- [ ] 導入実績の誇張 - 適切な事例紹介
- [x] フリーミアム中途解約ペナルティ - サブスクリプション途中解約時の返金なし
- [ ] オプトアウト選択肢欠如 - 退会・削除権利明記
- [x] 包括同意強制 - 第三者AIモデルへのデータ共有が包括的
- [ ] セキュリティ監査情報の非開示 - 適切な保護措置記載

**検出要素**: 2/18項目
**厚黒学的リスク**: 低

## 自薦・他薦の声

**あやみ（マーケティング）氏**:
> "「イベント用の投げ銭アプリ作って」の指示だけで、Stripe連携のアプリが作れた"

**利害関係分析**: 
- アフィリエイトリンクなし
- スポンサード表示なし
- 純粋な体験共有と判定

**SHIFT AI（木内翔太氏）**:
公式アンバサダーとして活動、利害関係を適切に開示

**技術コミュニティでの評価**:
- 日本のユーザーが全体の50%以上を占める
- 技術系イベントでの積極的なデモンストレーション
- オープンな技術仕様の公開

## 推奨対応

### 即座の対応
- **企業利用**: 条件付きで推奨
- **個人利用**: 安全に利用可能
- **注意事項**: 機密情報の入力は避ける

### 代替案
同等の安全性を持つ選択肢：
- **Replit**: 米国、オンラインIDE
- **StackBlitz**: 米国、ブラウザベース開発環境
- **Lovable**: 米国、AIアプリ開発プラットフォーム

### 監視項目
1. 第三者AIモデルとの契約変更
2. データ保存場所の変更
3. 投資家構成の変化
4. 利用規約の重要な改定

## 追加調査項目

1. **エンタープライズプランの詳細セキュリティ仕様** - より厳格な要件を持つ企業向けの追加保護措置
2. **SOC2・ISO27001等の認証取得状況** - 国際的なセキュリティ標準への準拠状況
3. **データ駐留化オプション** - EU・日本国内でのデータ処理選択肢
4. **監査ログ・アクセス制御機能** - 企業のコンプライアンス要件への対応
5. **競合他社との機能・セキュリティ比較** - より詳細なベンチマーク分析

## 最終総括

Anything（旧Create.xyz）は、信頼できる米国企業が運営する技術的に優秀なAIプラットフォームです。Stanford出身の経験豊富な創業者と、LinkedIn・Shopifyなどの成功企業に投資してきた老舗VCの支援により、健全な成長を続けています。

地政学的リスクは極めて低く、プライバシー保護も適切に実装されており、一般的な利用においては安全性に大きな懸念はありません。ただし、第三者AIモデルへのデータ共有という構造的特性上、機密性の高い企業情報の入力は避けるべきです。

技術者・法務担当者には、条件を理解した上での導入を推奨します。個人開発者や小規模チームにとっては、開発効率を大幅に向上させる価値の高いツールとして活用できるでしょう。

---

*調査時点: 2025年8月* 
*評価基準: AI安全性評価システム v3.2*
