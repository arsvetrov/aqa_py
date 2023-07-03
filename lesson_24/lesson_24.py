import requests
from lxml.html import fromstring

# отримати вміст
r = requests.get('https://www.babyshop.com')
# перетвоюємо його в зрозуміле дерево через lxml
tree = fromstring(r.content)
# добуваємо дані по xpath
mainmenu = tree.xpath('//*[@class="text-base babyshop:font-bold md:text-lg"]/text()')
# дивимся, що вийшло
print(mainmenu)
