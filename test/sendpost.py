import requests

URL = 'http://10.0.0.185:8080'

r = requests.get(URL)

print(r.text)

r = requests.post(URL, data={'url': "kzVVVNT4ic4"})

print(r.text)  # displays the result body.
