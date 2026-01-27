import fitz  # PyMuPDF
from groq import Groq
import os



pdf = fitz.open("Resume final.pdf")
resume_text = ""

for page in pdf:
    resume_text += page.get_text()

with open("resume_text.txt", "w", encoding="utf-8") as file:
    file.write(resume_text)

print(" Resume text saved to resume_text.txt")



pdf_new = fitz.open()
page = pdf_new.new_page()


page.insert_textbox(
    fitz.Rect(50, 50, 550, 800),   # proper page layout
    resume_text,
    fontsize=11
)

pdf_new.save("output.pdf")
pdf_new.close()

print("Full resume PDF created: output.pdf")



client = Groq(api_key=os.getenv("API_key"))

def LLmCall(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content



job_description = """
We are hiring a Python Developer.

Required Skills:
Python, SQL, Machine Learning, Git, REST APIs,
problem-solving ability, good communication skills.
"""



prompt = f"""
You are a professional resume and ATS expert.

Resume Text:
{resume_text}

Job Description:
{job_description}

Tasks:
1. Identify skills already present in the resume
2. Suggest missing skills to add
3. Categorize them into:
   - Technical Skills


   - Soft Skills

Return concise bullet points only.
"""

result = LLmCall(prompt)

print("\n AI Skill Suggestions:\n")
print(result)
