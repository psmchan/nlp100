"""
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""
"""
基本形でやる(?)
cat neko.txt.mecab | grep "Ａ"
これでAを探す
"""

import n30

word = n30.neko()

word_dict = {} # 答えを入れる辞書作っとく

for neko_list in word : # forで分解
    for neko_dict in neko_list : # forで分解
        if neko_dict["pos"] == "記号" : # 一応付け加えた。「。、」とか省くため
            continue # スキップ
        if neko_dict["base"] not in word_dict : # word_dictになかったら追加
            word_dict[neko_dict["base"]] = 1 # 初めて入れるのでvalueは1
        else : # すでにあった場合
            word_dict[neko_dict["base"]] += 1

ans_list = sorted(word_dict.items(), key = lambda x :x[1], reverse = True) #dictのsort,lambdaを使う
for ans_tuple in ans_list : # すべてをまとめてリストになってる、その中にタプルが入ってる
    ans = str(ans_tuple[1]) + " " + ans_tuple[0] # valueがintなのでstrにする。value 空白 key
    print(ans)
