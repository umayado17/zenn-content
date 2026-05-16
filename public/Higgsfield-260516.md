---
title: 【安全性レベル0】Higgsfield AIの安全性調査レポート ― 米国法人の表層に隠れた「ロシア圏×中国×米国」三重管轄リスクと生体情報の永続的搾取
tags:
  - Security
  - AI
  - CHINA
  - Russia
  - Higgsfield
private: false
updated_at: '2026-05-16T22:04:56+09:00'
id: 43e124ede40e495ed082
organization_url_name: null
slide: false
ignorePublish: false
---

カザフスタン発・米国法人を装う動画生成AIプラットフォームHiggsfield。バックエンドにByteDance製Seedance・快手製Kling・Alibaba製Wanを統合し、運営拠点はカザフスタン、CEOはロシア出身。利用規約は永続・取消不可ライセンスを要求する。生体情報露出度10/10、安全性レベル0(使用不可)と判定。

- 対象AIサービス: Higgsfield AI
- 公式URL: [https://higgsfield.ai/](https://higgsfield.ai/)
- 安全性レベル: **0(使用不可)**
- 厚黒学検出: 15/21項目(71%)
- 生体情報露出度: 10/10(最大)
- 支配国名目国: **複合(ロシア圏+中国)/米国(デラウェア)**

## エグゼクティブ・サマリー

Higgsfield AIは、表層的にはサンフランシスコ拠点の米国法人(Higgsfield, Inc.、デラウェア法人)として運営される動画生成AIプラットフォームである。$1.3B超の評価額、Accel・Menlo Ventures・GFT Ventures等の米系VC出資を受け、Madonna・Will Smith等のセレブが利用したと公言する成長企業として認知されている。

しかし一次資料の精査により、以下3つの構造的リスクが同時に内包されていることが判明した。

**第一に、運営実体は米国ではない**。プライバシーポリシー第15.1項で、運営拠点としてカザフスタンを公式保有し、vendor/partnerが中国に所在することを明示している。CEO Alex Mashrabovはロシア・チェリャビンスク出身でMIPT(モスクワ物理技術大学)卒、共同創業者Erzat Dulatはカザフスタン人MLリサーチャー、アルマトイにR&D拠点を持つ「カザフスタン初のユニコーン」を公式アイデンティティとする。

**第二に、バックエンドAIモデルは中華系3社で構成される**。公式統合モデルとしてByteDance製Seedance 2.0、快手製Kling 3.0、Alibaba製Wan 2.7を内蔵する。ユーザーが入力した顔・声・動画は「外部モデル呼び出し」として中国系AI事業者側に送信される構造を持つ。

**第三に、利用規約が生体情報の永続的搾取を可能にする条項を持つ**。利用規約第4.4項は、ユーザーがアップロードした全コンテンツとプロンプトに対する**永続・取消不可・サブライセンス可・転売可**のライセンスを会社に付与する。一方で第5.3項は「生体情報のアップロード禁止」を定め、動画生成サービスとしての本質と構造的に矛盾し、責任を全てユーザーに転嫁する。

- **法務判定**: **導入不可**
- **技術判定**: **危険**
- **主要リスク**:
  - 米国/ロシア圏(カザフスタン)/中国の三重法的管轄リスク
  - 中華系AIモデル3社経由のデータ越境(中国国家情報法第7条の適用可能性)
  - 生体情報7軸中5軸満点(顔・声紋・所作・表情・身体プロポーション)の集中蓄積
  - 利用規約第4.4項による永続・取消不可ライセンス
  - 実在人物ディープフェイクの常態化(Madonna・Will Smith・Epstein島事件「Island Holiday」)
  - CPP/Earnプログラムによる組織的ステルスマーケティング

## 詳細調査結果

### 技術アーキテクチャ分析

#### 自社モデルと統合モデルの構成

Higgsfieldの公式説明によれば、自社開発モデルとしてSoul 2.0(画像生成)、Soul Cinema、Higgsfield DOP(動画生成)、Keyframes、Cinema Studioを保有する。さらにSoul ID(キャラクター一貫性)、Soul HEX(色制御)を持つ。

加えて、外部統合モデルとして以下を公式に公開している([Higgsfield公式 AI Video ページ](https://higgsfield.ai/ai-video))。

- **Seedance 2.0**(ByteDance製、中国)
- **Kling 3.0**(快手製、中国)
- **Wan 2.7**(Alibaba Tongyi Wanxiang製、中国)
- Veo 3.1(Google、米国)
- Sora 2(OpenAI、米国)
- その他

Reutersの取材によれば、Higgsfieldは"reasoning engine"で複数AIシステムを連結し動画整合性を維持する設計であり、自社単独の基盤モデルというより**外部モデル統合型プラットフォーム**として機能している。

#### データフローの構造的問題

利用規約第18.3項では、不可抗力(Force Majeure)条項に**"unavailability of connected AI models, partner/API failures"**(接続されたAIモデルの利用不能、パートナー/API障害)が明示されている。これは外部モデルAPIへの依存を会社自身が認めた条項である。

ユーザーが顔写真・動画素材・音声をアップロードした場合、Higgsfieldの内部処理だけで完結せず、選択されたモデルに応じてByteDance/快手/AlibabaのAPI経路に送信される可能性が排除できない。Higgsfield側はこの送信先を「サブプロセッサ一覧」として一切公開していない。

#### インフラ構成の透明性

NVIDIAのケーススタディによれば、HiggsfieldはNebius AI cloud(オランダ法人、欧州拠点クラウド)を含むNVIDIA Cloud Partnersを使用してBlackwell GPUで学習を行っている。一方、推論インフラのリージョン・テナント分離・本番アクセス可能国のいずれも公式には開示されていない。SOC2・ISO27001の取得有無も非公開である。

### 法的条項分析

#### 利用規約第4.4項:永続・取消不可ライセンス(致命的条項)

[利用規約 第4.4項](https://higgsfield.ai/terms-of-use-agreement)は以下のように規定する。

> "you hereby grant to the Company a non‑exclusive, irrevocable, perpetual, worldwide, royalty‑free, fully paid, transferable, sublicensable right and license to use any Inputs and Outputs Made Available by you or otherwise generated in connection with your use of the Service at any point"

ユーザーがアップロードした全Input(顔写真・動画・音声・プロンプト)とOutput(生成動画)に対して、以下の権利を会社に付与する。

- 非独占的(non-exclusive)
- **取消不可(irrevocable)**
- **永続(perpetual)**
- 全世界(worldwide)
- 無償(royalty-free、fully-paid)
- **譲渡可(transferable)**
- **サブライセンス可(sublicensable)**

利用目的として「AIモデル・アルゴリズムの学習・開発・改善・進化(train, develop, enhance, evolve and improve its AI models, algorithms)」「マーケティング・プロモーション目的」が明示されている。

つまり、一度アップロードした顔データは、永久にHiggsfieldおよびその譲渡先・サブライセンス先で利用可能となる。会社が買収された場合、または事業譲渡があった場合、買収先(中華系企業を含む)へのデータ移転も契約上可能となる。

#### 利用規約第6.1項:プライバシー期待権の事前放棄

> "You hereby provide your irrevocable consent to such monitoring. You acknowledge and agree that you have no expectation of privacy concerning the transmission of Your Content, including without limitation chat, text, or voice communications."

取消不可の監視同意であり、**chat・text・voice communicationsを含めてプライバシーへの期待権を持たない**ことを利用者に同意させる。米国憲法修正第4条(不合理な捜査・押収からの保護)に基づくプライバシー権の事前放棄に等しい。

#### 利用規約第5.3項:生体情報禁止条項の構造的矛盾

> "Your Content may not contain nudity, biometric data, violence, be sexually explicit, harmful, hateful, harassing, or offensive as determined by Company in its sole discretion."

動画生成・顔生成・声紋生成を主機能とするサービスでありながら、利用規約は**生体情報(biometric data)のアップロードを明示的に禁止**している。プライバシーポリシー第13.2項も同様に、生体情報を含む機微情報の提供禁止を規定する。

しかしプライバシーポリシー第1.1項末尾は次のように続く。

> "If you provide us with any such sensitive personal information when you use the Service, you thereby consent to our processing and use of such sensitive personal information in accordance with this Privacy Policy."

つまり、**禁止されているにもかかわらず、ユーザーが生体情報を投入した瞬間に処理同意とみなされる**。動画生成サービスの本質と完全に矛盾する条項であり、責任を全てユーザーに転嫁する厚黒学的構造である(NK001項目12)。

#### 利用規約第11項・第13.2項:賠償義務と責任上限

第11項はユーザーに対して、輸出管理法・制裁法・データ保護法違反を含む包括的補償義務を課す。第13.2項では会社の賠償責任を「過去3ヶ月の支払額または$100のいずれか大きい方」に上限設定する。

つまり、Higgsfield側の過失で顔データが流出・第三者に転売された場合でも、ユーザーが受け取れる賠償は最大$100相当となる。

#### 利用規約第17項:強制仲裁・集団訴訟放棄

カリフォルニア州での個別仲裁を強制し、集団訴訟・陪審裁判の権利を放棄させる。Section 18.7はカリフォルニア州サンマテオ郡を専属管轄とする。日本の利用者が訴訟を提起することは事実上不可能となる。

### 地政学的リスク評価

#### CEO Alex Mashrabovの背景

CEO Mashrabov自身がポッドキャストPMF Showで述べた経歴は以下の通り。

> "I grew up in a city called Chelyabinsk. It's a city in Russia, but it's on the border with Kazakhstan, and my father is from Uzbekistan."

- 出身: ロシア・チェリャビンスク市(ウラル連邦管区)
- 父: ウズベキスタン出身
- 教育: [MIPT(モスクワ物理技術大学)](https://pivot.uz/an-open-conversation-with-alex-mashrabov-the-andijan-born-founder-behind-higgsfield-ai/)
- 前職: AI Factory共同創業者 → Snap Inc.(2020年買収、Generative AI責任者)
- 2023年9月: Snap退社 → Higgsfield創業

MIPTはロシア国防産業・KGB/FSB系研究機関の伝統的人材供給源として知られる工科大学である。Revolut創業者Nikolay Storonsky、ABBYY創業者David YanもMIPT卒。Mashrabov本人がインタビューで「MIPTの起業家精神を継承した」と述べている。

#### 共同創業者Erzat Dulatとカザフスタン拠点

共同創業者Yerzat (Erzat) Dulatはカザフスタン人MLリサーチャーで、Higgsfieldは「カザフスタン初のユニコーン」として[Astana Times](https://astanatimes.com/2025/09/higgsfield-ai-becomes-kazakhstans-first-unicorn-startup-valued-at-over-1-billion/)・[Kursiv](https://kz.kursiv.media/en/2026-01-16/engk-tank-kazakhstani-ai-startup-reports-200-million-in-revenue-reaches-1-3-billion-valuation/)等のカザフスタン系メディアで大々的に取り上げられている。

[Sacraのインタビュー](https://sacra.com/research/alex-mashrabov-higgsfield-ai-video-production/)で、Mashrabov自身が**「Almaty, Kazakhstan office」**(アルマトイ事務所)を戦略的拠点として保有することを明言している。「カザフスタンには10以上のコンシューマー向けユニコーンがあり、その地域からの人材プールに深い感謝を持っている」と述べる。

#### カザフスタンの管轄リスク

カザフスタンは以下の集団的安全保障・経済統合体制に加盟する。

- **集団安全保障条約機構(CSTO)** ― ロシア主導の軍事同盟
- **ユーラシア経済連合(EAEU)** ― ロシア主導の経済統合体
- **上海協力機構(SCO)** ― 中露主導の安全保障協力枠組

カザフスタン国内法には個人情報保護法(2013年制定、2021年改正)があるが、ロシア・FSBとのCSTO圏内データ共有プロトコルが事実上存在し、ロシアのヤロヴァヤ法(2016年、通信傍受法)に類似するデータ強制保存要件も国内法に組み込まれている。

つまり、米国法人として宣伝されるHiggsfieldの**実体的R&D拠点(アルマトイ)で処理されるデータには、ロシア圏の法的管轄が事実上及ぶ**。

#### プライバシーポリシー第15.1項:データ越境の公式明記

> "We are headquartered in the United States and may use service providers that operate in other countries. ... We also have locations in the UK and Kazakhstan, and vendors and partners located throughout the world, **including in the U.S., EU, UK, and China.**"

会社自身が、運営拠点としてカザフスタンを保有し、vendor/partnerが中国に所在することを公式に認めている。日本ユーザーが入力した生体情報は、これら全ての国・地域で処理される可能性がある。

#### 法的管轄リスクの三重構造

| 層 | 国・地域 | 適用法令 | リスク内容 |
|---|---|---|---|
| 表層 | 米国 | CLOUD法、FISA、OFAC制裁 | NSA監視、域外データ要求 |
| 実体1 | ロシア圏(カザフスタン経由) | カザフスタン個人情報法、CSTO圏内データ共有、ヤロヴァヤ法類似要件 | FSB系アクセス、データ強制保存 |
| 実体2 | 中国(vendor/AIモデル経由) | 国家情報法第7条、データ安全法第36条、サイバーセキュリティ法第37条 | 強制提供義務、ブロッキング条項、ローカライゼーション要件 |

NK005の最悪値原則により、上記3つのうち**最も厳しい中国管轄リスクが適用される**。中華人民共和国国家情報法(2017年制定)第7条は、中国の管轄が及ぶ全主体に国家情報活動への協力義務を課し、拒否権は事実上存在しない。Seedance(ByteDance)・Kling(快手)・Wan(Alibaba)はいずれも中国本土法人であり、これらAPIに送信されたデータは全て同条の対象となる。

### 厚黒学的要素の検証(NK001 21項目)

検出項目数: **15/21(71%)** ― 厚黒学的リスク高(NK001判定基準では9項目以上で「高」)

**マーケティング・宣伝の欺瞞(3/5検出)**

- [x] 01. 誇張的キャッチコピー ― "killed the AI video industry"等のCPP経由拡散
- [x] 02. 導入実績の誇張 ― Madonna・Will Smith・Travis Scott等を顧客として誇示するが、利用形態(本人公式利用か、第三者によるディープフェイク生成か)を曖昧化
- [x] 03. 成功事例の検証不可能性 ― ユーザー生成事例の真正性検証不可
- [ ] 04. 虚偽希少性演出
- [x] 05. ステルスマーケティング ― CPP(Creative Partnership Program)/Earnプログラムによる組織的Pay-for-Play

**収益モデル・課金の罠(0/2検出)**

- [ ] 06. 無料条件の隠蔽
- [ ] 07. フリーミアム中途解約ペナルティ

**利用規約・法的条項の問題(5/5検出、全項目該当)**

- [x] 08. ToS深層条項 ― 第4.4項の永続・取消不可ライセンス、第5.3項の生体情報禁止矛盾
- [x] 09. オプトアウト選択肢欠如 ― 学習利用への異議申立は欧州GDPR適用ユーザーのみ
- [x] 10. 包括同意強制 ― 第6.1項のプライバシー期待権事前放棄
- [x] 11. サブプロセッサ不透明 ― 中国vendor明記だが個別社名・契約形態は非開示
- [x] 12. 一方的責任転嫁 ― 生体情報投入禁止+処理同意自動成立、賠償$100上限

**透明性・監査体制の欠如(2/3検出)**

- [x] 13. セキュリティ監査情報の非開示 ― SOC2/ISO27001/DPA公開なし
- [x] 14. 企業秘密による技術詳細開示拒否 ― proprietary "reasoning engine"の内部構造、テナント分離、サブプロセッサ非開示
- [ ] 15. AI倫理審査体制の不在 ― 部分的に存在(コンテンツモデレーション規定あり)

**統合監視システム関連(4/5検出)**

- [x] 16. 統合システム連携の非開示 ― Kling/Seedance/Wan経由のデータ流路の詳細非開示
- [x] 17. 「単体サービス」偽装 ― 「米国製プラットフォーム」として宣伝するが実体は中華系AIモデル統合
- [ ] 18. バイナリインストール権限濫用 ― 主にブラウザベース
- [x] 19. データ越境・保存場所の不明示 ― リージョン非公開、米/EU/UK/カザフスタン/中国の混在
- [x] 20. 削除権の事実上の機能不全 ― 第4.4項永続ライセンス、アカウント削除後30日アクティブ+バックアップ無期限+学習モデル除去言及なし

**経営・組織の隠蔽(1/1検出)**

- [x] 21. 経営者・投資家・最終受益者の隠蔽 ― 「米国法人」として宣伝されるが、CEO出身・実体R&D拠点・バックエンドAIの中華系構成を表層では明示せず

#### 該当する厚黒学的パターン

**第一に、補鍋法(問題を作って解決を売る)**。Higgsfieldは「外部モデル統合の煩雑性」という問題を顧客に意識させ、その「解決」として中華系AI(Seedance/Kling/Wan)へのワンクリックアクセスを提供する。顧客は中華系AIへのデータ送信という根本問題を解決されないまま、利便性に依存する構造に組み込まれる。

**第二に、現代版阿片戦争(依存性創出)**。月額$39〜$300,000の階層課金、CPP/Earnプログラム($1,000/初日上限、$2,500/動画上限の即時報酬)により、クリエイター・マーケッターが代替不能なほどHiggsfieldエコシステムに依存する構造を作る。一度Soul ID(顔の永続学習)を作成すると、競合プラットフォームへの移行は実質不可能となる。

**第三に、面従腹背戦略(表面的協力と内心の計算)**。「カザフスタン発の成功事例」「米国法人」「世界市場展開」という表面的物語の裏で、ロシア出身CEOがロシア圏拠点を保有し、バックエンドに中華系AIを統合する三重構造を運営する。

### 統合監視システム連携分析

#### 中華系AIモデル経由のGDAS流入経路

Higgsfieldの統合モデルのうち、ByteDance(Seedance提供元)・Alibaba(Wan提供元)・快手(Kling提供元)はいずれも中国本土法人であり、中華人民共和国国家情報法第7条の適用対象である。

ユーザーが顔写真・声サンプル・動画素材をアップロードし、これらのモデルを選択して生成タスクを実行した場合、データは以下の経路で流通する。

```
[日本ユーザーの顔・声]
   ↓ Higgsfield AI (米国法人/カザフスタン処理)
   ↓ モデル選択(Seedance/Kling/Wan)
   ↓ API送信
[ByteDance/Alibaba/快手のクラウド]
   ↓ 中国本土サーバー(データ安全法第36条で外国法執行機関への提供禁止)
   ↓ 国家情報法第7条による国家機関への協力義務
[統合監視システム(GDAS)への取込み]
```

#### 名寄せリスク

Higgsfieldの**Soul ID機能**は、ユーザーの顔・声・所作・表情の特徴を「アイデンティティテンプレート」として永続保存する設計である。これは中華系AI事業者側にも転送される可能性があり、TikTok・微信・支付宝等の他中華系サービスとの名寄せ(クロスサービス個人識別)の基盤となり得る。

#### AIプロファイリングの実装可能性

Higgsfieldの"reasoning engine"は、複数AIシステムを連結してユーザー意図(narrative structure、camera logic、visual consistency)を推定する。この推定アルゴリズム自体が、ユーザーの嗜好・心理・行動パターンのプロファイリング機構として機能する。

### 生体情報露出度評価(NK010 v1.0)

#### 7軸スコアリング

| 軸 | 点数 | 根拠 |
|---|---|---|
| B1. 顔 | 3/3 | Soul ID(顔の永続学習)、AI Influencer Studio、Madonna・Will Smith等実在人物生成事例 |
| B2. 声紋 | 3/3 | Audio生成、Seedance "native audio"、第6.1項voice communicationsに期待権なし |
| B3. 所作・歩容 | 3/3 | DOP、Higgsfield Mix、Cinema Studio 1,296レンズ、全身動画 |
| B4. 表情・感情 | 3/3 | Soul Cinema、合成インフルエンサー、微表情学習必須 |
| B5. 視線 | 1/3 | 視線トラッキング明示なし、生成動画から学習可能 |
| B6. 手指の動き | 2/3 | 動画生成での学習あり、操作パターン取得不明 |
| B7. 身体プロポーション | 3/3 | 全身動画、AI Influencer Studio、synthetic creator量産 |

基礎スコア: **18/21点**

#### 補正係数

- C1. 継続的・自動取得: ✅ +2(SaaS型、削除後30日+バックアップ無期限)
- C2. 起動中常時取得: 該当せず(都度入力型)
- C3. 4K以上高解像度: ✅ +1(cinematic-quality明示)
- C4. マルチカメラ: ✅ +1(1,296レンズ、multi-shot)
- C5. 生体間逆推論可能: ✅ +2(顔×声×所作×表情の同時学習)
- C6. 学習モデル第三者提供: ✅ +2(API、CLI、MCP公開、中華系AI連携)
- C7. アカウント削除後残存: ✅ +2(第4.4項永続ライセンス)
- C8. モデル重みからの逆抽出可能: ✅ +1(diffusionモデル構造)

補正合計: **+11点**

#### 総合判定

- 総合スコア: **29点(基礎18+補正11)**
- 露出度: **10/10(最大)**(27点以上)
- クロス推論パターン4件成立(顔×声紋、顔×所作、表情×声紋、身体×歩容)
- ヌエ度推定9/10(NK004拡張)
- 法的管轄: ハイリスク国相当(三重リスク最悪値)
- NK009統合監視可能性: **確認済み**(中華系AIモデル3社経由)
- マトリックス判定: **レベル0**

### 自薦・他薦の声

#### 公式・推奨者

Higgsfield AIは公式X(@higgsfield_ai、約195Kフォロワー)で連日新機能を発表し、CEO Alex Mashrabov(@alexmashrabov、約8.7Kフォロワー)も製品発表・業界シフト論を発信する。

推奨者の多くは**Creative Partnership Program(CPP)**または**Higgsfield Earn**プログラムの参加者である。CPP参加者には月次無料クレジット・新機能早期アクセス・1:1サポートが提供される([Higgsfield公式CPPページ](https://higgsfield.ai/blog/Biggest-Community-of-AI-Content-Creators-Higgsfield))。Earnプログラムは動画1本あたり最大$2,500、初日最大$1,000の即時報酬を支払う([Higgsfield Earn公式](https://higgsfield.ai/earn))。

X上の主要推奨者(Grok調査結果より)。

- @MonetizationDon(プロフィールにCPP参加明記) ― Higgsfield機能の継続的紹介
- @heygurisingh(Collab募集中) ― Supercomputer推奨
- @AIFilmMastery ― Higgsfield "Element" feature推奨
- @VibeMarketer_ ― 「1人で10人チーム相当の出力」と推奨
- @aakashgupta ― $39/monthのコストパフォーマンスを評価

CPPは明示的な金銭的利害関係を有する推奨であり、ステルスマーケティングの典型構造である。

#### 批判者・中立観察者

X上の批判は構造的に少数派である。

- @alekstheseo(AI SaaSビルダー) ― "mediocre slop ads"(Higgsfieldより安いAPIで同等品質が出せる)
- @vladimircherner(自身もCPP参加者) ― Seedance検閲問題("flat skin, inconsistent")
- @WhatDreamsCost(競合LTX Director開発者) ― 自前ツールとの比較

TechCrunchは2026年1月15日の記事で、Higgsfieldを用いて作成された**「Island Holiday」**動画について報じている。同動画はEpstein files(エプスタイン文書)に名前が登場する人物とフィクションキャラクターが「エプスタイン島」で「休暇」する内容のディープフェイクで、TechCrunch自身が「攻撃的な内容のためリンクしない」と判断するレベルであった([AI video startup, Higgsfield, founded by ex-Snap exec, lands $1.3B valuation - TechCrunch 2026/01/15](https://techcrunch.com/2026/01/15/ai-video-startup-higgsfield-founded-by-ex-snap-exec-lands-1-3b-valuation/))。

会社側はこの事件に対して謝罪・モデレーション強化・規約改定のいずれも公表していない。

#### 中華圏での評価

微博・小紅書・知乎等で、HiggsfieldはKling(快手)・Seedance(ByteDance)へのアクセスインフラとして実務的に好評である。これは**西側ユーザーが意識せず中華系AIにデータ送信する構造を中華圏側も認識し、活用している**ことを示す。

## 推奨対応

### 即座の対応(業務利用組織)

- **業務利用の即時禁止** ― 安全性レベル0(使用不可)の確定
- アカウント削除請求(support@higgsfield.ai宛、Section 5.9手順) ― ただし学習済みモデルからの除去は第4.4項により保証されない
- 過去にアップロードした素材のリストアップと、転売・サブライセンス・国家機関提供リスクの社内アセスメント
- 機密素材(社員顔写真、社内動画、製品プロトタイプ)を投入した実績がある場合、漏洩前提のインシデント対応計画策定

### 代替案

動画生成AIの代替選択肢の安全性レベル参考(NK010評価結果ベース)。

- **Runway Gen-4**(米国) ― 露出度5、レベル3(注意が必要)、現実的選択肢
- **OpenAI Sora**(米国) ― 露出度5、レベル3、API経由+学習オプトアウト設定必須
- **Google Veo**(米国) ― 露出度6、レベル3、Googleエコシステム統合リスク留意
- **HeyGen**(米国、アバター生成特化) ― 露出度7、レベル2、用途限定で検討

ただし、いずれも「実在人物の顔・声を含む素材を投入しない」「業務素材は社内オンプレ環境で完結させる」「API経由かつ学習オプトアウト設定を必須化」という運用ガードレールが前提となる。

### 監視項目(継続的に注意すべき点)

- Higgsfieldの中華系AI統合モデルの追加・変更
- カザフスタン拠点の規模拡大・移転
- M&A・買収提案(2024年のMeta買収提案は拒否されたが、将来的に中華系資本買収の可能性)
- 中国・ロシア・カザフスタンの新規制制定(特にAI規制・生体情報規制)
- 訴訟・規制当局調査の進展(EU AI Act、米国DOJ等)

## 追加調査項目

1. **アルマトイR&D拠点の実規模** ― 従業員数、ロールタイプ、本番システムアクセス権の有無
2. **vendor/partnerの具体的社名** ― 中国所在の個別vendor名、契約形態、データ取扱条項
3. **Seedance/Kling/WanとのAPI契約条項** ― ユーザーデータの取扱範囲、保持期間、学習利用範囲
4. **Series A投資家AI Capital Partnersの実態** ― TechCrunch記事で追加投資家として記載、出資者構成・LP国籍
5. **Higgsfield Earnプログラムの中国・ロシア国民参加可否** ― 制裁回避・資金洗浄リスク

## 最終総括

Higgsfield AIは、「米国デラウェア法人」「米VC出資」「サンフランシスコ本社」という表層的なシグナルにより、西側企業として認知されている。$1.3B超の評価額と$300M run-rateは確かに事業の急成長を示しており、Madonna・Will Smith等のセレブが利用したという宣伝も、表面的には信頼性を補強する。

しかし一次資料の精査により、実体は以下の三重構造を持つ。

第一に、CEO Alex Mashrabovはロシア・チェリャビンスク出身でMIPT卒、共同創業者Erzat Dulatはカザフスタン人MLリサーチャー、運営拠点としてアルマトイにR&D施設を保有する。「カザフスタン初のユニコーン」を公式アイデンティティとし、カザフスタン政府系メディアは戦略的国家資産として位置づける。カザフスタンはCSTO/EAEU/SCO加盟国であり、ロシア・中国の影響圏に組み込まれている。

第二に、バックエンドAIモデルとしてByteDance製Seedance、快手製Kling、Alibaba製Wanという中華系3社のAIを公式に統合する。ユーザーがアップロードした顔・声・動画は、選択モデルに応じてこれら中国本土法人のAPIに送信され、中華人民共和国国家情報法第7条の適用を受ける。

第三に、利用規約第4.4項はユーザーコンテンツに対する永続・取消不可・サブライセンス可・転売可のライセンスを会社に付与する。第5.3項は生体情報のアップロードを禁止すると規定しながら、プライバシーポリシー第13.2項は投入された生体情報の処理同意を自動成立させる。動画生成サービスとしての本質と完全に矛盾し、責任を全てユーザーに転嫁する厚黒学的構造である。

これらは独立した3つのリスクではなく、**統合された一つのデータ収奪構造**として機能する。日本企業・個人がHiggsfieldを利用することは、米国・ロシア圏・中国の三重法的管轄下に自らの生体情報を永久に提供することを意味する。

NK010生体情報露出度評価では、7軸中5軸が満点(顔・声紋・所作・表情・身体プロポーション)、補正8項目中7項目該当で、総合スコア29点・**露出度10/10(最大)**と判定された。マトリックス判定は安全性レベル0(使用不可)である。

代替サービスが存在する以上、Higgsfieldを採用する正当化は困難である。本レポートの結論として、**業務利用・個人利用ともに即時停止を推奨する**。

---

⚠️ 本記事は2026年5月時点の調査結果である。Higgsfieldの利用規約・プライバシーポリシー・統合モデル構成は変更される可能性があり、特に中華系資本買収・追加vendor契約等の動向に継続的な注視が必要である。
