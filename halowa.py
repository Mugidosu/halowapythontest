##おおもと　http://su-gi-rx.com/2017/11/06/python_14/
#coding:utf-8
import requests
from bs4 import BeautifulSoup


#画像取得対象とするURLをテキストファイルから取得
with open('target_url.txt','r') as f:
    for row in f:
        target_url = row.strip()
images = []

soup = BeautifulSoup(requests.get(target_url).content,'lxml')
for link in soup.find_all("img"): # imgタグを取得しlinkに格納
    if link.get("src").endswith(".jpg"): # imgタグ内の.jpgであるsrcタグを取得
        images.append(link.get("src")) # imagesリストに格納
    elif link.get("src").endswith(".png"): # imgタグ内の.pngであるsrcタグを取得
    	images.append(link.get("src")) # imagesリストに格納

for target in images: # imagesからtargetに入れる
    re = requests.get(target)
    with open('img/' + target.split('/')[-1], 'wb') as f: # imgフォルダに格納
        f.write(re.content) # .contentにて画像データとして書き込む

print("halowa!")
