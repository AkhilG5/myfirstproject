from flask import Flask, jsonify, request, render_template, redirect, url_for
from database import get_db_connection
from logger_config import get_logger

app = Flask(__name__)
log=get_logger("main_app_logger")

@app.route("/")
def home():
    log.info("inside / route")
    return render_template("index.html",error=None)


# ...existing code...

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")

        if not name or not password:
            return "Username and Password required", 400

        try:
            conn = get_db_connection()
            if conn is None:
                return render_template("index.html", error="Database connection failed")
            
            cur = conn.cursor()
            query = """
            SELECT * FROM users_details
            WHERE username=%s AND password=%s
            """
            cur.execute(query, (name, password))
            user = cur.fetchone()
            
            if user:
                return render_template("homepage.html", name=name)
            else:
                return render_template("index.html", error="Invalid username or password")
        except Exception as e:
            log.error(f"Error in login: {e}")
            return render_template("index.html", error="An error occurred")
        finally:
                cur.close()
                conn.close()

    return render_template("index.html", error=None)



    

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/register', methods=['GET','POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        mobile = request.form['mobile_no']
        email = request.form['email']
        profile = request.form['profile']

        if password != confirm_password:
            return "Passwords do not match"

        try:
            conn = get_db_connection()
            cur = conn.cursor()

            cur.execute(
                """
                INSERT INTO user_details (username,password,mobile_no,email,profile)
                VALUES (%s,%s,%s,%s,%s)
                """,
                (username, password, mobile, email, profile)
            )

            conn.commit()

            log.info(f"User {username} registered successfully")

            return redirect(url_for('login'))

        except Exception as e:
            log.error(f"Registration error: {e}")
            return "Registration failed", 500

        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()

    return render_template("register.html")

@app.route('/forgot-password', methods=['GET','POST'])
def forgot_password():
    return render_template("forgot_password.html")

if __name__ == "__main__":
    app.run(debug=True)