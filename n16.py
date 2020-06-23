"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ．
"""

import sys

count = 0
N = sys.argv[2] #ここでNを受け取る
file = sys.argv[3:3 + int(N) - 1]

with open(sys.argv[1],"r") as f1, open(sys.argv[2],"w") as f2 :
    for line in f1 :
        count += 1 # カウントする
    else :
        num = count // int(N) # 何行で分割するか

"""
疑問:これって分割する分ファイルを用意しないといけないのか。
ここから分割していこうと思ったけどわからない。
"""
