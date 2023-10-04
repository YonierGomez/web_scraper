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

        get_news = []
        for r_title in title.find_all('article'):
            get_news.append(f'*{r_title.div.h2.text}: {r_title.div.a["href"]}')
            
        return get_news

if __name__ == '__main__':
    print('='*130)
    print('Muy Linux - Principales noticias Sr Yonier')
    print('='*130)
    for new in news('https://www.muylinux.com/'):
        print(new, '\n')
        print('='*130)
