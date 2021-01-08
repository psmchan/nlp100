import n40

class Chunk() :
    def __init__(self) :
        self.id = -1
        self.morphs = []
        self.dst = -1
        self.srcs = []

    def get_dst(self, saki) :
        self.dst = saki
        if "D" in self.dst :
            dst = self.dst.replace("D", "")
            dst = int(dst)
        return dst

    def get_srcs(self, dst, moto, moto_dict) :
        if dst in moto_dict :
            moto_list = moto_dict[dst]
            moto_list.append(moto)
            moto_dict[dst] = moto_list
        else :
            moto_list = self.srcs
            moto_list.append(moto)
            moto_dict[dst] = moto_list
        return moto_dict

    def id_morphs(self, moto, morph, im_dict) :
        self.id = moto
        self.morphs.append(morph)
        if self.id in im_dict :
            im_dict[self.id] + self.morphs
        else :
            im_dict[self.id] = self.morphs
        return im_dict

def read_txt() :
    moto_dict = dict() # dstとsrcsのdict
    im_dict = dict()
    final_dst_srcs = []
    final_id_morph = []
    with open("ai.ja.txt.parsed","r") as f : # ファイル読み込み
        for line in f : # 1行ずつ読む
            line = line.rstrip("\n") # 改行取る
            if line[0] == "*" : # cabochaの行
                #print(line)
                line_list = line.split() # splitでわける
                chunk_ans = Chunk() # chunkクラス
                moto = int(line_list[1]) # かかり元
                saki = line_list[2] # かかり先
                dst = chunk_ans.get_dst(saki) # かかり先,get_dst
                #print("dst:" + dst)
                dst_srcs = chunk_ans.get_srcs(dst, moto, moto_dict) # dstとsrcsのdictを作る
                #print("dst:srceのdict")
                #print(dst_srcs)
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
                #print(final_dst_srcs)
                #print(final_id_morph)
                moto_dict = dict()
                im_dict = dict()
            else : # それ以外の行
                sur = line.split("\t")
                #if len(sur) != 1 : # 単語の行
                pos = sur[1].split(",")
                morph_class = n40.Morph(sur[0], pos[6], pos[0], pos[1])
                morph_surface = morph_class.get_surface()
                    #print("surface :" + morph_surface)
                id_morph_dict = chunk_ans.id_morphs(moto, morph_surface, im_dict)
                    #print("idとmorphのdict")
                    #print(id_morph_dict)
                    #print("word")
                #else : # EOSの行
                    #print("EOS")
                    #print("dst:srcsのdict")
                    #print(dst_srcs)
                    #print("idとmorphのdict")
                    #print(id_morph_dict)
                    #final_dst_srcs.append(dst_srcs)
                    #final_id_morph.append(id_morph_dict)
                    #moto_dict = dict()
                    #im_dict = dict()
        return final_dst_srcs, final_id_morph

if __name__ == "__main__" :
    ans = read_txt()
    dst_srcs = ans[0]
    id_morph = ans[1]
    #num = 0
    #for dst_srcs_dict in dst_srcs :
        #print(dst_srcs_dict)
    #for id_morph_dict in id_morph :
        #print(id)
    #while num < len(dst_srcs) :
    dst_srcs_dict = dst_srcs[1]
        #print(dst_srcs_dict)
    id_morph_dict = id_morph[1]
        #print(id_morph_dict)
        #num += 1
    for key,value in dst_srcs_dict.items() :
            #keys = int(key)
        if key == -1 :
            continue
        else :
            for values in value :
                    #value_num = int(values)
                    #print(type(key))
                    #print(type(values))
                    #print(id_morph_dict)
                moto_num = id_morph_dict[values]
                    #print(moto_num)
                saki_num = id_morph_dict[key]
                    #print(saki_num)
                moto_word = "".join(moto_num)
                saki_word = "".join(saki_num)
                print(moto_word + "->" + saki_word)
    #num =-2
    #dst_srcs = ans[0]
    #print(len(dst_srcs))
    #id_morph = ans[1]
    #for key, value in dst_srcs.items() :
        #key = int(key)
        #print(key)
        #if key == -1 :
            #continue
        #else :
            #print("ans")
            #for values in value :
                #moto_word = id_morph[values]
                #saki_word = id_morph[key]
                #moto_word = "".join(moto_word)
                #saki_word = "".join(saki_word)
                #print(moto_word + "->" + saki_word)
        #num += 2
    #for num in dst_srcs :
        #print(num)
    #id_morph = ans[1]
    #for id in id_morph :
        #print(id)
