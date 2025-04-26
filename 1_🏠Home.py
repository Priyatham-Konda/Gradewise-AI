import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import backend
import streamlit_extras

# __import__('streamlit_extras')
# import sys

# sys.modules['streamlit_extras'] = sys.modules.pop('streamlit_extras')

st.set_page_config(
    page_title="Main Page",
    page_icon="👋",
)

# Custom CSS to increase font size and change font style
st.markdown("""
<style>
    .big-font {
        font-size: 300%;
        font-style: san-serif; /* Change font style here */
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='big-font'>Welcome to Gradewise.ai! 🤖</h1>", unsafe_allow_html=True)

st.markdown(
    """
    Traditional answer script evaluation poses significant challenges for educators, especially when dealing with a large volume of scripts. Teachers often face time constraints and delays in providing feedback, which can hinder students' learning and academic progress.

At Gradewise AI, we aim to streamline this process by leveraging artificial intelligence to evaluate student answer scripts efficiently and accurately. Here's how our platform works:

Bulk Answer Script Processing: Teachers can upload a zip file containing scanned PDFs of student answer scripts. This simplifies the submission process and ensures all scripts are organized in one place.

Automated Text Extraction: Our system extracts the text from each answer script, making it ready for analysis by our AI model. This eliminates the need for manual data entry and ensures accuracy.

AI-Powered Evaluation: Using advanced natural language processing, our AI model evaluates student answers against the provided question paper and the teacher's answer key. It assesses the correctness, relevance, and completeness of each response.

Personalized Feedback: Gradewise AI generates detailed feedback for each student, highlighting areas of improvement and strengths. This targeted guidance helps students enhance their understanding and performance.

#### Grading and Reporting
- The platform assigns grades based on predefined criteria or customizable rubrics. Teachers can review and track student progress through an intuitive dashboard, which provides insights into overall performance and trends.

With Gradewise AI, educators can save valuable time while ensuring accurate and consistent evaluation of student answer scripts. By automating the grading process and delivering personalized feedback, we empower teachers to focus on fostering learning and academic growth, ultimately driving better outcomes for students.
"""
)
st.markdown("## Lets get started!")
page_1 = st.button("Go to step 1 - Upload Student data")
if page_1:
    switch_page("step1️⃣ - Upload student data and essay📄")