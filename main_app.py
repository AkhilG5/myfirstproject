from flask import Flask, jsonify, request, render_template
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="myfirstdb",
    user="postgres",
    password="root",
    port=5432
)

@app.route("/")
def home():
    return render_template("index.html",error=None)


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/login", methods=["POST"])
def login():

    name = request.form.get("username")
    password = request.form.get("password")

    if not name or not password:
        return "Username and Password required", 400

    cur = conn.cursor()

    query = """
    SELECT * FROM users_login
    WHERE username=%s AND password=%s
    """

    cur.execute(query, (name, password))
    user = cur.fetchone()
    cur.close()

    if user:
        return render_template("homepage.html", name=name)
    else:
        return render_template("index.html",error = "Invalid username or password")

    

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)