import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from diabetes.diabetes_model import train_diabetes_model

def diabetes_ui():
    model, scaler, X_test, y_test, train_acc, test_acc, diabetes_df = train_diabetes_model()

    st.title("🩸Prediction System")
    st.markdown("This app predicts the risk of **diabetes** and gives insights into your health condition based on input medical parameters.")

    try:
        img = Image.open("images/img.jpeg")
        st.image(img, caption="Diabetes Awareness", width=200)
    except:
        st.warning("Image not found in /data. Skipping image display.")

    st.subheader("📝 Enter Patient Information")

    gender = st.selectbox("Gender", ["Male", "Female"])

    # Show Pregnancies slider only if Female
    if gender == "Female":
        preg = st.slider('Pregnancies', 0, 17, 3)
    else:
        preg = 0  # Automatically set to 0 for males

    glucose = st.slider('Glucose', 0, 199, 117)
    bp = st.slider('Blood Pressure', 0, 122, 72)
    skin = st.slider('Skin Thickness', 0, 99, 23)
    insulin = st.slider('Insulin', 0, 846, 30)
    bmi = st.slider('BMI', 0.0, 67.1, 32.0)
    dpf = st.slider('Diabetes Pedigree Function', 0.078, 2.42, 0.3725, 0.001)
    age = st.slider('Age', 21, 81, 29)

    if st.button("🔍 Predict Diabetes"):
        features = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
        features_scaled = scaler.transform(features)
        prob = model.predict_proba(features_scaled)[0][1]

        #  Risk Interpretation
        if prob < 0.3:
            risk_level = "Healthy"
            status = "✅ Healthy & Fit"
            color = "green"
            reason = "Your glucose, BMI, and age are within healthy ranges."
        elif prob < 0.5:
            risk_level = "Borderline"
            status = "⚠️ Borderline – Risk may develop"
            color = "yellow"
            reason = "Mild signs of imbalance; consider regular checkups."
        elif prob < 0.7:
            risk_level = "Moderate"
            status = "⚠️ Moderate Diabetes Risk"
            color = "orange"
            reason = "Indicators show moderate insulin resistance or glucose levels."
        else:
            risk_level = "High"
            status = "🚨 High Diabetes Risk"
            color = "red"
            reason = "Strong signs of diabetes detected: high glucose/BMI."

        #  Show result
        st.markdown(f"<h3 style='color:{color}'>{status}</h3>", unsafe_allow_html=True)
        st.info(reason)
        st.write(f"**Predicted Risk Score:** `{prob:.2f}`")
        st.subheader("📉 Risk Probability")
        st.progress(prob)

        #  Comparison
        st.subheader("📊 Your Features vs Dataset Average")
        user_df = pd.DataFrame(features, columns=diabetes_df.columns[:-1])
        avg_df = diabetes_df.drop("Outcome", axis=1).mean().to_frame().T
        compare_df = pd.concat([user_df, avg_df])
        compare_df.index = ["You", "Average"]

        fig, ax = plt.subplots(figsize=(10, 4))
        sns.barplot(data=compare_df.T)
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # Recommendation form
        if st.button("📩 Get Personalized Recommendations"):
            from recommendation_form import show_recommendation_form
            show_recommendation_form()

    #  Model Performance
    st.subheader("📈 Model Performance")
    st.write(f"**Training Accuracy:** `{train_acc:.2f}`")
    st.write(f"**Test Accuracy:** `{test_acc:.2f}`")

    #  Confusion Matrix
    st.subheader("📌 Confusion Matrix")
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["No Diabetes", "Diabetes"])
    disp.plot(ax=ax, colorbar=False)
    st.pyplot(fig)

    #  Sample Data
    st.subheader("🧾 Sample of Dataset")
    st.dataframe(diabetes_df.head())
