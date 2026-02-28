from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Akhil Good Morning"

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({
        "received": data
    }), 200

if __name__ == "__main__":
    app.run(debug=True)