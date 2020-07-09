import pandas as pd
import json
import re

df_gz = pd.read_json("jawiki-country.json.gz",compression = "infer", lines = True)
uk = df_gz.query('title == "イギリス"')["text"].values[0]
word = "\[\[ファイル:(.*)\]\]"
remove_word = "\|.*"

for line in uk.split("\n") :
    ans = re.search(word,line)
    if ans != None :
        answer = re.sub(remove_word,"",ans.group(1))
        print(answer)
    else :
        continue
