# lab_phoneme_count

This is a script to count how many times a phoneme occurs in a set of HTS ".lab" files. I personally like to know how many of each phoneme there are in datasets. This script will only work on Windows and will output in Japanese on systems that have their UI set to Japanese.

## How to use:

```
pip install -r requirements.txt
```
```
python phoneme_count.py
```
You'll be asked to select a database. Your best bet is to select the folder containing the data, no extra files, just in case.

A file called "phoneme_count.txt" will be output into the root folder.

# 日本語

このスクリプトは、HTSの「lab」ファイル群から、音素の出現回数を数えます。個人的にはデータセットに含まれる音素の数を知ることが欲しいです。このスクリプトはWindowsでのみ動作し、UIが日本語に設定されているシステムで日本語で出力されます。

## 操作方法

```
pip install -r requirements.txt
```
```
python phoneme_count.py
```
データベースを選択するプロンプトが表示されます。念のため、余分なファイルは入れずに、データがあるフォルダを選択することが良いです。

ルートフォルダに「音素の出現回数.txt」というファイルが出力されます。
