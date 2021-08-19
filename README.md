# 機械学習パイプライン

---

![表紙](building-ml-pipelines-ja.png)

---

本リポジトリはオライリー・ジャパン発行書籍『[機械学習パイプライン](https://www.oreilly.co.jp/books/978487311XXXX/)』のサポートサイトです。

## レポジトリの構成

各章のノートブックがあります。また、それぞれのノートブックはGoogle Colaboratoryを使いブラウザで実行できます。

- [サンプルパイプラインのコード](https://github.com/oreilly-japan/building-ml-pipelines-ja/blob/master/interactive-pipeline/interactive_pipeline.ipynb)/[Google Colabで開く](https://colab.research.google.com/drive/1Yy9QdVD7xHjCaYezOm3vhCsKZjWs8vik?usp=sharing)
- [2章のサンプルコード](https://github.com/oreilly-japan/building-ml-pipelines-ja/blob/master/chapters/intro_tfx/Apache_beam_example_notebook.ipynb)/[Google Colabで開く](https://colab.research.google.com/drive/1VbYmZRrt-68LwMZzlr_Ielllskj8ag7h?usp=sharing)
- [3章のサンプルコード](https://github.com/oreilly-japan/building-ml-pipelines-ja/blob/master/chapters/data_ingestion/data_ingestion.ipynb)/[Google Colabで開く](https://colab.research.google.com/drive/1z0ymuyD3FL6WXbqbdQuZYRZPJaFvy6gz?usp=sharing)
- [4章のサンプルコード](https://github.com/oreilly-japan/building-ml-pipelines-ja/blob/master/chapters/data_validation/data_validation.ipynb)/[Google Colabで開く](https://colab.research.google.com/drive/1PoEXmZztor8oehh03UqYrj51jJcxYQjE?usp=sharing)
- [7章のサンプルコード](https://github.com/oreilly-japan/building-ml-pipelines-ja/blob/master/chapters/model_analysis/model_analysis.ipynb)/[Google Colabで開く](https://colab.research.google.com/drive/1ai4dV75JZKto4FAABrhwemThIQ7nMgx7?usp=sharing)
- [10章のサンプルコード](https://github.com/oreilly-japan/building-ml-pipelines-ja/blob/master/chapters/adv_tfx/Custom_TFX_Components.ipynb)/[Google Colabで開く](https://colab.research.google.com/drive/1VUfmS_fti2wHurq6phBINuVjD889CMwA?usp=sharing)
- [14章のサンプルコード](https://github.com/oreilly-japan/building-ml-pipelines-ja/blob/master/chapters/data_privacy/differential_privacy.ipynb)/[Google Colabで開く](https://colab.research.google.com/drive/1g5_10KM0gDzZuxRKu0nfd4pVTsN-f2nA?usp=sharing)

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
