import flask
app = flask.Flask(__name__)

@app.route("/")
def index():
    k=5
    u=k+12
    return(u)
