---
title: '【3: 注意が必要】Voice-in Chrome拡張機能の安全性調査レポート'
tags:
  - Chrome
  - Security
  - AI
  - privacy
  - VoiceRecognition
private: false
updated_at: '2025-08-31T12:48:42+09:00'
id: 23067416e7f4d15dc716
organization_url_name: null
slide: false
ignorePublish: false
---

Voice-in は600,000+ユーザーが利用する音声入力Chrome拡張機能です。「ローカル処理のみ」を謳っていますが、実際はGoogleサーバーでの処理が必要な点に注意が必要です。

- 対象AIサービス: Voice In - Speech-To-Text Dictation
- 公式URL: [Voice-in公式サイト](https://dictanote.co/voicein/)
- 安全性レベル: 3
- 厚黒学レベル: -3/18
- 支配国名目国: アメリカ

## エグゼクティブ・サマリー

Voice-in Chrome拡張機能は、インド系アメリカ人開発者（MIT PhD）が開発した音声入力ツールです。技術的には問題なく動作しますが、「ローカル処理のみ」という説明が実態と異なる点で注意が必要です。実際は Chrome Web Speech API を使用し、音声データは Google サーバーで処理されます。

- **法務判定**: 条件付き導入可（音声内容のGoogle送信を理解した上で）
- **技術判定**: 注意が必要（技術的記載の不正確性）
- **主要リスク**: 
  - 音声データのGoogle送信
  - 技術説明の不正確性
  - 企業利用時のコンプライアンス課題

## 詳細調査結果

### 技術アーキテクチャ分析

#### 実際の処理フロー
Voice-inは以下の技術構成で動作します：

```
音声入力 → Chrome Web Speech API → Googleサーバーで音声認識 
→ テキスト結果を受信 → ブラウザの入力フィールドに挿入
```

**重要な発見**：[MDN Web Speech API公式文書](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API)では明確に記載されています：

> "Chrome等の一部ブラウザでは、Web Speech APIの使用時はサーバーベースの認識エンジンを使用する。音声は認識処理のためWebサービスに送信され、オフラインでは動作しない"

#### 送信されるデータの詳細
技術分析により以下のデータが確実にGoogleに送信されることが判明：

- [ ] 完全な音声録音データ
- [ ] 使用サイトのドメイン情報  
- [ ] ブラウザの言語設定
- [ ] ウェブサイトの言語設定
- [ ] IPアドレス（接続情報として）

**送信されないデータ**：
- [x] Cookie情報
- [x] ブラウザの識別情報

### 法的条項分析

#### Voice-inプライバシーポリシーの主張
[Voice-in Privacy Policy](https://dictanote.co/voicein/privacy/) では以下のように記載：

> "Voice In does not transmit dictated audio or transcribed text to Voice In's servers"
> 
> "All audio processing is conducted locally using the browser's native speech-to-text capabilities"

#### 技術的現実との比較

| Voice-inの主張 | 技術的現実 | 評価 |
|---------------|-----------|------|
| 音声データはローカル処理のみ | Web Speech API使用時は必ずGoogleサーバーに送信 | ❌ 不正確 |
| 外部送信されない | 音声データは完全にGoogleに送信される | ❌ 不正確 |
| ブラウザネイティブ処理 | 実際はGoogleクラウドで処理 | ❌ 不正確 |

#### Google側のデータ処理
Googleの処理については[Google Cloud Speech-to-Text Data Usage FAQ](https://cloud.google.com/speech-to-text/docs/data-usage-faq) で説明されていますが、**Web Speech APIの詳細は別途管理**されており、具体的な保存期間や削除ポリシーは公開されていません。

### 地政学的リスク評価

#### 開発者・企業の背景
**Anil Shanbhag** (開発者)
- 学歴: MIT Computer Science PhD
- 職歴: Microsoft Research → Google → 現Instabase Staff Engineer  
- 透明性: LinkedIn、個人サイトで経歴完全公開
- 所在地: サンフランシスコ ベイエリア

**Dictanote** (運営企業)
- 設立: 2018年
- 所在地: インド・バンガロール
- 法的管轄: インド（準同盟国、政治的中立）

**地政学的評価**: 低リスク
- アメリカ在住の開発者
- インド企業（非ハイリスク国）
- 技術処理はアメリカ（Google）

### 厚黒学的要素の検証

#### 検出された要素 (3/18項目)

- [ ] **技術的虚偽表示**: 「ローカル処理のみ」の不正確な主張
- [ ] **責任転嫁**: Web Speech API仕様の詳細説明回避
- [ ] **表面的解決**: 技術的制約を利用規約で十分に説明していない

#### 非該当要素 (15項目)
- [x] 誇張的キャッチコピー
- [x] 導入実績の誇張
- [x] フリーミアム中途解約ペナルティ
- [x] オプトアウト選択肢欠如
- [x] 虚偽希少性演出
- [x] その他10項目

**厚黒学的評価**: 軽微（-3/18項目）
- 技術的認識不足による記載ミスの可能性が高い
- 悪意的な隠蔽の証拠は発見されず

### Chrome利用規約・商用利用適合性

#### Web Speech APIの商用利用許可
複数の法的分析により確認済み：

**カリフォルニア州著作権弁護士Rod Underhill氏の正式見解**：
> "ToS（利用規約）に商用利用を禁止する制限はない"

**W3C公式回答**：
2013年のW3C公開メーリングリストで「Web Speech APIは商用利用可能」との公式回答

**制限事項**：
- サービス再販禁止: Web Speech APIそのものを商品として販売することは禁止
- 利用した**アプリケーション**の商用提供は許可

#### 利用制限の現実
- **デスクトップ版**: ユーザーごとの制限が存在（実用上の問題）
- **Android版**: 制限なし（内部API使用のため）
- **時間制限**: 連続60秒の制限

## 自薦・他薦の声

### 推奨者の発言
**Chrome Web Store**:
- 4.4/5 (2,400+レビュー)
- 「アクセシビリティ向上に有効」
- 「音声入力の効率化に貢献」

**技術系コンテンツ**:
一般的な技術系YouTuberやブログでの紹介が中心。特定の利害関係は確認されず。

### 批判的意見
- プライバシー懸念を表明する技術者の投稿
- Web Speech APIの実態について正確に理解しているユーザーからの指摘

## 推奨対応

### 即座の対応
#### 個人利用者向け
- **一般的用途**: 音声内容がGoogleに送信されることを理解した上で使用可能
- **機密情報**: 重要な機密情報の音声入力は避ける
- **代替案検討**: より透明性の高い音声認識ソリューションの検討推奨

#### 企業向け
- **一般企業**: リスク評価を実施した上で条件付き使用可能
- **規制業界（HIPAA等）**: 使用停止を推奨
- **GDPR適用企業**: データ処理の説明責任を果たせるかの検討必要
- **機密性の高い業務**: 使用停止を推奨

### 代替案
#### より透明性の高い選択肢
- **西側クラウドベース**: 
  - [Azure Speech Services](https://azure.microsoft.com/ja-jp/products/cognitive-services/speech-services)
  - [Amazon Transcribe](https://aws.amazon.com/jp/transcribe/)
- **プライバシー重視**: 
  - [OpenAI Whisper](https://openai.com/blog/whisper/) (ローカル実行可能)
- **オンプレミス**: 
  - Mozilla DeepSpeech
  - Wav2Vec2

### 監視項目
- Chrome Web Speech APIのプライバシーポリシー変更
- Voice-inの技術説明の修正対応
- Google側のデータ処理透明性向上

## 追加調査項目

1. **Chrome Privacy Whitepaperの最新版**での詳細記載確認
2. **Mozilla Firefox Web Speech API実装**との比較調査  
3. **企業向け音声認識ソリューション**の詳細比較分析

## 最終総括

Voice-in Chrome拡張機能は、開発者の高い透明性と技術的な機能性を持つ有用なツールです。しかし、**「ローカル処理のみ」という技術説明が実態と異なる**点で注意が必要です。

実際は Chrome Web Speech API を使用し、**すべての音声データがGoogleサーバーで処理**されます。これは技術界では周知の事実ですが、多くのユーザーが誤解している現状があります。

**推奨**: 音声内容がGoogleに送信されることを**理解した上での使用**であれば、同盟国企業（アメリカ）での処理であり、基本的な法的保護が存在するため、条件付きで使用可能です。ただし、機密性の高い情報や規制業界での使用は慎重な検討が必要です。

**安全性レベル3（注意が必要）**: 技術的記載の不正確性とプライバシー懸念はありますが、悪意性は低く、同盟国企業による処理で基本的な法的保護が存在するため。

---

*調査実施日: 2025年8月30日*  
*調査者: AI安全性評価システム 主任アナリスト*
