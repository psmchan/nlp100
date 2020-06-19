"""
12で作ったcol1.txtとcol2.txtを結合し,
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
"""
import sys

count = 0

with open(sys.argv[1],"r") as f1 , open(sys.argv[2],"r") as f2 , open(sys.argv[3],"w") as f3 :
    for line1 in f1 : # col1.txtを1行ずつ見る
        ans1 = line1.strip() # 出力したら改行あったから改行抜いた
        ans2 = f2.readline() # col2.txtを1行ずつ読み込む
        f3.write(ans1 + "\t" + ans2) # col1とcol2をタブで結合
