"""
pandasでのjsonファイルの読み込み
pd.read_json("ファイル名")
圧縮ファイルを読み込む場合
pd.read_json("ファイル名",compression = "infer")
lines = True
で1行ごとにJSONオブジェクトとして読み込み

queryメソッド
〇〇.query('列名 == "探す文字列"')
で完全一致で抽出

列の抽出
["カラム名"]

values:実際のデータの値のこと
colums:列名
index:行名
"""

import pandas as pd
import json

df_gz = pd.read_json("jawiki-country.json.gz",compression = "infer", lines = True)
ans = df_gz.query('title == "イギリス"')["text"].values[0]
print(ans)

"""
自分で考えたらそもそもの考え方ミスしてました。textからイギリス探してた。
str.containsで文字列探せるみたいな。
ans = df_gz[df_gz["text"].str.contains("イギリス")]
print(ans)
"""
