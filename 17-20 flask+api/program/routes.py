from datetime import datetime

import requests
from flask import render_template,request

from program import app


@app.route('/')
@app.route('/index')
def index():
    time_now = str(datetime.today())
    return render_template('index.html', time=time_now)


@app.route('/100days')
def hundred_days():
    return render_template('test.html')


@app.route('/chuck')
def chuck():
    joke = get_chuck_joke()
    return render_template('chuck.html', joke=joke)


@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    pokemons = []
    if request.method == 'POST' and 'pokecolor' in request.form:
        color = request.form.get('pokecolor')
        pokemons = get_poke_color(color)

    return render_template('pokemon.html', pokemons=pokemons)


def get_chuck_joke():
    response = requests.get('https://api.chucknorris.io/jokes/random')
    data = response.json()
    return data['value']


def get_poke_color(color: str):
    response = requests.get('https://pokeapi.co/api/v2/pokemon-color/' + color.lower())
    pokedata = response.json()
    pokemons = []

    for i in pokedata['pokemon_species']:
        pokemons.append(i['name'])

    return pokemons
