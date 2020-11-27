import requests
import bs4
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/detik-populer')
def detik_populer():
    url = 'https://www.detik.com/terpopuler?tag_from=framebar'
    content = requests.get(url)
    # print(content.text)
    html = bs4.BeautifulSoup(content.text, "html.parser")
    # print(html)
    populer_area = html.find(attrs={'class': 'grid-row list-content'})
    titles = populer_area.find_all(attrs={'class': 'media__title'})
    images = populer_area.find_all(attrs={'class': 'media__image'})
    return render_template('detik-scraper.html',images=images)

@app.route('/idr-rates')
def idr_rates():
    source = requests.get('http://www.floatrates.com/daily/idr.json')
    json_data = source.json()
    return render_template('idr-rates.html', datas=json_data.values())

if __name__ == '__main__':
    app.run(debug=True)