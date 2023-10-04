import requests
from bs4 import BeautifulSoup


def news(URL):
    """Funcion para obtener noticias de muy linux"""
    r = requests.get(URL)

    if r.ok:
        r_content = r.text
        leer = r.text
        
        soup = BeautifulSoup(leer, 'html.parser')
        title = soup.find('section', {'class': 'zox-blog-grid left zoxrel left zox100 infinite-content zox-divr zox-s6'})

        print('='*130)
        print('Muy Linux - Principales noticias Sr Yonier')
        for r_title in title.find_all('article'):
            print('='*130)  
            print(f'* {r_title.div.h2.text}: {r_title.div.a["href"]}', '\n')

if __name__ == '__main__':
    news('https://www.muylinux.com/')
