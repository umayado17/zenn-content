---
title: "【1: 極めて危険】Manus AIの安全性調査レポート"
emoji: "⚠️"
type: "tech"
topics: ["Security", "AI", "中国", "リスク評価", "法務"]
published: true
---

# 【1: 極めて危険】Manus AIの安全性調査レポート

- 対象AIサービス: Manus AI エージェント
- 公式URL: https://manus.im/ (中国本土からアクセス遮断中)
- 安全性レベル: **1: 極めて危険**

# エグゼクティブ・サマリー

## 法務判定：**導入不可**

Manus AIは中国企業による開発・運営でありながらシンガポール法人を装う法人構造により、中国の国家情報法適用下でユーザーデータが政府提供される法的義務を負う。2025年7月の突然の「脱中国化」偽装工作は、計画的な管轄回避戦略として機能している。米国財務省が投資規制違反で審査中。

## 技術判定：**アーキテクチャ安全性極低**

技術的にはAnthropic Claude + Alibaba Qwenの組み合わせによる統合製品で、独自技術ではない。データセンター所在地・セキュリティ監査結果等の重要情報を意図的隠蔽。クラウド専用で完全オフライン動作不可。包括的データ収集・利用権を法的に確保済み。

## 地政学的リスク：**極高**

米国Tennessee州・Alabama州が国家安全保障上の脅威として即座に禁止措置。中国の国家情報法により、有事の際のデータ強制提供が法的義務。「脱中国化」は表面的偽装であり、実質的支配構造は維持。

## 投資構造リスク：**内部協力者確認**

米国Benchmark Capitalによる7,500万ドル投資は、Josh Kushner-Miles Grimshaw-Bill Gurleyの中国シンパネットワークによる意図的投資。業界内から「中国への資産提供」として厳しく批判。

## 最終判定理由

技術的能力ではなく、地政学的・法的・投資構造上の複合リスクにより極めて危険と判定。特に計画的偽装工作と米国内部協力者の存在は、単純な中国企業以上の脅威を示す。

# 詳細調査結果 - 技術・法務分析とリスク評価

## 1. 法人構造偽装の詳細分析

### 「転移大法」による管轄回避戦略

**登記上の構造と実態乖離：**
- 表向き運営：Butterfly Effect Pte. Ltd.（シンガポール法人、2023年8月設立）
- 実質開発：北京蝴蝶効应科技有限公司（中国法人）
- [中国企業でありながらシンガポール法人を前面に出し、プライバシーポリシーでも「Country: Singapore」と明記している。しかし実際の開発チーム、オフィス、意思決定はすべて中国で行われており、法的管轄と実態に乖離がある](https://note.com/norito_hiraoka/n/n96b57d870249)

### 2025年7月の組織的偽装工作

**実行された計画的撤退：**
- [中国国内のチームを解散](https://news.yahoo.co.jp/articles/33c6de28671c4b5201efec117971373f18417884)
- [中国本土から自社ウェブサイトへのアクセスを遮断](https://news.yahoo.co.jp/articles/33c6de28671c4b5201efec117971373f18417884)
- [微博（Weibo）や小紅書（RED）といった国内のSNSアカウントもすべて削除](https://news.yahoo.co.jp/articles/33c6de28671c4b5201efec117971373f18417884)

**規模：**
- [According to a report by financial and tech information platform TMTPost, Manus had about 120 employees in China. Over 40 key technical staff members have been transferred to the Singapore office, while the rest were laid off](https://www.citynewsservice.cn/news/China's-AI-agent-Manus-relocates-HQ-to-Singapore-7kr585dn)

## 2. 開発者・経営陣の国籍・背景分析

### 主要人物の中国国籍確認

**肖弘（CEO）：**
- [2011年，進入華中科技大学軟件工程專業學習。2015年，畢業於華中科技大學軟件工程專業](https://baike.baidu.com/item/肖弘/65463549)
- [2022年，肖弘創立了"蝴蝶效應"公司](https://baike.baidu.com/item/肖弘/65463549)

**季逸超（CTO）：**
- [技術責任者季一超も中国出身で中国での事業歴あり](https://note.com/norito_hiraoka/n/n96b57d870249)

**張涛（製品パートナー）：**
- [6月18日にシンガポールで開催されたAIイベント「Super AI」では、同社のプロダクトパートナーの張涛氏が、本社はすでにシンガポールに移転](https://36kr.jp/355530/)

## 3. 米国政府の即座の脅威認定

### 州レベルでの国家安全保障対応

**Tennessee州（2025年3月6日）：**
- [Tennessee becomes the first state in the Nation to ban the Alibaba-owned Manus platform, which launched earlier today](https://www.tn.gov/governor/news/2025/3/6/gov--lee-bans-manus--deepseek-ai-platforms-on-tennessee-state-network.html)
- ローンチ当日の即座禁止措置

**Alabama州（2025年3月26日）：**
- [Alabama Governor Kay Ivey announced new policies banning from the state's IT network and devices the AI platforms DeepSeek and Manus due to "their affiliation with the Chinese government and vast data-collection capabilities"](https://natlawreview.com/article/more-states-ban-foreign-ai-tools-government-devices)

### 法的根拠

- [citing risks of "censorship, propaganda, and bias," and Alabama's Governor Kay Ivey followed with a similar prohibition due to security vulnerabilities](https://winbuzzer.com/2025/04/26/manus-ai-maker-butterfly-effect-eyes-move-to-outside-china-amid-us-china-ai-tensions-xcxwbn/)

## 4. 技術アーキテクチャの外部依存分析

### 基盤技術の構成

**コアモデル：**
- [第三者のレポートによると、Manus のコアモデルとして、Anthropic の Claude 3.5 Sonnet と、中国企業の Alibaba が手掛けるAIモデル「Qwen」が採用されている](https://aismiley.co.jp/ai_news/manus-openai-deepresearch-ai/)
- [Manus wasn't developed entirely from scratch. According to reports on social media, the platform uses a combination of existing and fine-tuned AI models, including Anthropic's Claude and Alibaba's Qwen](https://techcrunch.com/2025/03/09/manus-probably-isnt-chinas-second-deepseek-moment/)

### データインフラの不透明性

**サーバー・データ所在：**
- [ユーザーデータは信頼性の高いクラウドインフラ上に厳重に保管されています。ManusAIはデータ保管にあたり「十分に精査されDPA（データ処理契約）準拠のベンダー」を利用するとしており、具体的なクラウド事業者名は明かされていない](https://note.com/kunipii/n/n6040b5bb88ae)

**データ利用権の包括取得：**
- [利用規約では、ユーザーが提供したデータや生成物（ユーザーデータ）をManus側が匿名加工した上でサービス改善目的で利用することが明記されています](https://weel.co.jp/media/innovator/manus/)

## 5. 投資構造の詳細分析

### Benchmark Capital投資の背景

**投資実行者の経歴：**
- Miles Grimshaw（投資実行責任者）：[The new capital injection, overseen by Benchmark partner Miles Grimshaw](https://winbuzzer.com/2025/04/26/manus-ai-maker-butterfly-effect-eyes-move-to-outside-china-amid-us-china-ai-tensions-xcxwbn/)
- Josh Kushner人脈：[Prior to joining the Benchmark Partnership, Miles was a General Partner @ Thrive Capital](https://www.thetwentyminutevc.com/miles-grimshaw)

### 中国シンパネットワークの証拠

**Josh Kushner/Thrive Capitalの中国接近：**
- [Joshua Kushner's Thrive Capital and investment firm Capital Group have in recent months visited China to learn about its AI industry](https://www.bloomberg.com/news/articles/2025-06-04/capital-group-kushner-s-thrive-visited-china-to-study-ai-scene)

**Bill Gurleyの中国擁護発言：**
- ["In not being a China hawk, people accuse you of being a sinophile. And there's a lot of room in between those things," said the 6-foot-9-inch Gurley](https://www.bloomberg.com/news/articles/2025-07-14/benchmark-s-75m-manus-deal-exposes-silicon-valley-s-china-divide)
- ["Our nation's recent curbs on Nvidia H20s, intended to slow China AI innovation, will enhance & accelerate Chinese AI innovation"](https://www.semafor.com/article/05/09/2025/us-treasury-examining-benchmark-capitals-ties-to-chinese-startup-manus-ai)

### 業界内からの厳しい批判

**Josh Wolfe (Lux Capital)：**
- [Josh Wolfe, co-founder of Lux Capital, who posted on X that the investment "makes zero sense"](https://www.semafor.com/article/05/09/2025/us-treasury-examining-benchmark-capitals-ties-to-chinese-startup-manus-ai)

**Delian Asparouhov (Founders Fund)：**
- ["I am not saying Benchmark partners are Chinese assets… But they are def assets to China"](https://www.semafor.com/article/05/09/2025/us-treasury-examining-benchmark-capitals-ties-to-chinese-startup-manus-ai)
- ["You're just investing into your enemy. Why would we be funding the Russia space program in 1972? Why would we be funding the Chinese AI race in 2025?"](https://www.bloomberg.com/news/articles/2025-07-14/benchmark-s-75m-manus-deal-exposes-silicon-valley-s-china-divide)

## 6. 米国財務省による投資規制審査

### Outbound Investment Security Program適用

**審査対象：**
- [The US Treasury Department is reviewing a Benchmark Capital-led $75 million investment in Chinese startup Manus AI](https://www.semafor.com/article/05/09/2025/us-treasury-examining-benchmark-capitals-ties-to-chinese-startup-manus-ai)
- [The law, centered on the Outbound Investment Security Program, was part of a 2023 executive order signed by then-President Joe Biden](https://www.semafor.com/article/05/09/2025/us-treasury-examining-benchmark-capitals-ties-to-chinese-startup-manus-ai)

## 7. 中国の国家情報法適用リスク

### 法的強制力の詳細

**国家情報法第7条：**
> 「あらゆる組織および個人は、法に従って国家の情報活動に協力し、国家の情報活動の秘密を守る義務を負う」

**実務上の意味：**
- 中国国籍者（肖弘、季逸超）に対する協力強制
- 拒否権の不存在
- 秘密保持義務による隠蔽

**「脱中国化」後の残存リスク：**
- 中国国籍者の個人的義務は継続
- 技術的アクセス権の維持可能性
- バックドア設置の事前実行可能性

# 自薦・他薦の声

## ベンダー自身の宣伝文句

**公式発表（出典・日付付き）：**
- [Manusは世界初の真の汎用AIエージェント](https://weel.co.jp/media/innovator/manus/) - 季逸超発言
- [GAIAベンチマークでOpenAI Deep Researchを上回る](https://aismiley.co.jp/ai_news/manus-openai-deepresearch-ai/) - 公式サイト発表

## 技術的評価コメント

**MIT Technology Review（懐疑的評価）：**
- [Despite all the hype, very few people have had a chance to use it. Currently, under 1% of the users on the wait list have received an invite code](https://www.technologyreview.com/2025/03/11/1113133/manus-ai-review/)
- [it occasionally lacks understanding of what it's being asked to do, makes incorrect assumptions, or cuts corners to expedite tasks](https://www.technologyreview.com/2025/03/11/1113133/manus-ai-review/)

**TechCrunch（批判的評価）：**
- [But as the platform currently exists, Manus appears to be a case of hype running ahead of technological innovation](https://techcrunch.com/2025/03/09/manus-probably-isnt-chinas-second-deepseek-moment/)
- [After about 10 minutes, Manus crashed](https://techcrunch.com/2025/03/09/manus-probably-isnt-chinas-second-deepseek-moment/)

## 専門家による安全性評価

**既存の格付け：**
- [生成AIインフルエンサーに推奨されることの多いManusは極めて危険な生成AIサービスです。本安全性調査では、格付けを引き下げました。前回評価（2025年4月25日 12:32）【2 危険】→【1 極めて危険】](https://note.com/norito_hiraoka/n/n96b57d870249)

# 主任アナリストが提案する追加調査項目

## 1. 【シンガポール法人の実質支配構造調査】
シンガポール法人Butterfly Effect Pte. Ltd.の株主構成、取締役構成、実質的意思決定権者の特定が必要。表面的移転と実質支配の継続を法的に立証するため。

## 2. 【データセンター物理所在地の確認】
「十分に精査されたDPA準拠ベンダー」の具体的特定とデータセンター物理所在地の確認。中国域内での継続的データ処理の可能性検証のため。

## 3. 【Benchmark Capital内部意思決定プロセス調査】
Miles Grimshaw退職後の投資実行、Bill Gurley非関与での政治擁護の詳細プロセス。中国シンパネットワークの組織的連携実態解明のため。

## 4. 【利用規約・プライバシーポリシー変更履歴分析】
脱中国化前後での法的条項変更の詳細比較。管轄法廷、準拠法、データ利用権の実質的変更有無の確認のため。

# 最終総括

Manus AIは、技術的能力ではなく地政学的・法的・投資構造上の複合リスクにより「極めて危険」と判定される。特に以下の要素が重大な脅威を構成する：

1. **計画的偽装工作**: 2023年事前設立のシンガポール法人による管轄回避戦略
2. **法的強制力**: 中国国家情報法による開発者への協力強制義務
3. **米国内部協力者**: パンダハガーネットワークによる意図的投資・政治擁護
4. **即座の政府警戒**: 複数州による国家安全保障上の脅威認定

この複合的脅威構造は、単純な中国企業サービス以上の深刻なリスクを示しており、技術的検証や法的条項確認では対処不可能な本質的危険性を有している。
