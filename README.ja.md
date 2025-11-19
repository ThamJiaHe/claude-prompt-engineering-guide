<!-- Language Selector -->
<div align="center">

📖 **言語を選択してください：**

[English](./README.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md)

</div>

---

# 🎯 Claude プロンプトエンジニアリングガイド

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/claude-prompt-engineering-guide?style=social)](https://github.com/yourusername/claude-prompt-engineering-guide)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-Nov%202025-blue)](https://github.com/yourusername/claude-prompt-engineering-guide)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 🚀 **Opus、Sonnet、Haikuモデル向けの専門的なClaudeプロンプト作成ガイド。MCP、スキル、Superpowers、高度なプロンプトエンジニアリングテクニックの包括的なカバレッジを含みます。**

---

## 📖 目次

- [概要](#概要)
- [機能](#機能)
- [クイックスタート](#クイックスタート)
- [スキルコレクション](#スキルコレクション)
- [コアコンテンツ](#コアコンテンツ)
- [ドキュメント構造](#ドキュメント構造)
- [主要セクション](#主要セクション)
- [例とテンプレート](#例とテンプレート)
- [貢献](#貢献)
- [ライセンス](#ライセンス)
- [謝辞](#謝辞)

---

## 🌟 概要

このガイドは、**Anthropicの公式ベストプラクティス**と**実践的なプロンプトエンジニアリング技法**を統合し、Claude 4.xモデル向けの包括的なリソースです。WebインターフェースからデスクトップアプリケーションやClaude Code CLI、APIを通じてClaudeを使用している場合でも、このガイドはClaudeの機能を最大限に活用するための実証済みのパターンとフレームワークを提供します。

### 対象者

- **開発者** - ClaudeのAPIでアプリケーションを構築しています
- **プロンプトエンジニア** - チーム向けの本番環境プロンプトを設計します
- **AI エンジニア** - Claudeをワークフローに統合します
- **Claude Code ユーザー** - エージェント機能を活用します
- **研究者** - Claudeの推論能力を探索します
- **すべての人** - 専門的なプロンプトエンジニアリングをマスターしたい方

### 重要な理由

Claude 4.xモデルは非常に高い能力を持っていますが、その能力を引き出すには**構造化されたプロンプト作成**が必要です。このガイドは以下を提供します：

✅ **Anthropicの10コンポーネントフレームワーク** — 専門的なプロンプトの公式な構造
✅ **Claude 4.xのベストプラクティス** — Opus、Sonnet、Haikuモデル向けの特定の技法
✅ **高度な技法** — XMLタグ、思考の連鎖、拡張思考などを含む
✅ **実世界のパターン** — コードレビュー、ビジネス分析、研究、文書作成
✅ **ツール統合** — MCP、スキル、Superpowers、Perplexity統合
✅ **環境ガイド** — Claude.ai、Desktop、Code、APIの最適なアプローチ

---

## ✨ 機能

このガイドには以下が含まれています：

- 📚 **1000行以上の包括的なリファレンス資料**
- 🏗️ **公式10コンポーネントプロンプトフレームワーク** 詳細説明付き
- 💡 **5つの高度なプロンプトパターン** 完全な例を含む
- 🛠️ **ツール統合ガイド** (MCP、スキル、Superpowers)
- 🎯 **環境固有の最適化** (Web、Desktop、CLI、API)
- 📋 **プロンプトテンプレート** (最小限版と包括版)
- 🔍 **複数のドメイン向けの実世界ユースケース**
- ⚙️ **モデル比較チャート** (OpusとSonnetとHaikuの比較)
- 📊 **料金とパフォーマンスガイド**
- 🚀 **長時間の推論向けのベストプラクティス**
- 🧠 **思考の連鎖と拡張思考の技法**
- 🔐 **セキュリティとプロンプトインジェクション防止**

---

## 🚀 クイックスタート

### 1. メインガイドを読む

包括的な**[Claude プロンプトエンジニアリングガイド](./Claude-Prompt-Guide.md)**から始めてください。以下の内容をカバーしています：
- Claudeのアーキテクチャと哲学
- 10コンポーネントフレームワーク
- Claude 4.xのベストプラクティス
- 高度な技法
- 完全なパターン例

### 2. お使いの環境を選択する

- **Claude.aiを使用しますか？** → [Claude.ai最適化ガイド](./docs/quick-start.md)を読む
- **Claude Desktopを使用しますか？** → [MCP統合ガイド](./docs/mcp-integration.md)を読む
- **Claude Code CLIを使用しますか？** → [Claude Codeガイド](./docs/claude-code-guide.md)を読む
- **APIで構築しますか？** → [API統合ガイド](./docs/api-guide.md)を読む

### 3. あなたのユースケース向けの例を探す

- [コーディングタスク](./docs/examples/coding-tasks.md)
- [研究と分析](./docs/examples/research-tasks.md)
- [ビジネス分析](./docs/examples/business-analysis.md)
- [文書作成](./docs/examples/document-creation.md)

### 4. テンプレートを使用する

提供されているテンプレートの1つをカスタマイズしてください：
- [最小限プロンプトテンプレート](./templates/minimal-prompt-template.md) — クイックプロジェクト向け
- [包括的プロンプトテンプレート](./templates/comprehensive-prompt-template.md) — 複雑なタスク向け

### 5. Claude スキルを探索する

再利用可能なスキルパッケージをご確認ください：
- **[スキルディレクトリ](./skills/)** — 利用可能なスキルを参照し、独自のスキルを投稿します
- **[スキルテンプレート](./skills/examples/example-feedback-analyzer.md)** — スキルの例：フィードバック分析
- **スキル作成を学ぶ** — [skills/README.md](./skills/README.md)の完全なドキュメント

---

## 📦 スキルコレクション

### Claude スキルとは？

**Claude スキル**は、ドメイン固有の知識、手順、ワークフローを使用してClaudeの機能を拡張するモジュール式の再利用可能なタスクパッケージです。以下のように設計されています：

- ✅ **モジュール化** — 自己完結型で、特定のタスクに焦点を当てています
- ✅ **再利用可能** — 異なる会話やプロジェクト全体で使用できます
- ✅ **合成可能** — 複数のスキルがシームレスに連携します
- ✅ **発見可能** — Claudeが関連するスキルを自動的に識別します
- ✅ **効率的** — 段階的な情報開示でコンテキストブロートを防止します

### 利用可能なスキル

包括的なコレクションには**22個の本番環境対応スキル**が含まれています：

**Web開発**: NextJSアプリケーションルーター、Tailwindデザインシステム、NextAuth、API開発
**インフラストラクチャ**: AWS、GCP、Neon Serverless、Prisma ORM
**テスト**: Vitest、Playwright E2E、コードレビュー、テストフレームワーク
**DevOps**: Vercelデプロイメント、データベース移行、監視とログ、Gitワークフロー
**標準**: TypeScript、パフォーマンス、SEO、セキュリティ、アクセシビリティ、フィードバック分析

[→ すべての22スキルを表示](./skills/)

### クイックリンク

- 📚 **[スキル完全ドキュメント](./skills/README.md)** — スキルについてすべてを学ぶ
- 🛠️ **[スキル作成方法](./skills/README.md#-スキルの作成方法)** — ステップバイステップガイド
- 📋 **[スキルテンプレート](./skills/examples/example-feedback-analyzer.md)** — 開始点として使用
- 🤝 **[スキルに貢献](./skills/README.md#-貢献)** — コミュニティで共有

### なぜスキルを使うのか？

スキルは以下を実現できます：

- 📚 **プロセスの標準化** チーム全体
- 🎯 **一貫性の確保** 出力とワークフロー
- ⏱️ **時間の節約** 事前に構築されたプロシージャ
- 🔧 **Claudeをカスタマイズ** 特定のドメイン向け
- 📈 **品質向上** 実証済みのパターンを通じて

### 開始する

1. **参照** [skills/examples/](./skills/examples/) の利用可能なスキル
2. **コピー** 会話で使用するスキル
3. **参照** プロンプト内：「[スキル名]を使用して...」
4. **作成** [テンプレート](./skills/README.md#-スキルテンプレート)に従うことで独自のスキル
5. **貢献** スキルをコミュニティに還元

---

## 📚 コアコンテンツ

### [Claude プロンプトエンジニアリングガイド](./Claude-Prompt-Guide.md)

以下を含む包括的なリファレンス文書：

#### セクション1：Claudeのアーキテクチャを理解する
- Claudeのキャラクターと哲学
- ナレッジカットオフ日
- Claudeがプロンプトを処理する方法

#### セクション2：Claude モデル概要
- **Claude Opus 4.1** — 最も強力なモデル
- **Claude Sonnet 4.5** — バランスの取れたパフォーマンスとコスト
- **Claude Haiku 4.5** — 高速で効率的
- 料金とパフォーマンスの比較

#### セクション3：システムプロンプトとユーザープロンプト
- システムプロンプトを使用する場合
- ユーザープロンプトを使用する場合
- 各パターンのベストプラクティス

#### セクション4：Anthropicの公式プロンプト構造
- **10コンポーネントフレームワーク**（公式構造）
- コンポーネント説明と例
- この構造が機能する理由

#### セクション5：Claude 4.xのベストプラクティス
- 明示的な指示を提供する
- コンテキストを追加してパフォーマンスを向上させる
- 長時間推論技法
- 状態追跡のベストプラクティス
- ツール使用パターン
- 出力形式の制御
- 並列ツール呼び出し
- リサーチアプローチ
- ハルシネーション回避

#### セクション6：高度な技法
- 構造用XMLタグ
- 思考の連鎖プロンプト作成
- 拡張思考
- プロンプトチェーニング
- ロールプロンプト作成

#### セクション7：ツール、MCP、スキルとSuperpower
- Model Context Protocol（MCP）
- MCPファイルシステムサーバー
- Claude スキルシステム
- Superpowersプラグイン（obra製）
- Perplexity MCP統合

#### セクション8：異なる環境向けプロンプトエンジニアリング
- Claude.ai Webインターフェース
- Claude Desktopアプリ
- Claude Code（CLI/VS Code）
- Claude API（直接統合）

#### セクション9：一般的なパターンと例
- パターン1：技術コードレビュー
- パターン2：データを含むビジネス分析
- パターン3：長期間のコーディングタスク
- パターン4：研究と統合
- パターン5：スキル統合による文書作成

#### セクション10：クイックリファレンスカード
- 最小限プロンプトテンプレート
- 包括的プロンプトテンプレート
- クイックチェックリスト

---

## 📖 ドキュメント構造

```
claude-prompt-engineering-guide/
├── README.md                          # このファイル
├── Claude-Prompt-Guide.md             # メイン包括ガイド
├── LICENSE                            # MITライセンス
├── CONTRIBUTING.md                    # 貢献ガイドライン
├── CHANGELOG.md                       # バージョン履歴
├── .gitignore                         # Git無視ルール
│
├── docs/                              # 追加ドキュメント
│   ├── quick-start.md                # スタートガイド
│   ├── mcp-integration.md            # MCP設定と使用
│   ├── skills-guide.md               # スキルドキュメンテーション
│   ├── superpowers-guide.md          # Superpowersプラグインガイド
│   ├── api-guide.md                  # API統合ガイド
│   ├── claude-code-guide.md          # Claude Code CLIガイド
│   └── examples/                      # 実世界の例
│       ├── coding-tasks.md
│       ├── research-tasks.md
│       ├── business-analysis.md
│       └── document-creation.md
│
├── templates/                         # 使用可能なテンプレート
│   ├── minimal-prompt-template.md    # クイックテンプレート
│   └── comprehensive-prompt-template.md # 完全なテンプレート
│
├── skills/                            # Claude スキルコレクション
│   ├── README.md                     # スキルガイドとドキュメンテーション
│   └── examples/                      # スキル例
│       └── example-feedback-analyzer.md # 顧客フィードバック分析スキル
│
└── .github/                          # GitHub設定
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md
    │   └── feature_request.md
    └── PULL_REQUEST_TEMPLATE.md
```

---

## 🎯 主要セクション

### 10コンポーネントフレームワーク（公式）

これは**Anthropic推奨の専門的なプロンプト構造**です：

1. **タスクコンテキスト** — WHO と WHAT（Claudeの役割を定義）
2. **トーンコンテキスト** — HOW（コミュニケーションスタイル）
3. **背景データ** — 関連するコンテキストとドキュメント
4. **詳細なタスク説明** — 明示的な要件と規則
5. **例** — 望ましい出力の1〜3の例
6. **会話履歴** — 関連する事前のコンテキスト
7. **直近のタスク説明** — 今すぐ必要な特定の成果物
8. **ステップバイステップの思考** — 意図的な推論を促進
9. **出力形式** — 構造を明示的に定義
10. **事前入力応答** — Claudeの応答を開始してスタイルをガイド

### Claude 4.x のベストプラクティス

📌 **明示的である** — Claude 4.xは正確な指示に対応します
📌 **コンテキストを追加する** — WHAT ではなく WHY を説明する
📌 **例を使用する** — 単に言うのではなく、示す
📌 **推論を促進する** — 思考の連鎖は大幅に品質を向上させます
📌 **出力形式を定義する** — 構造とスタイルについて具体的に
📌 **並列ツール活用** — 複数の操作を同時に実行

---

## 📋 例とテンプレート

### 実世界のパターン

1. **技術コードレビュー** — セキュリティ、パフォーマンス、ベストプラクティスのコードレビュー
2. **ビジネス分析** — メトリクス分析と戦略的推奨提供
3. **長期コーディング** — 複数のコンテキストウィンドウ間での完全な機能構築
4. **研究と統合** — 包括的な競争分析実施
5. **文書作成** — スキル統合によるプレゼンテーション構築

### すぐに使えるテンプレート

- **最小限テンプレート** — クイックタスク向けの必須コンポーネント
- **包括的テンプレート** — 複雑なプロジェクト向けの完全フレームワーク

完全な例は[templates/](./templates/)ディレクトリを参照してください。

---

## 🤝 貢献

貢献を歓迎します。以下の内容で貢献できます：
- 📝 新しい例またはパターンの追加
- 🐛 問題報告または改善提案
- 📚 ドキュメント改善
- 🎯 独自のプロンプトエンジニアリング発見の共有

詳細なガイドラインは[CONTRIBUTING.md](./CONTRIBUTING.md)を参照してください。

---

## 📜 ライセンス

このプロジェクトは**MIT ライセンス**の下でライセンスされています — 詳細は[LICENSE](./LICENSE)を参照してください。

Claude プロンプトエンジニアリングガイドは、Anthropicドキュメントとオープンソースコミュニティリソースから公開されている情報を統合しています。

---

## 🙏 謝辞

**作成日：** 2025年11月19日
**場所：** シンガポール
**目的：** 専門的なClaudeプロンプトエンジニアリング向けの深いリサーチ統合

### クレジット

- **Anthropic** - ClaudeとドキュメントのためのAnthropicチーム
- **Anthropicチーム** - 10コンポーネントフレームワークとベストプラクティス
- **オープンソースコミュニティ** - MCP、スキル、Superpowersエコシステム
- **Claudeユーザーと開発者** - 実世界のパターン発見

---

## 📞 サポートと質問

### ヘルプが必要ですか？

- 📖 **ガイドを読む** — [Claude-Prompt-Guide.md](./Claude-Prompt-Guide.md)から始める
- 📚 **例を確認** — [docs/examples/](./docs/examples/)をチェック
- 🎯 **テンプレート使用** — [テンプレート](./templates/)をカスタマイズ

### 問題を報告

バグを見つけたまたは提案がありますか？ [問題を開く](https://github.com/yourusername/claude-prompt-engineering-guide/issues)：
- 問題の明確な説明
- 例（該当する場合）
- 改善提案（オプション）

### 貢献

このガイドを改善したいですか？ プロセスについては[CONTRIBUTING.md](./CONTRIBUTING.md)を参照してください。

---

## 🚀 スタートガイド

1. **このリポジトリをクローン**
   ```bash
   git clone https://github.com/yourusername/claude-prompt-engineering-guide.git
   cd claude-prompt-engineering-guide
   ```

2. **メインガイドを開始**
   ```bash
   # 包括ガイドを読む
   cat Claude-Prompt-Guide.md
   ```

3. **パスを選択**
   - Claudeが初めてですか？ → [クイックスタートガイド](./docs/quick-start.md)
   - アプリを構築しますか？ → [APIガイド](./docs/api-guide.md)
   - パターンが欲しいですか？ → [例を参照](./docs/examples/)

4. **テンプレートを選択**
   - クイックプロジェクト？ → [最小限テンプレート](./templates/minimal-prompt-template.md)
   - 複雑なタスク？ → [包括的テンプレート](./templates/comprehensive-prompt-template.md)

---

## 📊 統計

- **ページ数：** 1000行以上の包括的なリファレンス
- **パターン数：** 5つの実世界のプロンプト例
- **テンプレート数：** 2つの本番環境対応テンプレート
- **例数：** 異なるドメイン全体の15以上のユースケース
- **カバレッジ：** Claude Opus、Sonnet、Haiku、API、Desktop、CLI、Web

---

## 🌐 関連リソース

### 公式Anthropic

- [プロンプトエンジニアリングガイド](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Claude APIドキュメンテーション](https://docs.anthropic.com)
- [Claude Code ドキュメント](https://docs.anthropic.com/en/docs/claude-code)
- [システムプロンプトガイド](https://docs.anthropic.com/en/release-notes/system-prompts)

### コミュニティ

- [Model Context Protocol](https://modelcontextprotocol.io)
- [Claude クックブック](https://github.com/anthropics/claude-cookbooks)
- [素晴らしいClaudeスキル](https://github.com/travisvn/awesome-claude-skills)
- [Superpowersプラグイン](https://github.com/obra/superpowers-chrome)

---

<div align="center">

**❤️でClaudeコミュニティのために作成されました**

[⭐ このリポジトリにスターを付ける](https://github.com/yourusername/claude-prompt-engineering-guide) 役に立つと感じた場合！

[問題を報告](https://github.com/yourusername/claude-prompt-engineering-guide/issues) • [貢献](./CONTRIBUTING.md) • [議論](https://github.com/yourusername/claude-prompt-engineering-guide/discussions)

</div>
