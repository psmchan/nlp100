"""
与えられた文の係り受け木を有向グラフとして可視化せよ．
可視化には，Graphviz等を用いるとよい．
"""
"""
ノード追加
〇〇.node("〇〇")
辺追加
〇〇.edge("〇〇","〇〇")
"""
from n42 import read_txt
from graphviz import Digraph

graph = Digraph(format = "png")

ans = read_txt()
dst_srcs = ans[0]
id_morph = ans[1]
dst_srcs_dict = dst_srcs[1]
id_morph_dict = id_morph[1]
for key,value in dst_srcs_dict.items() :
    if key == -1 :
        continue
    else :
        for values in value :
            moto_num = id_morph_dict[values]
            saki_num = id_morph_dict[key]
            moto_word = "".join(moto_num)
            saki_word = "".join(saki_num)
            #print(moto_word + "->" + saki_word)
            graph.node(moto_word)
            graph.node(saki_word)
            graph.edge(moto_word, saki_word)
graph.render("answer44")
