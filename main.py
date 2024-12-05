import os
from datetime import datetime
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def return_basic():
    now = datetime.now()
    return '<h1>Welcome to Cloud Functions and Cloud Build demo by Simform</h1><br/>' + str(now)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))  # Default to port 8080
    app.run(host="0.0.0.0", port=port)
