import requests

print('Testing~\n\n')

URL = 'http://10.0.0.185:8080'

r = requests.get(URL)

print("Get request: %s\n" % r.text)

r = requests.post(URL, data={"url": "kzVVVNT4ic4"})

print("Post request: %s\n" % r.text)
print(r)
