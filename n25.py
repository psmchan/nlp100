"""
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
辞書オブジェクトとして格納せよ．
"""
"""
flags = re.DOTALL
. で改行を含めてマッチングさせる

pprintモジュール
リストや辞書などのオブジェクトを整形して出力・表示したり、文字列に変換できる
import pprint
pprint.pprint()
width のデフォルトは80
数が大きくなるほど、printしたときの形に近づく
" +$"
$:行末
 +:空白文字の連続
"""
"""
import pandas as pd
import json
import re
import pprint

df_gz = pd.read_json("jawiki-country.json.gz",compression = "infer", lines = True)
uk = df_gz.query('title == "イギリス"')["text"].values[0]
word = r"\{\{基礎情報.*\n\}\}"
word = re.search(word, uk, flags = re.DOTALL)
kihon = word.group()
#print(kihon)
keyword = r"(.*?)=(.*)" # ?つけて、非貪欲マッチにした
remove_word = r"^\|"

list1 = []
list2 = []

for line in kihon.split("\n") :
    key = re.search(keyword,line)
    if key != None :
        list1_word = re.sub(remove_word, "", key.group(1))
        list1_word = re.sub("^ +","",list1_word) # 最初の空白削除
        list1.append(re.sub(" +$","",list1_word)) # 最後の空白削除
        #list1.append(re.sub(remove_word, "", key.group(1))) # 最初の|を消去
        list2_word = re.sub("^ +","",key.group(2)) # 最初の空白削除
        list2.append(list2_word)
    else :
        continue

#print(list1)
#print(list2)

data = dict(zip(list1,list2))
#print(data)
pprint.pprint(data,width = 400) # width = 400 は、解答の4行目を1行で表示させるために400にした。
"""
import n20
import re

def tem() :
    uk = n20.uk()

    word = r"\{\{基礎情報.*\n\}\}"
    word = re.search(word, uk, flags = re.DOTALL)
    kihon = word.group()
    keyword = r"(.*?)=(.*)" # ?つけて、非貪欲マッチにした
    remove_word = r"^\|"

    list1 = []
    list2 = []

    for line in re.split("^\||^\}", kihon, flags = re.MULTILINE) :
        key = re.search(keyword, line, flags = re.DOTALL)
        if key != None :
            list1_word = re.sub(remove_word, "", key.group(1))
            list1_word = re.sub("^ +","",list1_word) # 最初の空白削除
            list1.append(re.sub(" +$","",list1_word)) # 最後の空白削除
            #list1.append(re.sub(remove_word, "", key.group(1))) # 最初の|を消去
            list2_word = re.sub("^ +","",key.group(2)) # 最初の空白削除
            list2_word = re.sub("\n$", "", list2_word)
            list2.append(list2_word)
        elif line[0] == "}" :
            continue

    data = dict(zip(list1,list2))
    return data

if __name__ == "__main__" :
    ans = tem()
    for key, value in ans.items() :
        print(key, value)
