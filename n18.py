"""
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""

import sys

emp = ""
n = 0

with open(sys.argv[1],"r") as f1, open(sys.argv[2],"w") as f2 :
    for word in f1 :
        col3 = word.split("\t")[2]
        if len(col3) == 4 :
            col3_rjust = col3.rjust(5)
        else :
            col3_rjust = col3
        emp += col3_rjust + "\n"
    else :
        col3list = emp.split("\n")
        sortlist = sorted(col3list,reverse = True)
        #for num in sortlist :
        #    f2.write(num + "\n")

with open(sys.argv[1],"r") as f1, open(sys.argv[2],"w") as f2 :
    for line in f1 :
        if sortlist[n] in line :
            f2.write(line)
            n += 1
        else :
            continue
