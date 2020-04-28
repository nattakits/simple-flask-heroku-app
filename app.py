import flask
app = flask.Flask(__name__)
import time
import datetime
@app.route("/")
def index():
    time.sleep(10)
    return datetime.datetime.now()
