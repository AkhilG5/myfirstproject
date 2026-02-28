from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/echo", methods=["POST"])
def echo():
    name = request.form.get("name")

    if not name:
        return jsonify({"error": "Name is required"}), 400

    return jsonify({
        "message": f"Successfully done, {name}!"
    }), 200

if __name__ == "__main__":
    app.run(debug=True)