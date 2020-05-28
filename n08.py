"""
調べた内容(?)
・そもそも(219-文字コード)の意味が分かってなかったので(やってなかった)調べて見つけた時に付け足した
・復号化のこともよくわかっていなかったので付け足した
・文字列の入力をしてもらうところも自分で文を作って入れていたので付け加えた。
"""
def cipher(something) : # 関数の実装
    ans_1 = [something[n] for n in range(len(something))] # 1個ずつ文字をわける
    # word = [ord(ans_1[w]) for w in range(len(ans_1)) if str.islower(ans_1[w]) else ~~]
    word = []
    for w in range(len(ans_1)) : # 1文字ずつ確認
        if str.islower(ans_1[w]) : # もし英小文字なら(str.islower()は()の中が全て英小文字化調べる)
            word.append(chr(219 - ord(ans_1[w]))) # ord(1文字):文字に対応するUnicodeを調べる、chr(整数)は整数が示すUnicodeを文字列で返す
        else : # 英小文字でなければ
            word.append(ans_1[w]) # そのままリストに入れる
    fi = "".join(map(str,word)) # 普通の文字列にする、"区切り文字".join(リスト)、map(関数、イテラブル)、今回は数字も繋げられるように全てstr(文字)にしている
    return fi # fiを返す

sen = input("文字列を入力してください:") # 入力する

# 暗号化
answer_1 = cipher(sen)
print(answer_1)

# 復号化
answer_2 = cipher(answer_1) # 暗号化したとき219を引いているから、219-暗号化のUnicodeで復号化される。
print(answer_2)
