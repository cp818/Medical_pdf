# Medical Report Analyzer

This web application allows doctors to upload medical reports in PDF format, extract text from the reports, and analyze the text using OpenAI's GPT-4 model. The app provides insightful reports and potential diagnoses based on the analyzed text.

## Features

- Upload PDF medical reports
- Extract text from PDF files
- Analyze extracted text using OpenAI's GPT-4 model
- Display analysis report and potential diagnosis

## Requirements

- Python 3.7 or higher
- Streamlit
- OpenAI
- PyPDF2
- python-dotenv

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/medical-report-analyzer.git
    cd medical-report-analyzer
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required libraries:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the project directory and add your OpenAI API key:**

    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```

## Running the Application

1. **Run the Streamlit app:**

    ```sh
    streamlit run app.py
    ```

2. **Access the app in your web browser:**

    Open the provided local URL (typically `http://localhost:8501`) in your web browser to access the app.

## Usage

1. **Upload a PDF file:**

    Use the file uploader to select and upload a PDF file containing the medical report.

2. **View extracted text:**

    The app will extract text from the uploaded PDF and display it.

3. **Analyze the text:**

    The app will analyze the extracted text using OpenAI's GPT-4 model and display the analysis report and potential diagnosis.

## License

This project is licensed under the MIT License.

# My website : meshalalsultan.com
# Linkedin : www.linkedin.com/in/meshalhandal