import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from heart.heart_model import train_heart_model

def heart_ui():
    model, scaler, X_test, y_test, train_acc, test_acc, heart_data = train_heart_model()

    st.title("💓 Heart Disease Prediction System")
    st.markdown("Use this app to predict the risk of **heart disease** and understand your **intensity level**.")

    try:
        img = Image.open("images/heart_img.jpg")
        st.image(img, caption="Healthy Heart Awareness", width=200)
    except:
        st.warning("Image not found in /images. Skipping image display.")

    st.subheader("📝 Enter Patient Information")

    age = st.number_input('Age (years)', min_value=1, max_value=120, value=45)
    sex = st.selectbox('Sex', options=[(1, 'Male'), (0, 'Female')], format_func=lambda x: x[1])[0]
    cp = st.selectbox('Chest Pain Type', options=[
        (0, 'Typical Angina'),
        (1, 'Atypical Angina'),
        (2, 'Non-anginal Pain'),
        (3, 'Asymptomatic')
    ], format_func=lambda x: x[1])[0]
    trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=80, max_value=200, value=130)
    chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=100, max_value=600, value=250)
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[(1, 'Yes'), (0, 'No')], format_func=lambda x: x[1])[0]
    restecg = st.selectbox('Resting ECG Results', options=[
        (0, 'Normal'),
        (1, 'ST-T wave abnormality'),
        (2, 'Left ventricular hypertrophy')
    ], format_func=lambda x: x[1])[0]
    thalach = st.number_input('Max Heart Rate Achieved', min_value=60, max_value=250, value=150)
    exang = st.selectbox('Exercise Induced Angina', options=[(1, 'Yes'), (0, 'No')], format_func=lambda x: x[1])[0]
    oldpeak = st.number_input('Oldpeak (ST depression)', min_value=0.0, max_value=10.0, step=0.1, value=1.0)
    slope = st.selectbox('Slope of ST Segment', options=[
        (0, 'Upsloping'),
        (1, 'Flat'),
        (2, 'Downsloping')
    ], format_func=lambda x: x[1])[0]
    ca = st.slider('Major Vessels Colored by Fluoroscopy', 0, 3, 0)
    thal = st.selectbox('Thalassemia', options=[
        (1, 'Normal'),
        (2, 'Fixed Defect'),
        (3, 'Reversible Defect')
    ], format_func=lambda x: x[1])[0]

    if st.button("🔍 Predict Heart Disease"):
        features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                              thalach, exang, oldpeak, slope, ca, thal]])
        features_scaled = scaler.transform(features)
        prob = model.predict_proba(features_scaled)[0][1]

        #  Risk classification with color and brief reason
        if prob <= 0.1:
            status = "✅ Low Risk (≤ 0.1)"
            color = "green"
            reason = "Your heart metrics are excellent."
        elif prob <= 0.3:
            status = "🟡 Borderline Risk (0.1 - 0.3)"
            color = "gold"
            reason = "Minor signs – maintain a healthy lifestyle."
        elif prob <= 0.6:
            status = "🟠 Moderate Risk (0.3 - 0.6)"
            color = "orange"
            reason = "Some risk factors are present."
        else:
            status = "🔴 High Risk (> 0.6)"
            color = "red"
            reason = "Strong indicators of heart disease."

        # Show results
        st.markdown(f"<h3 style='color:{color}'>{status}</h3>", unsafe_allow_html=True)
        st.info(reason)
        st.write(f"**Predicted Risk Score:** `{prob:.2f}`")

        st.subheader("📉 Risk Probability")
        st.progress(prob)

        # Compare to dataset
        st.subheader("📊 Your Features vs Dataset Average")
        user_df = pd.DataFrame(features, columns=heart_data.columns[:-1])
        avg_df = heart_data.drop("target", axis=1).mean().to_frame().T
        compare_df = pd.concat([user_df, avg_df])
        compare_df.index = ["You", "Average"]

        fig, ax = plt.subplots(figsize=(10, 4))
        sns.barplot(data=compare_df.T)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # Model Performance
    st.subheader("📈 Model Performance")
    st.write(f"**Training Accuracy:** `{train_acc:.2f}`")
    st.write(f"**Test Accuracy:** `{test_acc:.2f}`")

    # Confusion Matrix
    st.subheader("📌 Confusion Matrix")
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["No Disease", "Disease"])
    disp.plot(ax=ax, colorbar=False)
    st.pyplot(fig)

    # Dataset Sample
    st.subheader("🧾 Sample of Dataset")
    st.dataframe(heart_data.head())
