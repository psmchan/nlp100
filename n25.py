"""
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
辞書オブジェクトとして格納せよ．
"""
"""
flags = re.DOTALL
. で改行を含めてマッチングさせる

"""
import pandas as pd
import json
import re

df_gz = pd.read_json("jawiki-country.json.gz",compression = "infer", lines = True)
uk = df_gz.query('title == "イギリス"')["text"].values[0]
word = r"\{\{基礎情報.*\n\}\}"
word = re.search(word, uk, flags = re.DOTALL)
kihon = word.group()
#print(kihon)
keyword = r"(.*)=(.*)"
remove_word = r"^\|"

list1 = []
list2 = []

for line in kihon.split("\n") :
    key = re.search(keyword,line)
    if key != None :
        list1.append(re.sub(remove_word, "", key.group(1))) # 最初の|を消去
        list2.append(key.group(2))
    else :
        continue

#print(list1)
#print(list2)

data = dict(zip(list1,list2))
print(data)
