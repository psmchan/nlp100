"""
今回のメモ
random.shuffle →　文字列やタプルはイミュータブル(変更不可)、元のオブジェクトを変更するrandom.shuffle()はTypeErrorになる。
新たなオブジェクトを生成するrandom.shuffle()を使った。
スコープを気にしたら今回はうまくいった。(04元素記号の問題)
"""
import random # randomモジュールをインポート

s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
word = s.split() # 空白で区切ってリストへ
# print(word) 確認用
fi = "" # 答えの用意
for i in range(len(word)) : # 単語の個数文まわす
    if len(word[i]) > 4 : # 単語の長さが4文字より多いなら
        sr = "".join(list(word[i][0]) + random.sample(word[i][1:-1],len(word[i])-2) + list(word[i][-1])) # 1文字目と最後はそのままで、それ以外ランダムに
    else : # ４文字以下なら
        sr = "".join(word[i]) # そのまま
    # for fi_word in sr :
    fi += (sr + " ") # fiに全部入れていく
print(fi)
