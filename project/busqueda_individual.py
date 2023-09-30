import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('site.html', 'r') as file:
        site = file.read()

    soup = BeautifulSoup(site, 'html.parser')

    title = soup.find('title')
    print(title)
    print(title.text)
