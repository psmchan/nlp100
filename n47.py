"""
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．
・「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
・述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
・述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
・述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
例えば「また、自らの経験を元に学習を行う強化学習という手法もある。」という文から，以下の出力が得られるはずである．
学習を行う	に を	元に 経験を
"""
"""
今までのプログラムを使っても「サ変接続」の部分は持ってこられないから、45みたいにもう1回改変するしかない
あとはわかりにくい変数名が多いから、綺麗に書き直したい
"""
from n40 import Morph
from n41 import Chunk

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
                chunk_ans = Chunk()
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
                morph_class = Morph(sur[0], pos[6], pos[0], pos[1])
                morph_pos = morph_class.get_pos()
                if morph_pos == "記号" :
                    continue
                else :
                    morph_base = morph_class.get_base()
                    morph_pos1 = morph_class.get_pos1()
                    morph_list = [morph_base, morph_pos, morph_pos1]
                    id_morph_dict = chunk_ans.id_morphs(moto, morph_list, im_dict)
        return final_dst_srcs, final_id_morph

if __name__ == "__main__" :
    moto_base = []
    moto_pos = []
    ans = verb()
    dst_srcs = ans[0]
    id_morph = ans[1]
    for number in range(len(dst_srcs)) :
        dst_srcs_dict = dst_srcs[number]
        id_morph_dict = id_morph[number]
        for key ,values in dst_srcs_dict.items() : # key:かかり先,value:かかり元
            if key != -1 :
                saki_bunsetsu = id_morph_dict[key] # 文節がこれ
                for saki_tango in saki_bunsetsu :
                    # print(saki_tango)
                    if "動詞" in saki_tango :
                        #print(key, values)
                        for value in values : # 動詞にかかるかかり元のリスト
                            #print(value)
                            moto_bunsetsu = id_morph_dict[value]
                            # print(moto_bunsetsu)
                            for num in range(len(moto_bunsetsu)) :
                                try :
                                    meishi = moto_bunsetsu[num]
                                    wo = moto_bunsetsu[num + 1]
                                    if "サ変接続" in meishi and "を" in wo :
                                        moto_list = []
                                        j_list = []
                                        w_list = []
                                        sahen_wo = meishi[0] + wo[0]
                                        saki = saki_tango[0]
                                        # print(sahen_wo + saki)
                                        # print(key) # sakiの動詞
                                        # print(value) #　サ変接続 + を
                                        # print(values) # サ変接続 + を の文節の番号、それ以外の番号
                                        if len(values) > 1 : # サ変接続 + を の文節のみではない場合
                                            for val in values :
                                                if val != value : # サ変接続 + を の文節でない場合
                                                    bunsetsu = id_morph_dict[val]
                                                    # print(bunsetsu)
                                                    for word in bunsetsu : # 単語を回す
                                                        moto_base.append(word[0])
                                                        moto_pos.append(word[1])
                                                    # print(moto_base)
                                                    # print(moto_pos)
                                                    if "助詞" in moto_pos :
                                                        tango = "".join(moto_base)
                                                        m_num = [num for num, jyoshi in enumerate(moto_pos) if jyoshi == "助詞"]
                                                        for num in m_num :
                                                            jyoshi_word = moto_base[num] # jyoshi_wordは助詞の単語
                                                            jyoshi_list = [jyoshi_word, tango]
                                                            moto_list.append(jyoshi_list)
                                                    moto_base = []
                                                    moto_pos = []
                                            # print(moto_list)
                                            moto_list.sort() # 助詞を基準に「あ」から「ん」の順で並べ替える
                                            # print(moto_list)
                                            for jyoshi_bunsetsu in moto_list :
                                                j = jyoshi_bunsetsu[0] # 助詞の取り出し
                                                j_list.append(j)
                                                w = jyoshi_bunsetsu[1] # 単語 + 助詞の取り出し
                                                if w not in w_list : # 被りを防ぐ
                                                    w_list.append(w)
                                            j_word = " ".join(j_list)
                                            w_word = " ".join(w_list)
                                            # print(sahen_wo + saki + "\t" + j_word + "\t" + w_word)
                                        #else :
                                            #print(sahen_wo + saki)
                                            #continue
                                except :
                                    break
