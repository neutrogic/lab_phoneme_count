#Copyright (c) neutrogic 2022

#Counts the amount of times a phoneme
#appears in HTS style .lab files.
#This script will only work on Windows

#HTS形式のlabファイルにおいて、音素の出現回数を数えます。
#Windowsだけで動作します。

#=== How to run/操作方法 ===
#python phoneme_count.py

import sys
import os
import yaml
import locale
import ctypes
import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw() #Prevents an empty tkinter window

#=== Detect system language ===
#=== システム言語の検出 ===

windll = ctypes.windll.kernel32
lang = ''

if locale.windows_locale[windll.GetUserDefaultUILanguage()] == 'ja_JP':
    lang = 'jp'

#=== Read each lab file by line and put them in a list ===
#=== すべてのlabファイルを一行ずつ読み込んでリストにします。 ===

if lang != 'jp':
    print(
        '\nCopyright (c) neutrogic 2022\n\n' +
        'Select directory of .lab files\n'
        )
else:
    print(
        '\nCopyright (c) neutrogic 2022\n\n' +
        'labファイルのディレクトリを選択します。\n'
        )

labs = filedialog.askdirectory()

phone_list = []


for file in os.listdir(labs):
    with open(os.path.join(labs, file), 'r') as f:
        for line in f:
            x1, x2, phone = line.strip().split()
            phone_list.append(str(phone))

#=== Count the amount of times a phoneme appears ===
#=== 音素の出現回数を数えます。 ===

phone_cnt = {}

for item in phone_list:
    phone_cnt[item] = phone_list.count(item)

#=== Format the dict to make it more readable using yaml ===
#=== yamlで、読みやすいようにdictをフォーマットします。 ===

if lang != 'jp':
    body = 'Phoneme count of .lab files in ' + labs + '\n\n'
else:
    body = labs + '内のlabファイルの音素数。\n\n'
    
body = body + yaml.dump(phone_cnt, sort_keys=True, default_flow_style=False)

#=== Write body to a file called 'phoneme_count.txt' ===
#=== bodyを「音素の出現回数.txt」という名前のファイルに書き込みます。 ===

if lang != 'jp':
    f = open('phoneme_count.txt', 'w')
    f.write(body)
    f.close()
else:
    f = open('音素の出現回数.txt', 'w')
    f.write(body)
    f.close()

if lang != 'jp':
    print('\nDone!')
else:
    print('\n完了!')