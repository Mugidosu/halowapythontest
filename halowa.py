##おおもと　http://su-gi-rx.com/2017/11/06/python_14/
# coding:utf-8
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

#画像取得対象とするURLをテキストファイルから取得
with open('target_url.txt','r') as f:
    for row in f:
        target_url = row.strip()
print(target_url)
target_netloc = '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(target_url))
target_netloc = target_netloc[:-1]
print(target_netloc)
images = []
#imgタグのsrcアトリビュートの名前ずらし追跡用
img_attr_name = ["src","data-original"]
img_ext_name = ["jpg","png"]

soup = BeautifulSoup(requests.get(target_url).content,'lxml')
for link in soup.find_all("img"): # imgタグを取得しlinkに格納
    print("imglink- " + str(link))
    for ext in img_ext_name:
        bExsits = False
        for attr in img_attr_name:
            if link.get(attr) is not None:
                existattr = link.get(attr).endswith("."+ext) # imgタグ内の.jpgであるsrcタグを取得
                if existattr is not None:
                    bExsits = True
                    images.append(link.get(attr)) # imagesリストに格納
                    break
        if bExsits:
            break

if len(images) > 0:
    for target in images: # imagesからtargetに入れる
        if target is None:
            continue
        if target.startswith('http'):
            imageurl = target
        else:    
            imageurl = target_netloc + target
        print (imageurl)
        re = requests.get(imageurl)
        with open('img/' + imageurl.split('/')[-1], 'wb') as f: # imgフォルダに格納
            f.write(re.content) # .contentにて画像データとして書き込む

#pushのてすと
#print("halowa!")
