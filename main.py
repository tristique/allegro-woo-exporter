#import certifi
#import urllib3
#import lxml
import lxml.html
import requests
#from urllib.request import urlopen


#user = 'LumariGold'
'''
# section working fine already
user = 'allora_pl'

site_main = 'https://allegro.pl/uzytkownik/' + user
print ('Address: ' + site_main)

res = requests.get(site_main)
print('Response: ' + str(res))
content_main = lxml.html.fromstring(res.content)
print('Content: ' + str(content_main))
# sample site from https://www.ipeen.com.tw/comment/778246
# name = doc.xpath(".//meta[@itemprop='name']/@content")
pages = content_main.xpath('.//div[4]/div/div/div/span[@class="m-pagination__text"]/text()')[0]
print('Pages: ' + str(pages))

for x in range(0, int(pages)):
    subpage = site_main + '?p=' + str(x+1)
    print(' Subpage: ' + subpage)
    res = requests.get(subpage)
    content_subpage = lxml.html.fromstring(res.content)
    print('  Content: ' + str(content_subpage))
    items = content_main.xpath('.//article/div/div/div[1]/div/div[1]/a/@href')
    
    for item_url in items:
        print('    ' + str(item_url))
        res = requests.get(item_url)
        item_page = lxml.html.fromstring(res.content)
        print('    Content: ' + str(item_page))
'''
# for testing purposes only
item_page = 'https://allegro.pl/oferta/bransoletka-sznurkowa-2mm-charms-gratis-6921443347'
res = requests.get(item_page)
print('Response: ' + str(res))
content_item = lxml.html.fromstring(res.content)
print('Content: ' + str(content_item))
title = content_item.xpath('.//div[2]/h1/text()')[0].capitalize()
print(title)
section = content_item.xpath('.//div/div/div[1]/div/div/div/div/div/div[5]/a/span/text()')[0].lower()
print(section)
price = content_item.xpath('?')
print(price)
