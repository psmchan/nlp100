"""
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""
"""
ので繋がれてるやつ
"""

import n30

nou = n30.neko()

ans = ""
for neko_list in nou :
    num = 0 # リスト回す前に設定
    while num < len(neko_list) - 2 : # あらかじめ行き過ぎるの防止するために-2しておく
        if neko_list[num]["pos"] == "名詞" : # もし名詞なら
            ans += neko_list[num]["surface"] # ansにつっこんでおく
            num += 1 # num +1して
            count = 0 # countは0に設定
            while True : # Trueの間回しておく
                if neko_list[num]["surface"] == "の" and neko_list[num + 1]["pos"] == "名詞" : # の、名詞が続いたら
                    ans += (neko_list[num]["surface"] + neko_list[num + 1]["surface"]) # ansにプラスしておく
                    num += 2 # numは +2
                    count += 1 # countは +1
                else : # の、名詞が続かなくなったら
                    if count != 0 : # 名詞のみか見分けるために、countが1でなかったら
                        print(ans) # ansを出力
                        ans = "" # ans初期化
                    else : # 名詞単体なら、(countが0なら)
                        ans = "" # ans初期化
                    break # 終わったらブレイク
        else : # 名詞でないなら
            num += 1 # num +1する
