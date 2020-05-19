es = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = es.split() # 単語ごとにわける

word_list = list(words) # wordsのリストを作る
#print(word_list)

num_1 = {1,5,6,7,8,9,15,16,19}
data = {}

num = 0
for name in word_list : # 単語と数字を組にする
    num += 1
    if num in num_1 : # num_1の値なら
        fi_name = name[0] # 1文字目だけ取り出す
    else :              # そうでないなら
        fi_name = name[:2] # 2文字目まで取り出す
    data[fi_name] = num
print(data)
