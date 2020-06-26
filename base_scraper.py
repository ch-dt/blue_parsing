from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl
import re

#class Announcement:

links_to_websites = [] #список ссылок из выборки #TODO названия
list_of_announcements = [] #object with fields #todo или надо оформлять в виде объекта класса?

html = urlopen('https://www.cian.ru/cat.php?deal_type=sale&district%5B0%5D=325&engine_version=2&maxmcad=50&object_type%5B0%5D=1&offer_type=suburban') #TODO возможность вставлять любую сссылку (или вообще сделать чтобы работало через командную строку
bs = BeautifulSoup(html.read(), 'html.parser') #todo что есть кроме html.parser

query_results_list = bs.findAll('div', {'class': re.compile('--main-info--')})
i = 1 #todo просто для отладки
for result in query_results_list:
    #print(i)
    a = result.find('a').attrs['href'] #todo remove for about a half of redundant links FIND FINDALL
    if 'https' in a:
        links_to_websites.append(a)
    #print(a)
    i = i + 1

for link in links_to_websites:
    html = urlopen(link)
    bs = BeautifulSoup(html.read(), 'html.parser')
    aobj = {}
    aobj['html'] = link

    geo_iterator = bs.find('address').children #TODO как добавить в список только теги, без запятых + ЛИШНЯЯ промежуточная переменная
    geo_data = []
    for child in geo_iterator:
        geo_data.append(child)
    aobj['district'] = geo_data[2].text
    aobj['settlement'] = geo_data[6].text
    aobj['moscow_or_not'] = geo_data[0].text
    list_of_announcements.append(aobj)

    #TODO PRICE price_iterator = bs.findAll('div', {'class': re.compile('--price-container--')})

    #TODO BUILDING building_iterator

    #TODO VIEWS iterator

print('RESULT')
print(list_of_announcements)

wb = openpyxl.Workbook()
sheet = wb["Sheet"]
sheet['A1'] = 'веб адрес'
sheet['B1'] = 'город'
sheet['C1'] = 'округ'
sheet['D1'] = 'поселение'
for i in range(1, len(list_of_announcements)+1): #todo так перебирать тупо
    a = 'A{}'.format(i)
    b = 'B{}'.format(i)
    c = 'C{}'.format(i)
    d = 'D{}'.format(i)
    sheet[a] = list_of_announcements[i-1]['html']
    sheet[b] = list_of_announcements[i-1]['moscow_or_not']
    sheet[c] = list_of_announcements[i-1]['district']
    sheet[d] = list_of_announcements[i-1]['settlement']

wb.save('first_excel.xlsx')




