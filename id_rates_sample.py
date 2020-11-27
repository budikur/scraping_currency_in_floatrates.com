import requests

url = 'http://www.floatrates.com/daily/idr.json'
jason_data = requests.get(url)

for i in jason_data.json().values():
    #print(i)
    print(i['code'])
    print(i['name'])
    print(i['date'])
    print(i['inverseRate'])
