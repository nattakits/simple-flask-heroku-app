import flask
app = flask.Flask(__name__)
import time
import datetime
@app.route("/")
def index():
    return datetime.datetime.now()
