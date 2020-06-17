"""
タブ1文字につきスペース1文字に置換せよ．
確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

sed s/置換対象文字列/置換後文字列/ファイル名

"""
"""
sys.argv[0] = n11.py
sys.argv[1] = popular-names.txt
sys.argv[2] = answer_11.txt
"""
import sys

with open(sys.argv[1],"r") as f1 , open(sys.argv[2],"w") as f2 :
    for tab in f1 :
        #tab = tab.strip() # ファイルに書き込んだら改行が元から無かったから消した
        tab = tab.replace("\t"," ")# タブをスペース1文字に置換
        f2.write(tab)
