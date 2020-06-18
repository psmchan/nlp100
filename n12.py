"""
各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．
"""
"""
文字列に直すときに改行していれたいけど文字化け起こす。
とりあえず1列目だけ、2列目だけを抜き出すことはできた
"""

import sys # sysをインポートする

with open(sys.argv[1],"r") as f1 , open(sys.argv[2],"w") as f2 , open(sys.argv[3],"w") as f3 :
    for word in f1 : # 1行ずつ見る
        col1 = word.split("\t")[0]
        col2 = word.split("\t")[1]
        f2.write(col1 + "\n")
        f3.write(col2 + "\n")   # +"\n"したいけど文字化け起こす
