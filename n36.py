"""
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font_path = "/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf" # TakaoPGothicってやつ使いました
font_prop = FontProperties(fname = font_path)
matplotlib.rcParams["font.family"] = font_prop.get_name() # ここまでフォントの設定

left_list = [] # leftはx軸上の数値
height_list = [] # 各棒の高さ

with open("answer_35.txt","r") as f : # 35の答え使う
    for _ in range(10) : # 10回繰り返す
        line = f.readline() # 1行読んで
        line = line.split() # 空白で区切って
        left_list.append(line[1]) # 項目
        height_list.append(int(line[0])) # 数値、intに直す

# print(left_list)
# print(height_list)

left = np.array(left_list) # この形で書いたら出力できるらしい
height = np.array(height_list)
plt.bar(left, height)

plt.savefig("n36.png") # ファイルの名前だけ設定
