import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Setting page configuration

st.set_page_config(
    page_title="AI Healthcare Diagnosis Assistant",
    page_icon="🏥",
    layout="wide"
)
# Setting Title and description 

st.title("🏥 AI Healthcare Diagnosis Assistant")

st.write("Welcome to the AI Healthcare Diagnosis Assistant!")

st.info("This project predicts possible diseases based on the symptoms selected by the user.")

# Loading the dataset

@st.cache_data
def load_data():
    return pd.read_excel("feature_dataset.xlsx")

df = load_data()

# Preparing the data

diseases = df["Disease"]

features = df.drop("Disease", axis=1)

# Cleaning the disease name
def clean_disease(name):

    name = name.split("^")[0]

    if "_" in name:
        name = name.split("_",1)[1]

    return name.title()

diseases = diseases.apply(clean_disease)

# Dashboard creation

col1, col2, col3 = st.columns(3)

col1.metric("Diseases", len(diseases))
col2.metric("Symptoms", len(features.columns))
col3.metric("Dataset Rows", len(df))

st.divider()

st.subheader("Dataset Preview")

st.dataframe(df.head())

# ==================================
# Sidebar
# ==================================

st.sidebar.title("🏥 AI Healthcare")

st.sidebar.markdown("---")

st.sidebar.header("Project")

st.sidebar.write("""
AI Healthcare Diagnosis Assistant

This application predicts the most probable diseases based on the symptoms selected by the user.
""")

st.sidebar.markdown("---")

st.sidebar.header("Technology")

st.sidebar.write("""
- Python
- Streamlit
- Pandas
- NumPy
- Scikit-Learn
- Cosine Similarity
""")

st.sidebar.markdown("---")

st.sidebar.info(
    "⚠️ This tool is for educational purposes only and should not replace professional medical advice."
)

# Symptom Selection 
st.divider()

st.header("🩺 Select Symptoms")

# Get all symptom column names
symptom_list = list(features.columns)

# Function to clean symptom names
def clean_symptom(symptom):

    if "_" in symptom:
        symptom = symptom.split("_", 1)[1]

    return symptom.replace("_", " ").title()

# Create cleaned symptom list
clean_symptoms = [clean_symptom(symptom) for symptom in symptom_list]

# Multi-select widget
selected_symptoms = st.multiselect(
    "Choose one or more symptoms",
    clean_symptoms
)

# Predict Button
predict = st.button(
    "🔍 Predict Disease",
    use_container_width=True
)

# ==================================
# Disease Prediction
# ==================================

if predict:

    if len(selected_symptoms) == 0:

        st.warning("⚠ Please select at least one symptom.")

    else:

        # User Symptom Vector
        user_vector = np.zeros(len(symptom_list))

        for symptom in selected_symptoms:

            index = clean_symptoms.index(symptom)
            user_vector[index] = 1

        # Cosine Similarity
        similarity = cosine_similarity(
            [user_vector],
            features.values
        )[0]

        # Top 3 Diseases
        top3 = np.argsort(similarity)[::-1][:3]

        st.success("Prediction Completed Successfully!")

        st.divider()

        st.header("🏆 Top Disease Predictions")

        # medals = ["🥇", "🥈", "🥉"]

        for rank, i in enumerate(top3):

            disease = diseases.iloc[i]

            score = similarity[i] * 100

            st.subheader(f"{[rank]} {disease}")

            # Progress Bar
            st.progress(float(similarity[i]))

            # Match Score
            st.metric(
                "Match Score",
                f"{score:.2f}%"
            )

            # Rating
            if score >= 30:
                st.success("⭐⭐⭐⭐⭐ Excellent Match")

            elif score >= 20:
                st.info("⭐⭐⭐⭐ Good Match")

            elif score >= 10:
                st.warning("⭐⭐⭐ Possible Match")

            else:
                st.error("⭐⭐ Weak Match")

            # Matched Symptoms
            disease_vector = features.iloc[i]

            matched = []

            for j, value in enumerate(disease_vector):

                if value == 1 and user_vector[j] == 1:

                    matched.append(clean_symptoms[j])

            st.write("### ✅ Matched Symptoms")

            if matched:

                for symptom in matched:
                    st.write("✔", symptom)

            else:

                st.write("No exact matched symptoms found.")

            st.divider()