"""
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
"""
import re
import n25

def em() :
    tem1 = n25.tem()

    empha = r"\'{2,5}"

    for key in tem1 :
        value = tem1[key]
        em_s = re.search(empha,value)
        if em_s != None :
            value = re.sub(empha,"",value)
            tem1[key] = value
        else :
            continue
    return tem1

if __name__ == "__main__" :
    ans = em()
    for key, value in ans.items() :
        print(key, value)
