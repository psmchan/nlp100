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
    ans = verb()
    dst_srcs = ans[0]
    id_morph = ans[1]
    for number in range(len(dst_srcs)) :
        dst_srcs_dict = dst_srcs[number]
        id_morph_dict = id_morph[number]
        for key ,values in dst_srcs_dict.items() : # key:かかり先,value:かかり元
            if key != -1 :
                for value in values :
                    moto_bunsetsu = id_morph_dict[value] # 1個の文節
                    # print(moto_bunsetsu)
                    for moto_tango in moto_bunsetsu :
                        # print(moto_tango)
                        if moto_tango[1] == "名詞" and moto_tango[2] == "サ変接続" : # [1]が名詞、[2]がサ変接続
                            sahen = moto_tango[0] # サ変接続の名詞の単語
                            motoindex = moto_bunsetsu.index(moto_tango) # 参照できるようにする
                            print(motoindex)
