import streamlit as st
from summarizer import generate_summary

st.title("Text Summarizer")

input_text = st.text_area("Enter text to summarize")

if st.button("Summarize"):
    summary = generate_summary(input_text)
    st.subheader("Summary:")
    st.write(summary)
