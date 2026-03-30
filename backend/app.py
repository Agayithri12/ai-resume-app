from flask import Flask, request, render_template
from pdfminer.high_level import extract_text
import os
import spacy

app = Flask(__name__)

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Folder for uploaded resumes
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Example skills database
skills_db = ["python", "java", "sql", "machine", "learning", "data", "analysis"]

# Example job database
jobs_db = {
    "Data Scientist": ["python", "machine", "learning"],
    "Backend Developer": ["java", "sql"],
    "Data Analyst": ["data", "analysis", "sql"]
}


# Function to extract skills
def extract_skills(text):
    doc = nlp(text.lower())
    found_skills = []

    for token in doc:
        if token.text in skills_db:
            found_skills.append(token.text)

    return list(set(found_skills))


# Function to calculate score
def calculate_score(skills):
    score = len(skills) * 20
    return min(score, 100)


# Function to match jobs
def match_jobs(skills):
    matched_jobs = []

    for job, required in jobs_db.items():
        if any(skill in skills for skill in required):
            matched_jobs.append(job)

    return matched_jobs


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Resume analysis
@app.route("/analyze_resume", methods=["POST"])
def analyze_resume():

    file = request.files["resume"]

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Extract text from PDF
    text = extract_text(filepath)

    # Analyze
    skills = extract_skills(text)
    score = calculate_score(skills)
    jobs = match_jobs(skills)

    return render_template(
        "result.html",
        skills=skills,
        score=score,
        jobs=jobs
    )


if __name__ == "__main__":
    app.run(debug=True)