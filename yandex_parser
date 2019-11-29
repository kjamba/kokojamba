import requests
from bs4 import BeautifulSoup
import lxml



def get_html(url):
    r = requests.get(url)
    return r.text

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    links = soup.find('ul', class_ = 'serp-list').find_all('li', class_ = 'serp-item')

    for link in links:
        title = link.find('div', class_='organic').find('a', class_='link').text.strip()
        href = link.find('div', class_ = 'path').find('a', class_ = 'link').text.strip()
        # page = link.get('data-fast')

        data = {'title': title,
                'href': href,}
                # 'page': page}
        print(data)


   # for link in links:


def main():
    
    base_url = 'https://yandex.ru/search/?text='
    query = 'купить%20окно'
    page = '&p='

    
    # headers = {'accept': '*/*',
    #            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

    for i in range(2):
        url_gen = base_url + query + '&lr=43' + page + str(i)
        # session = requests.session()
        # request = session.get(url_gen, headers = headers)
        # if request.status_code == 200:
        #     print('ok')
        # else:
        #     print('error')

        html = get_html(url_gen)
        get_page_data(html)
        # print(url_gen)



if __name__ == '__main__':
    main()
