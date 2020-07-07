"""
正規表現を利用するときは re モジュール
import re

エスケープシーケンス:メタ文字
. ^ $ [ ] * + ? | ( ) とか
メタ文字を単なる普通の文字として検索したい場合は、メタ文字の前に　\　を追加
. とにかくなんでもいい1文字
* 直前の文字が1個以上連続する
.* なんでもいい1文字が1個以上連続する

re.search(正規表現、検索対象の文字列)
〇〇.group() マッチした文字列を取得
"""
import pandas as pd
import json
import re

df_gz = pd.read_json("jawiki-country.json.gz",compression = "infer", lines = True)
uk = df_gz.query('title == "イギリス"')["text"].values[0]
#print(ans)
word = r"\[\[Category:.*\]\]"
for line in uk.split("\n") :
    ans = re.search(word,line)
    if ans != None :
        print(ans.group())
    else :
        continue
