"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ．

あまりをやらなきゃ
"""

import sys

N = sys.argv[2]

count = 0
n = 0

with open(sys.argv[1],"r") as f1, open("amari.txt","w") as f2  :
    for line in f1 :
        count += 1 # 行数数える
    else :
        num = count // int(N) # 終わったら、1つのファイルに書き込む行数を出す
        amari = count % int(N)
        if amari > 0 :
            num += 1
            amari -= 1
        else :
            num = num
        f2.write(str(num))

with open(sys.argv[1],"r") as f1 :
    for i in range(1,int(N) + 1) : # filenameのためのfor文
        filename = f"answer_16_{i}.txt"
        with open(filename,"w") as ansfile : # 書き込むたびにファイルを開く
            for line in range(n,num) : # nからnum行目まで書き込む
                ansline = f1.readline() # 1行ずつ読み込んで
                ansfile.write(ansline) # 書き込む
            else :
                n += num     # 終わったら次のファイルに書き込むために+numしていく
                num += num
                if amari == 0 : # 最初にamariの分+1してしまっているので、amariがなくなったら-1する
                    num -= 1
                else :
                    num = num
                amari -= 1
