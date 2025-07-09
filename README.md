# Vital-Scope-AI-Powered-Health-Companion-
A Python-based web app for predicting heart disease and diabetes, featuring a custom chatbot for interactive user support. Built with Streamlit, Flask, and scikit-learn.
PROJECT DESCRIPTION:
HOW TO RUN: 
1.	By requirements.txt:
Run: pip install -r requirements.txt

OR install all separately if that does not work.
2.	By individual REQUREMENTS:
1.	Web frameworks
streamlit
flask
flask-cors
RUN: 
pip install streamlit
pip install flask
pip install flask-cors

2.	Chatbot logic
fuzzywuzzy
python-Levenshtein  
RUN: 
pip install fuzzywuzzy
pip install python-Levenshtein  # optional but speeds up fuzzywuzzy

3.	ML
scikit-learn
pandas
numpy
joblib
RUN:
pip install scikit-learn
pip install pandas
pip install numpy
pip install joblib

4.	Using image files
Pillow
RUN:
pip install Pillow

AFTER INSTALLING ALL DEPENDENCIES, RUN BOTH FLASK CHATBOT BACKEND AND STREAMLIT FRONTEND:
In split terminal 1, first run: python chatbot.py 
shows: Running on http://127.0.0.1:5000
In split terminal 2, second run: streamlit run app.py
shows: Local URL: http://localhost:8501
            Network URL: http://192.168.1.3:8501
My python version is: Python 3.12.7 (which is stable to run all pip and other necessary commands.)


