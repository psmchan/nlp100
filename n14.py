"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ．
"""

import sys

num = sys.argv[3]

with open(sys.argv[1],"r") as f1 , open(sys.argv[2],"w") as f2 :
    for line in range(int(num)) :
        line = f1.readline()
        f2.write(line)
