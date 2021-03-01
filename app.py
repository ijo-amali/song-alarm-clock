from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS()


@app.route('/', methods=['GET'])
def get():
    f = open("youtube-IDs.txt")
    return f.read()


@app.route('/', methods=['POST'])
def result():
    url = request.form["url"]

    print(url)

    f = open("youtube-IDs.txt", "a")
    f.write("%s\n" % url)
    f.close()

    return 'Request received! Url sent was %s' % url
