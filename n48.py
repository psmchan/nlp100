"""
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ．
ただし，構文木上のパスは以下の仕様を満たすものとする．
・各文節は（表層形の）形態素列で表現する
・パスの開始文節から終了文節に至るまで，各文節の表現を” -> “で連結する
「ジョン・マッカーシーはAIに関する最初の会議で人工知能という用語を作り出した。」という例文を考える．
CaboChaを係り受け解析に用いた場合，次のような出力が得られると思われる．
"""
"""
番号 -> 番号 -> 番号
のリストを先に作ってしまおう
最後以外に名詞が入っている状態
"""
from n47 import verb
ans = verb()
dst_srcs = ans[0]
id_morph = ans[1]
# print(dst_srcs) #tupleの[0]がかかり先:[かかり元]
# print(id_morph) # tupleの[1]がid:[単語]
for number in range(len(dst_srcs)) : # 1文ごとに回す
    dst_srcs_dict = dst_srcs[number]
    id_morph_dict = id_morph[number]
    # print(dst_srcs_dict)
    # print(id_morph_dict)
    num_dict = dict()
    for key, values in dst_srcs_dict.items() :
        # print(key) # かかり先の番号
        # print(values) # かかり元の番号のリスト
        if key != -1 : # keyが-1の時は飛ばす
            for value in values : # かかり元を1つずつ回す
                if key in num_dict : # 前に付け足せるようにしたい
                    val = num_dict[key]
                    val += [value]
                    val.sort() # 並び替えておく
                    num_dict.setdefault(value, val)
                else :
                    num_dict[value] = [value, key]
    num_dict_sort = sorted(num_dict.items(), key = lambda x:x[0]) # ソートする
    # print(num_dict_sort) # タプル型で出る
    meishi_base = []
    meishi_pos = []
    tango_base = []
    tango_pos = []
    meishi = []
    horyu = []
    for num_dict in num_dict_sort :
        k = num_dict[0] # タプルの1つ目,番号
        v_list = num_dict[1] # タプルの2つ目,番号のリスト
        for v in v_list : # 番号のリストを回す
            if v < k : # もしリストの番号が、keyの番号よりも小さければ飛ばす
                continue
            else : # 同じもしくは大きければ
                # print(v) # 番号
                bunsetsu = id_morph_dict[v] # 文節の番号から文節を引っ張ってくる
                # print(bunsetsu) # 文節を出す
                for tango in bunsetsu : # 単語ごとに見る
                    if v == v_list[-1] : # 1番最後なら
                        tango_base.append(tango[0])
                        tango_pos.append(tango[1])
                    else : # 1番最後でなければ
                        meishi_base.append(tango[0])
                        meishi_pos.append(tango[1])
                # print(meishi_base) # meishi_base,meishi_pos,tango_baseは数に応じた分出てくる
                # print(meishi_pos) # 例えばmeishi_base,meishi_posがある場合はtango_baseは空で出力される
                # print(tango_base)  # 逆もしかり
                if "名詞" in meishi_pos :
                    meishi.append(meishi_base)
                if len(tango_base) != 0 and len(meishi) != 0:
                    # print(meishi)
                    # print(tango_base)
                    # print(tango_pos)
                    ans_list = []
                    for me in meishi : # いくつかある場合があるので回す
                        m = "".join(me)
                        ans_list.append(m)
                    t = "".join(tango_base)
                    ans_list.append(t)
                    if "動詞" in tango_pos :
                        if len(horyu) != 0 and horyu[-1] == ans_list[0] :
                            del horyu[-1] # かぶっている分削除
                            h = " -> ".join(horyu)
                            a = " -> ".join(ans_list)
                            print(h + " -> " + a)
                            horyu = []
                        ans = " -> ".join(ans_list)
                        print(ans)
                        ans_list = []
                    else : # もし動詞が入ってなければ述語ではないので繋げたい
                        horyu = ans_list
                    meishi = []
                tango_base = []
                tango_pos = []
                meishi_base = []
                meishi_pos = []
