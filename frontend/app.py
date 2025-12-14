import streamlit as st
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR / "backend"))

from main import predict_spam

st.set_page_config(page_title="SMS Spam Detector")

st.title("SMS Spam Detector")

input_sms = st.text_area("Enter message")

if st.button("Predict"):
    if input_sms.strip() == "":
        st.warning("Please enter a message.")
    else:
        result = predict_spam(input_sms)

        if result == 1:
            st.error("Spam")
        else:
            st.success("Not Spam")
