"""
動詞の表層形をすべて抽出せよ．
"""
import n30

ver = n30.neko()

for neko_list in ver :
    for neko_dict in neko_list :
        if neko_dict["pos"] == "動詞" :
            print(neko_dict["surface"])
