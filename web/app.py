from flask import Flask, render_template
import requests
import itertools
from flask_bootstrap import Bootstrap
import os


app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', defaults={'region': ''})
@app.route('/<string:region>', methods=['GET'])
def index(region):
    '''
    Endpoint that responsible for sending a request to the scrapyrt endpoint and displaying 
    the response in a prettier frontend.

    '''
    # environment variable containing scrapyrt's endpoint URL
    scrapyrt_url = os.environ.get("SCRAPY_URL")

    respG1 = requests.get(
        url=f"{scrapyrt_url}/crawl.json?start_requests=true&spider_name=g1&region={region}"
    ).json()

    respTerra = requests.get(
        url=f"{scrapyrt_url}/crawl.json?start_requests=true&spider_name=terra&region={region}"
    ).json()

    # making a list that contains both responses merged in order
    items = filter(None, sum(itertools.zip_longest(
        respG1.get('items'), respTerra.get('items')), ()))

    # list containing all brazillian states, to be displayed in the options button
    regions = {"AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG",
               "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"}

    # passing both lists to template
    return render_template('index.html', news=items, regions=regions)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
