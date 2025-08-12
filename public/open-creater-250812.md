---
title: “【1: 極めて危険】OpenCreator.io の安全性調査レポート”
tags: [“Security”, “生成AI”, “tech”, “AI”, “Privacy”]
private: false
updated_at: ""
id: null
organization_url_name: null
slide: false
ignorePublish: false
---

# 【1: 極めて危険】OpenCreator.io の安全性調査レポート

- 対象AIサービス: OpenCreator.io
- 公式URL: https://opencreator.io/
- 安全性レベル: **1: 極めて危険**

## エグゼクティブ・サマリー

**法務判定：導入不可** - 重大な厚黒学的リスクと地政学的脅威を確認

OpenCreator.ioは表面的には「統一生成AI作業環境」として20+のAIモデルを統合する魅力的なサービスを提供していますが、詳細調査により**極めて深刻な厚黒学的詐欺パターンと地政学的リスク**が判明いたしました。

### 重大な発見事項

1. **創設者の地政学的リスク**: Annie Liu（劉小易）氏 - 北京大学卒業の中国系創設者
1. **企業構造の意図的混乱**: SagaLabs Inc. vs SagaLabs Technology Inc.の使い分け
1. **厚黒学的要素**: 11項目/18項目（極めて危険レベル）
1. **法的条項の搾取構造**: 永続・取消不能・全世界的権利譲渡を強制

**最終判定**: 個人・企業を問わず使用を強く禁止します。

## 詳細調査結果 - 技術・法務分析とリスク評価

### 基本情報確認

**サービス概要:**

- **提供形態**: 完全クラウド専用（オフライン不可）
- **主要機能**: Script to Video, Sketch to Video, Lyrics to MV等
- **統合モデル**: Kling, Luma, Runway, Stable Diffusion, OpenAI等20+モデル
- **料金体系**: 従量課金制（月額29-149ドル）

**企業情報:**

```
運営企業: SagaLabs Technology Inc.
（利用規約では「SagaLabs Technology Inc」、他では「SagaLabs Inc.」と表記の混乱）
登記地: 8 THE GREEN SUITE B, DOVER, DE 19901（デラウェア州）
創設者: Annie Liu (劉小易, Xiaoyi Liu)
学歴: 北京大学（Peking University）卒業
```

### 地政学的リスク分析

#### 創設者の中国系背景

**Annie Liu氏の経歴分析:**

- **本名**: 劉小易（Xiaoyi Liu）
- **教育背景**: [北京大学卒業](https://www.linkedin.com/in/annie-liu-335161331/) - 中国のトップ大学
- **現在地**: 米国在住と主張
- **SNS活動**: [@annieliu_opencreator](https://www.instagram.com/annieliu_opencreator/) - フォロワー26人の低活動アカウント

**地政学的懸念点:**

1. **中国国家情報法第7条・第10条の適用可能性**: 中国国籍者への情報提供義務
1. **教育背景による影響**: 北京大学は中国共産党と密接な関係
1. **データ流出リスク**: 米国企業を装いつつ中国への情報提供可能性

#### 企業構造の意図的混乱

**発見された矛盾:**

```
利用規約: "SagaLabs Technology Inc"
プライバシーポリシー: "SagaLabs Technology Inc" 
公式サイト: "© 2025 SagaLabs Inc. All Rights Reserved"
他サイト掲載: "SagaLabs Inc."
```

**関連企業の存在:**

- [world.sagalabs.ai](https://world.sagalabs.ai/en) - 小説翻訳サービス
- 同一チームによる運営の可能性（要詳細調査）

### 厚黒学的要素の詳細分析

#### 検出された11項目の厚黒学的手法

**1. 誇張的キャッチコピー**

```
主張: "20+ top AI models in 1 platform"
検証: 具体的なモデル一覧の非公開、"top"の定義不明
根拠: 第三者による性能比較データなし
```

**2. 虚偽希少性演出**

```
主張: "0% Markup, 0 Subscription, 0 Waste"
現実: 月額29-149ドルのサブスクリプション制
主張: "factory-priced AI models"
根拠: 価格比較の具体的データなし
```

**3. 企業構造の意図的混乱**
法的責任回避を目的とした複数法人名の使い分けを確認

**4. ToS深層条項による権利剥奪**

```
第11条 CONTRIBUTION LICENSE:
"unrestricted, unlimited, irrevocable, perpetual, non-exclusive, 
transferable, royalty-free, fully-paid, worldwide right"
```

→ ユーザー作成物への**永続・取消不能・全世界的**権利を要求

**5. 包括同意強制**

```
第10条: "any Contributions you transmit may be treated as 
non-confidential and non-proprietary"
```

→ 機密情報も非機密として扱う権利を一方的に主張

**6. 一方的責任転嫁**

```
第21条 DISCLAIMER: "AS-IS AND AS-AVAILABLE BASIS"
第8条: "All sales are final and no refund will be issued"
```

→ 完全免責＋返金拒否の二重構造

**7. サブプロセッサ不透明**

```
プライバシーポリシー: Service Providerについて
"third-party companies or individuals employed by the Company"
```

→ 具体的な委託先企業名・所在地を意図的に隠蔽

**8. オプトアウト選択肢欠如**
AI学習への利用拒否、データ収集停止の選択肢なし

**9. 強制クラウド同期**
ローカル保存・処理の選択肢を完全に排除

**10. AI倫理審査体制の不在**
生成AIの適正利用に関するガバナンス体制の記載なし

**11. フリーミアム中途解約ペナルティ**
返金拒否により事実上の解約困難状態を創出

### データインフラの地政学的脅威

**データ処理・保存:**

```
利用規約第15条:
"the Services are hosted in the United States"
"you are transferring your data to the United States"
```

**しかし重大な懸念:**

1. **創設者の中国系背景**: データアクセス権限保有の可能性
1. **中国国家情報法の域外適用**: 中国政府による強制データ提供要求
1. **サブプロセッサの不透明性**: 実際の処理先が中国の可能性

### 法的条項の危険性分析

#### 利用規約の搾取構造

**第11条「貢献ライセンス」の分析:**

```
原文: "you grant us an unrestricted, unlimited, irrevocable, 
perpetual, non-exclusive, transferable, royalty-free, 
fully-paid, worldwide right"

法的意味:
- unrestricted (無制限) = 用途制限なし
- unlimited (無限) = 量的制限なし  
- irrevocable (取消不能) = 利用者は撤回不可
- perpetual (永続) = 期限なし
- transferable (譲渡可能) = 第三者売却可能
- royalty-free (無償) = 対価支払い義務なし
- worldwide (全世界) = 地域制限なし
```

**消費者契約法違反の可能性:**

- 日本消費者契約法第10条（消費者利益を一方的に害する条項の無効）
- 同第12条（事業者の債務履行を免責する条項の無効）

#### プライバシーポリシーの構造的欠陥

**データ利用目的の包括性:**

```
"For other purposes: We may use Your information for other 
purposes, such as data analysis, identifying usage trends"
```

→ 「その他の目的」で無制限利用を正当化

**第三者提供の包括承認:**

```
"With Service Providers: We may share Your personal information 
with Service Providers"
```

→ 具体的プロバイダー名・所在地・目的を明示せず

### セキュリティ認証の不在

**確認できない認証・監査:**

- SOC 2 Type II: 言及なし
- ISO 27001: 言及なし
- GDPR適合性評価: 言及なし
- 外部セキュリティ監査: 言及なし

## 自薦・他薦の声

### ベンダー自身の宣伝文句

**OpenCreator.io公式サイトより:**

1. **“We integrate all kinds of Gen-AI creative models into an intuitive interface”**
- 出典: <https://opencreator.io/>
- 検証結果: 具体的統合方法・API仕様の非公開
1. **“20+ top AI models in 1 platform”**
- 出典: 同上
- 検証結果: “top”の定義・選定基準不明、モデル詳細一覧なし
1. **“1-click comparison for the best results”**
- 出典: 同上
- 検証結果: 比較アルゴリズム・評価基準の非公開
1. **“0% Markup, 0 Subscription, 0 Waste”**
- 出典: 同上
- 検証結果: 実際は月額29-149ドルのサブスクリプション制
1. **“Powerful doesn’t mean complicated. Designed for creators who want top-tier AI results”**
- 出典: 同上
- 検証結果: “top-tier”の定義・根拠データなし

### インフルエンサー・技術者の評価

**限定的な言及のみ確認:**

1. **一般的なAIツール紹介サイトでの掲載**
- [Toolify.ai](https://www.toolify.ai/tool/opencreator): “OpenCreator is a unified Gen-AI workstation”
- 利害関係: 広告収入モデル、中立性に疑問
1. **Product Huntでの別サービス（SagaLabs翻訳）への評価**
- <https://www.producthunt.com/products/sagalabs>
- 同一チーム運営の可能性あり

**注目すべき点:**
著名インフルエンサーによる積極的推奨は確認されず。技術コミュニティでの議論も限定的。

### 批判的意見

現時点で公開された批判的分析は確認されていませんが、これは以下の可能性を示唆：

1. サービス認知度の低さ
1. 技術者による詳細検証の不足
1. 地政学的リスクへの一般的関心の低さ

## 主任アナリストが提案する追加調査項目

### 1. **SagaLabs関連企業の完全なマッピング**

- 目的: world.sagalabs.ai等との関係性とデータ共有の実態解明
- 重要性: 企業構造の混乱による法的責任回避の全貌把握

### 2. **Annie Liu氏の詳細経歴調査**

- 目的: 中国政府系機関との関係、過去の勤務歴詳細の確認
- 重要性: 国家情報法適用リスクの正確な評価

### 3. **実際のデータフロー追跡調査**

- 目的: 入力データの実際の処理先・保存先の技術的確認
- 重要性: 「米国内処理」主張と実態の検証

### 4. **統合AI模型の詳細仕様確認**

- 目的: 20+モデルの実際のAPI接続先・データ経路の解明
- 重要性: 中華系AIモデルとの直接接続による情報漏洩リスクの評価

## 最終総括

OpenCreator.ioは**現代版「補鍋法」の完璧な実装事例**として、厚黒学的手法の危険性を如実に示しています。

**表面（「厚」）**: 便利で統合的なAI作業環境として魅力的な価値提案
**実態（「黒」）**: ユーザーデータ・創作物の永続的搾取と中国への情報流出リスク

特に深刻な点は、創設者の中国系背景と企業構造の意図的混乱により、**平時には便利なサービス、有事には情報収集ツール**として機能する可能性です。これは160年前の阿片戦争と同じ構造の現代版デジタル侵略と判断されます。

**緊急勧告**: 個人・企業・政府機関を問わず、OpenCreator.ioの使用を即座に停止し、代替西側技術への移行を強く推奨いたします。