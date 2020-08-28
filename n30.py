"""
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は
表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとする
マッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""
"""
マッピング型
{
     key1 : value1,
     key2 : value2,
     ...
     keyN : valueN
}

形態素解析の結果
表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
"""
def neko() :
    neko_list = []
    neko_dic = []
    with open("neko.txt.mecab","r") as f :
        for line in f :
            line.rstrip("\n")
            sur = line.split("\t")
            if len(sur) != 1 : # EOSまでで1つのリストにする
                if sur[0] == "" :
                    continue
                else :
                    pos = sur[1].split(",")
                    dic = {
                        "surface" : sur[0],
                        "base" : pos[6],
                        "pos" : pos[0],
                        "pos1" : pos[1]
                        }
                    if dic["base"] == "*\n" :
                        dic["base"] = "*"
                    neko_dic.append(dic)
            else :
                if len(neko_dic) != 0 : # リストが空っぽの場合は飛ばす
                    neko_list.append(neko_dic)
                    neko_dic = []
        return neko_list

if __name__ == "__main__" :
    ans = neko()
    for ans_list in ans :
        for ans_dict in ans_list :
            print(ans_dict)
