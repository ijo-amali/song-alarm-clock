from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    f = open("youtube-IDs.txt")
    return f.read()


@app.route('/', methods=['POST'])
def result():
    url = request.form

    print(url)

    f = open("youtube-IDs.txt", "a")
    f.write("\n%s" % url)
    f.close()

    return 'Request received! Url sent was %s' % url
