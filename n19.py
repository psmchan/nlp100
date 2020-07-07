"""
value_counts()は、ユニークな要素の値がindex,その出現個数がdataとなる
pandas.Seriesを返す。
"""
import pandas as pd

df = pd.read_table("popular-names.txt",header = None) # データを読み込む
ans = df[0].value_counts() # 1行目をカウントしてソート
ans.to_csv("answer_19.txt", header = None, sep = "\t") # headerをNoneにして区切りをタブ
