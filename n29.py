"""
テンプレートの内容を利用し，国旗画像のURLを取得せよ．
"""
"""
API:画像の情報
https://www.mediawiki.org/wiki/API:Imageinfo/ja
ここに載っていたサンプルコード↓
import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": "File:Billy_Tipton.jpg"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for k, v in PAGES.items():
    print(v["title"] + " is uploaded by User:" + v["imageinfo"][0]["user"])
"""
import requests
import n28

uk = n28.med() # 前回の内容使うよ

s = requests.Session()

flag = uk["国旗画像"] # 探してほしいのは"国旗画像"

url = "https://ja.wikipedia.org/w/api.php" # これを使うらしい

params = {
    "action" : "query", # 汎用パラメータ
    "format" : "json", # 出力フォーマット
    "prop" : "imageinfo", # 記事の各構成要素を取得。action : queryを指定した場合に指定
    "titles" : "File:" + flag,
    "iiprop" : "url" # urlを取得してね
}

r = s.get(url = url, params = params) # ここからほぼ真似だけ
data = r.json()
pages = data["query"]["pages"]
for k, v in pages.items() :
    print(v["imageinfo"][0]["url"]) # ここだけ変わってる
