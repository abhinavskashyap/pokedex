from flask import Flask, request, render_template, redirect
import pandas as pd
import requests
import os

app = Flask(__name__)
img = os.path.join('static', 'Image', 'sad_pikachu.jpg')

@app.route('/', methods = ['GET', 'POST'])
def show_search():
    if request.method == 'GET':
        return render_template('./form.html')
    else:
        pokemon = request.form['search']
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response = requests.get(url)
        if response.status_code == 404:
            return render_template('./error.html', imageerror = img)
        else:    
            abilities = []
            for x in response.json()['abilities']:
                abilities.append(x['ability']['name'])
            image = response.json()['sprites']['other']['official-artwork']['front_default']
            return render_template('./index.html', abilities = abilities, image = image)
    
# run the server
if __name__ == '__main__':
    app.run(debug = True)