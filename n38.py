"""
単語の出現頻度のヒストグラムを描け．ただし，横軸は出現頻度を表し，
1から単語の出現頻度の最大値までの線形目盛とする．
縦軸はx軸で示される出現頻度となった単語の異なり数（種類数）である．
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font_path = "/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf" # TakaoPGothicってやつ使いました
font_prop = FontProperties(fname = font_path)
matplotlib.rcParams["font.family"] = font_prop.get_name() # ここまでフォントの設定

num = []

with open("answer_35.txt", "r") as f :
    for line in f :
        line = line.split()
        num.append(int(line[0]))

x = np.array(num)
#print(x)

plt.hist(x, bins = 100, range = (1,100))

plt.savefig("n38.png")
