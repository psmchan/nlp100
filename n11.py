"""
タブ1文字につきスペース1文字に置換せよ．
確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""
import sys

with open("popular-names.txt") as f : # popular-names.txtをfとして開く
    for tab in f :
        tab = tab.strip() # 出力したときに1行空いてたから改行抜いた
        tab = tab.replace("\t"," ")# タブをスペース1文字に置換
        print(tab)
