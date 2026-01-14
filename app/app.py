from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def health():
    return jsonify({
        "service": "Telco Network Function",
        "status": "UP"
    })

@app.route("/route/<dest>")
def route(dest):
    return jsonify({
        "action": "FORWARDED",
        "destination": dest
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
