"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ．
"""

import sys

N = sys.argv[2]

count = 0
n = 0

with open(sys.argv[1],"r") as f1 :
    for line in f1 :
        count += 1
    else :
        num = count // int(N)

with open(sys.argv[1],"r") as f1 :
    for i in range(1,int(N) + 1) :
        filename = f"answer_16_{i}.txt"
        with open(filename,"w") as ansfile :
            for line in range(n,num) :
                ansline = f1.readline()
                ansfile.write(ansline)
                n += num
                num += num
