"""
1列目の文字列の種類（異なる文字列の集合）を求めよ．
確認にはcut, sort, uniqコマンドを用いよ．
"""

import sys

ans = ""
emp = ""

with open(sys.argv[1],"r") as f1 , open(sys.argv[2],"w") as f2 :
    for line in f1 :
        emp += line
    else :
        listline = emp.split("\n")
        setline = set(listline)
        listline = list(setline)
        listline_second = sorted(listline)
        # lenlistline = len(listline_second)
        #f2.write(str(lenlistline))
        for name in listline_second :
            f2.write(name + "\n")
