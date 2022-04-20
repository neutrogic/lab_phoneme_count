# lab_phoneme_count

This is a script to count how many times a phoneme occurs in a set of HTS ".lab" files. I personally like to know how many of each phoneme there are in datasets. This script will only work on Windows and will output in Japanese on systems that have their UI set to Japanese.

## How to use:

```
python -m phoneme_count.py
```

You'll then be  asked to select a directory that contains ".lab" files. Please make sure the directory only has ".lab" files in it!

A file called "phoneme_count.txt" will be output into the root folder.

# 日本語

このスクリプトは、HTSの「lab」ファイル群から、音素の出現回数を数えます。個人的にはデータセットに含まれる音素の数を知ることが欲しいです。このスクリプトはWindowsでのみ動作し、UIが日本語に設定されているシステムで日本語で出力されます。

## 操作方法

```
python -m phoneme_count.py
```

次に、「lab」ファイルを含むディレクトリを選択するように尋ねられます。ディレクトリには「lab」ファイルしかないことを確認してください。

ルートフォルダに「音素の出現回数.txt」というファイルが出力されます。
