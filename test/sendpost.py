import requests

r = requests.get("http://localhost:8080")

print(r.text)

r = requests.post("http://localhost:8080", data={'url': "kzVVVNT4ic4"})

print(r.text)  # displays the result body.
