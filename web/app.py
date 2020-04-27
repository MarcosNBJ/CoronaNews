from flask import Flask, render_template
import requests
import itertools
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', defaults={'region': ''})
@app.route('/<string:region>', methods=['GET'])
def index(region):

    respG1 = requests.get(
        url=f"http://localhost:9080/crawl.json?start_requests=true&spider_name=g1&region={region}"
    ).json()

    respTerra = requests.get(
        url=f"http://localhost:9080/crawl.json?start_requests=true&spider_name=terra&region={region}"
    ).json()

    items = filter(None, sum(itertools.zip_longest(
        respG1.get('items'), respTerra.get('items')), ()))

    regions = {"AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG",
               "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"}

    return render_template('index.html', news=items, regions=regions)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
