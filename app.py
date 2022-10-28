# ---------- import libs ---------
from flask import Flask, request

# ----------- routes and applications --------
app = Flask(__name__)

# Root page
@app.route("/")
def hello_world():
    return "Python PL optimization!"

@app.route("/optimization", methods=["POST"])
def optimization():
    if request.method == "POST":
        return request.json