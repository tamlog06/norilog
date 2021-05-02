
乗りログアプリ
＝＝＝＝＝＝＝


目的
＝＝＝

webブラウザーでコメントを投稿するwebアプリケーションの練習

ツールのバージョン
===============
:python: 3.6.8
:pip: 21.1.1

インストールと起動方法
===================

リポジトリーからコードを取得し、その下にvenv環境を用意する::

    $ git clone https://github.com/tam1006/norilog
    $ cd norilog
    $ python3 -m venv venv
    $ source venv/bin/activate
    (venv) $ pip install .
    (venv) $ norilog
    * Running on gttp://127.0.0.1:8000/

開発手順
=======

開発用インストール
---------------

1. チェックアウトする
2. 以下の手順でインストールする::

    (venv) $pip install -e .    