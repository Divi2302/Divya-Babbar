# AI-Powered Resume Optimizer & ATS Matcher

An intelligent command-line tool that parses PDF resumes, compares them against a target job description, and uses LLMs to perform a deep ATS (Applicant Tracking System) compatibility check and skill gap analysis.

## 🚀 Features
- **PDF Resume Parsing:** Extracts clean text from PDF documents using `PyMuPDF`.
- **ATS Match & Gap Analysis:** Compares resume text with job requirements using the Groq API (`Llama-3.1-8b-instant`).
- **Detailed Skill Mapping:** Categorizes matched skills and suggests missing technical and soft skills.
- **ATS-Friendly Rebuilding:** Generates a clean, optimized copy of the resume text back to PDF format.

## 🛠️ Tech Stack
- **Language:** Python
- **LLM API:** Groq API (Llama 3.1)
- **PDF Handling:** PyMuPDF (`fitz`)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Divi2302/Divya-Babbar
   cd Divya-Babbar
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your API Key:**
   - On Windows (Command Prompt):
     ```cmd
     set API_key="your_groq_api_key_here"
     ```
   - On Linux/macOS:
     ```bash
     export API_key="your_groq_api_key_here"
     ```

4. **Run the script:**
   ```bash
   python resume_updater.py
   ```

## 📊 Sample Output
```text
Resume text saved to resume_text.txt
Full resume PDF created: output.pdf

AI Skill Suggestions:

* Technical Skills Matched: Python, Git
* Missing Technical Skills: SQL, REST APIs, Machine Learning
* Soft Skills Suggestion: Problem-solving ability, Communication skills
```
