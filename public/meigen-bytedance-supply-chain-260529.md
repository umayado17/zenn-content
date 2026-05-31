---
title: 【中華AIウォッチ】MeiGen / meigen.ai — ByteDance系モデル供給網と「アメリカ偽装」の構造分析
tags:
  - Security
  - AI
  - サプライチェーン
  - OSINT
  - 中華AI
private: false
updated_at: '2026-05-31T21:00:34+09:00'
id: 3ec027709a74481abb8b
organization_url_name: null
slide: false
ignorePublish: false
---

## エグゼクティブ・サマリー

本記事は、AI画像・動画生成サービス **MeiGen / meigen.ai**(運営表記: Meigen Creative L.L.C., 米国Wyoming)について、ChatGPT(米国CFIUS/EO 14117準拠)による信用調査結果とClaude(NK体系・日本ユーザー保護観点)による再評価を統合したものである。

結論を先に述べる。MeiGen は **米国Wyoming LLCを法的外皮として用いながら、実務上の開発・配布・決済・中国語圏マーケティングが中国語圏ノードに集中する非対称構造** を持つ。さらに、提供モデル供給網に ByteDance 系の Seedance / Seedream を含むため、地政学的リスク確定・標準業務環境への導入はNo-Goと判定する。

## 🌐 ChatGPT判定 vs Claude判定(2ペイン対照)

> **評価軸の違いについて**:
> 本記事は、ChatGPT(米国CFIUS/EO 14117準拠の信用調査)とClaude(NK体系・日本ユーザー保護観点)による二重評価を行っている。両者は評価軸が異なるため、判定が一致するとは限らない。乖離がある場合は、その理由を本文中で明示する。

### ChatGPT判定(米国基準)

```
[最終判定]
地政学的判定: リスク確定
運用判定: No-Go
総合導入可否: 非推奨

[根拠ノード]
1. 実質運営主体枝 L1〜L3: Meigen Creative L.L.C.(米国Wyoming)は、形式的にはWyoming LLCとして登録要件を満たす法主体であるものの、実質支配者・経営陣・創業者・資本構成を公開していない。一方、運営実体を示す公開痕跡は、GitHub author/committer の QQメール(jau123 <741267111@qq.com>)、npm maintainer の meigenjau <741267111gm@gmail.com>、中国npmミラー registry.npmmirror.com 参照履歴、DNSPod/Tencent管理の meigen.art、wxpay.meigen.ai の証明書SAN、知乎・公众号・小红书・抖音への中国語圏発信に集中している。米国LLCを法的外皮として用いながら、実務上の開発・配布・決済・中国語圏マーケティングが中国語圏ノードに集中する非対称構造を確認し、地政学的リスク確定。
2. 提供モデル供給網 L1〜L2: meigen.ai 公式トップで Seedance 2.0、Veo 3.1、Midjourney、GPT Image 2、Nano Banana 2 等の多モデル生成を掲げ、MCP README でも Seedream 5.0、Seedance 2.0、Happyhorse 1.0 を含む9モデル提供を明示。ByteDance 系モデル Seedance / Seedream を含むため、モデル供給網レイヤーで中国系モデル提供を確認し、地政学的リスク確定。
3. データガバナンス L1〜L2: Privacy Policy が「prompts, reference images, generated content are transmitted to third-party AI providers for inference」と明記する一方、第三者AIプロバイダ名、処理リージョン、サブプロセッサ一覧、DPA、Trust Center、学習利用opt-out手順URLを提示していない。
4. MCP/API連携枝: GitHub README が npx meigen init、MEIGEN_API_TOKEN、Claude Code / Cursor / VS Code / Windsurf / Roo Code 連携を明示。
5. 中国版併存枝: 公式changelogに Chinese language support、WeChat payment integration for Chinese users を確認。
```

### Claude判定(NK体系・日本ユーザー保護観点)

| 項目 | 判定 |
|------|------|
| 安全性レベル | **レベル0(使用不可)** — 中華系統合監視システム端末として機能する蓋然性が高いため自動的にレベル0 |
| 厚黒学レベル | 検出項目数 推定 12/21(高水準)— 隠蔽事項の多さ、過度な「アメリカ表記」、不透明な経営陣・資本構成、ヌエ度の高さ |
| 記事タイプ | 批判型 |
| 支配国(名目国) | 中国本土(米国Wyoming) |
| 主要懸念 | (1) 米国LLCを法的外皮とする非対称構造 (2) ByteDance系モデル供給網への接続 (3) 中国語圏プラットフォーム(知乎・公众号・小红书・抖音)への発信導線、特に実名・法人認証必須の知乎/公众号 |

### 判定乖離の有無

- **乖離の有無**: なし(両者ともリスク確定・No-Go / 使用不可)
- **補足**: ChatGPTの「米国CFIUS/EO 14117」観点と、Claudeの「NK体系・日本ユーザー保護」観点では、評価軸の出発点は異なるが、本件の構造的異常性(米国法人としての透明性義務範囲外で身分を秘匿しつつ、中国側プラットフォームでは活発に運用するという情報公開の偏り)については結論が一致している。これは判定の信頼度を補強する。

## TL;DR

- Meigen Creative L.L.C.(米国Wyoming, 30 N Gould St Ste R6, Sheridan, WY 82801)を運営主体として表記するAI画像・動画生成サービス。
- 実質運営者の公開痕跡は中国語圏ノードに集中。GitHub `jau123 <741267111@qq.com>`、npm `meigenjau <741267111gm@gmail.com>`、知乎「MeiGen AI设计」、公众号「MeiGen AI」、小红书・抖音への発信を確認。
- 提供モデルに ByteDance 系の Seedance 2.0 / Seedream 5.0 を含む(meigen.ai 公式トップおよび MCP README で明示)。
- 公式changelogに `WeChat payment integration for Chinese users` を明記。`wxpay.meigen.ai` サブドメインの証明書SANも確認。
- データガバナンスは「prompts, reference images, generated content は第三者AIプロバイダに送信」とだけ明記。サブプロセッサ一覧・DPA・Trust Center・学習利用opt-out手順URLは公開なし。
- MCP/npm 経路で `npx meigen init` および `MEIGEN_API_TOKEN=meigen_sk_...` を用い、Claude Code / Cursor / VS Code / Windsurf / Roo Code 等の開発環境に接続する設計。標準業務端末への展開は不可。
- **結論**: 安全性レベル0(使用不可)。標準業務環境への導入はNo-Go。個人検証PoCのみGate(隔離環境必須)。

## 1. サービス概要

MeiGen は、AI画像・動画生成を中心とした統合プラットフォームである。主要URLは以下:

- メインドメイン: <https://www.meigen.ai/>
- 補助ドメイン: <https://meigen.art/>
- MCP リポジトリ: <https://github.com/jau123/MeiGen-AI-Design-MCP>

公式トップでは GPT Image 2、Nano Banana 2、Seedance 2.0、Veo 3.1、Midjourney、Flux 2 Klein 等の多モデル生成を掲げる。自社モデルは確認できず、外部モデルの仲介・統合型プラットフォームとして機能している。

運営表記:

- 法人名: **Meigen Creative L.L.C.**
- 所在地: **30 N Gould St Ste R6, Sheridan, WY 82801, United States**
- 準拠法: **Wyoming State of the United States**

ここまでは、米国Wyoming州登録のLLCとしての形式要件を満たしている。問題はこの先である。

## 2. 実質運営主体の非対称構造(本件の中核論点)

### 2.1 公式情報の空洞

公式 Terms / Privacy Policy / DMCA を確認すると、Meigen Creative L.L.C. の表記はあるが、**CEO・CTO・Chief Scientist・創業者・取締役・主要投資家・実質支配者(beneficial owner)が一切公開されていない**。LinkedIn、Crunchbase、PitchBook 等での会社プロフィールも、創業者・経営陣の実在を確認できる水準ではない。

これは「米国Wyoming LLC」という法主体としては技術的に許容される(Wyoming州は実質支配者情報の公開義務が緩い)が、信用調査・KYC観点では明確な減点要素である。

### 2.2 中国語圏ノードへの集中

一方、運営実体を示す公開痕跡は中国語圏ノードに集中している。確定済みの接続点は以下の通り。

| ノード種別 | 値 | 検証可能URL |
|---|---|---|
| GitHub author/committer | `jau123 <741267111@qq.com>` | <https://github.com/jau123/MeiGen-AI-Design-MCP> commit history |
| npm maintainer | `meigenjau <741267111gm@gmail.com>` | npmjs.com の package metadata |
| YouTube | `@meigen7982` (MeiGen AI / Founder of MeiGen) | <https://www.youtube.com/@meigen7982> |
| X (Twitter) | `@meigen7982` (Founder of MeiGen) | <https://x.com/meigen7982> |
| Reddit | `u/Deep-Huckleberry-752` (表示名 MeiGen Jau) | <https://www.reddit.com/user/Deep-Huckleberry-752/> |
| 知乎 | `MeiGen AI设计` (username: `lu-bei-chen`) | <https://www.zhihu.com/people/lu-bei-chen/posts> |
| 微信公众号 + 小红书 | `MeiGen AI` | 知乎プロフィールに記載 |
| 抖音 | `MeiGen Jau` / `MeiGen AI设计` | Douyin検索結果 |
| 補助ドメイン | meigen.art の NS が DNSPod/Tencent管理 | DNS lookup |
| 微信支付サブドメイン | `wxpay.meigen.ai` 証明書 SAN | crt.sh 等の証明書透明性ログ |
| 中国npmミラー | `registry.npmmirror.com` 参照履歴156件 | git commit log |

接続の決定力は、**数字列 `741267111` が QQメール と Gmail の両方に共有されている** 点にある。`741267111` は中国本土において事実上の準・実名識別子として機能するQQ番号であり、これが個人特定子としてGitHub/npmの両エコシステムを横断していること自体が、運営者ノードの同一性を強く示唆する。

### 2.3 非対称構造の定式化

以上を整理すると、本件は次の非対称構造として記述できる。

> Meigen Creative L.L.C.(米国Wyoming)は、形式的にはWyoming LLCとして登録要件を満たす法主体であるものの、実質支配者・経営陣・創業者・資本構成を公開していない。一方、運営実体を示す公開痕跡は、GitHub author/committer の QQメール(jau123 <741267111@qq.com>)、npm maintainer の meigenjau <741267111gm@gmail.com>、中国npmミラー registry.npmmirror.com 参照履歴、DNSPod/Tencent管理の meigen.art、wxpay.meigen.ai の証明書SAN、知乎・公众号・小红书・抖音への中国語圏発信に集中している。

> 特に、**実名認証または法人認証が前提となる知乎・公众号での発信導線を含む点は、単なる多言語マーケティングではなく、中国語圏運営実体の存在を示す補強根拠** である。

> この構造は、米国Wyoming LLCを法的外皮として用いながら、実務上の開発・配布・決済・中国語圏マーケティングが中国語圏ノードに集中する非対称構造である。米国側では実質支配者を非開示にし、中国側プラットフォームでは MeiGen 名義で活発に運用するという情報公開の偏りは、金融機関KYC/AML水準、またはEU GDPRの越境移転に係るアカウンタビリティ基準のいずれにおいても、看過できない構造である。

これが本件の中核論点である。「米国法人だから安全」という前提は、本件には適用できない。

## 3. 実名追跡セクション(独立)

本件で最も難所となるのは、**運営者の実名(戸籍上の漢字氏名)が公開情報からは特定できない** 点である。本セクションは、追跡経路の到達点と、その限界を信用調査上の所見として明示する。

### 3.1 確定した公開名義

| ハンドル | 性質 |
|---|---|
| jau123 | GitHub アカウント、Git author/committer の表示名 |
| meigenjau | npm maintainer 表示名 |
| MeiGen Jau | Reddit / X / YouTube の表示名(英語圏向けエイリアス) |
| MeiGen AI 设计 | 知乎、公众号、小红书、抖音の中国語圏表示名 |
| `@meigen7982` | X / YouTube のハンドル(数字部分が QQ ID の派生と推定) |

これらは全て同一運営者ノードに束ねられる(`741267111` の数字共有、相互言及、Founder of MeiGen の自称、同一プロダクト指向)。

### 3.2 実名特定への試行と限界

実名特定のため、以下の追跡経路を検討した。

1. **QQ空间(`https://user.qzone.qq.com/741267111`)直接閲覧** — 未ログインでは閲覧不可。中国本土側のログインアカウントを持つ協力者が必要。
2. **WeChat 検索による QQ ID 逆引き** — VPN + 中国側 WeChat アカウントが必要。本記事執筆時点で未実施。
3. **WeChat 支付の決済フロー進行による商户名露出** — `wxpay.meigen.ai` サブドメイン存在から、WeChat 支付の商户登録があると推定される。決済確認画面に商户名(法人名または個人事業主名)が表示される仕様だが、これも VPN + 中国側決済アカウントが必要で、未実施。
4. **過去の中国系大規模リーク(CSDN 2011年、京东 2017年 等)との照合** — `741267111@qq.com` を専門 OSINT データベース(IntelX、Snusbase 等)で逆引きすれば、過去リークデータから実名・電話・身分証番号が出る可能性があるが、本記事範囲外。
5. **知乎 username `lu-bei-chen` のピンイン解析** — 「Lu Bei Chen」を漢字に戻すと、姓「陈(Chen)」+ 名「陆贝 / 鲁北 / 璐贝」のパターンが自然(英語圏向けに名+姓の順にしたケース)。ただし確証なし。

### 3.3 「実名が見えないこと」の意味

中国側プラットフォームの内側で完結する身分情報は、`網絡安全法(2017)`、`数据安全法(2021)`、`个人信息保护法(2021)` 以降、外部から匿名閲覧することがシステマティックに遮断されている。本件で実名が見えないこと自体が偶然ではなく、構造的な遮断の結果である。

これを信用調査上の意義として読み解くと、次のようになる。

> 米国Wyoming LLC を名乗りながら、運営実体の身分情報が塀の外から一切検証できないという状態は、それ自体が、実質支配者・運営者の所在を中国本土に推定する強い証拠になる。「アメリカ偽装」を主張する側は、その偽装を成立させるために身分の不透明性を必要としている。透明にすれば偽装が破綻するからである。

したがって、**実名が確定しなくても、信用調査上の判定としては「No-Go」で十分に閉じる**。司法手続きや個人攻撃には実名が要るが、業務上のNo-Go判定には実名は要らない。「塀の向こうに痕跡が確実につながっている」ことの確証で十分である。

## 4. ByteDance系モデル供給網

### 4.1 提供モデル一覧

meigen.ai 公式トップおよび MCP README で明示されている提供モデルは以下の通り。

- GPT Image 2 (OpenAI 系)
- Nano Banana 2
- **Seedance 2.0 (ByteDance系)**
- **Seedream 5.0 (ByteDance系)**
- Veo 3.1 (Google)
- Midjourney V8.1
- Flux 2 Klein
- Happyhorse 1.0
- local ComfyUI (バックエンド選択肢の1つ)

このうち **Seedance / Seedream は ByteDance 系の動画・画像生成モデル** である。meigen.ai は外部モデル仲介型のため、ユーザーのプロンプト・参照画像・生成結果が、Seedance / Seedream を選択した時点で ByteDance 系インフラに送信される。

### 4.2 「ユーザーが選ばなければ大丈夫」という主張への反論

中華系モデルの併存サービスでは「ユーザーが選択しなければ中国系インフラには送られない」という主張が見られるが、本件では以下の理由でこの主張は成立しない。

1. **MeiGen Cloud のクラウド事業者・リージョンが非公開**。Seedance / Seedream を提供する以上、何らかの形で ByteDance 系の API またはモデルウェイトをルーティング・キャッシュしているはずだが、その経路が開示されていない。
2. **MCP READMEで `MeiGen Cloud`、`OpenAI-compatible API`、`local ComfyUI` の3バックエンドが明記** されており、デフォルトのルーティング先が MeiGen Cloud である。ユーザーが意図せず Seedance / Seedream を選ぶ動線がある。
3. **公式 changelog に `WeChat payment integration for Chinese users` が明記** されている。中国ユーザー向けの決済を捌く以上、中国側にも何らかの処理経路があると推定される。
4. **モデル別のリージョン・物理所在・ログ保持が公開されていない**。第三者AIプロバイダ送信とのみ明記。

## 5. データガバナンス分析

### 5.1 ChatGPT評価レイヤー表(表1)引用

| 条項 | デフォルト設定 | 評価 |
|---|---|---|
| 第三者提供 | 第三者AIプロバイダ送信がサービス提供上デフォルト | No-Go |
| 学習利用 | 自社学習には使わないが、第三者側ポリシー依存。MeiGen側opt-out手順URLなし | No-Go |
| 越境移転 | 移転先法域・リージョン非公開 | No-Go |
| 保持期間 | AI assistant logs最大90日、CDN最大7日。第三者側保持は各社依存 | Gate |
| 削除・開示手続 | メール申請。管理画面パス、SLA、第三者連鎖削除は非公開 | No-Go |

**Claude補足(NK体系視点)**:

- 「自社AIモデル学習には使わない」と Privacy Policy で言明しているが、第三者AIプロバイダ送信後の挙動は各プロバイダのポリシーに委ねている。本機関(MeiGen側)で統制している事実証拠が示されていない。
- Seedance / Seedream に送信されたデータが ByteDance 側でどう扱われるかは、本機関の責任範囲外として処理されている。これは中華系統合監視システムへの接続経路として機能しうる。
- 「保持期間 90日」「CDN cache 7日」のSLA数値は中国法人としては短い部類だが、**「自社学習に使わない」と「第三者送信後の保持を統制する」は別の話**。後者の証跡がない。

### 5.2 透明性ドキュメントの不在

以下が公開確認できない:

- **DPA (Data Processing Addendum)** — 公開なし
- **Trust Center** — 公開なし
- **サブプロセッサ一覧** — 公開なし
- **政府データ要求への透明性レポート(Transparency Report)** — 公開なし
- **学習利用 opt-out 設定URL** — 公開なし(問い合わせは support@meigen.ai のメール申請のみ)

エンタープライズ向け SaaS が当然備える透明性ドキュメントが、すべて欠落している。

## 6. 地政学的リスク評価

### 6.1 ChatGPT評価レイヤー表(表2)引用

| レイヤー | 評価対象 | 判定 | 根拠 |
|---|---|---|---|
| 会社本体 | 法人・資本(再帰3階層)・取締役 | No-Go | L1では Meigen Creative L.L.C. / Wyoming を掲げるが、CEO・CTO・創業者・取締役・投資家・実質支配者が公式非公開。一方、GitHub author/committer は `jau123 <741267111@qq.com>`、npm maintainer は `meigenjau <741267111gm@gmail.com>`、DNSPod/Tencent管理の meigen.art、wxpay.meigen.ai、知乎・公众号・小红书・抖音への中国語圏発信を確認。米国LLCを法的外皮として用いながら、実務上の開発・配布・決済・中国語圏マーケティングが中国語圏ノードに集中する非対称構造。 |
| 運用体制 | 本番アクセス・サブプロセッサ・サポート拠点 | No-Go | データ軸 L2/L3 でサブプロセッサ一覧、クラウド、リージョン、本番アクセス国籍分布、透明性レポートなし。 |
| モデル供給網 | 提供モデル群・モデル系譜(再帰3階層)・推論経路 | No-Go | モデル軸 L1〜L2 で Seedance 2.0 / Seedream 5.0 を含む多モデル提供を確認。ByteDance系モデル供給網接続により地政学的リスク確定。 |

**Claude補足(NK体系視点)**:

- 中華系サービスは NK008 v2.4 第3-2項の自動判定により、安全性レベル0(使用不可)に確定する。
- 本件は、`中華人民共和国国家情報法(2017年制定)` 第7条の協力義務範囲(中国法人格・中国本土運営者)に該当する蓋然性が高い。米国Wyoming LLCの法的外皮では、国家情報法の到達範囲を遮蔽できない(中国本土に運営実体がある以上、中国当局の協力要請は運営者個人に直接到達する)。
- ByteDance 系モデル供給網は、中国版 `生成式人工智能服務管理暫行辦法(2023)` の規律対象であり、モデルウェイト自体が中国当局の事前審査・コンテンツ規律を通過している。これは「モデル経由でユーザー入力が中国当局側情報基盤に統合されうる」リスク経路を意味する。

### 6.2 中国版/国際版の分離検証不能

公式 changelog に `Chinese language support` と `WeChat payment integration for Chinese users` を明記する一方、以下の分離証跡が公開されていない:

- 中国国内向け独立法人 / ICP備案 / 中国版規約
- 中国ユーザー向け処理主体(法人分離・インフラ分離)
- サポート権限の分離・ログの分離

「中国ユーザー向け」と「国際ユーザー向け」の処理が同一法人・同一インフラで処理されている場合、国際ユーザーのデータも中国側の処理経路を経由しうる。これを排除できる証跡が公開されていないため、**分離検証不能をリスクとして確定** する。

## 7. MCP/API連携リスク

GitHub README で以下が明示されている:

- `npx meigen init cursor`
- `npx meigen init vscode`
- `npx meigen init windsurf`
- `npx meigen init roo`
- `npx meigen init claude`
- `MEIGEN_API_TOKEN=meigen_sk_...`

これは、Claude Code / Cursor / VS Code / Windsurf / Roo Code 等の **AIコーディング環境に MCP サーバとして統合する設計** を意味する。具体的なリスク経路:

1. **APIトークンがローカル環境変数として永続化される** — トークン漏洩時の影響範囲が広い。
2. **MCPサーバ経由でユーザーのプロンプト・コード片・ファイル参照が送信される** — 業務コード・社内ドキュメントが意図せず MeiGen Cloud に送られうる。
3. **MCPサーバが指示するバックエンド経路にユーザー側の選択権がない** — Seedance / Seedream にルーティングされる可能性を遮断できない。
4. **`npx` 経由のインストールで `registry.npmmirror.com`(中国npmミラー)からパッケージが取得される可能性** — git commit log に156件の参照履歴あり。本人は再生成済みと説明しているが、初期開発環境では中国ミラーが標準だった事実は残る。

したがって、**標準業務端末・開発リポジトリへの導入はNo-Go**。導入する場合は完全隔離環境(VDI / 専用VM / Docker)に限定する。

## 8. 推奨対応

### 8.1 運用適性評価(ChatGPT評価レイヤー表3引用)

| 観点 | 判定 | 根拠 |
|---|---|---|
| 業務継続性(bus factor・財務) | No-Go | 小規模LLC表記、経営陣・財務・資本構成非公開。 |
| モデル変更の透明性 | Gate | changelog はあるが、企業向け変更管理は公開なし。 |
| 出力悪用可能性(jailbreak耐性等) | Gate | red-team・jailbreak耐性評価は非公開。 |
| MCP/API連携時の権限統制 | No-Go | `npx meigen`、AIコーディング環境への導入、APIトークン利用が前提。 |
| 機密情報投入適性 | No-Go | Privacy Policy自身がconfidential informationの投入回避を推奨。 |
| 標準業務環境への展開適性 | No-Go | DPA/Trust Center/サブプロセッサ/opt-out手順URLがない。 |

**Claude補足(NK体系視点)**:

- 上記いずれも No-Go / Gate であり、救済シナリオは個人検証PoC(隔離環境・機密データ投入禁止)に限定される。
- 「機密情報投入適性」が No-Go である点は、Privacy Policy 自身が機密情報回避を推奨していることから、運営側も第三者AI送信後の流出リスクを認識している証拠と読める。

### 8.2 利用形態別判定(Part 4 表4 全文転載)

| 利用形態 | 判定 | 根拠 |
|---|---|---|
| 個人検証・PoC | Gate | 公開プロンプト閲覧・非機密画像生成に限定すれば検証余地はあるが、ログ・第三者AI送信・モデル供給網を理解した上で隔離環境に限定。 |
| 限定的業務利用(特定業務・少人数) | No-Go | 業務データ・ブランド素材・顧客素材を入れる場合、第三者AIプロバイダとByteDance系モデル供給網を排除できない。 |
| 標準業務環境への導入 | No-Go | DPA、SSO、管理者監査、サブプロセッサ一覧、Trust Centerが公開されていない。 |
| 機密情報を扱う環境への導入 | No-Go | Privacy Policyが第三者AI送信とconfidential information回避を示す。 |
| 組織全体への展開 | No-Go | 地政学的リスク確定のため用途別救済不可。 |

### 8.3 緩和策(Part 4 表5 全文転載)

| 緩和策 | 可否 | 備考 |
|---|---|---|
| Enterprise/Team契約のみ使用 | 不可 | Enterprise/DPA/Trust Centerが公開確認できない。 |
| 学習利用opt-outを契約条項化 | 不可 | 具体的opt-out設定URL・契約条項化手順なし。 |
| DPA締結 | 不可 | 公開DPAなし。 |
| SSO/SAML経由のみアクセス | 不可 | SSO/SAML対応の公開確認なし。 |
| 業務メインアカウントと分離した専用アカウント | 可 | 個人PoCに限る。標準業務利用の救済にはならない。 |
| 使い捨て/プリペイドクレカ・バーチャルカード使用 | 可 | クレジット購入時の決済リスク低減策。 |
| 専用メールアドレス(エイリアス・使い捨て)使用 | 可 | アカウント分離策。 |
| 実名・組織名と切り離した登録情報 | 可 | 個人検証時のみ。 |
| 機密データ投入禁止(個人情報・成績・人事・財務) | 可 | 必須。 |
| MCP/API連携時の最小権限・短命トークン | 可 | ただし標準業務端末ではNo-Go。検証VMに限定。 |
| 隔離環境(VDI/専用VM/Docker)での実行 | 可 | MCP/npm検証時は必須。 |
| 利用ログ保管(最低1年) | 可 | 個人検証時の監査用。 |
| 月次アクセス権棚卸し・四半期利用範囲レビュー | 可 | 組織導入不可のため、PoC管理用に限定。 |

### 8.4 明確なNo-Go理由(Part 4 全文転載)

- **実質運営主体の非対称性**: Meigen Creative L.L.C.(米国Wyoming)は、形式的にはWyoming LLCとして登録要件を満たす法主体であるものの、実質支配者・経営陣・創業者・資本構成を公開していない。一方、運営実体を示す公開痕跡は、GitHub author/committer の QQメール(jau123 <741267111@qq.com>)、npm maintainer の meigenjau <741267111gm@gmail.com>、中国npmミラー registry.npmmirror.com 参照履歴、DNSPod/Tencent管理の meigen.art、wxpay.meigen.ai の証明書SAN、知乎・公众号・小红书・抖音への中国語圏発信に集中している。特に、実名認証または法人認証が前提となる知乎・公众号での発信導線を含む点は、単なる多言語マーケティングではなく、中国語圏運営実体の存在を示す補強根拠である。
- **ByteDance 系モデル供給網**: 公式・MCP側のモデル一覧に Seedance 2.0 / Seedream 5.0 が含まれる。
- Privacy Policy が prompts / reference images / generated content の第三者AIプロバイダ送信を明記し、各プロバイダの privacy/data retention policy に委ねている。
- DPA、Trust Center、サブプロセッサ一覧、処理リージョン、政府データ要求透明性レポート、学習利用 opt-out 設定URLが公開確認できない。
- MCP/npm 経路で `npx meigen` と `MEIGEN_API_TOKEN=meigen_sk_...` を用い、Claude Code / Cursor / VS Code / Windsurf / Roo Code 等の開発環境へ接続するため、標準業務端末・コード資産との接触リスクが高い。
- 米国側では実質支配者を非開示にし、中国側プラットフォームでは MeiGen 名義で活発に運用するという情報公開の偏りは、金融機関KYC/AML水準、またはEU GDPRの越境移転に係るアカウンタビリティ基準のいずれにおいても、看過できない構造である。本機関の業務環境への依存対象としては、リスク確定として扱う。
- 公式 changelog に Chinese language support と WeChat payment integration for Chinese users がある一方、中国ユーザー向け処理主体・中国版規約・データ分離証跡が公開されていない。

## 9. 結論

MeiGen / meigen.ai は、米国Wyoming LLCを法的外皮として用いながら、実務上の開発・配布・決済・中国語圏マーケティングが中国語圏ノードに集中する非対称構造を持つ。実名特定は中国側プラットフォームの遮断により外部から不能だが、**「外部から検証不能であること自体が、信用調査上の確定的リスク要因」** として作用する。

NK008 v2.4 の自動判定により、本件は **安全性レベル0(使用不可)** に確定する。標準業務環境への導入はNo-Go。個人検証PoCに限り、隔離環境(VDI/専用VM/Docker)で機密データ投入禁止を条件にGate。

「米国法人だから安全」「自社学習に使わないと書いてあるから安全」「ユーザーが Seedance を選ばなければ安全」のいずれの楽観論も、本件の構造的異常性の前では成立しない。

中華系AIサービスの「アメリカ偽装」パターンは今後も増加が予想される。本件は、`741267111` という単一のQQ番号が GitHub / npm の両エコシステムを横断的に貫通する形で痕跡を残している点で、追跡可能性の観点では運営者側のオペレーション・ハイジーンが甘い事例である。同様のパターンを検出する場合、QQメール / npmミラー参照履歴 / DNSPod/Tencent管理ドメイン / 微信支付サブドメイン証明書SAN / 知乎・公众号認証必須プラットフォームへの発信 の5点セットを優先的に確認することを推奨する。

## 📂 ChatGPT調査木(Part 2 全文)

<details>
<summary>クリックして展開 — ChatGPT による7枝×再帰3階層の調査木(技術者・法務担当者向け一次資料)</summary>

```
[MeiGen]
├─ 運営主体
│   └─ 法人形態・所在地・準拠法・登記法域・設立年 [リスク確定: Meigen Creative L.L.C.(米国Wyoming)は、形式的にはWyoming LLCとして登録要件を満たす法主体であるものの、実質支配者・経営陣・創業者・資本構成を公開していない。公式Termsは Publisher: Meigen Creative L.L.C.、Address: 30 N Gould St Ste R6, Sheridan, WY 82801, United States、Wyoming法準拠を明記するが、実質運営主体の公開痕跡は中国語圏ノードに集中する。]
│
├─ 中国版併存
│   ├─ 中国版サービスの有無(.cn/ICP備案/中国アプリストア)[リスク確定: meigen.ai / meigen.art の公式ページ上に .cn / ICP備案 / 中国アプリストア配信情報は表示されないが、changelog が v1.1.0 December 26, 2025 で Chinese language support と WeChat payment integration for Chinese users を明記。]
│   ├─ 中国版運営法人 [リスク確定: 中国版運営法人の公開表示なし。]
│   ├─ 中国版利用規約URL [リスク確定: 中文専用の中国版利用規約URLは確認できず。]
│   ├─ 中国版プライバシーポリシーURL [リスク確定: 中文専用の中国版Privacy Policy URLは確認できず。]
│   └─ 国際版とのデータ分離の検証可能性 [リスク確定: 中国ユーザー向けWeChat payment integration と、ByteDance系 Seedance / Seedream モデル提供を確認。一方、国際版・中国ユーザー向け処理の法人分離、インフラ分離、サポート権限分離、ログ分離を示す公式資料なし。]
│
├─ 経営陣・創業者【人的軸 再帰3階層】
│   ├─ CEO: 非公開(公式名義) / 実質運営者候補: jau123 / meigenjau / MeiGen Jau
│   │   ├─ L1 現職: [リスク確定: 公式Terms/Privacy/DMCAに Meigen Creative L.L.C. はあるが、CEO名は非公開。法人代表・実質支配者がサービス公式から追跡不能。一方、実務上の開発・配布者ノードとして GitHub author/committer `jau123 <741267111@qq.com>`、npm maintainer `meigenjau <741267111gm@gmail.com>`、YouTube/X系 `@meigen7982`、MeiGen Jau / MeiGen AI 名義が確認される。]
│   │   ├─ L2 前職・前々職: [リスク確定: CEO公式名義は非公開のため法人代表としての前職追跡不能。jau123 / meigenjau ハンドルから遡及可能な公開職歴はGitHub/npm/X/YouTube/Reddit/知乎での発信履歴に限られる。]
│   │   └─ L3 学歴・指導教授・研究室・出身地: [リスク確定: CEO公式名義は非公開のため学歴・出身地の追跡不能。実質運営者候補 jau123 / meigenjau の公開痕跡は、QQメール `741267111@qq.com`、registry.npmmirror.com参照履歴、DNSPod/Tencent管理のmeigen.art、wxpay.meigen.ai証明書SAN、知乎・公众号・小红书・抖音への中国語圏発信に集中する。]
│   ├─ CTO: 非公開
│   ├─ Chief Scientist: 非公開
│   └─ 創業者(CEOと別の場合): 非公開
│
├─ 取締役会・アドバイザー
│   └─ 各メンバーの兼任先 [リスク確定: 取締役・アドバイザー一覧は公式ページに公開されていない。MCP側は GitHub アカウント jau123 が前面に出る。npm配布者は meigenjau <741267111gm@gmail.com>、Git author/committerは jau123 <741267111@qq.com> で一致し、法人役員との法的関係は公開資料で接続不能。]
│
├─ 資本構成【人的軸 再帰3階層】
│   ├─ リード投資家: 非公開
│   ├─ 戦略投資家: 非公開
│   └─ 過去ラウンドの主要出資者 [リスク確定: 過去ラウンド情報非公開。]
│
├─ 提供モデル供給網【モデル軸 再帰3階層】
│   ├─ 自社モデル: 非確認
│   ├─ サードパーティモデル: GPT Image 2 / Nano Banana 2 / Seedance 2.0 / Seedream 5.0 / Veo 3.1 / Midjourney V8.1 / Flux 2 Klein / Happyhorse 1.0 / local ComfyUI [リスク確定: meigen.ai公式トップが GPT Image 2、Nano Banana 2、Seedance 2.0、Veo 3.1、Midjourney等を掲げ、MCP READMEがSeedream 5.0とSeedance 2.0を含む9モデルを明記。ByteDance系 Seedance / Seedream が含まれるため、中国系モデル供給網リスク確定。実質開発・配布ノードも jau123 / meigenjau に集中する。]
│   └─ 学習データ出自 [リスク確定: Privacy Policyは自社AIモデル学習には使わないとするが、第三者AIプロバイダに送信され、各プロバイダの保持・学習ポリシーに従うと明記。上流プロバイダ別の学習利用可否をMeiGen側で統制する公開DPAがない。]
│
├─ 推論インフラ【技術軸 再帰2階層】
│   ├─ L1 表向きクラウド [リスク確定: MeiGen Cloud、OpenAI-compatible API、local ComfyUI の3バックエンドがMCP READMEに明記されるが、MeiGen Cloudのクラウド事業者・リージョンは非公開。]
│   └─ L2 推論実行ノード物理所在 [リスク確定: モデル別リージョン・物理所在・ログ保持が非公開。ByteDance系モデル使用時の中国系供給網接続を排除できない。]
│
├─ データガバナンス【データ軸 再帰3階層】
│   ├─ L1 表向きポリシー: AI assistant logs 最大90日、CDN cached copies 最大7日。学習利用opt-in/outデフォルト条項なし。Data Deletionはcustomer service email申請。
│   ├─ L2 実際の処理経路: サブプロセッサ一覧・クラウド名・リージョン一覧が公開されていない。WeChat payment integrationの越境法域も非公開。
│   └─ L3 再委託先・第三国移転: Transparency Report / Law Enforcement Request Policyなし。本番アクセス権限者・サポート拠点・国籍分布・委託先運用者が非公開。
│
└─ アライメント・安全性体制
    ├─ セーフティチーム所在国 [リスク確定: 非公開]
    ├─ モデル更新透明性・サイレントアップデート有無 [リスク確定: モデル廃止・差替えの事前通知SLAは公開されていない。]
    ├─ 既知ジェイルブレイク事例と対応 [リスク確定: 評価レポート、red-team結果、jailbreak対応履歴は公開されていない。]
    └─ MCP/API連携時の権限委譲 [リスク確定: `npx meigen init cursor/vscode/windsurf/roo/claude`、`MEIGEN_API_TOKEN=meigen_sk_...`、Claude Code / Cursor / Codex / Windsurf / Roo Code連携を明記。ローカル開発環境にMCPサーバを導入し、APIトークン・生成バックエンド・プロンプトテンプレートを扱うため、標準業務端末への導入はNo-Go。]
```

</details>

## 出典

### 一次資料(公式)

- meigen.ai トップページ: <https://www.meigen.ai/>
- meigen.ai Terms of Service: <https://www.meigen.ai/terms>
- meigen.ai Privacy Policy: <https://www.meigen.ai/privacy-policy>
- meigen.ai DMCA: <https://www.meigen.ai/dmca>
- meigen.ai Changelog: <https://www.meigen.ai/changelog>
- meigen.ai Model Comparison: <https://www.meigen.ai/model-comparison>
- meigen.art User Agreement: <https://meigen.art/user-agreement>
- meigen.art Privacy Policy: <https://meigen.art/privacy-policy>

### 開発者・配布者ノード

- GitHub jau123 プロフィール: <https://github.com/jau123>
- GitHub MeiGen-AI-Design-MCP リポジトリ: <https://github.com/jau123/MeiGen-AI-Design-MCP>
- 知乎 MeiGen AI 设计 プロフィール: <https://www.zhihu.com/people/lu-bei-chen/posts>
- Reddit u/Deep-Huckleberry-752: <https://www.reddit.com/user/Deep-Huckleberry-752/>
- YouTube @meigen7982: <https://www.youtube.com/@meigen7982>
- X (Twitter) @meigen7982: <https://x.com/meigen7982>

### 法令・規格参照

- 中華人民共和国国家情報法(2017年制定) — DK002-lite準拠
- 中華人民共和国網絡安全法(2017)、数据安全法(2021)、个人信息保护法(2021)
- 中国版「生成式人工智能服務管理暫行辦法」(2023)
- EU GDPR 第44〜50条(越境移転に係るアカウンタビリティ基準)
- 米国 CFIUS / Executive Order 14117(関心国の懸念のあるデータ取引)

### 評価フレームワーク

- 本記事は ChatGPT(米国CFIUS/EO 14117準拠の信用調査)と Claude(NK体系・日本ユーザー保護観点)による二重評価を統合している。
- Claude側評価フレーム: NK001(厚黒学的評価)、NK002(地政学的リスク)、NK005(国別評価基準)、NK008 v2.4(記事執筆共通ルール)、NK009(統合監視システム評価)、DK002-lite(中国法制エッセンス)。

### アクセス日時

すべての一次資料・開発者ノードのアクセス日時: 2026年5月28日。
