# 📄 Resume-Analyzer

Resume-Analyzer is a privacy-first, local AI-powered application built using **Streamlit** and **Ollama**. It allows users to upload PDF resumes to instantly extract key insights, match candidates against job descriptions, and get optimization suggestions—all completely offline.

## ✨ Features

- 🔒 **100% Private:** Powered by local LLMs via Ollama. Your data never leaves your machine.
- 📄 **PDF Support:** Seamlessly upload and parse PDF resumes.
- 💼 **Job Description Matching:** Compare resumes against specific job roles to calculate a match score.
- 💡 **Smart Insights:** Tailored feedback on how to improve the resume for ATS (Applicant Tracking Systems).

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **LLM Engine:** Ollama
- **Language:** Python

---

## 🚀 Getting Started

### Prerequisites

1. Install **Python 3.9+**
2. Install **Ollama**
3. Pull your preferred model:

```bash
ollama pull llama3
```

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/portside001/Resume-Analyzer.git
cd Resume-Analyzer
```

### 2. Create a virtual environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### Step 3: Launch the Streamlit app

```bash
streamlit run app.py
``
