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

フォルダの構成に関しては、以下の通りです。

| フォルダ名                   | 説明                                          |
| ----------------------- | ------------------------------------------- |
| chapters                | 各章に関するコードを含む                                |
| components              | 顧客の苦情データに対する前処理やモデルのコードを含む                  |
| interactive-pipeline    | 顧客の苦情データに対するインタラクティブなTFXパイプラインのコードを含む       |
| pipelines               | さまざまなオーケストレーターに対するパイプライン全体を含む。詳細は11章と12章を参照 |
| pre-experiment-pipeline | 著者たちの特徴エンジニアリングやモデルアーキテクチャに関する実験のコードを含む     |
| requirements            | 実行に必要なPythonパッケージに関する情報を含む                  |
| utils                   | データセットのダウンロードに関するコードを含む                     |

## データセットのダウンロード

サンプルプロジェクトで使うデータは、`utils/download_dataset.py`を実行することでダウンロードできます。データセットは、米消費者金融保護局が提供している顧客の苦情に関する公開データセットです。データセットをダウンロードするには、リポジトリのルートで次のスクリプトを実行します。

```bash
python utils/download_dataset.py
```

スクリプトの実行を終えると、`consumer_complaints_with_narrative.csv`という名前のファイルを含む`data`ディレクトリが作成されます。

## ライセンス

[MIT](https://github.com/oreilly-japan/building-ml-pipelines-ja/blob/master/LICENSE)

## 正誤表

下記の誤りがありました。お詫びして訂正いたします。

本ページに掲載されていない誤植など間違いを見つけた方は、japan@oreilly.co.jpまでお知らせください。

### 第1刷

#### ■14章 P.295 最終段落の重複
**誤**
```
データのプライバシーと機械学習の目標はよく一致しています。とりわけ、1人の個人について学習するより、集団全体について学習し、誰にとっても等しく良い予測をしたいという点で一致しています。プライバシーを追加することで、ある人のデータに、モデルが過学習するのを防ぐことができます。将来的には、モデルが個人データで学習される際に、機械学習パイプラインにプライバシーが最初から組み込まれた設計になることでしょう。

データのプライバシーと機械学習の目標はよく一致しています。とりわけ、1人の個人について学習するより、集団全体について学習し、誰にとっても等しく良い予測をしたいという点で一致しています。プライバシーを追加することで、モデルがある人のデータに過学習するのを防ぐことができます。将来的には、モデルが個人データで学習される際に、機械学習パイプラインにプライバシーが最初から組み込まれた設計になることでしょう。
```
**正**
```
データのプライバシーと機械学習の目標はよく一致しています。とりわけ、1人の個人について学習するより、集団全体について学習し、誰にとっても等しく良い予測をしたいという点で一致しています。プライバシーを追加することで、モデルがある人のデータに過学習するのを防ぐことができます。将来的には、モデルが個人データで学習される際に、機械学習パイプラインにプライバシーが最初から組み込まれた設計になることでしょう。
```
