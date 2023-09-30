import requests
from bs4 import BeautifulSoup


def news(URL):
    """Funcion para obtener noticias de muy linux"""
    r = requests.get(URL)

    if r.ok:
        r_content = r.text
        leer = r.text
        
        soup = BeautifulSoup(leer, 'html.parser')
        title = soup.find('div', {'class': 'content-container'})

        print('='*130)
        print('Xataka - Principales noticias Sr Yonier')
        for r_title in title.find_all('article', class_='recent-abstract abstract-article', limit=10):
            print('='*130)  
            print(f'* {r_title.h2.text}: {r_title.a["href"]} ', '\n')

if __name__ == '__main__':
    news('https://www.xataka.com/')
