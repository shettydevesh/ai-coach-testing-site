import streamlit as st
import requests as r
from claude import claude_answer
from gpt import gpt_answer
import time
from sheets import update_feedback

# Set page configuration
st.set_page_config(page_title="AI Coach A/B Testing", page_icon=":robot_face:", layout="wide", menu_items={
    'About': "This is the website to test the different outputs between the Claude Haiku Model and GPT 3.5 Turbo Model. "
})

# Set custom CSS styles
css = """
    <style>
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #4c4c4c;
        }
        .input-container {
            margin-bottom: 20px;
        }
        .output-container {
            display: flex;
            justify-content: space-between;
        }
        .output-card {
            width: 48%;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

def main():
    # Main content
    with st.container():
        st.title("AI Coach A/B Testing")
        with st.form("query_form"):
            q = st.text_input("Enter your query:")
            submit_button = st.form_submit_button(label="Submit")

        if submit_button and q:
            # Show the loader
            with st.spinner('Getting answers from AI models...'):
                canwser = claude_answer(q)
                ganswer = gpt_answer(q)

            # Hide the loader when answers are ready
            st.success('Answers fetched!')

            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Output From Claude:")
                    st.write(canwser)
                with col2:
                    st.subheader("Output From GPT:")
                    st.write(ganswer)

def feedback_page():
    st.title("Feedback")
    name = st.text_input("Please enter your name:")
    feedback = st.text_area("Please leave your feedback:")
    if st.button("Submit Feedback"):
        if feedback and name:
            with st.spinner('Uploading your feedback.....'):
                update_feedback(name, feedback)
            st.success(f"Thank you for your feedback")
        else:
            st.warning("Please enter some feedback or your name before submitting.")

# Add a sidebar menu
pages = {
    "AI Coach": main,
    "Feedback": feedback_page
}

selected_page = st.sidebar.selectbox("Select a page", list(pages.keys()))
pages[selected_page]()