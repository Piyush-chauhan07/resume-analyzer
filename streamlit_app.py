import streamlit as st
import pdfplumber
import pandas as pd
import requests

st.markdown("""
<style>

/* 🌌 Background Gradient */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b, #0f172a);
    color: white;
}

/* 🧊 Glass Cards */
div[data-testid="stContainer"] {
    background: rgba(255, 255, 255, 0.05);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 30px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

/* ✨ Title Glow */
h1 {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    background: linear-gradient(90deg, #00DBDE, #FC00FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* 🎯 Buttons */
button {
    border-radius: 12px !important;
    background: linear-gradient(45deg, #00c6ff, #0072ff) !important;
    color: white !important;
    font-weight: bold !important;
}

/* 📥 Upload box */
section[data-testid="stFileUploader"] {
    border: 2px dashed #00c6ff;
    padding: 20px;
    border-radius: 15px;
}

/* 📊 Progress bar */
div[data-testid="stProgress"] > div > div {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
}

</style>
""", unsafe_allow_html=True)
st.title("📄 Smart Resume Analyzer")
st.markdown("---")
st.markdown("### 🚀 Upload your resume and get instant AI insights")

# Upload file
file = st.file_uploader("Upload Resume (PDF)")

# Job description
job_desc = st.text_area("Paste Job Description")

# Extract text function
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.lower()

# Skills list
skills_list = ["python", "java", "c++", "machine learning", "sql", "react"]

# MAIN LOGIC
if file:
    with st.spinner("Analyzing Resume..."):
        text = extract_text(file)

    st.subheader("📄 Extracted Text")
    st.write(text[:500])

    # Skills detection
        # Skills
    found_skills = [skill for skill in skills_list if skill in text]
    missing_skills = [skill for skill in skills_list if skill not in text]
    score = min(len(found_skills) * 15, 100)
    st.subheader("💡 Smart Suggestions")

    if missing_skills:
        st.warning("🚀 Add these skills to improve your resume:")
        st.write(", ".join(missing_skills))
    else:
        st.success("🔥 Your resume is strong!")
        st.subheader("🤖 AI Resume Feedback")

        if found_skills:
            st.success("Your resume shows strong technical skills.")

        if missing_skills:
            st.warning("Consider adding these skills:")
            st.write(", ".join(missing_skills))

        if len(found_skills) > len(missing_skills):
            st.success("✅ Your resume is well aligned with job roles.")
        else:
            st.error("⚠️ Your resume needs improvement for better job matching.")

        st.info("💡 Tip: Add projects, certifications, and measurable achievements to improve impact.")


# 📄 Download Report
        report = f"""
        RESUME ANALYSIS REPORT

        Skills Found:
        {", ".join(found_skills)}

        Missing Skills:
        {", ".join(missing_skills)}

        Score: {score}/100
        """

        st.download_button(
            label="📄 Download Report",
            data=report,
            file_name="resume_report.txt",
            mime="text/plain"
        )
    
        
    if job_desc and job_desc.strip() != "":
        job_words = job_desc.lower().split()

        match_count = sum(1 for word in job_words if word in text)
        match_percent = int((match_count / len(job_words)) * 100)

        st.subheader("🎯 Job Match %")
        st.progress(match_percent)
        st.write(f"{match_percent}% match with job description")
        import pandas as pd

    data = pd.DataFrame({
        "Type": ["Found Skills", "Missing Skills"],
        "Count": [len(found_skills), len(missing_skills)]
    })

    st.subheader("📊 Skill Analysis Chart")
    st.bar_chart(data.set_index("Type"))

    # Layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧠 Skills Found")
        for skill in found_skills:
            st.success(f"✔ {skill}")

    with col2:
        st.subheader("❌ Missing Skills")
        for skill in missing_skills:
            st.error(f"✘ {skill}")

    # Score
    score = min(len(found_skills) * 15, 100)

    st.subheader("📊 ATS Score")
    st.progress(score)
    
    # =========================
# 🤖 AI CHAT
# =========================
    # =========================
# 🤖 AI CHAT (OLLAMA)
# =========================

st.subheader("🤖 AI Resume Assistant (Offline)")

user_input = st.text_input("Ask anything about your resume:")

if user_input:
    with st.spinner("AI is thinking... 🤖"):
        try:
            prompt = f"""
            You are an expert resume analyzer and career coach.

            Resume:
            {text}

            Question:
            {user_input}
            """

            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3",
                    "prompt": prompt,
                    "stream": False
                }
            )

            result = response.json()
            reply = result["response"]

            st.markdown(f"""
            <div style="background:#1e293b;padding:15px;border-radius:10px">
            🤖 {reply}
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")
    

    colA, colB, colC = st.columns(3)
    colA.metric("Skills Found", len(found_skills))
    colB.metric("Missing", len(missing_skills))
    colC.metric("Score", f"{score}/100")
    st.subheader("✨ AI Resume Improver")

if st.button("🚀 Improve My Resume"):
    with st.spinner("Rewriting your resume..."):
        prompt = f"""
        Improve this resume professionally. Make it ATS-friendly,
        add strong action verbs, and better structure.

        Resume:
        {text}
        """

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()
        st.success(result["response"])
        st.subheader("🔍 Highlighted Skills")

        for skill in skills_list:
            if skill in text:
                st.markdown(f"✅ **{skill}** found")
        st.subheader("📊 Detailed Score")

        col1, col2, col3 = st.columns(3)

        col1.metric("Skills", len(found_skills)*10)
        col2.metric("Match", match_percent if job_desc else 0)
        col3.metric("Overall", score) 
        if "experience" in text:
            st.info("📄 Detected: Experienced Resume")
        else:
            st.info("🎓 Detected: Fresher Resume")
            improved_text = ""

            if st.button("🚀 Improve My Resume"):
                with st.spinner("Rewriting your resume..."):
                    prompt = f"""
                    Improve this resume professionally. Make it ATS-friendly.

                    Resume:
                    {text}
                    """

                    response = requests.post(
                        "http://localhost:11434/api/generate",
                        json={
                            "model": "llama3",
                            "prompt": prompt,
                            "stream": False
                        }
                    )

                    result = response.json()
                    improved_text = result["response"]

                    st.success(improved_text)

# DOWNLOAD BUTTON
            if improved_text:
                st.download_button(
                    label="📥 Download Improved Resume",
                    data=improved_text,
                    file_name="improved_resume.txt",
                    mime="text/plain"
                ) 
                report = f"""
                RESUME ANALYSIS REPORT

                Skills Found:
                {", ".join(found_skills)}

                Missing Skills:
                {", ".join(missing_skills)}

                Score: {score}/100

                Job Match: {match_percent if job_desc else "N/A"}%
                """

                st.download_button(
                    label="📄 Download Full Report",
                    data=report,
                    file_name="resume_report.txt",
                    mime="text/plain"
                ) 

                # =========================
                # ✨ AI RESUME IMPROVER
                # =========================

                st.subheader("✨ AI Resume Improver")

                improved_text = ""

                if st.button("🚀 Improve My Resume"):
                    with st.spinner("Rewriting your resume..."):
                        prompt = f"""
                        Improve this resume professionally. Make it ATS-friendly.

                        Resume:
                        {text}
                        """

                        response = requests.post(
                            "http://localhost:11434/api/generate",
                            json={
                                "model": "llama3",
                                "prompt": prompt,
                                "stream": False
                            }
                        )

                        result = response.json()
                        improved_text = result["response"]

                        st.success(improved_text)

                # ✅ DOWNLOAD IMPROVED RESUME
                if improved_text:
                    st.download_button(
                        label="📥 Download Improved Resume",
                        data=improved_text,
                        file_name="improved_resume.txt",
                        mime="text/plain"
                    )

                # =========================
                # 📄 DOWNLOAD REPORT
                # =========================

                st.subheader("📄 Download Report")

                job_match = match_percent if job_desc else 0

                report = f"""
                RESUME ANALYSIS REPORT

                Skills Found:
                {", ".join(found_skills)}

                Missing Skills:
                {", ".join(missing_skills)}

                Score: {score}/100

                Job Match: {job_match}%
                """

                st.download_button(
                    label="📄 Download Full Report",
                    data=report,
                    file_name="resume_report.txt",
                    mime="text/plain"
                )
