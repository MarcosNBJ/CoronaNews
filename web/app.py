from flask import Flask, render_template
import requests
import itertools

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():

    respG1 = requests.get(
        url="http://localhost:9080/crawl.json?start_requests=true&spider_name=g1"
    ).json()

    respTerra = requests.get(
        url="http://localhost:9080/crawl.json?start_requests=true&spider_name=terra"
    ).json()

    items = filter(None, sum(itertools.zip_longest(
        respG1.get('items'), respTerra.get('items')), ()))

    return render_template('index.html', news=items)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
