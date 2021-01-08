"""
形態素を表すクラスMorphを実装せよ．
このクラスは
表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
をメンバ変数に持つこととする．
さらに，係り受け解析の結果（ai.ja.txt.parsed）を読み込み，
各文をMorphオブジェクトのリストとして表現し，冒頭の説明文の形態素列を表示せよ．
"""
"""
コンストラクタ → __init__
インスタンスを作成する際に重要な処理を含むもの
どのように生成するか、どのようなデータを持たせるかなど、
といった情報を定義するのに必要なメソッドになる。

名詞:クラス
動詞:メソッド

"""
class Morph : # Morphクラスを作る
    def __init__(self, surface, base, pos, pos1) : # 要素としてsurface,base,pos,pos1を持つよ
        self.__surface = surface
        self.__base = base
        self.__pos = pos
        self.__pos1 = pos1
        return

    def make_dict(self) : #　make_dictメソッドを作る
        if self.__base == "*\n" : # もしbaseが"*\n"で入ってきたら
            self.__base = "*" # "*"に変えておいてね
        morph_dict = { # morph_dict を作る
            "surface" : self.__surface, # surfaceはself.__surface
            "base" : self.__base, # baseはself.__base
            "pos" : self.__pos, # posはself.__pos
            "pos1" : self.__pos1 # pos1はself.__pos1を使う
        }
        return morph_dict

    def get_surface(self) :
        return self.__surface

    def get_base(self) :
        #if self.__base == "*\n" :
        return self.__base
        #else :
            #return self.__base

    def get_pos(self) :
        return self.__pos

    def get_pos1(self) :
        return self.__pos1

    def disp_morph(self) :
        return self.__surface, self.__base, self.__pos, self.__pos1

def ai() :
    ai_list = []
    final_list = []
    with open("ai.ja.txt.parsed", "r") as f :
        for line in f :
            if line[0] == "*" : # cabochaの要素の行はスキップ
                continue
            else :
                line.rstrip("\n")
                sur = line.split("\t")
                if len(sur) != 1 :
                    pos = sur[1].split(",")
                    base = pos[6]
                    if base == "*\n" :
                        base = "*"
                    morph = Morph(sur[0], base, pos[0], pos[1]) # Morphクラスの__init__のところ
                    display_morph =" ".join(morph.disp_morph()) # disp_morphをつかう.表示がタプルなのでjoinでひっつける
                    ai_list.append(display_morph)
                else :
                    if len(ai_list) != 0 :
                        final_list.append(ai_list)
                        ai_list = []
        return final_list

if __name__ == "__main__" :
    ans = ai()
    for ans_final in ans[1:2] :
        for ans_ai in ans_final :
            print(ans_ai)
