import requests
import pystache
import click
from base64 import b64encode
from clickclick import Action, info


def fetch_pokemon(number):
    r = requests.get('http://pokeapi.co/api/v2/pokemon/{}/'.format(number))
    r.raise_for_status()
    data = r.json()
    name = data['name']
    image_url = data['sprites']['front_shiny']
    r = requests.get(image_url)
    r.raise_for_status()
    encoded_img = b64encode(r.content)
    return {
        'pokemonName': str.lower(name.title()),
        'pokemonImage': encoded_img
    }


@click.command()
@click.option('--start', default='1', type=click.INT)
# end is exclusive!
@click.option('--end', default='10', type=click.INT)
@click.option('--file', default='./STUPS_cheatsheet.svg', type=click.Path())
def main(start, end, file):
    template = file
    with open(file) as read_file:
        template = read_file.read()
    print(start)
    info("Fetching Pokemon {} to {} (exclusive)".format(start, end))
    for i in range(start, end):
        pokemon = None
        rendered = ''
        with Action('Fetching Pokemon #{}'.format(i)):
            pokemon = fetch_pokemon(i)
        with Action('Rendering Pokemon #{}'.format(i)):
            rendered = pystache.render(template, pokemon)
        with Action('Saving Pokemon #{}'.format(i)):
            with open('./STUPS_cheatsheet_{}.svg'.format(i), 'w') as out:
                out.write(rendered)


if __name__ == '__main__':
    main()
