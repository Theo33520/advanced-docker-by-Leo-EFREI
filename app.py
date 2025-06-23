from os import getenv
from flask import Flask, jsonify

app = Flask(__name__)

LISTEN_PORT = getenv("LISTEN_PORT", 8000)

@app.route("/")
def hello_world():
    return jsonify(message="Good, World!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=LISTEN_PORT, debug=True)