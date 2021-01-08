"""
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""
import n30

nou = n30.neko()

noun = "" # forで回す前に作っておく。じゃないと都度作られてうまくいかない
count = 0 # 同じく
for neko_list in nou : # forで分解
    for neko_dict in neko_list : # forで分解
        if neko_dict["pos"] == "名詞" : # posが名詞だった場合
            noun += neko_dict["surface"] # nounにsurfaceを突っ込んでいく
            count += 1 # countを1増やす
        else : # posが名詞でなかった場合
            if count >= 2 : # 直前までのカウントが2以上(つまり名詞が2つ以上続いている)
                print(noun) # nounを出力して
                noun = "" # noun初期化
                count = 0 # countも初期化
            else : # もしカウントが0や1なら(名詞が連接していない)
                noun = "" # そのまま初期化
                count = 0 # そのままcountも初期化
