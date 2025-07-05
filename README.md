🔐 PASSWORDLESS OTP-BASED LOGIN SYSTEM USING FLASK

This project is a secure and efficient passwordless authentication system built using Python Flask, which replaces traditional password logins with a more user-friendly email-based OTP (One-Time Password) approach. The application enables users to authenticate themselves by simply entering their email address, receiving a six-digit OTP via email, and verifying it within a set time limit. This ensures a streamlined login process while maintaining a good level of security for basic use cases.

💡 KEY FEATURES

🔑 Passwordless Authentication using email-based OTP

⏳ OTP Expiry System (default: 60 seconds)

🔄 Resend OTP option after cooldown period

🧠 Session Management to track authenticated users

❌ OTP Expiration Handling and validation

📬 Email Integration using Gmail SMTP server

🧱 SQLite Database to store OTP entries and expiration

🎨 Responsive Frontend UI with professional HTML, CSS, JS


🛠️ TECH STACK USED

Frontend: HTML, CSS, JavaScript

Backend: Python with Flask

Database: SQLite

Email Service: Gmail SMTP (with App Password)


🔄 AUTHENTICATION FLOW (How It Works)

User lands on the homepage and enters their email address.

The server generates a secure OTP and sends it to the provided email using Gmail's SMTP server.

The OTP is stored in the SQLite database with a timestamp set to expire after 60 seconds.

The user is redirected to a verification page where they can enter the OTP.

The server checks the entered OTP against the most recent one sent. If the OTP is valid and within the expiration time, the user is successfully logged in.

If the OTP is incorrect or expired, appropriate flash messages inform the user.

A Resend OTP button is shown after the 60-second timer completes, allowing the user to request a new code if needed.


📁 PROJECT STRUCTURE

passwordless_login

│

├── app.py                      # Main Flask application logic

├── templates/                # Jinja2 templates for frontend rendering

│   ├── index.html            # Email input form

│   ├── otp.html              # OTP verification form

│   └── dashboard.html        # Protected user dashboard

├── static/                   # CSS and JavaScript files

│   ├── style.css             # Frontend styling

│   └── timer.js              # JS logic for countdown and resend button

├── venv/                     # Virtual environment (optional but recommended)

└── README.md                 # Project documentation


⚙️ INSTALLATION AND SETUP

To run this project locally, follow these steps:

CLONE THE REPOSITORY

git clone https://github.com/your-username/passwordless-login.git
cd passwordless-login

CREATE A VIRTUAL ENVIRONMENT

python -m venv venv
venv\Scripts\activate    # On Windows

INSTALL REQUIRED PACKAGES

pip install -r requirements.txt

SETUP YOUR GMAIL CREDENTIALS

In app.py, replace the placeholder values:

EMAIL_ADDRESS = "your-email@gmail.com"

EMAIL_PASSWORD = "your-16-digit-app-password"

👉 You must enable App Passwords in your Google account. Follow the official instructions to generate one.

RUN THE FLASK APP

python app.py

Visit in your browser

http://127.0.0.1:5000


📸 EXAMPLE USE CASES

A user enters example@gmail.com and submits.

An email arrives with: Your OTP is 348921.

They input the OTP within 60 seconds.

On success, they are redirected to a Dashboard.

If time exceeds, OTP becomes invalid and must be resent.


✅ LLEARNING OUTCOMES

By building this project, you'll gain hands-on experience with:

Real-world Flask application development

Integrating Python with external APIs (SMTP)

OTP generation, validation, and expiration handling

Secure session tracking

Clean, interactive frontend design

SQLite database usage in Flask


![Screenshot 2025-07-04 235549](https://github.com/user-attachments/assets/98fb74ac-fab2-4d86-993b-9a578d2c2ca0)

![Screenshot 2025-07-04 235624](https://github.com/user-attachments/assets/b3ff2ad9-419d-4192-982a-c8677a99a7b9)

![Screenshot 2025-07-04 235652](https://github.com/user-attachments/assets/201336ee-c3ef-45cf-9180-34ac84f304c8)

![Screenshot 2025-07-04 235639](https://github.com/user-attachments/assets/f34892bc-4434-4784-895d-c54ab885fa13)

![Screenshot 2025-07-04 235711](https://github.com/user-attachments/assets/459f9e1f-c2a2-42b7-9f84-4bba2dd672f5)

![WhatsApp Image 2025-07-05 at 15 41 00_5f354572](https://github.com/user-attachments/assets/4f5af179-6a58-48a6-9350-a9610a6200b3)



