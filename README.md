# 機械学習パイプライン

---

![表紙](building-ml-pipelines-ja.png)

---

本リポジトリはオライリー・ジャパン発行書籍『[機械学習パイプライン](https://www.oreilly.co.jp/books/978487311XXXX/)』のサポートサイトです。

## サンプルコード

### ファイル構成

|フォルダ名              |説明                         |
|:--                     |:--                          |
|chapters                |ほげほげ...                  |
|components              |ほげほげ...                  |
|interactive-pipeline    |顧客の苦情データに対するインタラクティブなTFXパイプラインのコードを含む|
|pipelines               |さまざまなオーケストレーターに対するパイプライン全体を含む。             |
|pre-experiment-pipeline |ほげほげ...                  |
|requirements            |ほげほげ...                  |
|utils                   |ほげほげ...                  |

The `pipelines` folder contains complete pipelines for the various orchestrators. See Chapters 11 and 12 for full details.

## デモプロジェクトの準備

まずはデータセットをダウンロードします。リポジトリのルートで次のスクリプトを実行します。

```bash
python utils/download_dataset.py
```

スクリプトの実行を終えると、`consumer_complaints_with_narrative.csv`という名前のファイルを含む`data`ディレクトリが作成されます。

## ライセンス

[MIT](https://github.com/oreilly-japan/building-ml-pipelines-ja/blob/master/LICENSE)

## 正誤表

まだありません。誤植など間違いを見つけた方は、japan@oreilly.co.jpまでお知らせください。
