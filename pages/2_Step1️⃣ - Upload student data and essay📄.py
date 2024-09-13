import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
from backend import backend

st.markdown("### Upload Student Answer scripts in zip file containing images in folders")
uploaded_zip = st.file_uploader("Upload zip file",accept_multiple_files=True)

st.markdown("### Upload question paper with key in '.pdf' or '.docx' format")
ques_key = st.file_uploader("Upload reference pdf or docx file", type=["pdf", "docx"])

submit = st.button("Submit")
if submit:
    with st.spinner('Loading...'):
        backend.analysis(uploaded_zip, ques_key)
    st.success('Done!')
    switch_page("step2️⃣ - download and save results")