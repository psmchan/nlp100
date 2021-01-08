"""
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
"""
import n40
import n41

def read_txt() :
    moto_dict = dict()
    im_dict = dict()
    final_dst_srcs = []
    final_id_morph = []
    with open("ai.ja.txt.parsed", "r") as f :
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
                    morph_surface = morph_class.get_surface()
                    id_morph_dict = chunk_ans.id_morphs(moto, morph_surface, im_dict)
        return final_dst_srcs, final_id_morph

if __name__ == "__main__" :
    ans = read_txt()
    dst_srcs = ans[0]
    id_morph = ans[1]
    dst_srcs_dict = dst_srcs[1]
    id_morph_dict = id_morph[1]
    for key,value in dst_srcs_dict.items() :
        if key == -1 :
            continue
        else :
            for values in value :
                moto_num = id_morph_dict[values]
                saki_num = id_morph_dict[key]
                moto_word = "".join(moto_num)
                saki_word = "".join(saki_num)
                print(moto_word + "->" + saki_word)
