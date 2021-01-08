"""
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
45の仕様に加えて，以下の仕様を満たすようにせよ．
"""
from n45 import verb

moto_s = []
moto_p = []
saki_s = []
saki_p = []
moto_list = []
jyoshi_list = []
j_list = []
b_list = []
ans = verb()
dst_srcs = ans[0]
id_morph = ans[1]
for number in range(len(dst_srcs)) :
    dst_srcs_dict = dst_srcs[number]
    id_morph_dict = id_morph[number]
    #print(dst_srcs_dict) # 1文の{かかり先番号:[かかり元番号]...}
    #print(id_morph_dict) # {文節番号:[単語,単語]...}
    for key, value in dst_srcs_dict.items() :
        #print(key, value) # key:かかり先,value: かかり元
        if key == -1 :
            continue
        else :
            for values in value :
                # print(values) # かかり元がリストになっているので1つずつ回す
                moto_num = id_morph_dict[values] # moto_num
                # print(moto_num) # id_morph_dictの[単語、品詞]のリスト
                for moto in moto_num :
                    moto_s.append(moto[0]) # moto[0]:単語
                    moto_p.append(moto[1]) # moto[1]:品詞
                if "助詞" in moto_p : # 助詞が入っていたら
                    tango = "".join(moto_s) # 助詞を含む文節全て
                    m_num =  [num for num, jyoshi in enumerate(moto_p) if jyoshi == "助詞"] # 1つの文節に助詞がいくつかある場合もある
                    for num in m_num :
                        moto_word = moto_s[num]
                        #moto_list.append(moto_word) # 文節
                        jyoshi_list = [moto_word, tango]
                        moto_list.append(jyoshi_list)
                moto_s = []
                moto_p = []
            saki_num = id_morph_dict[key]
            for saki in saki_num :
                saki_s.append(saki[0])
                saki_p.append(saki[1])
            if "動詞" in saki_p :
                s_num = saki_p.index("動詞")
                saki_word = saki_s[s_num]
                moto_list.sort()
                #moto_jyoshi = " ".join(moto_list)
                #tango_jyoshi = " ".join(tango_list)
                #print(saki_word + "\t" + moto_jyoshi)
                #print(saki_word)
                #print(moto_list)
                for jyoshi_bunsetsu in moto_list :
                    jyoshi = jyoshi_bunsetsu[0]
                    j_list.append(jyoshi)
                    bunsetsu = jyoshi_bunsetsu[1]
                    if bunsetsu not in b_list :
                        b_list.append(bunsetsu)
                #print(saki_word)
                #print(j_list)
                #print(b_list)
                j = " ".join(j_list)
                b = " ".join(b_list)
                print(saki_word + "\t" + j + "\t" + b)
            saki_s = []
            saki_p = []
            moto_list = []
            jyoshi_list = []
            j_list = []
            b_list = []
