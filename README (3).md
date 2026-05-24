# 📄 Smart Resume Analyzer

An AI-powered Resume Analyzer built using **Streamlit**, **Python**, and **Ollama (Llama3)**.  
This project analyzes resumes, calculates ATS scores, matches resumes with job descriptions, detects skills, and provides AI-powered resume improvement suggestions.

---

# 🚀 Features

✅ Upload Resume in PDF format  
✅ Extract Resume Text Automatically  
✅ ATS Score Calculation  
✅ Skill Detection & Missing Skills Analysis  
✅ Job Description Matching  
✅ AI Resume Feedback  
✅ AI Resume Improvement using Ollama + Llama3  
✅ Download Resume Analysis Report  
✅ Modern Glassmorphism UI Design  
✅ Offline AI Support with Ollama

---

# 🛠️ Tech Stack

- Python
- Streamlit
- pdfplumber
- Pandas
- Requests
- Ollama
- Llama3

---

# 📂 Project Structure

```bash
resume-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
└── sample_resume.pdf
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

---

## 2️⃣ Create Virtual Environment (Optional)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Create a `requirements.txt` file and add:

```txt
streamlit
pdfplumber
pandas
requests
```

---

# 🤖 Install Ollama (For AI Features)

Download Ollama from:
https://ollama.com

## Pull Llama3 Model

```bash
ollama run llama3
```

---

# ▶️ Run the Project

```bash
streamlit run app.py
```

If Streamlit does not work:

```bash
python3 -m streamlit run app.py
```

---

# 📊 Functionalities

## 📄 Resume Upload
Users can upload resumes in PDF format.

## 🧠 Resume Text Extraction
Extracts text using pdfplumber.

## 📊 ATS Score
Calculates resume strength based on detected skills.

## 🎯 Job Match
Matches resume content with job descriptions.

## 🤖 AI Resume Assistant
Uses Ollama + Llama3 for:
- Resume feedback
- Career guidance
- Resume improvements

## 📥 Download Reports
Users can download:
- Resume analysis report
- Improved resume version

---

# 🎨 UI Features

- Glassmorphism Design
- Gradient Background
- Animated Progress Bars
- Responsive Layout
- Modern Dashboard Style

---

# 🔥 Future Improvements

- Resume Ranking System
- Multiple Resume Comparison
- AI Interview Questions
- Resume Templates
- LinkedIn Profile Analyzer
- Cloud Deployment
- Authentication System

---

# ☁️ Deployment Options

You can deploy this project on:

- Streamlit Cloud
- Render
- Railway
- Hugging Face Spaces

---

# 👨‍💻 Author

**Piyush Chauhan**

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you like this project:

⭐ Star the repository  
🍴 Fork the project  
📢 Share with others

---

# 🙌 Acknowledgements

- Streamlit
- Ollama
- Llama3
- Open Source Community
