import requests

print('Testing~\n')

url = 'http://10.0.0.185:8080'

r = requests.get(url)

print("Get request: %s\n" % r.text)

r = requests.post(url, data={"url": "kzVVVNT4ic4"})

print("Post request: %s\n" % r.text)
print(r)
