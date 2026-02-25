def generate_resume_feedback(resume_text):

    feedback = []

    if "project" not in resume_text.lower():
        feedback.append("Add more projects to improve resume strength.")

    if "python" not in resume_text.lower():
        feedback.append("Add Python skills if you know them.")

    if "github" not in resume_text.lower():
        feedback.append("Add GitHub portfolio links.")

    return feedback if feedback else ["Resume looks good 👍"]