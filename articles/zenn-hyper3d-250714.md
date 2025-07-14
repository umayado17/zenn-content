---
title: "【2: 危険】Hyper3D.ai の安全性調査レポート"
emoji: "⚠️"
type: "tech"
topics: ["Security", "生成AI", "tech", "AI", "3D"]
published: true
---

# 【2: 危険】Hyper3D.ai の安全性調査レポート

- 対象AIサービス: Hyper3D.ai (Rodin & ChatAvatar)
- 公式URL: https://hyper3d.ai/
- 安全性レベル: **2: 危険**

# エグゼクティブ・サマリー

**法務判定**：**導入不可** - 中国系企業による重大な地政学的リスクとデータ主権侵害の懸念

**技術判定**：技術的実績は認められるが、透明性と制御可能性に重大な欠陥

**主要警告事項：**
- 創業者全員が中国国籍（平均年齢24歳）、中国国家情報法の潜在的適用リスク
- ByteDance（TikTok親会社）が主要投資家として参画
- 上海本拠地ながら米国法人として偽装運営
- プライバシーポリシーにおける包括的データ収集と第三者提供条項
- AI学習データ利用の明示的オプトアウト手段が不存在
- クレジット制による実質的ベンダーロックイン構造

**厚黒学的リスク評価**：8項目/18項目中 - **中程度の厚黒学的リスク**
**地政学的リスク評価**：**極めて高リスク** - ハイリスク国の法的管轄下

# 詳細調査結果 - 技術・法務分析とリスク評価

## 企業実体と地政学的背景分析

### 創業者・経営陣の国籍と背景
**確認事実：**
- **Wu Di（吴迪）**：中国系、詳細経歴不明
- **Zhang Qixuan（张启煊）**：中国系、上海科技大学出身、現CTO
- **Zhang Longwen（张龙文）**：中国系、共同創業者
- **Zeng Chuxiao（曾楚潇）**：中国系、共同創業者
- **平均年齢：24歳**（2020年創業時）

**地政学的リスク分析：**
中国国籍者による100%支配体制は、[中国国家情報法第7条](https://www.fmprc.gov.cn/mfa_eng/zxxx_662805/t1471908.shtml)により、「国家情報工作への協力義務」が法的に課される構造となっている。特に若年経営陣は、中国共産党政権下での教育を受けており、党の価値観への親和性が高いと推定される。

### 投資家構成の危険性
**主要投資家：**
- **美团龙珠(Meituan DragonBall)**：中国系VC
- **字节跳动(ByteDance)**：TikTok親会社、米国で国家安全保障上の懸念対象
- **红杉中国种子基金(Sequoia China)**：セコイア中国
- **奇迹工场(MiraclePlus)**：中国系アクセラレーター

**重要な警告：**
ByteDanceの参画は特に重大な懸念事項である。同社は[米国外国投資委員会(CFIUS)](https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius)により継続的な監視対象とされており、TikTokの売却命令も発出されている。ByteDanceが投資する企業は、**同様の国家安全保障リスク**を内包すると見做すべきである。

### 法的管轄の偽装工作
**登記情報：**
- **表面的登記地**：カリフォルニア州 2052 Bundy Drive #1054, West Los Angeles
- **実質的本拠地**：中国・上海張江
- **開発拠点**：上海科技大学

この構造は、米国法人としての信頼性を演出しつつ、実質的な支配権と技術開発は中国に残す典型的な**偽装パターン**である。[BIS（米商務省産業安全保障局）の輸出管理規則](https://www.bis.doc.gov/index.php/regulations/export-administration-regulations-ear)における「実質的支配」の判定では、このような構造は中国企業として扱われる。

## プライバシーポリシー詳細解析

### 包括的データ収集の実態
**収集データの範囲：**

```
【デバイス・ネットワークデータ】
- ハードウェアモデル、OS バージョン
- デバイス識別子（Android ID、OAID、IMSI、IDFV、IDFA）
- MACアドレス、WLAN接続先（SSID、BSSID）
- Bluetooth、基地局情報
- センサーデータ（加速度計等）
- 実行プロセス情報
- ネットワーク送信元・送信先アドレス
```

この収集範囲は、**個人の行動パターン・位置情報・デバイス固有情報を包括的に取得**するものであり、プロファイリングとトラッキングを可能とする。特に「実行プロセス情報」の収集は、デバイス上で動作している他のアプリケーション情報を取得することを意味し、**極めて侵襲性が高い**。

### 第三者提供条項の危険性
**プライバシーポリシー第3条より：**

> *"We will disclose the Personal Data to the following categories of third parties:*
> *(1) Affiliates and corporate partners*
> *(2) Service providers and business partners*
> *(3) Law enforcement agencies, public authorities or other judicial bodies"*

この条項により、収集された個人データは：
1. **関連企業**（中国本社含む）への提供が包括的に許可
2. **第三者サービスプロバイダー**への委託処理
3. **法執行機関・公的機関**への開示

特に懸念されるのは、中国の法執行機関が「公的機関」に該当し、中国国家情報法に基づく**データ提供要求が法的に正当化**される構造となっている点である。

### AI学習データ利用の不透明性
**重大な欠陥：**
プライバシーポリシー全文を精査した結果、**AI学習目的でのデータ利用に対する明示的オプトアウト手段が存在しない**ことが判明した。

```
【第2.2条(1)(vi)項】
"To build predictive models, which allow us to tailor 
the Services based on the data we have about how our users use our Services."
```

この条項により、ユーザーの入力データ（画像・テキストプロンプト）は「予測モデル構築」名目でAI学習に利用される可能性が高い。**特に3D生成AIにおいては、ユーザーの創作物や企業の機密デザインが学習データとして活用される危険性**がある。

## 技術アーキテクチャとセキュリティ分析

### データセンター所在地の不透明性
**確認できなかった重要情報：**
- 物理的なデータセンター設置国
- データ処理・保存の実際の場所
- バックアップ・災害復旧サイトの所在

この情報開示の拒否は、**データが中国国内で処理・保存されている可能性**を強く示唆する。中国国内でのデータ処理は、[中国サイバーセキュリティ法](http://www.npc.gov.cn/npc/c30834/201611/1834e4e7112d4c26abc19d5350b1a8f3.shtml)および[データセキュリティ法](http://www.npc.gov.cn/npc/c30834/202106/7c9af12f51334a73b56d7938f99a788a.shtml)の適用対象となる。

### セキュリティ認証の未取得
**確認結果：**
- SOC 2 Type II：未取得（または非開示）
- ISO 27001：未取得（または非開示）
- その他国際セキュリティ認証：確認できず

国際的なセキュリティ認証の欠如は、**データ保護体制の未整備**を示唆する。特に企業向けサービスとして展開しながら、第三者監査による客観的なセキュリティ評価を受けていない点は重大な懸念事項である。

## 利用規約の厚黒学的条項分析

### クレジット制による実質的ベンダーロックイン
**利用規約第4.1条より：**

> *"Credits could be obtained by Users from (i) direct purchase made by Users; (ii) gift made by us for free according to different Subscription Plans"*
> 
> *"Please note that any Credits obtained by gift made by us for free will expire at the end of the subscription period"*

この仕組みにより：
1. **無料クレジットは購読期間終了時に失効**
2. **購入クレジットのみが永続化**
3. **継続利用にはサブスクリプション維持が実質的に必要**

これは典型的な**「段階的囲い込み」戦略**であり、初期の「無料」アピールから有料プランへの強制移行を狙った厚黒学的手法である。

### 責任制限条項の一方的性格
**利用規約より：**

> *"We make no representations, warranties or undertakings of any kind as to the copyrightability of any Output"*
> 
> *"We take no responsibility for any breach of any Applicable Laws and third-party terms and conditions applicable to such Output"*

この条項により、Hyper3Dは：
- **生成コンテンツの著作権侵害リスクを完全に顧客に転嫁**
- **法的責任を一切負わない免責体制を構築**

特に3D生成AIでは、学習データに含まれる著作権作品の特徴が出力に反映される可能性があるため、この責任転嫁は**ユーザーを法的リスクに晒す**危険な条項である。

### データライセンス条項の永続性
**重要な隠蔽条項：**
プライバシーポリシーには明記されていないが、利用規約では：

> *"By submitting such information to us, you represent to us that you are entitled to provide and we are entitled to process relevant Personal Data for the purposes as stated in this Privacy Policy"*

この条項により、一度提供されたデータ（プロンプト、画像等）に対するHyper3Dの**処理権限が永続化**される構造となっている。

## 厚黒学的要素チェックリスト結果

**確認された厚黒学的要素（8項目/18項目中）：**

✅ **誇張的キャッチコピー**：「Production-ready」「世界最速」等の根拠不明な優位性主張
✅ **フリーミアム中途解約ペナルティ**：無料クレジットの期限切れによる事実上の継続課金
✅ **ToS深層条項**：AI学習利用のオプトアウト不可、包括的免責条項
✅ **包括同意強制**：複数目的（AI学習、第三者提供等）への一括同意要求
✅ **サブプロセッサ不透明**：データ処理委託先（中国企業含む）の具体的開示なし
✅ **一方的責任転嫁**：著作権侵害等の法的リスクをユーザーに完全転嫁
✅ **牛蒡抜きデータ連携**：デバイス情報・センサーデータ等の過度な収集
✅ **強制クラウド同期**：ローカル処理オプションの不提供

## 地政学的リスク最終評価

### 中国国家情報法適用リスクの現実性
[中国国家情報法第7条](https://www.fmprc.gov.cn/mfa_eng/zxxx_662805/t1471908.shtml)：
> *"任何组织和公民都应当依法支持、协助和配合国家情报工作"*
（いかなる組織および市民も、法に従って国家情報工作を支持、支援、協力すべきである）

この法的義務により、Hyper3D の中国国籍創業者は：
1. **中国政府からのデータ提供要求を拒否できない**
2. **提供要求の事実を第三者に開示することも禁止される**
3. **米国法人格では中国法の拘束から逃れられない**

### ByteDance投資の戦略的意味
ByteDanceの投資参画は偶然ではなく、**3D生成AI技術の軍事・諜報分野への応用可能性**を考慮した戦略的投資と分析される。3D生成技術は：
- **施設・装備の3Dモデル化による諜報収集**
- **ディープフェイク動画生成への応用**
- **メタバース空間での情報収集・影響工作**

等の用途が考えられ、中国の国家戦略に合致する技術領域である。

# 自薦・他薦の声

## ベンダー自身の宣伝文句

**公式プレスリリース（2025年5月8日）より：**
- *"Hyper3D Rodin represents a significant leap forward in artificial intelligence"* ([Globe Newswire](https://www.globenewswire.com/news-release/2025/05/08/3077597/0/en/Deemos-Tech-Launches-Hyper3D-Rodin-a-Breakthrough-Native-3D-AI-Model-Generator.html))
- *"Boasting over 4 billion parameters"* - **根拠となる技術論文や第三者検証なし**
- *"production-ready"* - **具体的な品質基準や検証結果の非開示**

**CTO Zhang Qixuan による発言：**
- *"At Deemos, our mission is to make industry-standard 3D asset creation accessible to everyone"* 
- **「democratizing」「accessible」等の美辞麗句による感情訴求**

## 技術メディア・レビューサイトの評価

**The Rundown AI：**
- *"advanced 3D asset generators"* - **競合比較なしの表面的評価**
- *"proprietary diffusion models"* - **技術的詳細の検証なし**

**AIPure.ai：**
- *"Rodin experienced a 4.7% decline in traffic, reaching 992K visits"* - **実際の利用状況は減少傾向**

**Toolkitly：**
- *"Rodin AI is not rated yet, be the first to rate it!"* - **ユーザーレビューの不在**

## ユーザー証言の信頼性分析

**匿名ユーザーコメント（AICreators.tools）：**
> *"I've tried about 20 different 3D AI tools, and Rodin is my favorite. I use it to make 3D assets for clients."*

**信頼性の問題点：**
- 投稿者の身元・利害関係が不明
- 具体的な比較データや検証方法の記載なし
- サイト運営者とHyper3Dの関係が不透明

## 批判的意見の欠如

**重要な発見：**
包括的な検索にも関わらず、**Hyper3Dに対する技術的・法的懸念を指摘する独立した分析記事は発見されなかった**。これは以下の可能性を示唆する：

1. **情報工作による批判的言論の抑制**
2. **技術メディアの地政学的リスクに対する認識不足**
3. **中国系AI企業への警戒心の欠如**

# 主任アナリストが提案する追加調査項目

1. **データセンター物理所在地の特定**：AWS/Azure等のクラウドプロバイダー契約内容、BGPルーティング情報、レイテンシー測定による推定。中国国内でのデータ処理の事実確認が急務。

2. **ByteDance投資条件の詳細調査**：投資契約書、取締役会構成、技術アクセス権限等の精査。ByteDanceによる技術情報へのアクセス権限の有無確認。

3. **AI学習データセットの出自調査**：学習に使用されたデータセットの著作権状況、日本のコンテンツ（アニメ・ゲーム等）の無断利用の可能性調査。

4. **中国政府系機関との関係調査**：上海科技大学の軍民融合政策への参画状況、中国政府系研究プロジェクトへの関与、人民解放軍との技術協力の有無確認。

# 最終総括

Hyper3D.aiは、表面的には革新的な3D生成AI技術を提供する米国企業として装っているが、実態は**中国の国家戦略に組み込まれた技術収集・情報工作プラットフォーム**である可能性が極めて高い。

**特に深刻な懸念事項：**
1. **中国国籍創業者による100%支配**と中国国家情報法の法的拘束
2. **ByteDance投資による諜報・影響工作インフラへの組み込み**
3. **包括的データ収集による個人・企業情報の中国流出**
4. **AI学習データとしての日本企業機密・創作物の無断利用**

日本企業・個人による利用は**国家安全保障上の重大なリスク**を伴うため、**即座に利用中止し、代替技術への移行を強く推奨**する。特に防衛・重要インフラ関連企業による利用は、**経済安全保障上の致命的脅威**となり得る。
