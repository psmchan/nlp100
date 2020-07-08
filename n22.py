"""
re.sub : マッチする部分を置換
〇〇 = re.sub(正規表現パターン,置換先文字列,処理対象の文字列)
"""
import pandas as pd
import json
import re

df_gz = pd.read_json("jawiki-country.json.gz",compression = "infer", lines = True)
uk = df_gz.query('title == "イギリス"')["text"].values[0]
#print(ans)
word = "\[\[Category:(.*)\]\]" # 抽出したい部分を()でくくる,正規表現パターンをグルーピング
remove_word = "\|.*"
for line in uk.split("\n") :
    ans = re.search(word,line)
    if ans != None :
        answer = re.sub(remove_word,"",ans.group(1))
        print(answer)
    else :
        continue
