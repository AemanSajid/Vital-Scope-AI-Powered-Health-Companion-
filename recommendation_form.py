import streamlit as st
import json
import pandas as pd

@st.cache_data
def load_recommendation_data():
    """
    Loads health recommendation data from a JSON file.
    Uses st.cache_data to cache the data for better performance.
    Handles FileNotFoundError and JSONDecodeError.
    """
    try:
        with open("data/health_recommendations_detailed.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("Error: 'health_recommendations_detailed.json' not found. "
                 "Please ensure the data file is in a 'data' directory next to your script.")
        st.stop() 
    except json.JSONDecodeError:
        st.error("Error: Could not decode JSON from 'health_recommendations_detailed.json'. "
                 "Please check the file for syntax errors.")
        st.stop()

recommendation_data = load_recommendation_data()

def show_recommendation_form():

    st.markdown(
        """
        <style>
        .stButton > button {
            background-color: #4CAF50; /* Green */
            color: white;
            font-size: 16px;
            padding: 10px 24px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        .stSelectbox > div > div {
            border-radius: 8px;
        }
        .stCheckbox > label {
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }
        h1, h2, h3 {
            color: #2E86C1; /* A nice blue for headings */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("🌟 Your Personalized Health Companion")
    st.markdown(
        "Unlock **tailored Diet**, **Workout**, and **Medication** plans based on your health profile."
    )

    # Input selectors for Disease and Risk Level
    col1, col2 = st.columns(2)

    with col1:
        disease = st.selectbox(
            "🩺 **Select Your Primary Health Condition:**",
            list(recommendation_data.keys()),
            help="Choose the main health condition you are interested in receiving guidance for."
        )

    with col2:
        risk_level_options = ["Healthy", "Borderline", "Moderate", "High"]
        # Set default risk level intelligently based on presence in data
        default_risk_index = 0
        if disease in recommendation_data:
            available_risk_levels = list(recommendation_data[disease].keys())
            for level in ["High", "Moderate", "Borderline", "Healthy"]:
                if level in available_risk_levels and level in risk_level_options:
                    default_risk_index = risk_level_options.index(level)
                    break

        risk_level = st.selectbox(
            "⚠️ **Indicate Your Current Risk Level:**",
            risk_level_options,
            index=default_risk_index,
            help="Your current risk assessment for the selected condition. This helps tailor the intensity of recommendations."
        )

    # Form for preference selection and submission button
    with st.form("recommendation_form", clear_on_submit=False):
        st.markdown("---")
        st.markdown("### 📋 **What kind of plan are you looking for?**")
        col_choices = st.columns(3)
        with col_choices[0]:
            wants_diet = st.checkbox("🍽️ **Diet Plan**", value=True)
        with col_choices[1]:
            wants_workout = st.checkbox("🏋️ **Workout Plan**", value=True)
        with col_choices[2]:
            wants_medicine = st.checkbox("💊 **Medication Guidance**", value=True)

        st.markdown("---")
        st.markdown("### 🚨 **Do you have any specific health considerations?**")
        allergy_options = ["None", "Lactose Intolerant", "Anaphylaxis", "Gluten Allergy"]
        allergy = st.selectbox(
            "🤧 **Select any known dietary allergies:**",
            allergy_options,
            help="This helps us tailor your diet plan to avoid allergens. Note: 'Gluten Allergy' data might be limited."
        )

        st.markdown("---")
        submitted = st.form_submit_button("🚀 **Generate My Personalized Plan**")

    if submitted:
        st.markdown("---")
        st.markdown(f"## ✨ Your Personalized Plan for **{disease} - {risk_level}**")
        st.info("💡 **Disclaimer:** The information provided here is for general informational purposes only and does not constitute medical advice. Always consult with a qualified healthcare professional before making any changes to your diet, exercise, or medication regimen.")

        # Retrieve relevant data based on user selections
        data = recommendation_data.get(disease, {}).get(risk_level, {})

        if not data:
            st.error(
                f"❌ We couldn't find specific recommendations for **{disease}** at a **{risk_level}** risk level. "
                "Please try another combination or ensure the data file is up-to-date for this selection."
            )
            return

        allergy_key_map = {
            "None": "default",
            "Lactose Intolerant": "lactose",
            "Anaphylaxis": "anaphylaxis",
            "Gluten Allergy": "gluten" 
        }
        diet_allergy_key = allergy_key_map.get(allergy, "default")

        if wants_diet:
            st.subheader("🍽️ Diet Plan")
            diet_data_for_level = data.get("Diet", {})
            diet_plan = diet_data_for_level.get(diet_allergy_key)

           
            if not diet_plan and diet_allergy_key != "default":
                diet_plan = diet_data_for_level.get("default")
                if diet_plan:
                    st.warning(
                        f"Note: A specific diet for **{allergy}** was not found for this condition and risk level. "
                        "Displaying the **default** diet plan instead. Always verify food items carefully with your doctor or dietitian."
                    )
                else:
                    st.info("No diet plan (default or allergy-specific) is available for your selections.")

            if diet_plan:
                df_diet = pd.DataFrame(diet_plan[1:], columns=diet_plan[0])
                st.table(df_diet)
            else:
                st.info("No diet plan is available for your selections.")
            st.markdown("---")



        if wants_workout:
            st.subheader("🏋️ Workout Plan")
            workout_plan = data.get("Workout", []) 

            if workout_plan:
                if isinstance(workout_plan, list) and workout_plan and isinstance(workout_plan[0], dict):
                  
                    st.dataframe(pd.DataFrame(workout_plan))
                elif isinstance(workout_plan, list):
                   
                    for i, item in enumerate(workout_plan):
                        st.markdown(f"- **{i+1}.** {item}")
                else:
                    
                    st.markdown(f"- {workout_plan}")
            else:
                st.info("No workout plan is available for your selections.")
            st.markdown("---")


      
        if wants_medicine:
            st.subheader("💊 Medication Guidance")
            meds_data = data.get("Medications", {})

            general_advice = meds_data.get("general", [])
            if general_advice:
                st.markdown("**General Advice:**")
                for item in general_advice:
                    st.markdown(f"- {item}")
                st.markdown("---")

            allergy_note = meds_data.get("allergy")
            if allergy_note:
                st.markdown("**⚠️ Allergy Precaution:**")
                st.markdown(f"- {allergy_note}")
                st.markdown("---")

            detailed_plan = meds_data.get("detailed_plan", [])
            if detailed_plan:
                st.markdown("**Detailed Weekly Medication Plan:**")
                for week_data in detailed_plan:
                    st.markdown(f"**🗓️ Week {week_data['Week']}:**")
                    for treatment_item in week_data["Treatment"]:
                        st.markdown(f"- {treatment_item}")
                    st.markdown("---") 
            else:
                st.info("No detailed weekly medication plan is available for your selections.")
            st.markdown("---")

if __name__ == "__main__":
    show_recommendation_form()