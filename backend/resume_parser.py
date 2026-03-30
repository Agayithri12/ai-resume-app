import spacy

nlp = spacy.load("en_core_web_sm")

# predefined skills (can expand later)
skills_db = ["python", "java", "sql", "machine learning", "data analysis"]

def extract_skills(text):
    doc = nlp(text.lower())
    found_skills = []

    for token in doc:
        if token.text in skills_db:
            found_skills.append(token.text)

    return list(set(found_skills))