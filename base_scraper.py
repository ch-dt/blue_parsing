from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

links_to_websites = [] #список ссылок из выборки

html = urlopen('https://www.cian.ru/cat.php?deal_type=sale&district%5B0%5D=325&engine_version=2&maxmcad=50&object_type%5B0%5D=1&offer_type=suburban')
bs = BeautifulSoup(html.read(), 'html.parser')

query_results_list = bs.findAll('div', {'class': re.compile('--main-info--')})
i = 1
for result in query_results_list:
    print(i)
    print(result['class'])
    i = i + 1

