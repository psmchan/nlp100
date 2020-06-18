"""
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""
"""
wcコマンド
「wc」　テキストファイルの行数や単語数、文字列を数えるコマンド
-l # 改行の数を表示
"""
import sys

count = 0

with open(sys.argv[1],"r") as f : # popular-names.txtをfとして開く
    for line in f : # 行数をカウントする
        count += 1 # カウントしていく
print(count)
