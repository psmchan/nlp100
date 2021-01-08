"""
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
"""
import n40
import n41

def noun_verb() :
    moto_dict = dict()
    im_dict = dict()
    final_dst_srcs = []
    final_id_morph = []
    with open("ai.ja.txt.parsed", "r") as f : # ファイル読み込む
        for line in f : # 1行ずつ見る
            line = line.rstrip("\n") # 改行取る
            if line[0] == "*" : # cabochaの行
                line_list = line.split() # splitする
                chunk_ans = n41.Chunk() # chunkよんでくる
                moto = int(line_list[1]) # かかりもと、int型にしておく
                saki = line_list[2] # かかりさき
                dst = chunk_ans.get_dst(saki) # chunkクラスでかかり先処理
                dst_srcs = chunk_ans.get_srcs(dst, moto, moto_dict) # かかり先:[かかりもと]
            elif line[0:3] == "EOS" : # 1文の処理
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
                    morph_list = [morph_surface,morph_pos]
                    id_morph_dict = chunk_ans.id_morphs(moto, morph_list, im_dict)
        return final_dst_srcs, final_id_morph

if __name__ == "__main__" :
    moto_s = []
    moto_p = []
    saki_s = []
    saki_p = []
    ans = noun_verb()
    dst_srcs = ans[0] # returnのタプルの最初がdstとsrcs関係
    id_morph = ans[1] # あとがidとmorph
    dst_srcs_dict = dst_srcs[1] # 冒頭の1文
    id_morph_dict = id_morph[1] # 同じく
    #print(id_morph_dict)
    for key, value in dst_srcs_dict.items() :
        if key == -1 : # かかるところがない
            continue
        else :
            for values in value :
                moto_num = id_morph_dict[values]
                for moto in moto_num :
                    moto_s.append(moto[0])
                    moto_p.append(moto[1])
                saki_num = id_morph_dict[key]
                for saki in saki_num :
                    saki_s.append(saki[0])
                    saki_p.append(saki[1])
                if "名詞" in moto_p and "動詞" in saki_p :
                    moto_word = "".join(moto_s)
                    saki_word = "".join(saki_s)
                    print(moto_word + "\t" + saki_word)
                moto_s = []
                moto_p = []
                saki_s = []
                saki_p = []
