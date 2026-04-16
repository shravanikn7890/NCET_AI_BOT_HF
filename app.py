import streamlit as st
from transformers import pipeline

st.title("Text Summarizer")

# Load model
summarizer = pipeline("summarization")

# Input text
long_text = st.text_area("Enter text to summarize")

# Sliders
max_length = st.slider("Max Summary Length", min_value=50, max_value=300, value=130)
min_length = st.slider("Min Summary Length", min_value=20, max_value=100, value=30)

# Button
if st.button("Summarize"):
    if long_text:
        summary = summarizer(
            long_text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text!")
