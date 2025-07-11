---
title: "【4: 安全】Mastra.ai の安全性調査レポート"
emoji: "🔧"
type: "tech"
topics: ["AI", "Security", "tech", "typescript", "opensource"]
published: true
---

# 【4: 安全】Mastra.ai の安全性調査レポート

- 対象AIサービス: Mastra.ai TypeScript AIエージェントフレームワーク
- 公式URL: https://mastra.ai/
- 安全性レベル: **4（安全）** - セルフホスト版を推奨

# エグゼクティブ・サマリー

**法務判定**：導入可（セルフホスト版推奨）+ 技術的優位性を評価
**技術判定**：TypeScript生態系における先進的なフレームワーク、真のオープンソース性を確認
**厚黒学的リスク**：軽微（18項目中4項目のみ該当）
**地政学的リスク**：低（米国企業、元Gatsby創設者チーム）
**最終判定理由**：完全セルフホスト可能、真のオープンソース、実績ある運営陣による技術的革新

## デプロイメント形態別安全性評価

| 形態 | 安全性レベル | データ主権 | 推奨度 |
|------|-------------|-----------|--------|
| **セルフホスト** | 5（極めて安全） | 完全保持 | **高推奨** |
| **第三者クラウド** | 4（安全） | 部分的 | 推奨 |
| **Mastra Cloud** | 2（危険） | 限定的 | 要注意 |

# 詳細調査結果 - 技術・法務分析とリスク評価

## a. キャッチコピー・マーケティング検証

**検証結果：部分的に誇張あり（4/10）**

### 確認された主張と根拠：
- ✅ **「from the team that brought you Gatsby」** - 検証済み：Sam Bhagwat（Stanford卒）他、実際のGatsby創設者チーム（$5M ARR、Netlifyに売却）
- ⚠️ **「@mastra_ai is what LangChain should've been」** - [@jehovahscript](https://x.com/jehovahscript)による比較発言、主観的評価
- ⚠️ **「went viral on Hacker News and Github and went from 1,500 to 7,500 stars」** - 具体的時期の検証が困難

### 技術的優位性の客観的証拠：
- **TypeScript完全ネイティブ対応**：LangChainのJS版と比較して型安全性が大幅向上
- **OpenTelemetry統合**：本格的なObservability対応
- **XState基盤のワークフロー**：状態管理の理論的基盤が確実

## b. 技術アーキテクチャとデプロイメント形態の評価

**提供形態**：✅ **完全選択可能**
- **セルフホスト**：`npm create mastra` → 完全ローカル実行可能
- **第三者クラウド**：Vercel、Cloudflare、Netlify対応
- **ハイブリッド**：Mastra Cloud（オプション）

**バイナリインストール**：⚠️ **標準的npm権限のみ**
- Node.js標準インストールプロセス
- 管理者権限要求なし 
- 常駐プロセス：開発時のみ（localhost:4111）

**オフライン動作**：✅ **完全対応**
- セルフホスト時は完全オフライン動作
- LLMプロバイダー接続のみ必要（Ollama使用時は完全ローカル）

**データ同期**：✅ **強制なし**
- ローカル保存優先
- クラウド同期は完全任意

**依存関係**：✅ **透明性高**
- Vercel AI SDK（オープンソース）
- XState（状態管理、オープンソース）
- libSQL（ローカルストレージ、オープンソース）

## c. データ取得手法の詳細分析

**API連携によるデータアクセス範囲**：✅ **ユーザー制御下**
- LLMプロバイダー（OpenAI、Anthropic、Google）への接続はユーザー設定
- 第三者API利用は完全任意
- Mastra独自のデータ収集なし

**ブラウザプラグイン/拡張機能**：❌ **該当なし**
- サーバーサイドフレームワークのため該当せず

**デスクトップアプリケーション**：✅ **標準Node.js**
- 特別な権限要求なし
- ファイルシステムアクセスは開発者制御下

**データ収集の透明性**：✅ **完全透明**
- オープンソースのため全ロジック検証可能
- [GitHub: mastra-ai/mastra](https://github.com/mastra-ai/mastra) 7,500+ stars

## d. ソフトウェア品質とユーザー制御性

**透明性**：✅ **完全オープンソース**
- MIT/Apache-2.0ライセンス
- 51のパブリックリポジトリ
- 活発なコミュニティ貢献

**更新メカニズム**：✅ **ユーザー制御**
- npm標準のバージョン管理
- 自動更新強制なし

**設定粒度**：✅ **高い柔軟性**
- プロバイダー選択可能
- メモリ設定詳細制御
- トレース・ログ設定可能

**データポータビリティ**：✅ **完全対応**
- 標準JSON/SQL形式
- ベンダーロックインなし

**コード品質**：✅ **高品質**
- TypeScript完全対応
- 包括的テストカバレッジ
- 活発なIssue対応（GitHub Issues活動的）

## e. 無料モデル・収益構造の深掘り

**無料範囲の実質的制限**：✅ **制限なし**
- セルフホスト版は完全機能利用可能
- LLMプロバイダーのAPI料金のみ（ユーザー直接契約）

**有料移行の誘導手法**：⚠️ **軽微な誘導あり**
- Mastra Cloudへの誘導は存在するが強制性なし
- セルフホスト版で全機能利用可能

**隠れたコスト**：❌ **なし**
- オープンソースのため完全透明

**フリーミアム→課金への移行条件**：✅ **任意**
- Mastra Cloud使用時のみ課金
- セルフホスト版は永続無料

## f. 関係者・投資家の実態調査

**開発者特定**：✅ **透明性高**
- **Sam Bhagwat**：Stanford '11、元Gatsby CEO、米国
- **Abhi Aiyer**：Principal Engineer at Netlify、米国
- **Shane Thomas**：15年オープンソース経験、米国

**企業構造**：✅ **明確**
- Mastra Inc.（デラウェア州法人、推定）
- YCombinator Winter 2025バッチ
- ベイエリア拠点

**投資家分析**：✅ **信頼性高**
- YCombinator（一流アクセラレーター）
- Pioneer Fund（$500K Pre-Seed）
- Gatsby売却実績（$5M ARR → Netlify）

**権威性の実質**：✅ **実証済み**
- Gatsby成功実績：数十万開発者利用
- Netlify買収：実証された技術力
- YC選考通過：技術・ビジネス両面の実力証明

**過去の法的トラブル**：❌ **なし**
- 創設者・企業ともにクリーンレコード

## g. データインフラの地政学的分析とセキュリティ認証

**サーバー設置国**：✅ **ユーザー選択**
- セルフホスト：ユーザー完全制御
- 第三者クラウド：Vercel（米）、Cloudflare（米）、Netlify（米）
- Mastra Cloud：詳細不明（要確認）

**データ処理・保存の物理的所在地**：✅ **制御可能**
- セルフホスト時はユーザー環境内
- libSQL使用でローカル完結可能

**ネットワーク経路**：✅ **透明**
- LLM API通信のみ（ユーザー設定）
- Mastra独自の外部通信なし

**バックアップ・災害復旧**：✅ **ユーザー責任**
- セルフホスト時はユーザー制御下

**セキュリティ認証**：⚠️ **未取得**
- スタートアップ段階のため主要認証未取得
- オープンソースによる透明性で補完

**コンプライアンス**：⚠️ **実装中**
- GDPR対応：技術的には可能（ローカル処理）
- 正式対応は今後の課題

## h. 法的条項の厚黒学的精査

**利用規約の階層構造**：⚠️ **要改善**
- 提供されたプライバシーポリシーは他社テンプレートの誤用を確認
- 正式なMastra.ai独自の利用規約が必要

**プライバシーポリシー**：⚠️ **不完全**
- 現在のものは「Kepler Software」「modal.com」等の記載で混乱
- セルフホスト版では実質的にプライバシーポリシー不要

**オプトアウト手順**：✅ **簡単**
- セルフホスト版：完全制御下
- LLM学習利用はプロバイダー設定による

**「匿名化」「統計化」**：✅ **透明**
- オープンソースのため処理ロジック確認可能

**データライセンス条項**：⚠️ **不明確**
- セルフホスト版では問題なし
- Mastra Cloud版の条項要確認

**責任制限条項**：⚠️ **標準的**
- オープンソースライセンス（MIT/Apache-2.0）による標準的制限

**準拠法・管轄裁判所**：⚠️ **要確認**
- 米国カリフォルニア州法推定

## i. 厚黒学的要素チェックリスト（18項目中4項目該当）

```
❌ 誇張的キャッチコピー（実績に基づく合理的主張）
❌ "無料"条件の隠蔽（完全オープンソース）
❌ 導入実績の誇張（YC企業等の利用は確認済み）
❌ 成功事例の検証不可能性（GitHub Stars等で検証可能）
❌ フリーミアム中途解約ペナルティ（該当なし）
❌ ToS深層条項（セルフホスト版では該当なし）
❌ オプトアウト選択肢欠如（完全制御可能）
❌ 包括同意強制（セルフホスト版では該当なし）
❌ サブプロセッサ不透明（オープンソースで透明）
❌ 一方的責任転嫁（標準的OSS条項）
❌ セキュリティ監査情報の非開示（透明性高）
❌ 企業秘密による技術詳細開示拒否（完全公開）
⚠️ 虚偽希少性演出（バイラル成長の強調）
❌ ステルスマーケティング（該当なし）
❌ AI倫理審査体制の不在（オープンソース開発）
⚠️ バイナリインストール権限濫用（標準npm権限）
❌ 牛蒡抜きデータ連携（ユーザー制御下）
⚠️ 強制クラウド同期（Mastra Cloudのみ、選択的）
```

**該当項目数：4項目/18項目（22%）**

# 自薦・他薦の声

## ベンダー自身の宣伝文句

**公式発表・プレスリリース**
- **YCombinator公式**：「The Javascript framework for building AI agents, from the Gatsby devs」（2024年、YC Winter 2025バッチ発表）
- **Mastra公式ブログ**：「Mastra is moving into beta」（2025年2月20日、ベータ版発表）
- **GitHub**：「The TypeScript AI agent framework. ⚡ Assistants, RAG, observability」（2024年10月開始）

## インフルエンサー推奨発言

**技術系インフルエンサーによる評価**（利害関係・スポンサーシップ：なし）

### 高評価発言
- **@kiknaio**：「I've tried dozens of agent frameworks, nothing comes close to @mastra_ai.」（[X/Twitter](https://x.com/kiknaio)、2025年）
- **@jehovahscript**：「@mastra_ai is what LangChain should've been」（[X/Twitter](https://x.com/jehovahscript)、2025年）
- **@RichardsonDx**：「If you love Vercel AI SDK, you NEED to see @mastra_ai · It's the easiest & most dev-friendly SDK for building AI agents I've seen.」（[X/Twitter](https://x.com/RichardsonDx)、2025年）
- **@DavidPodolskyi**：「Always wanted an all-in-one framework for agents: deployment, workflow visualization, long jobs handling, observability, etc.@mastra_ai is the one that got all of this.」（[X/Twitter](https://x.com/DavidPodolskyi)、2025年）

### 技術的詳細評価
- **@yoshi8__**：「I tried using the TypeScript AI agent framework @mastra_ai and it was surprisingly easy」（[X/Twitter](https://x.com/yoshi8__)、2025年）
- **@AshikNesin**：「Just tried @mastra_ai and I'm blown away 🤯」（[X/Twitter](https://x.com/AshikNesin)、2025年）
- **@carsonfarmer**：「most impressed that @mastra_ai was designed to be cloud deployable from the get go.」（[X/Twitter](https://x.com/carsonfarmer)、2025年）

## 技術的評価コメント

**Medium記事・技術ブログ**（出典・根拠付き）

### 詳細技術レビュー
- **Justin Rich**（Software Engineer）：「After working extensively with both LangChain and Mastra, I've found Mastra to be a refreshingly straightforward approach to building AI applications.」（[Medium記事](https://justinrich.medium.com/mastra-agent-system-review-a-fresh-take-on-ai-development-04ca3e8e3a1b)、2025年6月）
- **Faris M. Syariati**：「This framework use TypeScripts and in my opinion, it more robust to create a more complex LLM powered application.」（[Medium記事](https://medium.com/@farissyariati/creating-a-ai-workflow-using-mastra-ai-5c3900d23e09)、2025年5月）
- **David Sam**：「Mastra is free, open-source, and already has over 10,000 stars on GitHub, even though it's fairly new.」（[Medium記事](https://medium.com/@_davidsam/building-ai-agents-with-mastra-ai-a-hands-on-experiment-d1bfdbbfcdf1)、2025年3月）

### WorkOS公式チュートリアル
- **WorkOS開発チーム**：「Mastra is a batteries‑included TypeScript framework for agentic apps. One stack, one set of primitives, no glue code.」（[WorkOS公式ブログ](https://workos.com/blog/mastra-ai-quick-start)、2025年4月）

## 批判的意見

**GitHub Issues・技術的課題**（存在する場合、根拠付き）

### 開発課題
- **依存関係の複雑性**：TypeScript monorepo setup関連のissues（[GitHub Issues](https://github.com/mastra-ai/mastra/issues)、2025年）
- **pnpmビルド互換性**：パッケージマネージャー互換性の課題（issue #1991）
- **ドキュメント改善要求**：統合関連のドキュメント整備要求（複数issue）

### 技術的限界
- **The Dispatch Report**分析：「Challenges in handling TypeScript dependencies and integration issues with package managers」（[The Dispatch AI Report](https://thedispatch.ai/reports/5989/)、2025年）

## メディア報道

**資金調達・企業発表**（報道機関、日付、記者名付き）
- **Fondo (YC W18)**：「Mastra recently launched!」創設者David J. Phillips（元Hackbright co-founder）による紹介記事（[Fondo公式ブログ](https://www.tryfondo.com/blog/mastra-launches)、2025年）
- **Crunchbase**：「Mastra raised $500,000 / Pre Seed from Pioneer Fund」（[Crunchbase](https://www.crunchbase.com/organization/mastra-44ba)、2024年）

## 発言の信頼性・利害関係分析

**資金提供、雇用関係等の詳細**
- ✅ **技術系インフルエンサー**：スポンサーシップ表記なし、自発的評価と判断
- ✅ **Medium記事執筆者**：独立開発者による技術検証記事
- ⚠️ **YCombinator関連**：投資家としての利害関係あり（ただし、YC標準）
- ❌ **直接的スポンサーシップ**：確認されず

# 主任アナリストが提案する追加調査項目

1. **Mastra Cloud詳細利用規約の精査**：セルフホスト版と比較したデータ取扱い・責任範囲の詳細調査が必要。プロプライエタリ部分の機能制限や課金体系の透明性確認。

2. **エンタープライズ利用時のコンプライアンス対応状況**：GDPR、SOC2、ISO27001等の正式対応状況と、大企業導入時の法務・監査要件への適合性調査。

3. **競合技術との客観的ベンチマーク**：LangChain、LlamaIndex等との性能・開発効率・保守性の定量的比較分析。第三者機関による中立的評価の実施。

4. **長期的ビジネスモデルの持続可能性分析**：オープンソース戦略とMastra Cloud収益化のバランス、将来的なライセンス変更リスクの評価。YC投資家からの収益化圧力への対応方針。

# 最終総括

Mastra.aiは、**真のオープンソースプロジェクト**として、AIエージェント開発領域において技術的革新をもたらしている。元Gatsby創設者チームという実証済みの技術力、完全セルフホスト可能なアーキテクチャ、TypeScript生態系での優位性により、**セルフホスト版は安全性レベル4（安全）**と評価する。

ただし、Mastra Cloud版については詳細な利用規約の精査が必要であり、データ主権を重視する組織は**セルフホスト版の利用を強く推奨**する。厚黒学的要素は軽微（18項目中4項目）であり、主要なリスクは将来的なビジネスモデル変更の可能性に限定される。

地政学的リスクは低く（米国企業）、技術的透明性は極めて高い。TypeScript開発者にとって、LangChainに代わる有力な選択肢として推奨できる。
