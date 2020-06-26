"""
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

pandas
import pandas as pd
import numpy as np

pandasのテキストファイル読み込み関数 = read_table()
変数 = pd.read_table("ファイル名")
ヘッダーがない場合は、("ファイル名",header = None)
テキストファイルとして出力
df.to_csv("ファイル名")
ヘッダーを消す場合は  header = None
行番号を消す場合は　  index = None
区切り文字を指定する場合は   sep = ""(デフォルトは",")
値の小さい順にソート
変数.sort_values(ソートする場所)
値の大きい順にソート
変数.sort_values(ソートする場所,ascending = False)
"""

import pandas as pd

# データフレーム df を作成
dates = pd.read_table("popular-names.txt",header = None)
ans = dates.sort_values(2, ascending = False)
ans.to_csv("answer_18.txt",header = None, index = None, sep = "\t")
