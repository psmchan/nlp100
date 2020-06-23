"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
確認にはtailコマンドを用いよ．
"""

import sys

count = 0

N = sys.argv[3]

with open(sys.argv[1],"r") as f1 , open(sys.argv[2],"w") as f2 :
    for line in f1 :
        count += 1
    else :
        num = count - int(N) # とりあえず飛ばす行出した

"""
一応考えているのが、飛ばす行分飛ばして、残り出力みたいな風にしたい。
結構考えたけどわからないから質問する。
"""
