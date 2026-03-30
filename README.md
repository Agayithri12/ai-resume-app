# AI Resume Analyzer & Job Recommendation System

## 📌 Project Overview

The AI Resume Analyzer is a web-based application that analyzes a candidate's resume using Natural Language Processing (NLP).
It extracts important skills from the resume, calculates an ATS-style score, and recommends suitable job roles based on the detected skills.

This system helps automate the resume screening process and provides intelligent insights for both candidates and recruiters.

---

## 🚀 Features

* Upload resume in **PDF format**
* **Automatic skill extraction** using NLP
* **ATS resume scoring system**
* **Job recommendation engine**
* Simple **web interface for resume upload**
* Built using **Flask and Python**

---

## 🧠 Technologies Used

* **Python**
* **Flask** – Web framework
* **spaCy** – Natural Language Processing
* **pdfminer.six** – Resume text extraction
* **HTML** – Frontend interface

---

## 📁 Project Structure

ai_resume_app
│
├── backend
│   ├── app.py
│   ├── resume_parser.py
│   ├── scorer.py
│   ├── matcher.py
│   ├── templates
│   │   ├── index.html
│   │   └── result.html
│   ├── uploads
│   └── venv
│
└── README.md

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

git clone https://github.com/your-username/ai-resume-app.git

### 2️⃣ Navigate to project folder

cd ai_resume_app/backend

### 3️⃣ Create virtual environment

python -m venv venv

### 4️⃣ Activate virtual environment

Windows:
venv\Scripts\activate

### 5️⃣ Install dependencies

pip install flask spacy pdfminer.six

### 6️⃣ Download NLP model

python -m spacy download en_core_web_sm

### 7️⃣ Run the application

python app.py

---

## 🌐 Running the Website

Open your browser and visit:

http://127.0.0.1:5000

Upload a resume and view the analysis results.

---

## 📊 Output

The system will display:

* Extracted skills
* Resume ATS score
* Recommended job roles

---

## 🎯 Future Improvements

* Resume improvement suggestions
* AI chatbot career advisor
* Skill gap analysis
* Better UI design
* Integration with job portals

---

## 👩‍💻 Author

Gayithri
Artificial Intelligence Engineering Student
