import requests
import codecs
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/2010010 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,aplication/xml;q=0.8'
           }


def work(url):
    jobs = []
    errors = []
    domain = 'https://www.work.ua'
    url = 'https://www.work.ua/ru/jobs-kyiv-python/'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', id='pjax-job-list')
        if main_div:
            div_lst = main_div.find_all('div', attrs={'class': 'job-link'})
            for div in div_lst:
                title = div.find('h2')
                href = title.a['href']
                content = div.p.text
                company = 'No name'
                logo = div.find('img')
                if logo:
                    company = logo['alt']
                jobs.append({'title': title.text, 'url': domain + href,
                             'description': content, 'company': company})
        else:
            errors.append({'url': url, 'title': "Div does not exists"})

    else:
        errors.append({'url': url, 'title': "Page do not response"})
    return jobs, errors


def rabota(url):
    jobs = []
    errors = []
    domain = 'https://rabota.ua'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        new_jobs = soup.find('div', attrs={'class': 'card-body'})
        table = soup.find('table', id='ctl00_content_vacancyList_gridList')
        if table:
            tr_lst = table.find_all('tr', attrs={'id': True})
            for tr in tr_lst:
                div = tr.find('div', attrs={'class': 'card-body'})
                if div:
                    title = div.find('p', attrs={'class': 'card-title'})
                    href = title.a['href']
                    content = div.p.text
                    company = 'No name'
                    p = tr.find('p', attrs={'class': 'company-name'})
                    if p:
                        company = p.a.text
                    jobs.append({'title': title.text, 'url': domain + href,
                                 'description': content, 'company': company})
        else:
            errors.append({'url': url, 'title': "Table does not exists"})

    else:
        errors.append({'url': url, 'title': "Page do not response"})
    return jobs, errors

if __name__ == '__main__':
    url = 'https://rabota.ua/zapros/python/киев'
    jobs, errors = rabota(url)
    h = codecs.open('work.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()
