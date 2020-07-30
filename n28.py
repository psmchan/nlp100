"""
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，
国の基本情報を整形せよ．
"""
import n27
import re
import pprint

def med() :
    tem = n27.link()

    for key in tem :
        value = tem[key]
        wiki = re.search("\{\{.*\}\}|[http://.*]",value)
        if wiki != None :
            value = re.sub("[\{\{\}\}]","",value)
            value = re.sub("\[http://.*\]","",value)
            tem[key] = value
        else :
            continue
    return tem

if __name__ == "__main__" :
    ans = med()
    pprint.pprint(ans,width = 400)
