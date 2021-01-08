"""
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい．
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で
出力せよ． ただし，出力は以下の仕様を満たすようにせよ．
"""
import n40
import n41

def verb() :
    moto_dict = dict()
    im_dict = dict()
    final_dst_srcs = []
    final_id_morph = []
    with open("ai.ja.txt.parsed", "r", encoding = "utf-8") as f :
        for line in f :
            line = line.rstrip("\n")
            if line[0] == "*" :
                line_list = line.split()
                chunk_ans = n41.Chunk()
                moto = int(line_list[1])
                saki = line_list[2]
                dst = chunk_ans.get_dst(saki)
                dst_srcs = chunk_ans.get_srcs(dst, moto, moto_dict)
            elif line[0:3] == "EOS" :
                try :
                    if next(f) == "EOS" :
                        continue
                    else :
                        final_dst_srcs.append(dst_srcs)
                        final_id_morph.append(id_morph_dict)
                except :
                    final_dst_srcs.append(dst_srcs)
                    final_id_morph.append(id_morph_dict)
                moto_dict = dict()
                im_dict = dict()
            else :
                sur = line.split("\t")
                pos = sur[1].split(",")
                morph_class = n40.Morph(sur[0], pos[6], pos[0], pos[1])
                morph_pos = morph_class.get_pos()
                if morph_pos == "記号" :
                    continue
                else :
                    morph_base = morph_class.get_base()
                    morph_list = [morph_base, morph_pos]
                    id_morph_dict = chunk_ans.id_morphs(moto, morph_list, im_dict)
        return final_dst_srcs, final_id_morph

if __name__ == "__main__" :
    moto_s = []
    moto_p = []
    saki_s = []
    saki_p = []
    moto_list = []
    ans = verb()
    dst_srcs = ans[0]
    id_morph = ans[1]
    #print(dst_srcs)
    #print(id_morph)
    for number in range(len(dst_srcs)) :
        dst_srcs_dict = dst_srcs[number]
        id_morph_dict = id_morph[number]
    #dst_srcs_dict = dst_srcs[1]
    #id_morph_dict = id_morph[1]
    #print(dst_srcs_dict)
    #print(id_morph_dict)
        for key, value in dst_srcs_dict.items() :
            #print(key, value) # key:かかり先,value:かかり元
            if key == -1 :
                continue
            else :
                for values in value :
                    #print(values)
                    moto_num = id_morph_dict[values]
                    #print(moto_num)
                    for moto in moto_num :
                        moto_s.append(moto[0])
                        moto_p.append(moto[1])
                    if "助詞" in moto_p :
                        m_num = [num for num, jyoshi in enumerate(moto_p) if jyoshi == "助詞"]
                        for num in m_num :
                            moto_word = moto_s[num]
                            moto_list.append(moto_word)
                    #print(moto_s)
                    #print(moto_p)
                    moto_s = []
                    moto_p = []
                saki_num = id_morph_dict[key]
                for saki in saki_num :
                    saki_s.append(saki[0])
                    saki_p.append(saki[1])
                if "動詞" in saki_p :
                    s_num = saki_p.index("動詞")
                    saki_word = saki_s[s_num]
                    #print(saki_word)
                    #print(moto_list)
                    moto_list.sort()
                    moto_jyoshi = " ".join(moto_list)
                    print(saki_word + "\t" + moto_jyoshi)
                #print(saki_s)
                #print(saki_p)
                saki_s = []
                saki_p = []
                moto_list = []