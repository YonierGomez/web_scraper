import requests
from bs4 import BeautifulSoup


# En news_fayer.py
def news(URL, DOMAIN):
    """Funcion para obtener noticias de Fayer Wayer News"""
    r = requests.get(URL)
    noticias = []

    if r.ok:
        r_content = r.text
        leer = r.text

        soup = BeautifulSoup(leer, 'html.parser')

        title = soup.find('div', {'class': 'container layout-section'})
        for r_title in title.find_all('div', class_='list-item'):
            # Formatea y agrega cada noticia a la lista de noticias
            noticias.append(f'* {r_title.h2.text}: {DOMAIN + r_title.div.a["href"]}')

    return noticias  # Devuelve la lista de noticias

if __name__ == '__main__':
    print(news('https://www.fayerwayer.com/internet/', 'https://www.fayerwayer.com'))
