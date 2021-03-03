from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'song-clock.glitch.me')

id_file = "youtube-IDs.txt"


@app.route('/', methods=['GET'])
def get():
    try:
        f = open(id_file)
        response = f.read()
        f.close()
        return response
    except:
        open(id_file, "x")
        return ''


@app.route('/', methods=['POST'])
def result():
    url = request.form["url"]

    print(url)

    f = open(id_file, "a")
    f.write("%s\n" % url)
    f.close()

    return 'Request received! Url sent was %s' % url
