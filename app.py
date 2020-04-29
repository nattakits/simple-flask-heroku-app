import flask
app = flask.Flask(__name__)
@app.route("/")
from test import text
def index():
    
    return text()
