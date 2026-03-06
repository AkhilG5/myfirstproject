from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from sqlalchemy import text
from database import get_db_connection
from logger_config import get_logger

app = Flask(__name__)
app.secret_key = "7065f4b97bec0a6fd86af4a393b9d241a7d457393ac81e37bcf2365fd46bd8bf"  # Required for session management
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

        db_session = get_db_connection()
        if db_session is None:
            return render_template("index.html", error="Database connection failed")
        
        try:
            query = text("""
            SELECT * FROM user_details
            WHERE username=:username AND password=:password
            """)
            result = db_session.execute(query, {"username": name, "password": password})
            user = result.fetchone()
            
            if user:
                log.info(f"User {name} logged in successfully")
                session["username"] = name  # Store username in Flask session
                return render_template("homepage.html", name=name) 
            else:
                return render_template("index.html", error="Invalid username or password")
        except Exception as e:
            log.error(f"Error in login: {e}")
            return render_template("index.html", error="An error occurred")
        finally:
            db_session.close()

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

        db_session = get_db_connection()
        if db_session is None:
            return "Database connection failed", 500
        
        try:
            db_session.execute(
                text("""
                INSERT INTO user_details (username,password,mobile_no,email,profile)
                VALUES (:username,:password,:mobile,:email,:profile)
                """),
                {
                    "username": username,
                    "password": password,
                    "mobile": mobile,
                    "email": email,
                    "profile": profile
                }
            )

            db_session.commit()

            log.info(f"User {username} registered successfully")

            return redirect(url_for('login'))

        except Exception as e:
            log.error(f"Registration error: {e}")
            db_session.rollback()
            return "Registration failed", 500

        finally:
            db_session.close()

    return render_template("register.html")

@app.route('/forgot-password', methods=['GET','POST'])
def forgot_password():
    return render_template("forgot_password.html")


@app.route("/logout")
def logout():
    username = session.get("username")

    if username:
        log.info(f"User '{username}' logged out successfully")

    session.clear()

    return render_template("index.html",error=None)


if __name__ == "__main__":
    app.run(debug=True)