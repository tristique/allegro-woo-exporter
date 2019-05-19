#import certifi
#import urllib3
#import lxml
import lxml.html
import requests
import re
#from urllib.request import urlopen

# normal mode - set to 0
# test mode - program will loop only X items
test_mode = 0
user = 'allora_pl'

site_main = 'https://allegro.pl/uzytkownik/' + user

# for test mode
if test_mode != 0:
    print('RUNNING IN TEST MODE - ONLY ' + str(test_mode) + ' ITEMS WILL BE FETCHED')

print ('Address: ' + site_main)

res = requests.get(site_main)
print('Response: ' + str(res))
content_main = lxml.html.fromstring(res.content)
print('Content: ' + str(content_main))
# sample site from https://www.ipeen.com.tw/comment/778246
# name = doc.xpath(".//meta[@itemprop='name']/@content")
pages = content_main.xpath('.//div[3]/div/div/div/div/div/div[2]/div[1]/div[2]/div[3]/div/div/div/div/span[@class="m-pagination__text"]/text()')[0]
print('Pages: ' + str(pages))

# for test mode
if test_mode != 0:
    pages = 1
    
output = open('C:\\Users\\trist\\Desktop\\allegro_output_3.csv','w+')
output.write('tax:product_type;post_title;category;post_content;regular_price;manage_stock;stock;stock_status;images;post_status\n')

# get product subpages, 60 items per subpage by default
for x in range(0, int(pages)):
    subpage = site_main + '?p=' + str(x+1)
    # print(' Subpage: ' + subpage)
    res = requests.get(subpage)
    content_subpage = lxml.html.fromstring(res.content)
    print('  Content: ' + str(content_subpage))
    items = content_main.xpath('.//article/div/div/div[1]/div/div[1]/a/@href')
    # print(items)

    # example item url: https://allegro.pl/oferta/woreczki-we-wzorki-opakowania-do-bizuterii-6x8cm-7622161189
    # for every item url get required data: title, description, images etc.

    # for test mode
    if test_mode != 0:
        items = items[:test_mode]
    
    for item_url in items:
        # print('    Item: ' + str(item_url))
        res = requests.get(item_url)
        item_page = lxml.html.fromstring(res.content)
        # print('    Content: ' + str(item_page))

        content_item = lxml.html.fromstring(res.content)
        # print('      Content: ' + str(content_item))
        
        # item number, for example 7622161189
        # not displayed on the allegro page already
        # item = content_item.xpath('//div[3]/div/div/div[7]/div/div/div/div/div/div/div/span[2]/text()')[0]
        # but still in url
        item = item_url[-10:]
        print('   Item ' + item, end='')

        title = content_item.xpath('.//div[3]/h1/text()')[0].capitalize()        
        print('.', end='')

        category = content_item.xpath('.//div/div/div[1]/div/div/div/div/div/div[5]/a/span/text()')[0].lower()
        # print(category)
        print('.', end='')

        price1 = content_item.xpath('//div/div/div/div/div/div/div[2]/div[@class="a08bbb79"]/div[1]/text()[1]')
        price2 = content_item.xpath('//div/div/div/div/div/div/div[2]/div[@class="a08bbb79"]/div[1]/span/text()[1]')
        price = str(float(price1[0] + '.' + price2[0]))
        # print(price)
        print('.', end='')


        tmp = str(content_item.xpath('.//div[2]/form/div[1]/div[2]/div[2]/text()'))
        amount = re.sub(r'\D', '', tmp)
        # print(amount)
        print('.', end='')

        images = content_item.xpath('//*[@id="user_field"]/article/div/section/div/section/img/@src')
        images_ext = [s + '.jpg' for s in images] # add extension to filenames
        for image in images:
            image +=  '.jpg'
            # print(image)
            print('.', end='')
        images_full =  ' , '.join(images_ext)

        descriptions = content_item.xpath('//*[@id="user_field"]/article/div/section/div/section/p/b/text()')
        for description in descriptions:
            # print(description)
            print('.', end='')
            desc_full =  ' '.join(descriptions)
        print('.')

        # then put item's data into csv output file
	# https://docs.woocommerce.com/document/product-csv-import-suite-column-header-reference/
        #output.write('tax:product_type;post_title;category;post_content;regular_price;manage_stock;stock;stock_status;images')
        output.write('simple' + ';' + title + ';' + category + ';' + desc_full + ';' + price + ';' + 'yes' + ';' + amount + ';' + 'instock' + ';' + images_full + ';draft\n')
output.close()
print('Finished.')
