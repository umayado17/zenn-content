---
title: "【レベル0】ByteDance「豆包/Cici/Dola」の利用規約二重構造:一次資料で読み解く『不矛盾な空白』という構造的欺瞞"
tags: [AI, セキュリティ, 中国, プライバシー, ByteDance]
private: false
slide: false
organization_url_name: ""
id: ""
updated_at: ""
ignorePublish: false
---

ByteDance は中国国内向け AI チャットボット「豆包(Doubao)」と、その海外版「Cici」(2025年12月に「Dola」へリブランド)を運営している。両者は UI もほぼ同一の事実上同一サービスだが、**利用規約・プライバシーポリシーは法的に全く異なる文書として設計されている**。本稿は両者の規約を一次資料で対比し、「中国法準拠の運用を否定せず、矛盾しないように書かれた」海外向け規約の構造的欺瞞を実証する。

- 対象AIサービス: 豆包(Doubao) / Cici / Dola
- 公式URL: [www.doubao.com](https://www.doubao.com/) / [www.dola.com](https://www.dola.com/)
- 安全性レベル: 0(使用不可)
- 厚黒学レベル: 該当 14/21 項目(検証可能範囲)
- 支配国名目国: 中国(海外版はシンガポール経由)

## エグゼクティブ・サマリー

ByteDance の AI チャットボットは、市場ごとにブランド名・運営主体・準拠法・データ保管場所を完全に分離した二重構造で提供されている。中国国内向け「豆包」は中華人民共和国法律準拠で北京春田知韵科技有限公司が運営し、データは中国国内に保管される。海外向け「Cici/Dola」はシンガポール法準拠で SPRING (SG) PTE. LTD. が運営し、データはインドネシア・マレーシア・シンガポール・米国に保管される。

本稿の最重要発見は、**海外向け規約が中国版の運用を否定する文書ではなく、矛盾しないように書かれた文書である**ことである。海外向け規約には中国国家情報法等への不適用を示す否認条項が一切存在せず、むしろ「Corporate Group 共有」条項により中国本土関連会社への導線を温存している。これは虚偽記述ではなく、選択的開示と選択的沈黙の組合せによる構造的欺瞞である。

- **法務判定**: 導入不可
- **技術判定**: 危険
- **主要リスク**:
  - 中華人民共和国国家情報法第7条の間接適用(海外向けユーザーデータが Corporate Group 経由で中国本土からアクセス可能)
  - データ越境規制を訓練済みモデル共有で迂回する設計
  - informed consent の実質的不成立(中国法管轄への導線を平均的ユーザーが推論不能)
  - 「Made in Singapore」を装う origin laundering(法的管轄の出自洗浄)
  - 米国市場の意図的排除による TikTok 規制リスクの先回り回避

## 詳細調査結果

### 取得した一次資料

本稿の全ての主張は以下の一次資料に基づく。

- [豆包 用户协議(2026年2月17日生効)](https://www.doubao.com/legal/terms)
- [豆包 隐私政策(2026年3月26日生効)](https://www.doubao.com/legal/privacy)
- [Dola Privacy Policy(2025年12月17日 Effective)](https://www.dola.com/legal/privacy/en)
- [Dola Terms of Service(2025年12月17日 Effective)](https://www.dola.com/legal/terms/en)

取得日: 2026年5月16日。すべて公式ドメインから `web_fetch` で直接取得した一次資料である。

### 技術アーキテクチャ分析

#### LLM バックエンドの二重構造

両サービスは UI が同一だが、内部の LLM バックエンドは異なる。

豆包(中国国内向け)は ByteDance 自社の Volcano Engine 基盤上で動作し、自社開発の Doubao 大型モデル(Seed 系)を使用する。

Cici/Dola(海外向け)は OpenAI GPT(Microsoft Azure 経由ライセンス)および Google Gemini を主力 LLM として使用する。これは Cici の Privacy Policy「How We Share Your Information - Standard Chatbots」セクションで以下のとおり明示されている。

> "When you interact with our chatbots, certain User Content and Automatically Collected Information may be shared with the third-party developers of integrated AI tools, including LLMs such as Gemini, to generate, optimise, and personalise output."

これは中国製 LLM を海外で使うことの政治的リスク(米中対立、輸出規制)を回避するための設計である。Wikipedia の ByteDance 記事および複数の独立した報道で確認されており、ByteDance は OpenAI API の利用について 2024 年初頭に一度アカウント停止を受けた経緯がある。

#### データ保管場所の分離

豆包 隐私政策 第4.1条「存储地点」は以下のとおり中国国内保管を明示する。

> 我们依照法律法规的规定,将在境内运营过程中收集和产生的你的个人信息存储于中华人民共和国境内。目前,我们不会将上述信息传输至境外。

これは中華人民共和国サイバーセキュリティ法第37条(重要情報基礎施設運営者の国内保管要件)への直接対応である。

Dola Privacy Policy「Supplemental Information - Brazil - International Transfers of Data」は以下のとおり海外複数拠点を明示する。

> We may store your personal data on secure servers located in Indonesia, Malaysia, Singapore, and the United States.

データの物理的所在地は完全に分離されている。しかし論理的アクセスは「Corporate Group」共有設計により分離されていない(後述)。

### 法的条項分析

#### 準拠法・訴訟管轄の完全な切り分け

豆包 用户協議 第13.1条/第13.2条は以下のとおり中国法準拠・北京海淀区裁判所管轄を明示する。

> 13.1 本协议的成立、生效、履行、解释及争议的解决均应适用中华人民共和国法律。
>
> 13.2 本协议的签订地为中华人民共和国北京市海淀区。若你与公司发生任何争议,双方应尽量友好协商解决,如协商不成,你同意应将争议提交至本协议签订地的人民法院诉讼解决。

Dola Terms of Service 第16条(a)「Applicable Law and Jurisdiction」は以下のとおりシンガポール法準拠・SIAC 仲裁を明示する。

> Subject to the "Supplemental Terms – Jurisdiction Specific", these Terms, their subject matter and their formation, are governed by the laws of Singapore. Any dispute arising out of or in connection with these Terms... shall be referred to and finally resolved by arbitration administered by the Singapore International Arbitration Centre ("SIAC")...

同じ ByteDance グループが運営する同じ機能のサービスに、完全に異なる法体系が適用される設計である。

#### 国家機関への提供条項の言語的差異

豆包 隐私政策 第1.12条(同意取得不要の例外)は以下のとおり国家機関への協力を明示する。

> a. 与我们履行法律法规规定的义务相关的;
> b. 与国家安全、国防安全直接相关的;
> c. 与公共安全、公共卫生、重大公共利益直接相关的;
> d. 与刑事侦查、起诉、审判和判决执行等直接相关的;

第3.4条(同意なし第三者提供の例外)も同様に「国家安全、国防安全」「刑事侦查、起诉、审判和判决执行」を理由とした提供を明示する。これらは中華人民共和国国家情報法第7条/第14条、サイバーセキュリティ法第28条の運用条項そのものである。

Dola Privacy Policy「Legal Obligations and Rights」は対応条項を以下のとおり曖昧化する。

> We may share the information described in "What Information We Collect" with certain competent law enforcement, regulatory or government agencies, courts, or other third parties if we have a good faith belief that it is necessary to:
> ● Comply with a legal obligation;
> ● Lawfully protect and defend the rights, property, safety, and security of the Services, our users, copyright holders, and others;
> ● Investigate potential violations of and enforce our Terms of Service and other policies; or
> ● Detect, investigate, and prevent against fraud, technical issues, copyright infringement, or other misleading or illegal activities.

「competent」「government agencies」「good faith belief」と一般化されており、どの国の政府機関を想定するかは明示されない。

#### 生成AI規制への準拠先の差

豆包 用户協議 第5.2.2条は中華人民共和国の生成 AI 規制パッケージへの完全準拠を以下のとおり明示する(抜粋)。

> 你输入、输出/生成、制作、评论、上传、发布、传播的信息应自觉遵守...遵守公共秩序,尊重社会公德和伦理道德、社会主义核心价值观、国家利益...等"七条底线"要求。
>
> (1)反对宪法确定的基本原则的;
> (2)危害国家安全和利益,泄露国家秘密的;
> (3)颠覆国家政权,推翻社会主义制度、损害国家形象、煽动分裂国家、破坏国家统一和社会稳定的;
> (4)损害国家荣誉和利益的;

これは中華人民共和国「生成式人工智能服务管理暂行办法」(2023年8月15日施行)第4条、および「互联网信息服务深度合成管理规定」(2023年1月10日施行)の禁止条項そのものである。同条第6.4条では生成AIコンテンツへの AI 標識義務も明示されている。

Dola Terms of Service 第5条は対応条項を以下のとおり西側規制パッケージに沿って構成する(抜粋)。

> - use the Services for the purpose of engaging or assisting in illegal or high risk activities, such as: military and warfare; development of weapons, explosives, or dangerous materials...purposes which are illegal under local laws where you are based or are using the Services, such as the EU AI Act.
> - use the Services for political purposes (e.g., building conversational or interactive bots for political campaigning or advocacy or lobbying purposes);

EU AI Act への準拠が明示され、Australia 向けには Online Safety Act 2021 対応、EU 向けには Digital Services Act 対応の Supplemental Terms が用意されている。中国の生成 AI 管理弁法・深度合成管理規定への言及は一切ない。

### 地政学的リスク評価

#### 運営主体構造

ByteDance の支配構造は以下のとおりである。

- ByteDance Ltd.(ケイマン諸島本社、Variable Interest Entity 構造)
- 北京字节跳动科技有限公司(ByteDance 中国本土親会社)
- 北京春田知韵科技有限公司(豆包の運営主体、中国本土法人、ByteDance 子会社)
- SPRING (SG) PTE. LTD.(Cici/Dola の運営主体、シンガポール法人、ByteDance 子会社)

豆包 用户協議 第1条は運営主体を明示する。

> 北京春田知韵科技有限公司及/或关联方(以下简称"公司"或"我们")...

Dola Terms of Service 第1条は運営主体を以下のとおり明示する。

> Dola is provided by SPRING (SG) PTE. LTD., with its address at 77 ROBINSON ROAD #06-03, ROBINSON 77, SINGAPORE (068896)...

Dola の規約本文中に「ByteDance」「字节跳动」「北京」「中華人民共和国」の文字は一切登場しない。例外は Privacy Policy「Brazil」Supplemental の DPO 連絡先のみであり、そこでは以下のとおり ByteDance ドメインを使用している。

> DPO. You may contact the Data Protection Officer by emailing: dpobrasil@bytedance.com.

LGPD(ブラジル一般データ保護法)の DPO 開示義務によって、ByteDance との関連が事実上開示される構造になっている。これは規約設計の意図せざる露呈である。

#### 中華人民共和国法律の間接適用

ByteDance グループは中国本土親会社を頂点とする企業集団である。中華人民共和国国家情報法第7条は「いかなる組織および公民も、法に基づき国家の情報活動の業務を支持・援助・協力し、知り得た国家情報活動に関する秘密を保持しなければならない」と規定する。同法第14条は「国家情報機関は、情報活動の遂行のため、関係機関・組織および公民に対し必要な支持・援助・協力の提供を求めることができる」と規定する。

これらの条項は中国法人である北京字节跳动科技有限公司・北京春田知韵科技有限公司に直接適用される。シンガポール法人 SPRING (SG) PTE. LTD. に直接適用されないが、SPRING (SG) PTE. LTD. のデータが「Corporate Group」共有設計により中国本土関連会社からアクセス可能である限り、**アクセスした時点で中国法の管轄下に入る**。

Dola Privacy Policy「Our Corporate Group」セクションは以下のとおり Corporate Group 内共有を明示する。

> We share the information described in "What Information We Collect" with members of our Corporate Group. Our Corporate Group may use your information in a manner consistent with this Privacy Policy, including for functions like: storage, content delivery, security, research, analytics, customer and technical support, product and technology improvement and development, including AI model training, and content moderation. Subject to applicable laws, AI models improved using personal information may be utilised by entities within our Corporate Group.

「Corporate Group」の構成員は明示されておらず、北京字节跳动科技有限公司を含む中国本土関連会社が含まれるか否かを規約から推論することはできない。

#### 米国市場の意図的排除

Dola は米国・カナダ・中国・オーストラリアで利用不可である(複数の独立した報道で確認)。これは TikTok 規制リスクの先回り回避戦略である。

Dola Terms of Service 第16条(j)「Trade Controls」では、米国に LLM ホスティングインフラの一部が存在することが間接的に開示されている。

> You understand that your use of Services, providing Input to and obtaining Output via Services, might be subject to the laws and regulations of export controls and sanctions laws (collectively "Trade Control Laws") where the generative AI models are hosted (including, without limitation, the United States)...

つまり、米国ユーザーにはサービスを提供しないが、米国インフラは使用するという構造である。

### 厚黒学的要素の検証

NK001 v2.0 の21項目チェックリストに照らして検証した結果、検証可能な範囲で **14 項目が該当** した。

#### 該当した主要項目

- [x] 05. ステルスマーケティング(Cici/Dola の ByteDance 関連性を 2024 年 Forbes 暴露まで規約に未記載)
- [x] 08. ToS深層条項(用户協議 第13.1/13.2条の中国法準拠規定は文末配置)
- [x] 09. オプトアウト選択肢欠如(学習データ利用のオプトアウト UI の実効性が不透明)
- [x] 10. 包括同意強制(「使用即同意」設計)
- [x] 11. サブプロセッサ不透明(海外向け規約で「Corporate Group」構成員を明示せず)
- [x] 12. 一方的責任転嫁(両規約とも極端な免責条項)
- [x] 13. セキュリティ監査情報の非開示(SOC2 / ISO27001 等の認証情報の規約記載なし)
- [x] 14. 企業秘密による技術詳細開示拒否
- [x] 15. AI倫理審査体制の不在(モデル運用ガバナンス枠組み未開示)
- [x] 16. 統合システム連携の非開示(ByteDance 内クロスサービス連携の具体的構成を非開示)
- [x] 17. 「単体サービス」偽装(Cici/Dola を独立シンガポール法人サービスと印象付け)
- [x] 19. データ越境・保存場所の不明示(海外向けで「outside of the country where you live」と曖昧化)
- [x] 20. 削除権の事実上の機能不全(学習済みモデルからの削除不能を明示せず)
- [x] 21. 経営者・投資家・最終受益者の隠蔽(海外向け規約での ByteDance 関連性の構造的隠蔽)

NK008 v2.1 判定基準では「9項目以上 = 厚黒学的リスク高、安全性レベル 2 以下が妥当」。本件は 14 項目該当に加え、NK008 第2-2項(中華系自動判定)発動により **安全性レベル 0** が確定する。

### 統合監視システム連携分析

ByteDance グループは以下の主要サービスを横断的に運営する。

- Douyin(中国国内向け TikTok、月間アクティブユーザー数億)
- TikTok(海外向け、グローバル)
- 豆包(中国国内向け AI チャットボット)
- Cici/Dola(海外向け AI チャットボット)
- Toutiao(中国国内向けニュースアプリ)
- CapCut(動画編集アプリ、グローバル)
- Lemon8(SNS、グローバル)

豆包 隐私政策 第1.1条 d は抖音(Douyin)アカウントとの直接バインドを以下のとおり明示する。

> 你可以使用抖音账号登录并绑定豆包账号...绑定状态下,你可以通过该抖音账号在豆包内直接使用抖音及抖音关联版本产品...的服务。

これは中国国内向けでのクロスサービス名寄せ設計の自己開示である。海外向け Dola Privacy Policy では「Corporate Group」内共有として抽象化されており、TikTok との具体的連携の有無は明示されていない。

GDAS(Global Digital Dang'an System、統合監視システム)への組込みについては DK006 を参照した詳細評価が必要であり、本稿の範囲を超える。本稿は規約一次資料の対比に限定する。

## 「不矛盾な空白」という構造的欺瞞(本稿の最重要論点)

ここまでで述べた構造を、より精密に再定式化する。本節は本稿の最重要論点である。

### 問題の本質

海外向け規約の問題は **何が書かれているか** ではなく **何が書かれていないか** にある。具体的には、海外向け規約には、以下のような **積極的な否認条項が一切存在しない**。

- 「我々は中国政府機関への情報提供を行わない」
- 「我々は中国国家情報法に基づく協力要請を受けない・受けても応じない」
- 「我々のデータは中国本土の関連会社からアクセスされない」
- 「我々は中国の刑事捜査・国家安全捜査に協力しない」
- 「我々のサービスは中華人民共和国の法的管轄下にない」

これらの否認条項が一つでも書かれていれば、海外版は「中国版と法的に異なるサービス」であることを **積極的に表明** したことになる。しかし書かれていない。書かれていないが故に、**中国国内向け規約に書かれた運用は、海外向けでも法的に排除されていない**。

すなわち、海外向け規約は中国版の運用を **否定する文書ではない**。同じ運用が **適用される余地を残したまま**、表面上は西側規制への準拠を表明する文書である。

### 「Corporate Group」という名の架け橋

決定的なのは、海外向け規約に **積極的に書かれている数少ない条項** が、上記の「不矛盾な空白」を埋める方向に機能していることである。Dola Privacy Policy「Our Corporate Group」セクションは前掲のとおり以下を明示する。

> "AI models improved using personal information may be utilised by entities within our Corporate Group."

「Corporate Group」の構成員は明示されていない。しかし ByteDance グループには北京の関連会社が含まれており、それらは中華人民共和国国家情報法第7条/第14条の管轄下にある。

したがって海外向け規約は、構造的に以下を意味する。

1. 中国版に書かれた運用への導線を否定しない(不作為による許容)
2. 同時に、その導線を実装するための条項を積極的に提供する(作為による準備)

この二重構造こそが、本稿の最重要発見である。

### これが「詐欺的」である理由

通常の詐欺は「虚偽の事実を述べる」ことで成立する。しかし本件の手法は **虚偽を一切述べない**。海外向け規約のすべての記述は技術的に真実である。

- SPRING (SG) PTE. LTD. は確かにシンガポール法人(真実)
- シンガポール法が準拠法である(真実)
- データは Indonesia, Malaysia, Singapore, USA に保管される(真実)
- GDPR/DSA/EU AI Act/LGPD 等への準拠を表明している(真実)

しかし、**「これらが真実である」ことと、「中国法の管轄が及ばない」ことは、論理的に等価ではない**。にもかかわらず、平均的なユーザーは前者を読んで後者を推論してしまう。

これは法的な意味での詐欺ではなく、**認知的詐欺**(cognitive fraud)、より正確には **構造的欺瞞**(structural deception)である。事実関係の操作ではなく、選択的開示と選択的沈黙の組合せによって、ユーザーに誤った推論をさせる手法である。

### informed consent 成立への疑義

GDPR 第6条/第7条、PIPL 第14条、LGPD 第8条を含む現代の個人情報保護法は、データ処理の法的根拠として informed consent(情報を与えられた上での同意)を要求する。しかし本件では以下のとおりである。

1. ユーザーは「シンガポール法人運営・シンガポール法準拠」を読んで同意した
2. しかし実態は「ByteDance グループ全体へのアクセス許諾」(間接的に中国本土含む)であった
3. 後者を知っていれば同意しなかったユーザーが存在しうる

この場合、**そもそも informed consent が成立していたのか** という論点が生じる。法的判断は管轄により異なるが、倫理的には明確に成立していない。ユーザーは「情報を与えられた上で」同意したのではなく、「選択的に隠された情報のせいで誤った推論をした上で」同意したからである。

### 一句で要約すれば

> 海外向け規約は、中国版の運用を否定する文書ではなく、中国版の運用と矛盾しないように書かれた文書である。

この一句が、本分析全体の最も精密な要約である。

## 推奨対応

### 即座の対応

- **豆包(Doubao)**: 業務利用および個人利用のいずれも禁止。すでに利用している場合は即座にアカウント削除、入力履歴の削除要求、関連デバイスからのアプリ削除。
- **Cici/Dola**: 同上。シンガポール法人運営であっても Corporate Group 共有設計により実質的リスクは Doubao と同等。
- **TikTok / Douyin / CapCut / Lemon8**: 本稿の分析範囲外だが、同じ ByteDance グループ運営である以上、同等の構造的リスクを内包する可能性が高い。組織として横断的に利用方針を見直すことを推奨。

### 代替案

業務用 AI チャットボットとして以下を検討すべきである(各社の利用規約・データ保管場所・準拠法を独立に評価した上で選択)。

- OpenAI ChatGPT(米国 OpenAI 運営、米国法準拠)
- Anthropic Claude(米国 Anthropic 運営、米国法準拠)
- Google Gemini(米国 Google 運営、米国法準拠)
- Microsoft Copilot(米国 Microsoft 運営、米国法準拠、エンタープライズ向けデータ保護コミットメントあり)
- 日本国内事業者の Sovereign AI 系サービス(法務評価を行った上で)

### 監視項目

- ByteDance グループの組織再編(特に Cici/Dola の運営主体が他のシェルカンパニーに移管された場合)
- 豆包・Cici/Dola の規約改訂(否認条項が新規追加された場合は再評価が必要)
- 中国 CAC(国家互联网信息办公室)による豆包の登録・処分情報
- 米国・EU・各国当局による ByteDance 関連の規制動向

## 追加調査項目

本稿はコア対比に絞ったため、以下は別稿で取り扱う。

1. 中国国内向け豆包の副次規約(社区公约、账号服务须知、AI云盘使用须知、AI分身使用须知、算法推荐说明)の精査
2. TikTok と Douyin の規約二重構造の対比(本稿手法の第2事例化)
3. 同手法の他中華系企業への横展開: Alibaba(通義千問/Qwen)、Tencent(混元/WeChat International)、Baidu(文心一言)、DeepSeek 等
4. 豆包と Cici/Dola のモデルバックエンド分離の技術的実証(API レスポンスフィンガープリント等)
5. ByteDance グループの完全な支配構造図の作成(VIE 構造を含む)
6. NK001 v2.0 への新項目「必要な否認条項の選択的欠落」追加の正式化

## 最終総括

ByteDance の豆包と Cici/Dola は、市場ごとに別ブランド・別運営主体・別準拠法・別データ保管場所を立てた典型的な二重規約構造で運営されている。中国国内向け規約は中華人民共和国法律準拠を明示し、国家機関への同意なし提供、データの中国国内保管、生成 AI 管理弁法への完全準拠を含む。海外向け規約はシンガポール法準拠を明示し、GDPR・DSA・EU AI Act・LGPD 等への準拠を表明し、中国法への言及を一切排除している。

しかし海外向け規約は、中国版の運用を **否定する文書ではない**。中国国家情報法の不適用を示す否認条項が一切なく、むしろ「Corporate Group 共有」設計により中国本土関連会社への導線を温存している。これは虚偽記述による詐欺ではなく、**選択的開示と選択的沈黙の組合せによる構造的欺瞞** である。平均的ユーザーは海外向け規約を読んで「中国法の管轄が及ばない安全なサービス」と推論してしまうが、その推論を支える法的根拠は規約のどこにも存在しない。

技術者・法務担当者がこの種の中華系 AI サービスを評価する際には、規約の **肯定的記述** だけでなく、**規約に書かれていない否認条項の不在** こそを評価対象とすべきである。「Corporate Group」「Affiliates」「Group Companies」等の抽象表現を用いる規約に対しては、その構成員の網羅的開示を要求すべきであり、開示されない場合はハイリスクと判定すべきである。

本稿の手法は、Alibaba・Tencent・Baidu・DeepSeek を含む他のすべての中華系 AI サービス評価に直接横展開可能である。今後の評価実務において、「不矛盾な空白」分析フレームを標準化することを強く推奨する。

---

*本稿は 2026年5月16日時点の公開規約に基づく。規約の改訂状況については上記の公式 URL で随時確認されたい。*

*分析手法および全データ対比については一次資料保全レポート「Doubao_TOS_中国国内版vs海外版_比較分析_v1_1.md」(社内資料)を参照。*
