import requests
from bs4 import BeautifulSoup


def crawler(data):
    base_url = 'http://en.wikipedia.org/wiki/'
    url = base_url + data
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    ul=soup.ul
    hrefs=[]
    i=0

    for link in ul.find_all('a'):
        href = url + link.get('href')
        hrefs.append(href)

    for link in soup.find_all('span', {'class': 'toctext'}, recursive='False'):
        title=link.string
        print (title)
        print (hrefs[i])
        print ('\n')
        i=i+1

print('\nWikipedia Search\n')
data = input('Enter topic to search wikipedia:')
print ('\n')
crawler(data)
#prompt=input('\nEnter Q to exit')