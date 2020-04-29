import flask
app = flask.Flask(__name__)
import time
@app.route("/")
def index():
    
    time.sleep(60)
    return 'test time'
