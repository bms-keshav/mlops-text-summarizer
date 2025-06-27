import os
import pandas as pd
import streamlit as st
from summarizer import generate_summary
from textblob import TextBlob
import datetime

# --- Page Config ---
st.set_page_config(page_title="Smart Summarizer", layout="wide")

# --- Background Styling ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0d0d0d;
        background-image: url("https://www.transparenttextures.com/patterns/stardust.png");
        background-size: cover;
        color: #e0e0e0;
    }
    textarea, .stTextInput > div > input {
        background-color: #1e1e1e !important;
        color: #f2f2f2 !important;
        border: 1px solid #444 !important;
        border-radius: 10px !important;
    }
    .summary-box {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(255,255,255,0.05);
        font-size: 16px;
        color: #f2f2f2;
    }
    .centered {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 20px;
        color: #cce6ff;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<div class='centered'>🧠 Smart Text Summarizer</div>", unsafe_allow_html=True)

# --- Input Area ---
st.markdown("### Enter your text below:")

# Initialize session state if not already done
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# Text area for input
input_text = st.text_area("📝 Input Text:", value=st.session_state.input_text, height=200, key="input_text")

# --- Spell Check ---
def get_misspelled_words(text):
    blob = TextBlob(text)
    return [word for word in blob.words if word.lower() != str(TextBlob(word).correct()).lower()]

if input_text.strip():
    word_count = len(input_text.split())
    char_count = len(input_text)
    st.info(f"📊 Word Count: {word_count} | 🧾 Character Count: {char_count}")

    misspelled = get_misspelled_words(input_text)
    if misspelled:
        st.warning(f"🔍 {len(misspelled)} likely misspelled words: {', '.join(misspelled[:5])}")
    else:
        st.success("✅ No spelling issues detected!")

# --- Summary Output ---
if st.button("🚀 Generate Summary"):
    with st.spinner("Generating summary..."):
        summary = generate_summary(input_text)
        st.success("✅ Done!")
        st.markdown("### 🔎 Summary Output:")
        st.markdown(f"<div class='summary-box'>{summary}</div>", unsafe_allow_html=True)

        filename = f"summary_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        st.download_button("⬇ Download Summary", data=summary, file_name=filename, mime="text/plain")

# --- Footer ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>Built with ❤️ using <a href='https://huggingface.co/t5-small'>T5</a>, "
    "<a href='https://streamlit.io'>Streamlit</a>, and <a href='https://textblob.readthedocs.io/'>TextBlob</a>.</p>",
    unsafe_allow_html=True
)
