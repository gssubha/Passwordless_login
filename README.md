 # 🔐 Passwordless OTP-Based Login System using Flask ✉️✨

Passwordless Login System is a Flask-based secure authentication tool that replaces traditional password fields with a more user-friendly One-Time Password (OTP) delivered via email. The system uses email verification and OTP expiration logic to ensure authentication is simple, efficient, and secure for basic applications like portals, forms, or dashboards.

---

## 💡 Key Features

- 🔑 No password required — login through a 6-digit OTP sent to your email
- ⏱️ OTP expiry logic with 60-second countdown
-🔄 Resend OTP button enabled after timer ends
- 🧠 Session handling with proper user tracking
- 📬 Gmail SMTP integration for reliable email delivery
- 🔐 Secure flash messaging and input validation
- 📊 OTP data storage using SQLite backend
- 🎨 Sleek front-end UI using HTML, CSS, JavaScript
- 📱 Mobile responsive and user-friendly interface

---

## 🛠️ Core Technologies Used
| Layer     | Tools & Libraries                           | Identifier |
| --------- | ------------------------------------------- | ----- |
| Backend   | Flask, Python                               | 🐍    |
| Frontend  | HTML, CSS, JavaScript                       | 🎨    |
| Database  | SQLite (`OTPRecord` model using SQLAlchemy) | 🗃️   |
| Email API | Gmail SMTP (with App Password)              | 📧    |
| Security  | Session cookies, OTP expiry, app passwords  | 🛡️   |

---

## 📁 File Structure & Components
| File / Folder              | Role & Description                                       | Identifier |
| -------------------------- | -------------------------------------------------------- | ----- |
| `app.py`                   | Main backend logic, routes, OTP generation, session mgmt | 🧠    |
| `templates/index.html`     | Email input form for initiating login                    | 📝    |
| `templates/otp.html`       | OTP verification page with countdown + resend logic      | 🔐    |
| `templates/dashboard.html` | Protected user area after login success                  | 📊    |
| `static/style.css`         | Design and responsive layout                             | 🎨    |
| `static/timer.js`          | Countdown timer + button enable logic                    | ⏲️    |
| `venv/`                    | Python virtual environment (recommended)                 | 🧪    |
| `README.md`                | Complete project documentation                           | 📘    |

---
## 🔄 Authentication Flow

User enters Email 

↓

Server generates OTP → Stores in DB with 60s expiry

↓

Email with OTP sent via Gmail SMTP

↓

User enters OTP on /verify page

↓

OTP validity checked  →  Session created

↓

User redirected to Dashboard or error shown

---

## ✅ Learning Outcomes

### By completing this project, you will learn:
- How to develop production-style web apps using Flask
- OTP generation and expiry management
- Connecting Flask with SQLite using SQLAlchemy
- How to send emails with Gmail SMTP + secure app passwords
- JavaScript-based timers and button state toggling
- Building fully responsive frontends with interactive feedback

---

## ⚙️ Setup & Execution
### Step 1: Clone the repository
```bash
git clone https://github.com/your-username/passwordless-login.git
cd passwordless-login
```
### Step 2: Create a virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```
### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```
### Step 4: Set up email credentials in app.py
```bash
EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"  # From Google App Passwords
```
### Step 5: Run the Flask app
```bash
python app.py
```

🧭 Open browser and visit: http://127.0.0.1:5000

---
## 📌 Important Note
### 🔐 This project uses Gmail’s SMTP server. To send emails:
- Enable 2-Step Verification on your Google account
- Generate a 16-digit App Password
- Use this app password in EMAIL_PASSWORD (not your normal password)

  ---
  
![Screenshot 2025-07-04 235549](https://github.com/user-attachments/assets/98fb74ac-fab2-4d86-993b-9a578d2c2ca0)

---
![Screenshot 2025-07-04 235624](https://github.com/user-attachments/assets/b3ff2ad9-419d-4192-982a-c8677a99a7b9)

---
![Screenshot 2025-07-04 235652](https://github.com/user-attachments/assets/201336ee-c3ef-45cf-9180-34ac84f304c8)

---
![Screenshot 2025-07-04 235639](https://github.com/user-attachments/assets/f34892bc-4434-4784-895d-c54ab885fa13)

---
![Screenshot 2025-07-04 235711](https://github.com/user-attachments/assets/459f9e1f-c2a2-42b7-9f84-4bba2dd672f5)

---

![Screenshot 2025-07-04 235748](https://github.com/user-attachments/assets/454cda41-b65c-45ff-b9d3-0b50c000c283)




