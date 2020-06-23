"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
確認にはtailコマンドを用いよ．
"""

import sys
import queue

q = queue.Queue() # FIFOキューの作成

N = sys.argv[3] # 3つ目で数字取得
N = int(N) # intにしとく

count = 0

with open(sys.argv[1],"r") as f1 , open(sys.argv[2],"w") as f2 :
    for line in f1 :
        q.put(line) # 蓄える
        count += 1 # ついでに行数数える
    else :
        num = count - N # 飛ばす行数える
    while num > 0 : # 飛ばす分
        emp = q.get() # とりあえず別のところに蓄えとく
        num -= 1
    while not q.empty() : # 残った分、最後までいれる
        f2.write(q.get())
