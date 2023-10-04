import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    def get_pokemon(URL, DOMAIN):

        r = requests.get(URL)

        if r.ok:
            soup = BeautifulSoup(r.text, 'html.parser')

            table = soup.find('table', {'id': 'pokedex'})
            for row in table.tbody.find_all('tr', limit=10):
                columns = row.find_all('td', limit=3)
                name = columns[1].a.text
                tipo = [a.text for a in columns[2].find_all('a')]

                link = DOMAIN+columns[1].a['href']

                r_specie = requests.get(link)
                if r_specie.ok:
                    species_content = r_specie.text

                    species_soup = BeautifulSoup(
                        species_content, 'html.parser')
                    table_species = species_soup.find(
                        'table', class_='vitals-table')

                    name_species = table_species.tbody.find_all('tr')[
                        2].td.text

                    print(f'Soy {name} y mi tipo es:', *tipo,
                          f'mi especie es {name_species}', link, '\n')
                # print(name + ':', *tipo)


get_pokemon('https://pokemondb.net/pokedex/all', 'https://pokemondb.net')
