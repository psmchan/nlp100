import pandas as pd
import json
import re

df_gz = pd.read_json("jawiki-country.json.gz",compression = "infer", lines = True)
uk = df_gz.query('title == "イギリス"')["text"].values[0]
#print(ans)
word = "\[\[Category:(.*)\]\]" # 抽出したい部分を()でくくる,正規表現パターンをグルーピング
for line in uk.split("\n") :
    ans = re.search(word,line)
    if ans != None :
        print(ans.group(1))
    else :
        continue
