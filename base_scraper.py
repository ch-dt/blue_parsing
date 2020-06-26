from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl
import re

#class Announcement:

links_to_websites = [] #список ссылок из выборки
list_of_announcements = [] #object with fields

html = urlopen('https://www.cian.ru/cat.php?deal_type=sale&district%5B0%5D=325&engine_version=2&maxmcad=50&object_type%5B0%5D=1&offer_type=suburban')
bs = BeautifulSoup(html.read(), 'html.parser')

query_results_list = bs.findAll('div', {'class': re.compile('--main-info--')})
i = 1
for result in query_results_list:
    #print(i)
    a = result.find('a').attrs['href'] #remove for about a half of redundant links
    if 'https' in a:
        links_to_websites.append(a)
    #print(a)
    i = i + 1

for link in links_to_websites:
    html = urlopen(link)
    bs = BeautifulSoup(html.read(), 'html.parser')
    aobj = {}
    aobj['html'] = link
    aobj['district'] = bs.find('address').children[1].text
    list_of_announcements.append(aobj)

print(list_of_announcements)


