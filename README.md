# Student Dropout Prediction

## Project Overview

This machine learning project predicts whether a student is at risk of dropping out.

The purpose of the project is to demonstrate how machine learning can support educational institutions by identifying students who may require early academic support.

## Problem Type

This is a binary classification problem.

- 1 = Dropout
- 0 = Not Dropout

## Dataset

The project uses the Predict Students' Dropout and Academic Success dataset.

The dataset contains 4,424 student records with academic, demographic, economic and enrollment-related features.

## Project Workflow

The project followed these steps:

1. Problem understanding
2. Dataset collection
3. Data cleaning
4. Data preprocessing
5. Exploratory Data Analysis
6. Logistic Regression model training
7. Model evaluation
8. Student dropout risk prediction
9. Application deployment

## Data Preprocessing

The dataset was checked for:

- Missing values
- Duplicate records
- Incorrect data types
- Inconsistent values

The target variable was converted into a binary classification variable.

The features were standardized using StandardScaler.

## Exploratory Data Analysis

EDA was performed to understand relationships between student characteristics and academic outcomes.

Academic features such as semester grades and approved curricular units showed important relationships with student outcomes.

## Machine Learning Model

Logistic Regression was used because the project is a classification problem.

The dataset was divided into:

- 80% training data
- 20% testing data

## Model Evaluation

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- ROC-AUC

## Student Risk Prediction

The trained model calculates a student's probability of dropping out.

Risk categories are:

- Low Risk: below 30%
- Medium Risk: 30%–59%
- High Risk: 60% or above

## Application

A Streamlit application was created where users can enter student information and receive a predicted dropout probability and risk category.

## Potential Real-World Use

Educational institutions could use a system like this as an early-warning tool.

Students identified as higher risk could receive academic guidance, counselling or additional support before dropping out.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Logistic Regression
- Streamlit
- Google Colab
- GitHub

## Conclusion

This project demonstrates the complete machine learning workflow from data collection and preprocessing to model training, evaluation and deployment.

The project shows how predictive analytics can be applied to educational data to identify students who may need early support.
