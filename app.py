from flask import Flask, request
from optimization import optimize


# EB looks for an 'application' callable by default.
application = Flask(__name__)

# Root page
@application.route("/")
def hello_world():
    return "It works!"

# Optimization endpoint
@application.route("/optimization", methods=["POST"])
def optimization():
    if request.method == "POST":
        return optimize(request.json["items"], request.json["maxVolume"])

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()