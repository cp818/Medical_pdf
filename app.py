import streamlit as st
from openai import OpenAI
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))




def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def analyze_text_with_openai(text):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that analyzes medical reports."},
        {"role": "user", "content": f"Analyze the following medical report text and provide insights and potential diagnosis:\n\n{text}"}
    ]
    response = client.chat.completions.create(model="gpt-4",
    messages=messages,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5)
    report = response.choices[0].message.content.strip()
    diagnosis = "Based on the report, a possible diagnosis might be required."  # Simplified example
    return report, diagnosis

st.title('Medical Report Analyzer')

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    #st.write("Extracting text from PDF...")

    text = extract_text_from_pdf(uploaded_file)
    #st.write("Text extracted:")
    #st.write(text)

    st.write("Analyzing text with OpenAI...")
    report, diagnosis = analyze_text_with_openai(text)

    st.header("Analysis Report")
    st.write(report)

    st.header("Potential Diagnosis")
    st.write(diagnosis)
