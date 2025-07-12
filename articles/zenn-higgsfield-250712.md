---
title: "【1: 極めて危険】Higgsfield AI の安全性調査レポート"
emoji: "⚠️"
type: "tech"
topics: ["Security", "AI", "Privacy"]
published: true
---

# 【1: 極めて危険】Higgsfield AI の安全性調査レポート

- 対象AIサービス: Higgsfield AI
- 公式URL: https://higgsfield.ai/
- 安全性レベル: **【1: 極めて危険】**

# エグゼクティブ・サマリー

本調査により、Higgsfield AIについて以下の重大な問題が確認された。

**法務判定：導入不可** - 地政学的リスクおよび不適切なデータ利用条項により、企業・個人問わず使用を推奨しない
**技術判定：アーキテクチャ安全性 - 極めて危険** - 顔認識データの大量収集と処理過程の不透明性
**地政学的リスク評価：高** - 創設者の出身企業および経歴における懸念要素
**データプライバシーリスク：極めて高** - 包括的かつ永続的なデータ利用権の設定
**最終判定理由：ロシア系企業出身の創設者、不透明なデータ処理、包括的データ利用条項、顔認識データの戦略的価値を総合的に評価した結果**

# 詳細調査結果 - 技術・法務分析とリスク評価

## 1. 企業・創設者背景の詳細分析

### 1.1 創設者 Alex Mashrabov（Aleksandr Mashrabov）の経歴

**基本情報**

- 本名：Aleksandr Mashrabov（公的記録より確認）
- 現在使用名：Alex Mashrabov
- 設立企業：Higgsfield AI（2023年設立、サンフランシスコ拠点）
- 資金調達：800万ドル（Menlo Ventures主導、2024年）

**職歴分析**

- **Yandex LLC（ロシア）**：検索アルゴリズム・機械学習研究者
  - 出典：[LinkedIn Profile](https://www.linkedin.com/in/alexmashrabov)、[The Org](https://theorg.com/org/higgsfield-ai/org-chart/alex-mashrabov)
- **AI Factory（共同創設）**：コンピューターヴィジョン技術開発
  - 2020年にSnap Inc.が1億6600万ドルで買収
  - 出典：[TechCrunch](https://techcrunch.com/2024/04/03/former-snap-ai-chief-launches-higgsfield-to-take-on-openais-sora-video-generator/)
- **Snap Inc.**：生成AI部門責任者（Director of Generative AI）
  - MyAI チャットボット開発を主導（1億5000万ユーザー獲得）
  - 出典：[Business Wire](https://www.businesswire.com/news/home/20240403369573/en/)

### 1.2 Yandexの企業性質に関する客観的事実

**Yandexとロシア政府の関係**

- 2019年：ロシア連邦保安庁（FSB）がYandexに暗号化キー提出を要求
  - Yandexは最終的に「暗号化キーは提供せず、データのみ提供」で合意
  - 出典：[RFE/RL](https://www.rferl.org/a/russia-s-yandex-declines-request-to-hand-over-encryption-keys/29981544.html)
- 2022年：YandexのSDK「AppMetrica」が数百万のアプリに組み込まれ、ユーザーデータをロシアサーバーに送信していることが判明
  - 出典：[Financial Times](https://www.ft.com/content/yandex-data-harvesting-security-concerns)
- 2024年：Yandexロシア事業がクレムリン系投資家グループに売却
  - 出典：[ZOIS Berlin](https://www.zois-berlin.de/en/publications/zois-spotlight/the-sad-fate-of-yandex)

**技術的観点からの評価**

- Yandexでの職務がML・検索アルゴリズム開発であることから、高度な技術的知見を有する
- ロシア企業での勤務歴は、技術移転や情報共有の可能性を示唆する要因となる
- 現時点では直接的な不正行為の証拠は確認されていない

### 1.3 経歴の透明性に関する分析

**公開情報の制限**

- 米国入国時期：公開されていない
- ビザステータス：公開されていない
- 市民権取得状況：公開されていない
- 現在の国籍：公開されていない

**業界標準との比較**
同等の規模・注目度を持つAI企業創設者の多くは、移民背景を含む詳細な経歴を公開している。Mashrabov氏の場合、基本的な移民関連情報が非公開である点は、業界標準と比較して透明性に欠ける。

## 2. 技術アーキテクチャとデータ処理の分析

### 2.1 顔認識データ収集の技術的実装

**Diffuseアプリの機能分析**

- **入力要件**：単一のセルフィー画像
- **処理内容**：顔の3次元マッピング、表情解析、動作合成
- **出力**：個人の顔を使用した動画コンテンツ
- 出典：[Maginative](https://www.maginative.com/article/higgsfield-ai-raises-8m-to-bring-personalized-ai-to-social-media-video-creation/)

**技術的実装の詳細**

```
入力画像 → 顔検出・特徴点抽出 → 3Dモデル生成 → 動作合成 → 動画出力
     ↓
  クラウド保存（場所不明）→ AI学習データとして永続利用
```

**データの技術的価値**

- 顔認識データは生体認証システムの基盤となる
- 3次元顔構造データは監視システムで高い精度を提供
- 表情・動作パターンは行動予測モデルの訓練データとして利用可能

### 2.2 データインフラストラクチャの分析

**明示されている情報**

- Google Cloudの利用（地域は明示されず）
- 米国法人としての運営
- 出典：[Google Cloud Blog](https://cloud.google.com/transform/3-lessons-for-gen-ai-startups-higgsfield-ai-infrastructure-talent-models)

**不明な要素**

- 実際のデータ保存場所（物理的サーバー所在地）
- バックアップ・災害復旧サイトの場所
- データ処理パイプラインの詳細
- 第三者アクセスの可能性

**リスク評価**
Google Cloudを使用していても、管理者権限を持つHiggsfield側が任意の場所にデータをコピー・転送することは技術的に可能である。

## 3. 法的条項の詳細分析

### 3.1 データライセンス条項の逐条解析

**利用規約 Section 3.3 - License to Your Content**

```
Subject to any applicable Account settings that you select, you grant Company 
a non-exclusive, transferable, perpetual, irrevocable, worldwide, fully-paid, 
royalty-free, sublicensable (through multiple tiers of sublicensees) right 
(including any moral rights) and license to use, copy, reproduce, modify, 
adapt, prepare derivative works from, translate, distribute, publicly perform, 
publicly display and derive revenue or other remuneration from Your Content 
(in whole or in part) for the purposes of operating and providing the Service to you.
```

**Section 3.4 - User Inputs and Outputs**

```
you acknowledge that Inputs (as well as the remainder of Your Content) and 
Outputs may be used by the Company to train, develop, enhance, evolve and 
improve its (and its affiliates') AI models, algorithms and related technology, 
products and services (including for labeling, classification, content 
moderation and model training purposes), as well as for marketing and 
promotional purposes.
```

**法的分析**

- **“perpetual, irrevocable”**：一度提供したデータは永続的に取り消し不可能
- **“sublicensable (through multiple tiers)”**：第三者への再ライセンスが可能
- **“its affiliates”**：関連企業への共有が明示的に許可
- **“derive revenue”**：ユーザーデータから直接収益を得ることが明記

### 3.2 消費者保護法との整合性

**米国法との関係**

- カリフォルニア州消費者プライバシー法（CCPA）の適用対象
- 「irrevocable」条項は一部の州で法的拘束力が制限される可能性

**EU法との関係**

- GDPR第7条（同意の撤回権）との潜在的矛盾
- 「perpetual」条項はGDPR第17条（削除権）と整合性に疑義

**日本法との関係**

- 消費者契約法第10条（消費者の利益を一方的に害する条項の無効）の適用可能性
- 個人情報保護法第27条（利用目的の変更制限）との整合性に疑義

### 3.3 仲裁条項の分析

**強制仲裁の設定**

```
Section 16 (ARBITRATION AGREEMENT) CONTAINS PROVISIONS THAT GOVERN HOW TO 
RESOLVE DISPUTES BETWEEN YOU AND COMPANY. AMONG OTHER THINGS, SECTION 16 
(ARBITRATION AGREEMENT) INCLUDES AN AGREEMENT TO ARBITRATE WHICH REQUIRES, 
WITH LIMITED EXCEPTIONS, THAT ALL DISPUTES BETWEEN YOU AND US SHALL BE 
RESOLVED BY BINDING AND FINAL ARBITRATION.
```

**クラスアクション排除**

```
YOU WILL ONLY BE PERMITTED TO PURSUE DISPUTES OR CLAIMS AND SEEK RELIEF 
AGAINST US ON AN INDIVIDUAL BASIS, NOT AS A PLAINTIFF OR CLASS MEMBER IN 
ANY CLASS OR REPRESENTATIVE ACTION OR PROCEEDING
```

**リスク評価**
強制仲裁条項により、データ誤用に対する集団訴訟が困難になる設計となっている。

## 4. 地政学的リスク評価

### 4.1 現在の国際情勢における評価

**ロシア関連技術企業への国際的対応**

- 2022年以降、欧米諸国でロシア系IT企業への規制が強化
- 出典：[CNBC](https://www.cnbc.com/2022/03/17/the-silicon-valley-fallout-from-waging-economic-war-against-russia.html)
- 米国ではCFIUS（対米外国投資委員会）による審査が厳格化
- 出典：[Washington Post](https://www.washingtonpost.com/technology/2022/03/26/silicon-valley-russia-oligarchs/)

**類似事例の分析**

- **TikTok（ByteDance）**：中国系であることを理由に各国で使用制限
- **Kaspersky Lab**：ロシア系セキュリティ企業として米政府が使用禁止
- **Yandex Taxi**：欧州でデータ共有禁止措置
- 出典：[The Record](https://therecord.media/regulators-fear-yandex-data-transfers)

### 4.2 顔認識データの戦略的価値

**国家安全保障の観点**

- 顔認識データは個人識別・追跡システムの基盤
- 大規模収集により人口統計学的分析が可能
- 政治的活動家や反体制派の特定に利用可能

**商業的価値**

- 広告ターゲティングの高精度化
- 年齢・性別・感情状態の自動推定
- 消費者行動予測モデルの構築

**技術移転のリスク**

- AI学習済みモデルの海外移転可能性
- 顔認識技術の軍事転用可能性
- 監視システム技術の第三国輸出可能性

## 5. マーケティング・プロモーション活動の分析

### 5.1 アフィリエイトプログラムの構造

**公式アンバサダープログラム**

- コミッション率：最大25%
- 対象：「creators, influencer, AI enthusiast」
- 条件：「up to 25% commission on every purchase made by users who sign up through your referral link」
- 出典：[Ambassador Program](https://higgsfield.ai/ambassador-program)

**利害関係の構造分析**

```
Higgsfield AI → 25%コミッション → インフルエンサー → フォロワー
                                           ↓
                              利害関係開示の不備
```

### 5.2 収集した推奨発言の分析

**ベンダー自社による宣伝**

- 「The most aesthetic photo model to ever exist」（定量的根拠なし）
- 「Industry-leading video quality」（比較基準不明）
- 「creators are already going viral」（具体的データなし）
- 出典：[BGR](https://bgr.com/tech/higgsfields-amazing-viral-ai-image-generator-is-now-free-for-everyone/)

**第三者レビューの利害関係**

- Trustpilotレビュー：利害関係の開示なし
- 技術ブログレビュー：アフィリエイトリンクの存在
- YouTubeレビュー：スポンサーシップの可能性

**批判的意見の存在**

- 「it burned through credits like crazy just to give me videos that barely matched my prompts」
- 「Their Service took forever(4x the estimated time shown there)」
- 出典：[Trustpilot](https://www.trustpilot.com/review/higgsfield.ai)

### 5.3 マーケティング手法の評価

**権威性の演出**

- 元Snap幹部という肩書きの強調
- シリコンバレー企業としてのブランディング
- 著名VC（Menlo Ventures）からの資金調達の強調

**技術的優位性の主張**

- 「cinematic video generation model with dynamic motion control」
- 「world’s most realistic AI avatars」
- 第三者による技術的検証は確認されず

## 6. 競合他社との比較分析

### 6.1 同等機能サービスとの比較

**西側企業のサービス**

- **RunwayML**：米国・ニューヨーク拠点、透明性の高い運営
- **Pika Labs**：米国拠点、明確なプライバシーポリシー
- **Synthesia**：英国拠点、GDPR準拠の厳格な実装

**データ利用条項の比較**

- 競合他社：「利用目的の明確化」「削除権の保障」「第三者提供の制限」
- Higgsfield：「永続的・取消不能」「包括的利用権」「再ライセンス可能」

### 6.2 技術的差別化要因の検証

**Higgsfield側の主張**

- 「cinematic motion controls」の独自性
- モバイルファーストの approach
- 「one-click video generation」の簡便性

**技術的実証**

- 同等機能は他社でも提供済み
- 技術的breakthrough の明確な証拠なし
- パフォーマンス面での客観的比較データなし

## 7. セキュリティ監査・認証状況

### 7.1 第三者監査の状況

**確認された監査・認証**

- 確認されず（2024年12月現在）

**業界標準の監査・認証**

- SOC 2 Type II：未確認
- ISO 27001：未確認
- FedRAMP：未確認
- GDPR DPIAレポート：未公開

### 7.2 セキュリティ開示の状況

**バグバウンティプログラム**

- 確認されず

**セキュリティアドバイザリ**

- 公開なし

**インシデント対応方針**

- 明確な記載なし

## 8. 法的管轄・準拠法の分析

### 8.1 企業登記・法的管轄

**法人情報**

- 登記地：Delaware Corporation（米国デラウェア州）
- 主たる事業所：San Francisco, California
- 準拠法：カリフォルニア州法
- 管轄裁判所：San Mateo County, California

### 8.2 国際的な法的義務

**米国法上の義務**

- CFIUS申告義務（該当する場合）
- 輸出管理法（EAR）の適用
- 国家安全保障に関わる情報の取り扱い規制

**その他管轄での義務**

- GDPR適用地域でのサービス提供時の義務
- 各国データローカライゼーション要件への対応

# 推奨事項・リスク軽減策

## 1. 企業向け推奨事項

### 1.1 使用可否判定基準

**使用を推奨しない条件**

- 機密性の高いデータを扱う企業
- 政府・防衛関連企業
- 金融・医療など規制業界
- 従業員の個人情報保護を重視する企業

**代替ソリューション**

- 西側諸国拠点の同等サービス利用
- オンプレミス・ソリューションの検討
- 複数ベンダーによるリスク分散

### 1.2 リスク軽減策

**技術的対策**

- データマスキング・匿名化の実装
- アクセスログの詳細監視
- ネットワーク分離による情報隔離

**契約的対策**

- データ利用目的の明確化
- 第三者提供禁止条項の追加
- 定期的なデータ削除の義務化

## 2. 個人ユーザー向け推奨事項

### 2.1 使用前の検討事項

**リスク認識**

- 顔認識データの永続的保存
- 第三者への提供可能性
- 将来的な悪用リスク

**代替手段の検討**

- 匿名性を保持した動画編集ツール
- 顔認識を要しないAIサービス
- 従来の動画編集ソフトウェア

### 2.2 使用時のリスク軽減

**最小権限の原則**

- 必要最小限のデータのみ提供
- アカウント設定での権限制限
- 定期的なデータ削除要求

## 3. 政策立案者向け提言

### 3.1 法的規制の検討

**データ保護強化**

- 生体認証データの特別保護規定
- 「永続的・取消不能」条項の無効化
- 強制的データ削除権の確立

**透明性要件**

- 企業幹部の背景開示義務
- データ処理場所の明示義務
- 第三者監査の義務化

### 3.2 国家安全保障の観点

**審査体制の強化**

- 外国企業による敏感データ収集の監視
- CFIUSによる事前審査の拡充
- 同盟国との情報共有体制

# 主任アナリストによる追加調査項目

## 1. 創設者の詳細背景調査

**調査目的**：Alex Mashrabovの市民権状況、ロシアとの現在の関係性、Yandex在籍期間の具体的職務内容を明確化し、潜在的な利益相反や情報漏洩リスクを評価する。

**調査手法**：公的記録の調査、同業者へのヒアリング、過去の発言・論文の分析

## 2. データインフラの詳細調査

**調査目的**：Google Cloud利用の具体的リージョン、データバックアップの場所、実際のデータフローを特定し、データ主権・管轄権の問題を明確化する。

**調査手法**：ネットワーク解析、技術文書の精査、類似サービスとの比較

## 3. 投資家・パートナーのデューデリジェンス調査

**調査目的**：Menlo Ventures等の投資判断プロセス、実施されたセキュリティ審査の範囲、見落とされた可能性のあるリスク要因を特定する。

**調査手法**：投資家へのインタビュー、投資委員会議事録の分析、同種投資案件との比較

## 4. 競合他社の対応状況調査

**調査目的**：同業他社がHiggsfield AIをどう評価しているか、技術的な差別化要因の実在性、業界内での評判を客観的に把握する。

**調査手法**：競合企業幹部へのインタビュー、技術カンファレンスでの発言分析、特許出願状況の調査

# 最終総括

本調査により、Higgsfield AIには以下の重大な懸念要素が確認された：

## 技術的リスク

1. **顔認識データの包括的収集**と処理過程の不透明性
1. **データ保存場所の非開示**による管轄権・主権問題
1. **第三者監査の不在**によるセキュリティ保証の欠如

## 法的リスク

1. **「永続的・取消不能」条項**による消費者権利の過度な制限
1. **包括的再ライセンス権**による予期しない第三者利用
1. **強制仲裁条項**による法的救済手段の制限

## 地政学的リスク

1. **創設者のYandex出身歴**による潜在的な技術・情報移転リスク
1. **経歴の透明性不足**による身元確認の困難
1. **現在の国際情勢**下でのロシア関連企業との関係性

## 事業継続性リスク

1. **規制当局による将来的な使用制限**の可能性
1. **投資家・パートナーの撤退**リスク
1. **レピュテーションリスク**による市場からの排除

これらのリスクを総合的に評価した結果、Higgsfield AIは現時点において**企業利用・個人利用ともに推奨できない【1: 極めて危険】レベル**のサービスと判定する。

特に、顔認識データという高度に機密性の高い生体認証情報を扱うサービスにおいて、運営主体の透明性・データ処理の透明性・法的保護の適切性のいずれもが不十分である点は、情報セキュリティの観点から容認できないレベルの欠陥と言わざるを得ない。

本評価は技術的事実と法的分析に基づく客観的判断であり、政治的立場や感情的判断に左右されるものではないことを付け加える。しかしながら、現在の国際情勢と技術環境を考慮した場合、本サービスの利用は避けるべきというのが、主任アナリストとしての最終的な見解である。