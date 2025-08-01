from prometheus_client import Counter, generate_latest
from flask import Flask, Response

app = Flask(__name__)

# Define a simple metric
REQUEST_COUNT = Counter("request_count", "Number of requests received")

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Hello, DevOps World!"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001 , debug=False)

# Triggering GitHub Actions adsjhvcdcdsc🚀
# Triggering GitHub Actions adsjhvcdcdsc🚀
