import streamlit as st
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR / "backend"))

from main import predict_spam


st.set_page_config(
    page_title="SMS Spam Detector",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
.stApp {
    background-color: #000000;
    color: #00FF00;
    font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
}

* {
    font-family: 'Consolas', 'Monaco', 'Courier New', monospace !important;
}

.st-emotion-cache-10trblm {
    color: #00FFFF;
    font-size: 2.5em;
    margin-bottom: 0.5em;
    text-transform: uppercase;
}

.stTextArea > div:first-child {
    border: 2px solid #00FF00 !important;
    border-radius: 0 !important;
}

.stTextArea textarea {
    background-color: #000000;
    color: #00FF00;
    border: none;
    padding-left: 20px;
    border-radius: 0 !important;
}

.stTextArea textarea:focus {
    outline: none !important;
    border-color: #00FF00 !important;
    box-shadow: none !important; 
}

.stButton>button {
    background-color: #000000;
    color: #00FF00;
    border: 2px solid #00FF00;
    border-radius: 0;
    text-transform: uppercase;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #00FF00;
    color: #000000;
    box-shadow: none;
}

.stTextArea textarea::placeholder {
    color: #00FF00 !important;
    opacity: 0.5;
}

</style>
""", unsafe_allow_html=True)


st.title("SMS SPAM DETECTOR")

st.markdown("### >> ENTER MESSAGE:")

input_sms = st.text_area(
    label="Enter message",
    label_visibility="hidden",
    height=150,
    placeholder="INPUT HERE..."
)

if st.button("[PREDICT]"):
    st.markdown("---")
    
    if input_sms.strip() == "":
        st.markdown('<p style="color:#FFFF00;">>> ERROR: INPUT FIELD EMPTY. PLEASE ENTER DATA.</p>', unsafe_allow_html=True)
    else:
        with st.spinner('>> [ANALYZING MESSAGE... STAND BY]'):
            import time
            time.sleep(0.5)
            
            result, prob_spam = predict_spam(input_sms) 
            percent_spam = f"{prob_spam * 100:.2f}%"
            percent_ham = f"{(1 - prob_spam) * 100:.2f}%"
            

            if result == 1:
                st.markdown('<p style="color:#FF0000;">>> SPAM DETECTED | PROBABILITY: ' + percent_spam + ' SPAM / ' + percent_ham + ' Regular Message</p>', unsafe_allow_html=True)
            else:
                st.markdown('<p style="color:#00FF00;">>> NOT SPAM | PROBABILITY: ' + percent_spam + ' SPAM / ' + percent_ham + ' Regular Message</p>', unsafe_allow_html=True)


st.markdown("---")
st.markdown(
    '<p style="color:#008000; font-size: 0.8em; text-align: center;">Ishrak Saleh Chowdhury, 232-134-034</p>',
    unsafe_allow_html=True
)