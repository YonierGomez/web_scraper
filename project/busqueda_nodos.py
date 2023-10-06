import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('site.html', 'r') as file:
        site = file.read()

    soup = BeautifulSoup(site, 'html.parser')

    """Estamos buscados los elementos hijos a los cuales les llamaremos nodos"""
    nodo = soup.find('div', {'class': 'producto'})
    # print(nodo.contents)  # ESTO ES UNA LISTA

    h3_item = nodo.contents[1]
    p_item = nodo.contents[3]

    print(h3_item)
    print(p_item)

    for child in nodo.children:
        print(child)
