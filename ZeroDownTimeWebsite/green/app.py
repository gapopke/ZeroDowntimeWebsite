from flask import Flask, jsonify
from datetime import datetime
import os

app = Flask(__name__)

DEPLOYMENT_COLOR = os.environ.get("DEPLOYMENT_COLOR", "unknown")
VERSION_NUMBER = os.environ.get("VERSION_NUMBER", "0.0.0")
DEPLOYED_AT = datetime.utcnow().isoformat() + "Z"

@app.route("/")
def info():
    return jsonify({
        "running_version": VERSION_NUMBER,
        "deployment_color": DEPLOYMENT_COLOR,
        "deployed_at": DEPLOYED_AT
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
