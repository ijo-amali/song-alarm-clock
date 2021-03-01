from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    return 'POST request, not GET'


@app.route('/', methods=['POST'])
def result():
    url = request.form['url']
    print(url)
    return 'Hello world! Url sent was %s' % url
