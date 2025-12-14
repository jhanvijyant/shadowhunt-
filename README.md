# 🛡️ ShadowHunt+

ShadowHunt+ is a beginner-friendly **phishing website detection tool** built using **Python and Flask**. It analyzes a given URL and its webpage content to determine whether the site is **Safe, Suspicious, or Phishing**.

This project is designed to demonstrate **real-world cybersecurity concepts** in a simple and understandable way, making it ideal for students, beginners, and hackathon demos.

🚀 Features

* 🔍 URL structure analysis (length, IP usage, special characters, HTTPS check)
* 🌐 Live webpage content inspection
* 🔐 Detects password fields and phishing keywords
* 📊 Risk scoring mechanism
* 🎯 Clear classification: Safe / Suspicious / Phishing
* 🖥️ Clean cyber-themed web interface
* ⚡ Lightweight and easy to run

---

## 🧠 How It Works

1. User enters a website URL
2. The system analyzes:

   * URL characteristics
   * Webpage content using HTTP requests
3. A risk score is calculated
4. The website is classified based on the score

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS (Cyber-themed UI)
* **Libraries:**

  * requests
  * BeautifulSoup
  * urllib
  * re

---

## 📂 Project Structure

```
ShadowHunt/
│
├── app.py
│
└── templates/
    └── index.html
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ShadowHunt+.git
cd ShadowHunt+
```

### 2️⃣ Install Dependencies

```bash
pip install flask requests beautifulsoup4
```

### 3️⃣ Run the Application

```bash
python app.py
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🧪 Basic Testing

The application includes basic test cases to validate:

* URL analysis logic
* Final decision classification

Tests run automatically when the app starts.

---

## 🎯 Use Cases

* Cybersecurity learning projects
* College mini projects
* Hackathon demos
* Understanding phishing detection techniques

---

## 📌 Future Enhancements

* Machine Learning based phishing detection
* URL reputation APIs integration
* Scan history dashboard
* Browser extension version
* Real-time phishing alerts

---

## 👩‍💻 Author

**Jhanvi**
Second-year student | Aspiring Cybersecurity Engineer


