"""
「猫」とよく共起する（共起頻度が高い）10語とその出現頻度を
グラフ（例えば棒グラフなど）で表示せよ．
"""
"""
一文のなかのカウント
"""
import n30

import numpy as np
from collections import defaultdict
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

neko = n30.neko()

word_dict = defaultdict(int) # defaultdict,(int)なら初期値が0
word_set = set()
for neko_list in neko : # forで回す
        if "猫" in [neko_dict["base"] for neko_dict in neko_list] : # 猫が文に含まれていたら
            for neko_dict in neko_list : # 猫が含まれている文の辞書を回す
                #print(neko_dict)
                if neko_dict["pos"] == "記号" or neko_dict["base"] == "猫": # 記号か猫ならスキップ
                    continue
                if neko_dict["pos"] == "助詞" or neko_dict["pos"] == "助動詞" :
                    continue
                if neko_dict["base"] == "*" :
                    continue
                else : # 上の3つ以外なら
                    word_set.add(neko_dict["base"])
            #print(word_set)
            #word_set.clear()
            for word in word_set :
                word_dict[word] += 1
            word_set.clear()
                    #word_dict[neko_dict["base"]] += 1 # valueに+1する

ans_list = sorted(word_dict.items(), key = lambda x :x[1], reverse = True) # 値が大きい順にソート

font_path = "/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf" # フォント設定
font_prop = FontProperties(fname = font_path)
matplotlib.rcParams["font.family"] = font_prop.get_name()

left_list = [] # np.arrayで使うために作っておく
height_list = []

for ans_tuple in ans_list[:10] : # 10個使う
    left_list.append(ans_tuple[0]) # 文字
    height_list.append(int(ans_tuple[1])) # 数字
print(left_list)
print(height_list)

left = np.array(left_list)
height = np.array(height_list)
plt.bar(left, height)

plt.savefig("n37.png")
