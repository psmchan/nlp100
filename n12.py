"""
各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．
"""
"""
文字列に直すときに改行していれたいけど文字化け起こす。
とりあえず1列目だけ、2列目だけを抜き出すことはできた
"""

import sys # sysをインポートする

#ans_col1 = ""
#ans_col2 = ""

with open(sys.argv[1],"r") as f1 , open(sys.argv[2],"w") as f2 , open(sys.argv[3],"w") as f3 :
    for word in f1 :
        #word = word.strip() # 改行抜いた
        word_list = word.split("\t") # タブを区切ってリストにつっこむ
        # print(word_list)
        col1 = [col1_word[0] for col1_word in word_list[0]]
        col2 = [col2_word[0] for col2_word in word_list[1]]
        for ans_col1 in col1 :
            f2.write(ans_col1)
        for ans_col2 in col2 :
            f3.write(ans_col2)
