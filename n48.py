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
    key_list = list()
    for key, values in dst_srcs_dict.items() :
        # print(key)
        # print(values)
        if key != -1 : # かかり先が無い場合は飛ばす
            key_list.append(key)
            for value in values : # かかり元のリストを回す
                if key in num_dict : # 前に付け足したい
                    val = num_dict.pop(key)
                    val.append(value)
                    val.sort()
                    num_dict[value] = val
                elif value in key_list : # 後に付け足したい
                    for k in num_dict :
                        # print(k)
                        v = num_dict[k]
                        if value == v[-1] : # 1番最後が一致
                            # print(k)
                            # print(v)
                            val = num_dict[k]
                            val.append(key)
                            val.sort()
                            num_dict[k] = val
                else :
                    num_dict[value] = [value, key]
    # print(num_dict)
    # print(key_list)
    tango_base = []
    tango_pos = []
    ans_list = []
    for keys, values in num_dict.items() :
        # print(keys)
        for num in range(len(values)) :
            value = values[num]
            bunsetsu = id_morph_dict[value]
            for tango in bunsetsu :
                tango_base.append(tango[0])
                tango_pos.append(tango[1])
            # print(tango_base)
            # print(tango_pos)
            if len(values) - 1 != num :
                if "名詞" in tango_pos :
                    base = "".join(tango_base)
                    ans_list.append(base)
            else :
                base = "".join(tango_base)
                ans_list.append(base)
            tango_base = []
            tango_pos = []
        # print(ans_list)
        ans = " -> ".join(ans_list)
        print(ans)
        ans_list = []
