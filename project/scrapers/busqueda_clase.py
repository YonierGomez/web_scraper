import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('site.html', 'r') as file:
        site = file.read()

    soup = BeautifulSoup(site, 'html.parser')

    """Para esto usaremos el metodo find_all()
        LAS BUSQUEDAS POR CLASES DEBEN SER PRECISAS    
    """
    print('-'*100)
    print('Probando opcion 1. attrs')
    for price in soup.find_all(attrs={'class': 'precio'}):
        print(price.text)

    print('-'*100)
    print('Probando opcion 2. class_ OPCIÓN RECOMENDADA')
    for price in soup.find_all(class_='precio'):
        print(price.text)
