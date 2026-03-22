import streamlit as st
import pdfplumber
import pandas as pd

# =========================
# 🎨 UI DESIGN
# =========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b, #0f172a);
    color: white;
}
h1 {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    background: linear-gradient(90deg, #00DBDE, #FC00FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
</style>
""", unsafe_allow_html=True)

st.title("📄 Smart Resume Analyzer")
st.markdown("### 🚀 Upload your resume and get instant insights")

# =========================
# 📥 INPUTS
# =========================
file = st.file_uploader("Upload Resume (PDF)")
job_desc = st.text_area("Paste Job Description")

# =========================
# 🧠 FUNCTIONS
# =========================
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.lower()

skills_list = ["python", "java", "c++", "machine learning", "sql", "react"]

# =========================
# 🚀 MAIN LOGIC
# =========================
if file:
    text = extract_text(file)

    st.subheader("📄 Extracted Text")
    st.write(text[:500])

    # Skills
    found_skills = [s for s in skills_list if s in text]
    missing_skills = [s for s in skills_list if s not in text]
    score = min(len(found_skills) * 15, 100)

    # Suggestions
    st.subheader("💡 Suggestions")
    if missing_skills:
        st.warning("Add these skills:")
        st.write(", ".join(missing_skills))
    else:
        st.success("Strong resume!")

    # =========================
    # 📊 SCORE
    # =========================
    st.subheader("📊 ATS Score")
    st.progress(score)
    st.write(f"{score}/100")

    # =========================
    # 📊 JOB MATCH
    # =========================
    if job_desc:
        job_words = job_desc.lower().split()
        match_count = sum(1 for w in job_words if w in text)
        match_percent = int((match_count / len(job_words)) * 100)

        st.subheader("🎯 Job Match")
        st.progress(match_percent)
        st.write(f"{match_percent}% match")

    # =========================
    # 📊 CHART
    # =========================
    data = pd.DataFrame({
        "Type": ["Found", "Missing"],
        "Count": [len(found_skills), len(missing_skills)]
    })
    st.bar_chart(data.set_index("Type"))

    # =========================
    # 📋 SKILL DISPLAY
    # =========================
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Found Skills")
        for s in found_skills:
            st.success(s)

    with col2:
        st.subheader("❌ Missing Skills")
        for s in missing_skills:
            st.error(s)

    # =========================
    # 📄 DOWNLOAD REPORT
    # =========================
    report = f"""
RESUME ANALYSIS REPORT

Skills Found:
{", ".join(found_skills)}

Missing Skills:
{", ".join(missing_skills)}

Score: {score}/100
"""
    st.download_button("📄 Download Report", report)

# =========================
# ⚠️ AI NOTICE
# =========================
st.subheader("🤖 AI Assistant")

st.info("⚠️ AI features are disabled on cloud. Works only locally with Ollama.")
