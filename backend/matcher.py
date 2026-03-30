jobs_db = {
    "Data Scientist": ["python", "machine learning"],
    "Backend Developer": ["java", "sql"],
    "Data Analyst": ["data analysis", "sql"]
}

def match_jobs(skills):
    matched_jobs = []

    for job, req_skills in jobs_db.items():
        if any(skill in skills for skill in req_skills):
            matched_jobs.append(job)

    return matched_jobs