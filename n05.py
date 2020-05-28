"""
for i in range(n) :
の使い方メモ

変数iには繰り返すたびに0,1,2,...n-1の数値が入る。
0からn回繰り返すので最後の値はn-1になる。
"""
def gram(seq,num) : # seq = sequence
    siki = [seq[x:x + num] for x in range(len(seq) - (num - 1))] # seqの文字数分繰り返す、x = 0(1番最初)からx + numまで、スライス
    return siki

sen = "I am an NLPer"

sen_word = sen.split()

print(gram(sen,1))
print(gram(sen,2))
print(gram(sen,3))

print(gram(sen_word,1))
print(gram(sen_word,2))
print(gram(sen_word,3))
