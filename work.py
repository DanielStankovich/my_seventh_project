import requests
import codecs

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/2010010 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,aplication/xml;q=0.8'
           }

url = 'https://www.work.ua/ru/jobs-kyiv-python/'
resp = requests.get(url, headers=headers)

h = codecs.open('work.html', 'w', 'utf-8')
h.write(str(resp.text))
h.close()