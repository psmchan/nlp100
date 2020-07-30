"""
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，
テキストに変換せよ
"""
"""
re.subで除去したい文字が複数あるとき
re.sub(r"[この中に除去したい文字を入れる]")
"""
import n26
import re
import pprint

def link() :
    tem2 = n26.em()
    #pprint.pprint(ans,width = 400)

    lin = r"\[\[(.*|.*\|.*|.*#.*\|.*)\]\]"

    for key in tem2 :
        value = tem2[key]
        lin_s = re.search(lin,value)
    #return lin_s
        if lin_s != None :
            value = re.sub(r"[\[\[#\|\]\]]","",value)
            tem2[key] = value
        else :
            continue
    return tem2

if __name__ == "__main__" :
    ans = link()
    pprint.pprint(ans,width = 400)
