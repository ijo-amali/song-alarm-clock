from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
def get():
    f = open("youtube-IDs.txt")
    return f.read()


@app.route('/', methods=['POST'])
@cross_domain("http://song-clock.glitch.me")
def result():
    url = request.form["url"]

    # print(request)
    # print(request.form)
    # print(request.form["url"])

    f = open("youtube-IDs.txt", "a")
    f.write("\n%s" % url)
    f.close()

    return 'Request received! Url sent was %s' % url
