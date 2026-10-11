import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/status")
def status():
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
