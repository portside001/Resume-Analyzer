import streamlit as st
from pdf_reader import extract_text
from analyzer import analyze_resume

st.set_page_config(
    page_title="SACHIN RAJPUT RESUME ANALYZER APP",
    page_icon=":bar_chart:",
    layout="wide",
)

st.title("Resume Analyzer App")
st.write("Upload your resume in PDF format to analyze it.")

# Keep results across reruns (e.g. when the download button is clicked)
if "resume_text" not in st.session_state:
    st.session_state.resume_text = None
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

uploaded_file = st.file_uploader("Upload Resume", type="pdf")

# Reset stored state if a new/different file is uploaded
if uploaded_file is not None and st.session_state.get("last_uploaded_name") != uploaded_file.name:
    st.session_state.resume_text = None
    st.session_state.analysis_result = None
    st.session_state.last_uploaded_name = uploaded_file.name

if uploaded_file:
    if st.session_state.resume_text is None:
        with st.spinner("Extracting text from the resume..."):
            try:
                st.session_state.resume_text = extract_text(uploaded_file)
            except Exception as e:
                st.error(f"Failed to extract text from PDF: {e}")
                st.stop()

    st.success("Resume Profile Read Successfully!")

    with st.expander("Preview extracted resume text"):
        st.text(st.session_state.resume_text)

    if st.button("Analyze Resume", type="primary"):
        with st.spinner("Analyzing resume..."):
            try:
                st.session_state.analysis_result = analyze_resume(
                    st.session_state.resume_text
                )
            except Exception as e:
                st.error(f"Failed to analyze resume: {e}")
                st.session_state.analysis_result = None

    # Show result if we have one (persists across the rerun triggered by download_button)
    if st.session_state.analysis_result:
        st.markdown("### Analysis Result")
        st.markdown(st.session_state.analysis_result)  # markdown renders nicer than st.text

        st.download_button(
            "Download Analysis Result",
            data=st.session_state.analysis_result,
            file_name="analysis_result.txt",
            mime="text/plain",
        )
else:
    # Uploader was cleared -> clear stale state
    st.session_state.resume_text = None
    st.session_state.analysis_result = None