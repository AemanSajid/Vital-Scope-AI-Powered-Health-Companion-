import streamlit as st
import streamlit.components.v1 as components 
from chat_ui import load_chatbot_ui

from heart.heart_ui import heart_ui
from diabetes.diabetes_ui import diabetes_ui
from recommendation_form import show_recommendation_form

st.markdown("""
<style>
    /* General App Background */
    .stApp {
        background-color: #D3D3D3;
        color: #000000;
    }

    /* Sidebar */
    .stSidebar {
        background-color: #E8E8E8 !important;
        color: #000000 !important;
    }

    .stSidebar .stRadio div[role="radiogroup"] label {
        color: #000000 !important;
    }

    .stSidebar .stRadio div[role="radiogroup"] label.st-dg {
        background-color: #00FFFF !important;
        color: #000000 !important;
        border-radius: 5px;
    }

    .stSidebar .stButton>button {
        background-color: #00FFFF !important;
        color: #000000 !important;
        border-radius: 5px !important;
    }

    .stSidebar .stButton>button:hover {
        background-color: #90EE90 !important;
        color: #000000 !important;
    }

    .stSidebar h2 {
        color: #008B8B !important;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6,
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #008B8B;
    }

    h4 {
        color: #008B8B !important;
    }

    /* Paragraphs and Text */
    p, .stMarkdown p, .stMarkdown span {
        color: #000000;
    }

    b, .stMarkdown b {
        color: #00AAAA;
    }

    /* Horizontal Rules */
    hr {
        border-top: 1px solid #90EE90;
    }

    .stMarkdown hr {
        border-top: 1px solid #C0C0C0;
    }

    /* Success Message */
    .stAlert.success {
        background-color: #F0F0F0 !important;
        color: #006400 !important;
        border-left: 8px solid #00FFFF !important;
    }

    .stAlert.success a {
        color: #006400 !important;
    }

    /* Chatbot Button */
    .chat-button {
        background-color: #00FFFF;
        color: #000000;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    .chat-popup {
        background-color: #FFFFFF;
        border: 1px solid #00FFFF;
    }

    .chat-popup-header {
        background-color: #00FFFF;
        color: #000000;
    }

    .chat-popup-body {
        color: #000000;
    }

    .chat-popup-body div b {
        color: #008B8B;
    }

    .chat-popup-input {
        background-color: #F0F0F0;
        border-top: 1px solid #00FFFF;
    }

    .chat-popup-input input {
        background-color: #FFFFFF;
        color: #000000;
        border: 1px solid #999999;
    }

    .chat-popup-input input::placeholder {
        color: #777777;
    }

    .chat-popup-input button {
        background-color: #00FFFF;
        color: #000000;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="VITAL SCOPE - Health Companion", layout="wide")
if 'sidebar_open' not in st.session_state:
    st.session_state.sidebar_open = False
if 'selection' not in st.session_state:
    st.session_state.selection = "Home"


with st.sidebar:

    if st.button("☰ Menu"):
        st.session_state.sidebar_open = not st.session_state.sidebar_open

    if st.session_state.sidebar_open:
        st.image("images/image (5).png", width=180) 
        st.markdown("---")
        st.session_state.selection = st.radio("Choose a Section:",
                                             ["Home",
                                              "Heart Disease",
                                              "Diabetes",
                                              "Recommendations",
                                              "Developers"],
                                             key="main_navigation")
        st.markdown("---")

selection = st.session_state.selection

if selection == "Home":
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("images/image (5).png", width=750)
    with col2:
        st.markdown("""
            <h1 style="color:#00AAAA;font-family:sans-serif;margin-bottom:0;">VITAL SCOPE</h1>
<h4 style="color:#008B8B;margin-top:5px;">Your AI-Powered Health Companion</h4>

        """, unsafe_allow_html=True)
    st.markdown("""<hr style="border:1px solid #00AAAA;">""", unsafe_allow_html=True)

    st.markdown("""
        <h2 style="color:#00AAAA;">Welcome to VITAL SCOPE</h2>

        Your digital companion for early disease detection and a healthier life.
        With advanced AI models and personalized suggestions, Vital Scope helps <b style="color:#D90429;">patients</b>, <b style="color:#D90429;">fitness enthusiasts</b>, and even <b style="color:#D90429;">healthy individuals</b> take control of their wellness.

        <hr style="border:1px solid #00AAAA;">
        <h3 style="color:#00AAAA;">Heart Disease Risk</h3>
    """, unsafe_allow_html=True)
    heart_col1, heart_col2, heart_col3 = st.columns([1, 2, 1])
    with heart_col2:
        st.image("images/heart_icon.png", width=450)
    st.markdown("""
        <p style="text-align: center; color:black; font-size:16px;">
        Heart disease is a broad term for conditions that affect your heart's structure and function.
        It often involves narrowed or blocked blood vessels that can lead to chest pain (angina), heart attack, or stroke.
        Understanding your risk factors and symptoms is crucial for early detection and prevention.
        </p>
        """, unsafe_allow_html=True)


    st.markdown("""
        <hr style="border:1px solid black;">
        <h3 style="color:#00AAAA;">Diabetes Screening</h3>
    """, unsafe_allow_html=True)
    diabetes_col1, diabetes_col2, diabetes_col3 = st.columns([1, 2, 1])
    with diabetes_col2:
        st.image("images/image (3).png", width=300)
    st.markdown("""
        <p style="text-align: center; color:black; font-size:16px;">
        Diabetes is a chronic condition characterized by high blood sugar levels.
        It occurs when your body either doesn't produce enough insulin or can't effectively use the insulin it produces.
        Unmanaged diabetes can lead to serious complications affecting the heart, kidneys, eyes, and nerves.
        </p>
        """, unsafe_allow_html=True)

    st.markdown("""
        <hr style="border:1px solid #black;">
        <h3 style="color:#00AAAA;">Workout & Gym Plan for a Stronger Heart</h3>
        <p style="color:black;">Boost your cardiovascular fitness with daily, easy-to-follow workouts.</p>

        <p style="color:black;">- Light walking (10–15 minutes daily)<br>
        - Low-impact cardio like cycling or swimming<br>
        - Strength training with resistance bands or body weight<br>
        - Guided breathing and stretching routines</p>

        <p style="color:black;">Regular movement reduces the risk of hypertension, obesity, and chronic heart problems.</p>
    """, unsafe_allow_html=True)
    st.image("images/image (4).png", caption="Healthy Heart, Active Life", width=600)

    st.markdown("""
        <hr style="border:1px solid #2A2A2A;">
        <h3 style="color:#00AAAA;">Eat Smart: Healthy Eating Tips</h3>
        <p style="color:black;">What you eat fuels your heart and body.</p>

        <p style="color:black;">A balanced and nutritious diet is fundamental for overall health and disease prevention. By focusing on whole, unprocessed foods, you can significantly reduce your risk of chronic conditions like heart disease and diabetes. Healthy eating provides essential nutrients, helps maintain a healthy weight, improves energy levels, and supports optimal bodily functions. It's about nourishing your body to thrive.</p>
    """, unsafe_allow_html=True)
    st.image("images/image (6).png", caption="Eat Clean, Live Better", width=600)

    st.success("Ready to explore? Use the menu button to access our disease predictors or view your health recommendations!")

    st.markdown("""<hr style="border:1px solid #00AAAA;">""", unsafe_allow_html=True)
    st.markdown("""
<h2 style="color:#00AAAA;">App Features</h2>

<p style="color:black;">VITAL SCOPE offers a suite of powerful tools designed to empower your health journey:</p>

<ul style="color:black; font-size:16px;">
    <li><b style="color:#00AAAA;">Heart Disease Prediction:</b> Utilize advanced AI models to assess your risk of heart disease based on various health parameters.</li>
    <li><b style="color:#00AAAA;">Diabetes Risk Detection:</b> Get insights into your likelihood of developing diabetes through intelligent analysis of your input.</li>
    <li><b style="color:#00AAAA;">AI Health Recommendations:</b> Receive personalized diet, workout, and medication guidance tailored to your specific health condition and risk level.</li>
    <li><b style="color:#00AAAA;">Smart Chatbot Support:</b> Get instant answers to your health-related questions with our intelligent chatbot, providing quick and reliable information.</li>
    <li><b style="color:#00AAAA;">User-Friendly Interface:</b> Navigate through a clean, intuitive, and accessible design, making health management simple for everyone.</li>
</ul>
""", unsafe_allow_html=True)

    st.markdown("""<hr style="border:1px solid #00AAAA;">""", unsafe_allow_html=True)


elif selection == "Heart Disease":
    st.markdown('<h1 style="color:#00AAAA;">Heart Disease Prediction</h1>', unsafe_allow_html=True)
    heart_ui()

elif selection == "Diabetes":
    st.markdown('<h1 style="color:#00AAAA;">Diabetes Risk Detection</h1>', unsafe_allow_html=True)
    diabetes_ui()

elif selection == "Recommendations":
    st.markdown('<h1 style="color:#00AAAA;">AI Health Recommendations</h1>', unsafe_allow_html=True)
    show_recommendation_form()

elif selection == "Developers":
    st.markdown('<h1 style="color:black;">Meet the Developers</h1>', unsafe_allow_html=True)
    st.markdown("""
    <p style="color:blue;">We are a dedicated team of students passionate about leveraging Artificial Intelligence for impactful health solutions. This project is the culmination of our efforts to create a user-friendly and intelligent health companion.</p>

    <h3 style="color:#D90429;">Team Members:</h3>

    <p style="color:black;">- <b style="color:#FFD700;">Aeman Sajid (FA22-BSE-084)</b><br>
        <span style="margin-left: 15px;"><b>Role:</b> Project Lead & Core AI Model Development (Heart Disease Prediction)</span><br>
        <span style="margin-left: 15px;"><b>Contributions:</b> Responsible for overall project architecture, integration of machine learning models for heart disease prediction, and ensuring seamless data flow across modules.</span></p>

    <p style="color:black;">- <b style="color:#FFD700;">Anosha Ali (FA22-BSE-075)</b><br>
        <span style="margin-left: 15px;"><b>Role:</b> Diabetes Model Development & User Interface Design</span><br>
        <span style="margin-left: 15px;"><b>Contributions:</b> Focused on developing and optimizing the AI model for diabetes risk detection, and played a key role in designing the intuitive and visually appealing user interface for the application.</span></p>

    <p style="color:black;">- <b style="color:#FFD700;">Anza Gulzar (FA22-BSE-076)</b><br>
        <span style="margin-left: 15px;"><b>Role:</b> AI Health Recommendations & Chatbot Integration</span><br>
        <span style="margin-left: 15px;"><b>Contributions:</b> Developed the logic for personalized health recommendations (diet, workout, medication plans) and integrated the smart chatbot functionality to provide instant Q&A support.</span></p>

    <h3 style="color:black;">Instructor:</h3>
    <p style="color:black;">We extend our sincere gratitude to <b style="color:#FFD700;">Sir Abdul Rafay Hannan</b> for his invaluable guidance, unwavering support, and profound insights throughout the development of this project. His expertise was instrumental in shaping our understanding and execution.</p>

    <h3 style="color:black;">Tools & Technologies Used:</h3>
    <p style="color:black;">
    - <b style="color:black;">Programming Language:</b> Python<br>
    - <b style="color:black;">Web Framework:</b> Streamlit (for interactive web application development)<br>
    - <b style="color:black;">Machine Learning Libraries:</b> scikit-learn (for building predictive models), pandas (for data manipulation and analysis), numpy (for numerical operations)<br>
    - <b style="color:black;">Datasets:</b>
        <span style="margin-left: 15px;">- `heart.csv` (from Kaggle - for Heart Disease Prediction Model)</span><br>
        <span style="margin-left: 15px;">- `diabetes.csv` (from Kaggle - for Diabetes Risk Detection Model)</span><br>
    - <b style="color:black;">Data Storage:</b> JSON files (`health_recommendations_detailed.json`, `health_qa.json` for recommendations and Q&A knowledge base)<br>
    - <b style="color:black;">Image Assets:</b> Stored in the `images/` directory (`image (5).png`, `heart_icon.png`, `image (3).png`, `image (4).png`, `image (6).png`, etc.)<br>
    - <b style="color:black;">Prediction Models:</b> Implemented using various machine learning algorithms (e.g., Logistic Regression, Support Vector Machines, Random Forest Classifiers) for classification tasks.<br>
    - <b style="color:black;">Chatbot Integration:</b> Custom HTML, CSS, and JavaScript for the floating chatbot UI, interacting with a backend (Flask/FastAPI, though not explicitly shown in this `app.py`) to process queries.
    </p>
    <p style="color:black;">📚 <b style="color:black;">Project:</b> Final Semester Project – 2025</p>
    """, unsafe_allow_html=True)
load_chatbot_ui()
0