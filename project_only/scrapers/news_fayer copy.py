import requests
from bs4 import BeautifulSoup


def news(URL, DOMAIN):
    """Funcion para obtener noticias de Fayer Wayer News"""
    r = requests.get(URL)

    if r.ok:
        r_content = r.text
        leer = r.text
        
        soup = BeautifulSoup(leer, 'html.parser')

        title = soup.find('div', {'class': 'container layout-section'})
        print('='*130)
        print('Fayer Wayer News - Principales noticias Sr Yonier')
        for r_title in title.find_all('div', class_='list-item', limit=3):
            print('='*130)  
            # print(r_title.text)
            return f'* {r_title.h2.text}: { DOMAIN + r_title.div.a["href"]}'
            # print(f'* {r_title.h2.text}: { DOMAIN + r_title.div.a["href"]}', '\n')

if __name__ == '__main__':
    news('https://www.fayerwayer.com/internet/', 'https://www.fayerwayer.com')
