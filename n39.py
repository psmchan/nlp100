"""
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font_path = "/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf" # TakaoPGothicってやつ使いました
font_prop = FontProperties(fname = font_path)
matplotlib.rcParams["font.family"] = font_prop.get_name() # ここまでフォントの設定

num = []
count_list = []

count = 0
with open("answer_35.txt", "r") as f :
    for line in f :
        line = line.split()
        num.append(int(line[0]))
        count += 1
        count_list.append(count)

x = np.array(num)
y = np.array(count_list)
print(x)
print(y)

plt.plot(x, y, marker = "o")
plt.xscale("log") # x軸をlog
plt.yscale("log") # y軸をlog

plt.savefig("n39.png")
