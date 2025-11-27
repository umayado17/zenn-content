---
title: '【0: 使用不可】LALAL.AI 安全性調査レポート：バイオメトリクスデータをロシア企業に送る危険性'
tags:
  - Security
  - AI
  - Russia
  - privacy
  - GeopoliticalRisk
private: false
updated_at: '2025-11-28T01:13:59+09:00'
id: 807344c19cc6a0a0403f
organization_url_name: null
slide: false
ignorePublish: false
---

LALAL.AIは、AIを用いた音声分離サービスとして技術的に優れた性能を持つ一方、**ロシア国籍者が100%所有するスイス法人**という構造により、**極めて高いリスク**を抱えています。本レポートでは、企業構造、法的リスク、バイオメトリクスデータの重要性、そして代替案を詳細に分析します。

- 対象AIサービス: LALAL.AI
- 公式URL: [https://www.lalal.ai/](https://www.lalal.ai/)
- 安全性レベル: **0（使用不可）**
- 厚黒学レベル: **-15/18**
- 支配国名目国: **ロシア（スイス）**

## エグゼクティブ・サマリー

- **法務判定**: **導入不可** - バイオメトリクスデータ × ロシア法制下 × 契約信頼性ゼロ
- **技術判定**: **極めて危険** - 技術的優秀性がリスクを覆い隠す典型例
- **主要リスク**:
  - 音声 = 声紋 = 指紋・顔認証と同等のバイオメトリクスデータ
  - ロシア国籍者100%所有（法人はスイスだが実質支配は完全にロシア）
  - 2024年7月ロシア最高裁判決：契約より「公共政策」優先 → プライバシーポリシー無効化リスク
  - 中国企業型迂回構造（EU規制回避の意図的設計）
  - 代替サービス豊富 → リスクを取る必要性ゼロ

## 詳細調査結果

### 企業構造分析：決定的証拠

#### 法人情報
- **企業名**: OmniSale GmbH
- **所在地**: スイス連邦・ツーク州
- **登記番号**: CHE-134.049.565
- **資本金**: CHF 20,000（約340万円）

**出典**: [Moneyhouse - OmniSale GmbH](https://www.moneyhouse.ch/en/company/omnisale-gmbh-4998187031)

#### 株主構成（最重要）

**100%単独所有者**: Dmitry Orlov（**ロシア国籍**）

**署名権者**: Céline Nadine Inglin（スイス国籍、被用者、**持分なし**）
→ 現地代表に過ぎず、実質的支配者ではない

**外部投資家**: なし（完全ブートストラップ）

**出典**: [Moneyhouse - OmniSale GmbH](https://www.moneyhouse.ch/en/company/omnisale-gmbh-4998187031)

#### 中国企業型迂回構造との完全一致

```
ロシア国籍者（Dmitry Orlov）
    ↓
ドイツ居住（EU圏内だが法人なし）
    ↓
スイス法人（非EU）→ EU最厳格規制（GDPR）を回避
```

**目的**: 音声データ処理（バイオメトリクス）をスイス法人で行い、**EU規制を迂回**

**中国企業の典型的パターンとの類似性**:
```
中国国籍者
    ↓
米国/シンガポール法人
    ↓
国際市場展開
```

### 創業者背景：6年間のハイリスク国企業経験

#### Dmitry Orlov（ドミトリー・オルロフ）

**LinkedIn**: [https://www.linkedin.com/in/dorlow/](https://www.linkedin.com/in/dorlow/)

- **国籍**: ロシア連邦
- **現居住地**: Baden-Baden, Germany
- **学歴**: Linguistics University of Nizhny Novgorod（1999-2005）

#### 職歴（ハイリスク国企業6年間）

1. **2012-2013**: Wargaming.net（**ベラルーシ**）- SEM Team Lead
2. **2013-2018**: Gaijin Entertainment（**ロシア系**、War Thunder開発）- Senior Marketing Manager
3. **2018-現在**: InterPromo GmbH（ドイツ）- Managing Director
4. **2020-現在**: LALAL.AI/OmniSale GmbH（スイス）- Co-Founder & Managing Partner

**出典**: [Dmitry Orlov LinkedIn](https://www.linkedin.com/in/dorlow/)

**評価**: 
- ベラルーシ企業1年 + ロシア系企業5年 = **合計6年間のハイリスク国企業経験**
- マーケティング出身（技術者ではない）→ 「技術的優秀性」の演出に長ける

### バイオメトリクスデータの重要性

#### 音声 = 声紋 = 指紋・顔認証と同等

**特性**:
- 生涯ほぼ不変
- 個人識別可能
- 感情・健康状態識別可能
- AI音声合成（ディープフェイク）悪用リスク

**LALAL.AIが扱うデータ**:
- アップロードされた音声ファイル全体
- 分離前の「生声」データ
- 処理過程で抽出される声紋特徴

**リスク評価**: 
**指紋や顔写真を外国企業に送るのと同じレベルのリスク**

### 法的リスク評価：契約信頼性ゼロ

#### 1. 米国国務省警告（2024年2月23日）

**出典**: [US State Department - Russia Business Advisory](https://2021-2025.state.gov/russia-business-advisory/)

> "Russia's kleptocratic environment undermines fair competition and the rule of law"

（ロシアの寡頭支配的環境は公正な競争と法の支配を損なう）

#### 2. ロシア最高裁判決（2024年7月26日）

**出典**: [Morgan Lewis - Russia Limits Enforcement of International Arbitration Awards](https://www.morganlewis.com/pubs/2024/09/russia-limits-enforcement-of-international-arbitration-awards-rendered-by-unfriendly-arbitrators)

**事案**: ドイツ企業 vs ロシア企業（穀物供給契約）
- 仲裁地: ロンドン
- 準拠法: 英国法
- **判断内容**: 仲裁人が「非友好国」出身であることを理由に仲裁判断無効

**意味**: 
**契約より「公共政策」優先 = プライバシーポリシーの約束に法的拘束力なし**

#### 3. GAN Integrity報告（2024年10月）

**出典**: [GAN Integrity - Russia Country Profile](https://www.ganintegrity.com/country-profiles/russia/)

> "Corruption significantly impedes businesses... inconsistent application of laws"

**具体例**:
- 司法制度の政治化・腐敗
- 警察幹部の汚職
- ナワリヌイ氏毒殺・投獄

#### 4. 制裁回避実態（FinCEN分析、2023年9月）

**約10億ドルの制裁回避**（SAR報告ベース）

**手法**:
- 中国・香港・UAE・トルコ経由迂回
- 電子機器密輸

### プライバシーポリシー分析

**出典**: [LALAL.AI Privacy Policy](https://www.lalal.ai/privacy-policy/)

#### 主要条項

**学習利用**: Section 4
> "does not use user files for artificial intelligence training or other content"

**評価**: 
- この記述を信頼できるか？ → ロシア法制下では契約不履行リスク
- 2024年7月最高裁判決により、「公共政策」名目での約束破棄が可能

**データ保持期間**: 「必要な期間」（具体的日数なし、企業裁量）

**削除手順**: support@lalal.ai へメール依頼（自動化なし）

#### サブプロセッサ

**出典**: [Nudge Security - LALAL.AI Security Profile](https://security-profiles.nudgesecurity.com/app/lalal-ai)

- AWS（リージョン不明）
- Mailgun
- KeyCDN
- Google Analytics
- Facebook Pixel
- Intercom
- Hotjar

**評価**: 
- AWSリージョン不明 → データの物理的所在地不透明
- 複数の米国企業経由 → データフロー複雑化

#### 管轄法

- **VSTプラグイン版**: スイス法・ツーク州裁判所明記
- **Web版TOS**: 管轄法明記なし（**重大な欠陥**）

**出典**: [LALAL.AI Terms of Service](https://www.lalal.ai/terms-of-service/)

### 厚黒学的評価

#### ヌエ度: 10/10項目（完全な多重人格的構造）

- [x] 国籍・居住地・法人所在地が全て異なる
- [x] 公式発表と実際の言語使用に乖離
- [x] 学歴・職歴に隠蔽部分なし（だが解釈が必要）
- [x] 政治的発言を巧妙に回避
- [x] 複数のアイデンティティ使い分け（InterPromo/OmniSale）
- [x] 投資家・パートナー関係を隠蔽（2024年まで非公開）
- [x] 「技術者」だが開発実績不明（マーケティング出身）
- [x] メディアで核心質問を回避
- [x] 同族・関係企業での循環構造（InterPromo ⇄ OmniSale）
- [x] 危機時の責任転嫁準備（現地代表設置）

#### 厚黒学レベル: -15/18項目

**該当パターン**:

**1. 面従腹背戦略**: 
西側規制に「表面的に従う」（スイス法人・GDPR準拠）が実質回避

**2. 求官六字真言**: 
段階的信頼獲得（技術的優秀性 → 制裁対象外 → 安全イメージ）

**3. 補鍋法**: 
問題創出→解決独占（音声分離の「需要」を作り市場独占）

**4. 鋸箭法**: 
表面処理のみ（プライバシーポリシーは美しいが契約不履行リスク無視）

### Phase 2: インフルエンサー分析

#### 日本国内の状況

**主要推奨者**:
- ヨシダシゲル（音楽家・YouTuber）
- スタジオ翁（音楽制作者）
- 複数のAI情報ブログ

**出典**: 
- [ヨシダシゲル記事](https://yoshidashigeru.com/lalal-ai/)
- [スタジオ翁記事](https://studio-okina.com/lalal-ai/)

**共通パターン**:
- 「技術的優秀性」のみ強調
- プライバシーリスクへの言及**ゼロ**
- ロシア起源への言及**ゼロ**
- バイオメトリクスデータの重要性への言及**ゼロ**

#### アフィリエイトリンク疑惑

**LALAL.AI公式アフィリエイトプログラム**:
- **コミッション**: 30%
- **クッキー期間**: 180日（業界最長クラス）
- **最低支払額**: $150
- **管理者**: Dmitry Orlov直接管理

**出典**: [Post Affiliate Pro - LALAL.AI Affiliate Program](https://www.postaffiliatepro.com/affiliate-program-directory/lalal-ai-affiliate-program-2/)

**判定**: 
日本の推奨記事の多くがアフィリエイトリンク経由の可能性（明示なし）

#### 英語圏の状況

**Product Hunt（ユーザーレビュー）**:

**肯定的評価**:
- 技術的品質の高さ
- 使いやすさ

**否定的評価（重要）**:
```
「セキュリティが非常に基本的（very basic security）」
- アカウントハッキング事例（200分以上盗難）
- サポート対応の遅さ・不十分さ
```

**出典**: [Product Hunt - LALAL.AI Reviews](https://www.producthunt.com/products/lalal-ai/reviews)

#### 業界全体の「目眩まし」

**要因**:
- 技術的優秀性が全てを覆い隠す
- 「スイス法人」という表面的安心感
- ロシア起源情報の非開示
- セキュリティ評価サイトもロシアリスク未評価

## リスクシナリオ

### シナリオ1: 家族への圧力

ロシア国内の親族を人質に、政府がDmitry Orlov氏に協力を強要

### シナリオ2: 資産凍結脅迫

ロシア国内資産の接収を示唆し、データ提供を要求

### シナリオ3: 入国時拘束

ロシア訪問時に逮捕・尋問、データアクセス強制

### シナリオ4: 旧同僚経由接触

Wargaming/Gaijin時代の人脈を利用した間接的圧力

## 推奨対応

### 既存ユーザー（24時間以内）

#### 1. アカウント削除申請

- **宛先**: support@lalal.ai
- **件名**: "Account Deletion Request - GDPR Article 17"
- **本文**: 
  ```
  GDPR第17条（忘れられる権利）に基づき、
  私のすべての個人データの完全削除を要求します。
  ```

#### 2. 確認

- 削除完了通知を受領
- 処理パック購入者は返金不可（規約上）

### 企業

#### 1. 全社使用禁止通達

IT部門 → 全従業員への即座の通達

#### 2. 使用実態調査

- 誰が・いつ・何を処理したか
- 機密情報の流出可能性評価

#### 3. 代替サービス移行

下記参照

#### 4. インシデント記録

将来の監査用に記録保持

## 代替サービス情報

### オンライン系

#### 1. Moises.ai
- **国籍**: ブラジル発
- **URL**: [https://moises.ai](https://moises.ai)
- **特徴**: 2-5ステム分離、練習用機能充実
- **料金**: 無料版あり

#### 2. PhonicMind
- **URL**: [https://phonicmind.com](https://phonicmind.com)
- **特徴**: 音質重視、プレビュー無料
- **料金**: 従量課金

#### 3. AudioStrip
- **特徴**: 複数AIモデル選択可、プロ向け
- **料金**: サブスクリプション

⚠️ **注意**: Media.io Vocal Remover（Wondershare系、中国ルーツ注意）

### ローカル系（推奨）

#### 1. Spleeter
- **開発**: Deezer（フランス）
- **URL**: [https://github.com/deezer/spleeter](https://github.com/deezer/spleeter)
- **特徴**: オープンソース、Python+TensorFlow、自社運用可能
- **利点**: 完全ローカル処理、データ流出リスクゼロ

#### 2. Ultimate Vocal Remover (UVR)
- **URL**: [https://github.com/Anjok07/ultimatevocalremovergui](https://github.com/Anjok07/ultimatevocalremovergui)
- **特徴**: 複数モデルGUI、MITライセンス、完全ローカル処理
- **利点**: ユーザーフレンドリー、高品質

### 選択基準

- **プライバシー重視** → Spleeter + UVR（ローカル完結）
- **手軽さ優先** → Moises、PhonicMind（オンライン）
- **音質重視** → 複数サービス試用（曲ごとに最適化）

## リスク評価マトリックス

| 評価項目 | レベル | 根拠 |
|---------|--------|------|
| バイオメトリクスデータ | 最高 | 音声 = 声紋 = 指紋同等 |
| 法的管轄リスク | 最高 | ロシア国籍者100%所有 |
| 契約信頼性 | ゼロ | 2024年7月最高裁判決 |
| 規制回避意図 | 高 | 中国企業型迂回構造 |
| 代替案の存在 | 豊富 | Spleeter等の高品質代替 |
| 総合判定 | **使用不可** | リスク >> 利便性 |

## 技術者向けチェックリスト

- [ ] LALAL.AI使用の有無を確認
- [ ] 使用者リスト作成（誰が・いつ・何を）
- [ ] 機密音声データの処理有無
- [ ] アカウント削除申請の実施
- [ ] 代替サービスへの移行計画策定
- [ ] 社内ガイドライン更新（使用禁止明記）
- [ ] 従業員への周知徹底
- [ ] インシデント記録の作成

## 法務部門向けチェックリスト

- [ ] ロシア法制下のリスク評価
- [ ] GDPR違反可能性の検討
- [ ] 契約不履行リスクの文書化
- [ ] 代替サービスの法的適合性確認
- [ ] 使用禁止ポリシーの法的妥当性確認
- [ ] 将来的な訴訟リスクの評価
- [ ] データ保護監督機関への報告要否検討

## 最終総括

LALAL.AIは、**技術的には優秀**であるが、**地政学的リスクと法的不確実性**により、**あらゆる用途での使用を推奨できない**。

特に以下の3点が決定的：

1. **バイオメトリクスデータ**（音声 = 声紋 = 指紋・顔認証同等）
2. **ロシア国籍者100%所有**（スイス法人は名目のみ）
3. **契約信頼性ゼロ**（2024年7月ロシア最高裁判決で実証）

代替サービスが豊富に存在する現状では、**リスクを取る必要性は皆無**。

Spleeter、UVR等の**ローカル処理型オープンソースソリューション**への移行を強く推奨する。

---

## 参照情報源

### 公式
- [LALAL.AI公式サイト](https://www.lalal.ai/)
- [Privacy Policy](https://www.lalal.ai/privacy-policy/)
- [Terms of Service](https://www.lalal.ai/terms-of-service/)

### 企業情報
- [Moneyhouse - OmniSale GmbH](https://www.moneyhouse.ch/en/company/omnisale-gmbh-4998187031)
- [Dmitry Orlov LinkedIn](https://www.linkedin.com/in/dorlow/)
- [Nudge Security - LALAL.AI Security Profile](https://security-profiles.nudgesecurity.com/app/lalal-ai)

### 法的証拠
- [US State Department - Russia Business Advisory](https://2021-2025.state.gov/russia-business-advisory/)
- [Morgan Lewis - Russia Limits Enforcement of International Arbitration Awards](https://www.morganlewis.com/pubs/2024/09/russia-limits-enforcement-of-international-arbitration-awards-rendered-by-unfriendly-arbitrators)
- [GAN Integrity - Russia Country Profile](https://www.ganintegrity.com/country-profiles/russia/)

### ユーザーレビュー
- [Product Hunt - LALAL.AI Reviews](https://www.producthunt.com/products/lalal-ai/reviews)

### 日本語推奨記事
- [ヨシダシゲル記事](https://yoshidashigeru.com/lalal-ai/)
- [スタジオ翁記事](https://studio-okina.com/lalal-ai/)

### アフィリエイト情報
- [Post Affiliate Pro - LALAL.AI Affiliate Program](https://www.postaffiliatepro.com/affiliate-program-directory/lalal-ai-affiliate-program-2/)

---

**調査実施日**: 2025年11月27日  
**報告書バージョン**: Phase 3（Qiita技術記事）
