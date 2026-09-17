
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("dropout_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")
feature_means = joblib.load("feature_means.pkl")

st.title("Student Dropout Risk Prediction")

age = st.number_input("Age at Enrollment", 15, 70, 20)
admission_grade = st.number_input("Admission Grade", 0.0, 200.0, 120.0)
sem1_grade = st.number_input("1st Semester Grade", 0.0, 20.0, 12.0)
sem1_approved = st.number_input("1st Semester Approved Units", 0, 30, 5)
sem2_grade = st.number_input("2nd Semester Grade", 0.0, 20.0, 12.0)
sem2_approved = st.number_input("2nd Semester Approved Units", 0, 30, 5)

if st.button("Predict Dropout Risk"):

    student = feature_means.copy()

    student["Age at enrollment"] = age
    student["Admission grade"] = admission_grade
    student["Curricular units 1st sem (grade)"] = sem1_grade
    student["Curricular units 1st sem (approved)"] = sem1_approved
    student["Curricular units 2nd sem (grade)"] = sem2_grade
    student["Curricular units 2nd sem (approved)"] = sem2_approved

    student_df = pd.DataFrame([student], columns=feature_names)
    student_scaled = scaler.transform(student_df)

    probability = model.predict_proba(student_scaled)[0][1]

    if probability < 0.30:
        risk = "Low Risk"
    elif probability < 0.60:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    st.subheader("Prediction Result")
    st.write(f"Dropout Probability: {probability * 100:.2f}%")
    st.write(f"Risk Category: **{risk}**")
