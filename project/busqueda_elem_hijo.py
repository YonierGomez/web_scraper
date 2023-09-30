import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('site.html', 'r') as file:
        site = file.read()

    soup = BeautifulSoup(site, 'html.parser')

    """Para esto usaremos el metodo find_all()"""
    for element in soup.find_all('div', {'class': 'producto'}):
        h3 = element.h3
        p = element.p

        if h3 and p:
            print("Nombre del producto:", h3.text)
            print("Precio del producto:", p.text)
            print("\n")
