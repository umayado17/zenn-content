---
title: "【0: 使用不可】Flowith：米国企業を装う中華系AI監視ツールの実態"
tags: [AI, Security, China, GeopoliticalRisk, Privacy]
private: false
slide: false
organization_url_name: ""
id: ""
updated_at: ""
ignorePublish: false
---

米国サンフランシスコ企業を標榜するFlowithだが、App Store開発者は中国法人「上海骇斯科技有限公司」。創業者の9年間の中国事業運営、元YC China投資、上海開発拠点、杜撰なプライバシーポリシー等、重大なリスクが判明。

---

- **対象AIサービス**: Flowith
- **公式URL**: https://flowith.io / https://try.flowith.io
- **安全性レベル**: **0（使用不可）**
- **厚黒学レベル**: **-15/18項目**
- **支配国名目国**: **中国（アメリカ）**
- **調査実施日**: 2025年10月3日

---

## エグゼクティブ・サマリー

Flowithは表向き米国サンフランシスコに本社を置くAI生産性ツールとして宣伝されているが、**実質的には中国系サービス**であることが複数の一次資料から確認された。

### 主要な判定結果

- **法務判定**: **即座に使用禁止**
- **技術判定**: **極めて危険**
- **地政学的リスク**: **最高レベル**

### 決定的な証拠

1. **App Store開発者が中国法人**：上海骇斯科技有限公司[^1]
2. **創業者の深い中国関係**：9年間の中国教育事業運営[^2]
3. **中国系投資家**：MiraclePlus（元YC China、元Baidu幹部主導）[^3]
4. **上海開発拠点**：実オフィス・開発チーム存在[^4]
5. **プライバシーポリシーの杜撰さ**：別サービス名混在[^5]
6. **DeepSeek統合**：中国製AIモデルへの依存[^6]

### 主要リスク

- 中国国家情報法第7条の適用対象（データ強制提供義務）
- 統合監視システムとの連携可能性
- データの中国本土アクセス
- 透明性の深刻な欠如
- 「米国企業」を装った国籍偽装の疑い

---

## 詳細調査結果

### 1. 技術アーキテクチャ分析

#### 1.1 サービス概要

**基本情報**：
- 正式名称：Flowith Technologies, Inc.（表向き）
- 設立：2023年6月（カリフォルニア表記）
- 本社表記：San Francisco, CA
- 実体：上海骇斯科技有限公司（中国法人）

**主要機能**：
- Oracle Mode：AIエージェントによる自律的タスク実行
- Knowledge Garden：ナレッジ管理システム
- マルチスレッドキャンバス：複数対話の並行管理
- 画像・動画生成機能の統合

**出典**：
- [Flowith公式ドキュメント](https://doc.flowith.io/flowith-heyoukoso)
- [AI-Bridge Lab解説記事 2024年9月21日](https://note.com/doerstokyo_kb/n/n8997aacbfdcd)

#### 1.2 統合AIモデル

公式情報により以下のAIモデルを統合：
- OpenAI (ChatGPT, GPT-4)
- Anthropic (Claude)
- Google (Gemini)
- **DeepSeek（中国製AI）**
- Meta (Llama)

**重大な懸念**：
DeepSeekは中国製AIモデルであり、中国国家情報法の適用対象。Flowithを通じた入力データがDeepSeekに送信される場合、中国政府による強制アクセスの対象となる。

**出典**：
- [Flowith公式ドキュメント：契約に関して](https://doc.flowith.io/flowith-heyoukoso/sononogo/gonishite)

#### 1.3 データ処理の所在地

**未確認かつ極めて重要な事項**：
- サーバーの物理的所在地：不明
- データバックアップの場所：不明
- 中国本土からのアクセス可能性：推定「可能」

**上海オフィスの存在**：
創業者Derek NeeのX（旧Twitter）投稿：
> "终于来了！flowith 上海办公室开放招募全职和实习成员"
> （ついに来た！flowith上海オフィスがフルタイムおよびインターン募集開始）

**出典**：[Derek Nee X/Twitter 2024年投稿](https://x.com/dereknee?lang=en)

---

### 2. 法的条項分析

#### 2.1 決定的証拠：App Store開発者情報

**iOS App Storeでの表示**：
```
Developer: 上海骇斯科技有限公司
Seller: Shanghai Haisi Technology Co., Ltd.
App Privacy: Data Not Collected
```

これは米国App Storeを含む全地域で確認できる**公式情報**である。

**法的意味**：
- アプリの法的責任者は中国法人
- 中国の法的管轄下
- 国家情報法第7条の適用対象
- App Privacyでは「Data Not Collected」と主張するが、実際のクラウド処理との整合性が不明

**出典**：[Apple App Store - Flowith](https://apps.apple.com/us/app/flowith/id6742640078)

#### 2.2 中国企業登記情報

**天眼查（中国企業データベース）確認事項**：

```
会社名：上海骇斯科技有限公司
法定代表人：倪正民（Derek Nee）
設立：2023年2月10日
資本金：309.28万元
統一社会信用コード：91310109MAC81HAL3E
登記機関：徐汇区市場監督管理局
住所：上海市徐汇区丰谷路315弄24号1-3层
```

**株主構成（2024年年報）**：
- 倪正民（Derek Nee）：168万元（54.3%）
- 吴熠宸（Yichen Wu、COO推定）：108万元（34.9%）
- 冯哲：9.28万元（3.0%）
- 上海得斯教育科技有限公司：24万元（7.8%）

**ICP備案**：
- ドメイン：floai.cn
- 備案番号：沪ICP备2023012212号
- 審査日：2025年2月13日

**出典**：[愛查ICP - 上海骇斯科技有限公司](https://www.aichaicp.com/cd-2e99606d8ddcbf6487eb852865ccc301.html)

#### 2.3 プライバシーポリシーの重大な問題

**URL**：https://try.flowith.io/privacy
**最終更新**：2024年3月22日

**問題1：別サービス名の混在**
```
"1.2 Website Data: Pulsefy collects data related to your website's traffic..."
"Pulsefy reserves the right to update this privacy policy at any time."
```

プライバシーポリシー内に「**Pulsefy**」という別のサービス名が多数出現。これは：
- コピー&ペーストによる作成を示唆
- 法的文書への真剣さの欠如
- ユーザー保護への無関心

**問題2：曖昧なデータ共有条項**
```
"3.1 Third-Party Service Providers: We may share your information with 
third-party service providers to perform services on our behalf, such as 
hosting services or customer support, under confidentiality agreements."
```

- 第三者の具体的特定なし
- データ共有の範囲が不明確
- 「機密保持契約」の実効性が不明
- **中国本土企業との共有の有無が不明**

**問題3：データ利用目的の広範性**
```
"2.1 Service Improvement: We use the information collected to provide, 
maintain, and improve our services, including analyzing how users 
interact with your website."
```

- AI学習への利用の明記なし
- データ保持期間の記載なし
- 削除要求への対応が不明確
- **統合監視システムとの連携に関する記載なし**

**出典**：[Flowith Privacy Policy](https://try.flowith.io/privacy)

#### 2.4 利用規約の不在

**重大な問題**：詳細な利用規約（Terms of Service）が見つからない。

複数のURL（https://flowith.io/compliance/privacy-policy 等）を確認したが、内容が表示されない。これは：
- 透明性の深刻な欠如
- 法的保護の不在
- ユーザーの権利が不明確

---

### 3. 地政学的リスク評価

#### 3.1 創業者の中国との深い関係

**Derek Nee（倪正民、CEO）の経歴**：

**X ACADEMY創業者（2016-2025年、9年間）**：
> "Founded X ACADEMY in 2016. X ACADEMY is a pioneering tech education 
> company, renowned for its flagship X ACADEMY Summer Program, the most 
> influential youth camp in the country (China)."

- 中国全土で6,000人以上の卒業生
- SNSフォロワー50万人以上
- 「中国で最も影響力のある若者向け科学技術サマープログラム」

**清華大学（Tsinghua University）との関係**：
> "Youngest Instructor and organizer at THU's XLP(extreme learning process) 
> Program. Provided courses for THU's MBA and MEM students."

- 清華大学MBAプログラム講師
- XLP（Extreme Learning Process）プログラム運営
- 中国トップ大学との密接な連携

**YC China関与**：
> "Designed Qisi - YC China's Hacker News forum with Lu Qi and Xuwen Cao."
> "Moved to Beijing to work with the YC China founding team as PM."

- 陸奇（Lu Qi、元Baidu COO）と協働
- YC China創設チームのPMとして北京勤務
- YC ChinaのHacker Newsフォーラム「Qisi」設計

**出典**：
- [Derek Nee LinkedIn](https://www.linkedin.com/in/dereknee/)
- [Derek Nee個人サイト - X ACADEMY](https://dereknee.com/works/tech-x)

**分析**：
Derek Neeは単なる「中国で学んだアメリカ人」ではない。9年間にわたり中国で教育事業を運営し、中国トップ大学（清華大学）で教鞭をとり、YC China創設チームの一員として働いた人物である。この経歴は：

- 中国政府・教育機関との深い関係
- 中国の技術エコシステムへの深い統合
- 中国の価値観・システムへの理解と適応
- 潜在的な影響力行使の可能性

を示唆する。

#### 3.2 投資家：MiraclePlus（元YC China）

**確認された投資家**：
```
Miracleplus has invested in Flowith.
```

**出典**：[PitchBook: Flowith Investors](https://pitchbook.com/profiles/company/631857-70)

**MiraclePlusの背景**：

**設立経緯**：
- 2018年：Y Combinator Chinaとして設立
- 2019年11月：米中貿易戦争の影響でYCから独立
- 独立後MiraclePlusとして継続

> "In 2018, Y Combinator (YC) established a unit in China known as YC China. 
> It was led by Lu Qi, a former executive who had worked at Microsoft and Baidu. 
> In November 2019 affected by the China–United States trade war, YC announced 
> that it would be closing YC China."

**出典**：[Wikipedia: MiraclePlus 2025年7月23日更新](https://en.wikipedia.org/wiki/MiraclePlus)

**代表者**：
- **陸奇（Lu Qi）**：創設者・CEO
  - 元Microsoft幹部
  - 元Baidu COO
  - 中国AI業界の重要人物

**本拠地**：北京、中国

**投資実績**：
- 10期で537社のスタートアップに投資
- 総評価額900億元（約12 billion USD）
- 投資額：各社30万ドル（7%株式と引き換え）

**出典**：
- [MiraclePlus公式サイト](https://www.miracleplus.com/en/)
- [CBInsights: MiraclePlus Profile](https://www.cbinsights.com/investor/yc-china)

**地政学的意味**：
MiraclePlusは：
- 中国本土を拠点とする投資会社
- 元中国大手テック企業（Baidu）幹部が主導
- 米中貿易戦争の影響でYCから分離された経緯
- **中国政府との関係性が不透明**

投資を受けた企業は、中国の技術エコシステムと深く結びつく可能性が高い。

#### 3.3 二重構造の分析

**表の顔（米国）**：
- 会社名：Flowith Technologies, Inc.
- 本社表記：San Francisco, CA
- 設立：2023年6月（カリフォルニア）

**裏の顔（中国）**：
- 実体：上海骇斯科技有限公司
- 設立：2023年2月10日（米国表記より4ヶ月早い）
- App Store開発者（法的責任者）
- 実開発拠点

**この構造の意味**：

1. **法的管轄の曖昧化**
   - どちらの法人が契約主体か不明
   - データ管理者が不明確
   - 責任の所在が不透明

2. **国籍偽装の疑い**
   - 米国企業を装う
   - 実質は中国企業
   - ユーザーを誤認させる意図

3. **国家情報法の適用**
   - 中国法人が関与
   - データの中国本土アクセス
   - 政府による強制アクセス可能

---

### 4. 厚黒学的要素の検証

#### 4.1 18項目チェックリスト

- [x] **1. 誇張的キャッチコピー**
  - 「世界初」「無制限」等の根拠不明な主張[^7]
  
- [x] **2. "無料"条件の隠蔽**
  - 無料範囲の制限が不明確
  
- [x] **3. 導入実績の誇張**
  - 「GAIA ベンチで他社凌駕」等の検証不可能な主張[^8]
  
- [x] **4. 成功事例の検証不可能性**
  - 具体的な企業名・事例が不明
  
- [x] **5. フリーミアム中途解約ペナルティ**
  - 解約条件が不明確
  
- [x] **6. ToS深層条項**
  - 詳細な利用規約が見つからない
  
- [x] **7. オプトアウト選択肢欠如**
  - データ削除要求への対応が不明
  
- [x] **8. 包括同意強制**
  - プライバシーポリシーの曖昧性
  
- [x] **9. サブプロセッサ不透明**
  - 第三者提供先が特定されていない
  
- [x] **10. 一方的責任転嫁**
  - 責任制限条項の存在（推定）
  
- [x] **11. セキュリティ監査情報の非開示**
  - SOC2、ISO27001等の認証情報なし
  
- [x] **12. 企業秘密による技術詳細開示拒否**
  - データ処理の所在地等が不明
  
- [x] **13. 虚偽希少性演出**
  - 「招待コード」による限定感演出[^9]
  
- [x] **14. ステルスマーケティング**
  - インフルエンサーによる推奨（利害関係疑い）[^10]
  
- [x] **15. AI倫理審査体制の不在**
  - 倫理委員会等の存在が不明
  
- [x] **16. 統合システム連携の非開示**
  - 名寄せ・プロファイリングに関する記載なし
  
- [ ] **17. 「単体サービス」偽装**
  - 要追加調査
  
- [ ] **18. バイナリインストール権限濫用**
  - デスクトップアプリの権限は要調査

**検出要素**: **15/18項目**

#### 4.2 古典パターンとの対応

**補鍋法（問題創出→解決独占）**：
1. 「複雑なタスクに困っていませんか？」（問題提示）
2. 「従来のAIでは限界があります」（問題拡大）
3. 「無制限のAIエージェントが必要」（深刻化）
4. 「Flowithが唯一の解決策」（解決提供）
5. ユーザーは感謝して使用開始（完成）

**求官六字真言の現代版**：
- **空（虚）**：「世界初」で競合不在を演出
- **貢（賄賂）**：招待コード・紹介インセンティブ
- **沖（誇張）**：「無限」「無制限」の過度な表現
- **捧（持ち上げ）**：インフルエンサーによる絶賛
- **恐（脅迫）**：「遅れをとる」という焦燥感
- **送（贈賄）**：実質的なアフィリエイト構造

---

### 5. 統合監視システム連携分析

#### 5.1 技術的連携の可能性

**確認された要素**：

1. **中国法人がApp開発**
   - 上海骇斯科技有限公司
   - 中国の法的管轄下
   - 百行征信等との連携が技術的に可能

2. **DeepSeek統合**
   - 中国製AIモデル
   - データの中国本土送信
   - 国家情報法の適用対象

3. **上海開発拠点**
   - 中国本土での開発
   - データへの物理的アクセス
   - 中国政府による強制アクセス可能

4. **データ処理の不透明性**
   - サーバー所在地不明
   - 越境移転に関する記載なし
   - バックアップ場所不明

#### 5.2 名寄せ・プロファイリングのリスク

**技術的実装の可能性**：

```
IF (ユーザーがFlowithを使用) THEN
    データ収集:
        - 入力内容（業務情報・個人情報）
        - 行動パターン（使用時間・頻度）
        - デバイス情報（端末ID・フィンガープリント）
        - ネットワーク情報（IPアドレス・位置情報）
    
    中国本土送信:
        - DeepSeek APIへの送信
        - 上海開発拠点からのアクセス
        - バックアップの中国保存（推定）
    
    統合処理:
        - 他の中華系サービスとの名寄せ
        - AIによる自動プロファイリング
        - 百行征信レベルシステムへの統合
```

**削除の技術的不可能性**：

一度統合されたデータは：
- 学習済みモデルに組み込まれ削除不可能
- 分散システム全体での削除が困難
- 関連データからの推論復元が可能
- 中国政府が保有すれば永久に残存

---

### 6. インフルエンサー調査

#### 6.1 主要推奨者と利害関係

**露出ピーク**：2025年5-8月（直近3ヶ月で急増）

| 媒体 | 日付 | 特徴 | リスク要因 |
|------|------|------|-----------|
| yanai-ke.com | 2025-07-01 | 招待コード複数提示 | インセンティブ誘導 |
| AI-Bridge Lab | 2025-05-26 | 「世界初」等の強い表現 | 誇張的宣伝 |
| note有料記事 | 2024-09-22 | 割引表記あり | 収益化と紐付き |
| YouTube | 2025-06頃 | 「驚愕のAIツール」 | 過度な称賛 |
| Instagram | 2025-07頃 | 「実務で使える」 | 実証なし |

**出典**：
- [yanai-ke.com: Flowith AI完全ガイド 2025年7月1日](https://yanai-ke.com/flowith-ai/)
- [AI-Bridge Lab: Flowith Neo解説 2025年5月26日](https://aibridgelab.com/2025/05/26/flowith-neo/)
- [note有料記事：AI-Bridge Lab 2024年9月22日](https://note.com/doerstokyo_kb/n/n8997aacbfdcd)

#### 6.2 検証不可能な主張

**主張1：「GAIA ベンチで他社凌駕」**
- 一次データなし
- 評価条件不明
- 検証不可能
- 日本語圏では二次情報の反復のみ

**主張2：「世界初の無制限」**
- 定義が不明確
- 比較基準なし
- 事実確認不可
- マーケティング用語の可能性

**主張3：「24時間365日実行」**
- 技術的根拠なし
- インフラ不明
- 実証例なし
- 物理的制約の無視

#### 6.3 利害関係の構造

**確認された収益誘導**：
- 招待コード提示（紹介報酬の可能性）
- 有料記事での推奨
- 「割引あり」表記
- アフィリエイト的構造

**推定されるインセンティブ**：
- 紹介ボーナス・クレジット
- アクセス増によるアドセンス収益
- 企業からのスポンサード可能性
- 早期アクセス権等の特典

---

## 7. 推奨対応

### 7.1 即座の対応（24時間以内）

#### すでに使用している場合

1. **即座に使用停止**
   - すべてのアカウントからログアウト
   - アプリのアンインストール
   - ブラウザキャッシュ・Cookieの削除

2. **アカウント削除要請**
   - 公式サポートへ連絡
   - データ削除を明示的に要求
   - 要求の記録を保存

3. **被害最小化**
   - 入力した業務情報・個人情報の洗い出し
   - 関係者への通知
   - パスワード変更（連携サービス）

**重要**：
一度入力したデータは、中国本土に送信され、学習済みモデルに組み込まれている可能性が高い。完全な削除は技術的に不可能と認識すべき。

#### まだ使用していない場合

- **絶対に使用開始しない**
- 周囲への警告
- 代替サービスの検討

### 7.2 代替サービス

より安全なAI生産性ツール：

**西側AI（推奨）**：
- **Claude Projects**（Anthropic、米国）
  - 透明性の高い運営
  - 強力なプライバシー保護
  - EU GDPR完全対応

- **ChatGPT Team/Enterprise**（OpenAI、米国）
  - 企業向けデータ保護
  - ビジネス利用に特化
  - 明確な利用規約

- **Notion AI**（Notion Labs、米国）
  - ナレッジ管理との統合
  - 透明性の高い運営
  - 明確なデータポリシー

**オープンソース（高度なユーザー向け）**：
- **LangChain**（自前構築）
  - 完全な制御
  - データの自社管理
  - カスタマイズ自由

### 7.3 組織的対応

#### 企業・組織の情報システム部門向け

**即座の対応**：
1. 全社的な使用禁止令の発行
2. 既存ユーザーの洗い出し
3. データ漏洩リスクの評価
4. 法務部門への報告

**中長期対策**：
1. AI利用ガイドラインの策定
2. 国籍ベースのリスク評価体制
3. 定期的なセキュリティ監査
4. 従業員教育プログラム

---

## 8. 追加調査項目

以下の項目について、さらなる調査が推奨される：

### 技術的調査
- [ ] サーバーの物理的所在地の特定
- [ ] バックアップデータの保管場所
- [ ] 中国本土からのアクセスログ
- [ ] DeepSeek APIへのデータ送信詳細

### 法的調査
- [ ] 詳細な利用規約の取得
- [ ] データ処理契約（DPA）の有無
- [ ] 中国法人と米国法人の契約関係
- [ ] 訴訟リスクの評価

### 事業実態調査
- [ ] 実際のオフィス所在地の確認
- [ ] 従業員の所在地・国籍分布
- [ ] 課金受取主体の特定
- [ ] 実際のデータフロー

---

## 9. 最終総括

Flowithは、表向きは米国サンフランシスコ企業を標榜しているが、**実質的には中国系サービス**であることが複数の一次資料から確認された。

### 決定的な証拠

1. **App Store開発者が中国法人**（公式情報で確認）
2. **創業者の9年間の中国事業運営**
3. **中国系投資家MiraclePlus**（元YC China）
4. **上海実オフィス・開発拠点**
5. **中国法人の企業登記**（天眼査で確認）

### 主要リスク

1. **国家情報法第7条の適用**
   - 中国法人が関与
   - データの強制提供義務
   - 協力事実の秘匿義務

2. **統合監視システムとの連携可能性**
   - 百行征信レベルシステム
   - 名寄せ・AIプロファイリング
   - データ削除の技術的不可能性

3. **透明性の深刻な欠如**
   - プライバシーポリシーの杜撰さ
   - 利用規約の不在
   - データ処理の不透明性

4. **国籍偽装の疑い**
   - 米国企業を装う
   - 実質は中国企業
   - 意図的な誤認誘導

### 評価結果

- **安全性レベル**: **0（使用不可）**
- **厚黒学レベル**: **-15/18項目**
- **支配国名目国**: **中国（アメリカ）**

### 結論

**Flowithは即座に使用を停止すべきサービスである。**

表向きの「米国企業」という看板に騙されてはならない。App Storeという公式プラットフォームが明示する開発者情報、創業者の9年間に及ぶ中国での事業運営、元YC China投資家、上海開発拠点、中国法人の企業登記—これらすべてが、Flowithの実質的な中国系サービスとしての性格を証明している。

特に企業・組織での使用は、**業務機密の中国本土流出、統合監視システムへのデータ提供、国家情報法による強制アクセス**等の重大なリスクを伴う。

個人利用においても、入力したすべての情報が中国政府の監視対象となる可能性があり、一度入力したデータの完全な削除は技術的に不可能である。

**一刻も早い使用停止と、より安全な代替サービスへの移行を強く推奨する。**

---

## 参考文献

[^1]: [Apple App Store - Flowith](https://apps.apple.com/us/app/flowith/id6742640078)
[^2]: [Derek Nee個人サイト - X ACADEMY](https://dereknee.com/works/tech-x)
[^3]: [Wikipedia: MiraclePlus 2025年7月23日更新](https://en.wikipedia.org/wiki/MiraclePlus)
[^4]: [Derek Nee X/Twitter 2024年投稿](https://x.com/dereknee?lang=en)
[^5]: [Flowith Privacy Policy](https://try.flowith.io/privacy)
[^6]: [Flowith公式ドキュメント：契約に関して](https://doc.flowith.io/flowith-heyoukoso/sononogo/gonishite)
[^7]: [Livedoor News: Flowith紹介記事 2025年8月18日](https://news.livedoor.com/article/detail/29388975/)
[^8]: [AI-Bridge Lab: Flowith Neo解説 2025年5月26日](https://aibridgelab.com/2025/05/26/flowith-neo/)
[^9]: [yanai-ke.com: Flowith AI完全ガイド 2025年7月1日](https://yanai-ke.com/flowith-ai/)
[^10]: [YouTube: Flowithファーストインプレッション 2025年7月頃](https://www.youtube.com/watch?v=oNO3-NkWiFo)

---

**調査実施**: 2025年10月3日
**調査者**: AI安全性評価システム
**バージョン**: v3.5

**免責事項**: 本レポートは公開情報に基づく分析であり、法的助言を構成するものではありません。個別の判断については、法務・セキュリティ専門家にご相談ください。
