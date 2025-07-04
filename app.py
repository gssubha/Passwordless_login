from flask import Flask, render_template, request, redirect, session, flash
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import smtplib, random, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Change this in production

# Configure server-side session
app.config["SESSION_TYPE"] = "filesystem"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///otp.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Session(app)
db=SQLAlchemy(app)

# Replace with your real Gmail and app password
EMAIL_ADDRESS = "misamizami1125@gmail.com"
EMAIL_PASSWORD = "lpddcidqlsioypuh"

class OTPRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    otp = db.Column(db.String(6), nullable=False)
    expiry_time = db.Column(db.DateTime, nullable=False)

# Send OTP to user's email
def send_otp(email, otp):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = email
    msg["Subject"] = "Your OTP Code"
    body = f"Your OTP is: {otp}"
    msg.attach(MIMEText(body, "plain"))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, email, msg.as_string())

# Home page - email input
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]
        otp = str(random.randint(100000, 999999))
        expiry_time = datetime.now() + timedelta(seconds=60)

        # Save to DB
        otp_record = OTPRecord(email=email, otp=otp, expiry_time=expiry_time)
        db.session.add(otp_record)
        db.session.commit()

        # Save email only in session
        session["email"] = email

        send_otp(email, otp)
        return redirect("/verify")

    return render_template("index.html")

# OTP verification page
@app.route("/verify", methods=["GET", "POST"])
def verify():
    email = session.get("email")
    record = OTPRecord.query.filter_by(email=email).order_by(OTPRecord.id.desc()).first()

    if request.method == "POST":
        entered_otp = request.form["otp"]

        if not record:
            flash("No OTP found for this email.", "danger")
            return redirect("/verify")

        if datetime.now() > record.expiry_time:
            flash("OTP expired. Please try again.", "danger")
            return redirect("/")

        if entered_otp == record.otp:
            session["logged_in"] = True
            flash("Login successful!", "success")
            return redirect("/dashboard")
        else:
            flash("Invalid OTP.", "danger")
            return redirect("/verify")

    # ✅ Pass expiry time to template as timestamp
    expiry_timestamp = int(record.expiry_time.timestamp()) if record else 0
    return render_template("otp.html", expiry_timestamp=expiry_timestamp, otp=record.otp if record else None)


from datetime import datetime, timedelta
@app.route("/resend", methods=["POST"])
def resend():
    email = session.get("email")
    if not email:
        flash("Session expired. Start over.", "danger")
        return redirect("/")

    otp = str(random.randint(100000, 999999))
    expiry_time = datetime.now() + timedelta(seconds=60)

    # Before generating OTP, check last one
    last_otp = OTPRecord.query.filter_by(email=email).order_by(OTPRecord.id.desc()).first()
    if last_otp and datetime.now() < last_otp.expiry_time - timedelta(minutes=4):
        flash("Please wait before resending OTP.", "warning")
        return redirect("/verify")

    # Save new OTP
    otp_record = OTPRecord(email=email, otp=otp, expiry_time=expiry_time)
    db.session.add(otp_record)
    db.session.commit()

    send_otp(email, otp)
    flash("New OTP sent!", "success")
    return redirect("/verify")

# Dashboard after successful login
from datetime import datetime, timedelta

@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect("/")
    
    sample_data = {
        "email": session.get("email"),
        "otp": session.get("otp"),
        "login_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "recent_logins": [
            {"device": "Chrome - Windows", "time": "2025-07-03 21:15"},
            {"device": "Edge - Android", "time": "2025-07-02 09:40"},
            {"device": "Safari - iPhone", "time": "2025-06-30 18:05"}
        ]
    }
    return render_template("dashboard.html", data=sample_data)

# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

