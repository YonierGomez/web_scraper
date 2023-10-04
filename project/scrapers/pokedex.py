import requests
from bs4 import BeautifulSoup


def get_pokemon(url):
    r = requests.get(url)

    if r.ok:
        soup = BeautifulSoup(r.text, 'html.parser')

        # Encuentra todos los nombres y tipos de Pokémon en la página
        names = []
        types = []

        for get_me_name in soup.find_all('td', class_='cell-name'):
            valid_name = get_me_name.find('a', class_='ent-name')
            names.append(valid_name.text)

        for get_me_type in soup.find_all('a', class_='type-icon'):
            types.append(get_me_type.text)

        # Imprime los nombres y tipos de Pokémon uno al lado del otro
        for name, type in zip(names, types):
            print(f"Nombre: {name} - Tipo: {type}")


if __name__ == '__main__':
    get_pokemon('https://pokemondb.net/pokedex/all')
