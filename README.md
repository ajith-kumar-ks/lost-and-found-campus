# 🎒 Lost & Found Campus

A web-based **Lost and Found Management System** built using **Flask** that helps students report lost/found items, search for items, submit claims, and communicate with the person who reported an item.

The project is designed to make the process of recovering lost belongings within a college campus easier and more organized.

---

## 🚀 Features

### 👤 User Authentication

* User registration
* User login/logout
* Password hashing
* Session-based authentication
* Protected routes for logged-in users

### 📦 Lost & Found Items

* Report a lost item
* Report a found item
* View lost items
* View found items
* View item details
* Track reported items

### 🔎 Search & Filtering

Users can search/filter found items based on:

* Item name
* Category
* Location

### 📩 Claim System

* Students can submit a claim for a found item
* Claimant can provide details to prove ownership
* Item reporter can review the claim
* Reporter can **accept or reject** a claim
* Users can view their submitted claims

### 💬 User Interaction

* A person who lost an item can approach the person who found it
* A person who found an item can contact the person who reported it as lost
* Designed to keep communication related to the item

---

## 🛠️ Tech Stack

### Backend

* **Python**
* **Flask**

### Frontend

* HTML
* CSS
* Jinja2 Templates
* JavaScript

### Database

* SQLite

### Development Tools

* Visual Studio Code
* Git
* GitHub
* Postman

---



---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/lost-and-found-campus.git
```

### 2. Navigate to the project

```bash
cd lost-and-found-campus
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python run.py
```

The application will be available at:

```text
http://127.0.0.1:5000/
```

---

## 🗄️ Database

The project currently uses **SQLite** through Flask-SQLAlchemy.

The main entities include:

### User

Stores registered user information such as:

* User ID
* Name
* Email
* Password

### Item

Stores information about reported items such as:

* Item ID
* Item name
* Category
* Location
* Description
* Status
* Reporter/User

### Claim

Stores information about claims submitted by users for found items.

---

## 🔄 Application Flow

```text
                    ┌───────────────┐
                    │     User      │
                    └───────┬───────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
        Report Lost                  Report Found
              │                           │
              ▼                           ▼
        Lost Item DB                 Found Item DB
              │                           │
              └─────────────┬─────────────┘
                            │
                            ▼
                    Search / Filter
                            │
                            ▼
                    Submit Claim
                            │
                            ▼
                    Item Reporter
                     /          \
                 Accept        Reject
                   │
                   ▼
              Communication
```

---

## 🔐 Authentication Flow

```text
Register
   ↓
User Account Created
   ↓
Login
   ↓
Flask-Login Session
   ↓
Access Protected Routes
```

Protected features require the user to be logged in.

---

## 🔎 Search Example

Users can filter found items using query parameters such as:

```text
/found-items?search=wallet
```

or:

```text
/found-items?category=Electronics
```

or:

```text
/found-items?location=Library
```

Multiple filters can also be combined.

---

## 🔌 REST API

The project also includes REST API concepts for interacting with the backend using JSON.

Example:

```text
POST /api/login
```

Request:

```json
{
    "email": "user@example.com",
    "password": "password"
}
```

The API approach can be extended later to support a separate frontend or mobile application.

---

## 🧪 Testing

API endpoints can be tested using **Postman**.

The application itself can be tested through the browser by:

1. Registering a new user
2. Logging in
3. Reporting a lost item
4. Reporting a found item
5. Searching/filtering items
6. Submitting a claim
7. Accepting/rejecting the claim
8. Testing user communication

---

## 🔮 Future Improvements

Some possible improvements for future versions:

* 📸 Upload images of lost/found items
* 🔔 Notifications for new claims
* 📧 Email notifications
* 💬 Real-time messaging
* 🔐 JWT authentication for APIs
* 🗃️ Migration from SQLite to MySQL/PostgreSQL
* 📱 Mobile-friendly UI
* 🤖 AI-based item matching
* 📍 Campus map/location integration
* 🧑‍💼 Admin dashboard
* 📊 Statistics and analytics
* 🚨 Automatic detection of duplicate reports

---

## 🎯 Project Objective

The main objective of this project is to provide a simple and centralized platform for students to **report, search, claim, and recover lost belongings within a college campus**.

Instead of relying on WhatsApp groups, notice boards, or word of mouth, students can use one platform to manage the entire lost-and-found process.

---

## 👨‍💻 Author

**Ajith Kumar K S**

B.Tech — Computer Science and Engineering
SJCE, Mysore

---

## 📜 License

This project is created for **educational and academic purposes**.
