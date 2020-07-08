import pandas as pd
import json
import re

df_gz = pd.read_json("jawiki-country.json.gz",compression = "infer", lines = True)
uk = df_gz.query('title == "イギリス"')["text"].values[0]

word = "==+.*==+"
one_sec = "={2}"
two_sec = "={3}"
three_sec = "={4}"
for line in uk.split("\n") :
    ans = re.search(word,line)
    if ans != None :
        answer = ans.group()
        #print(answer)
        if re.match(three_sec,answer) :  # ここから先、数が大きい順に並べないとうまくいかない
            print(ans.group() + "3")
        elif re.match(two_sec,answer) :
            print(ans.group() + "2")
        else :
            print(ans.group() + "1")
    else :
        continue
