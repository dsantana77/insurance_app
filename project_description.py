import pickle
import pandas as pd
import streamlit as st

# Page COnfig
st.set_page_config(
    page_title='Insurance Prediction',
    page_icon="img/stethoscope.png"

    )

st.sidebar.header('Project Description')

st.write("# Welcome to the Insurance Prediction App")
st.write("\n\n")

st.image('img\image.jpg')
st.write('\n\n')

st.markdown(
    """
Insurance Prediction App:

The Insurance Prediction App is a tool designed to estimate insurance premiums for individuals based on key factors such as smoking status, age, number of children, and BMI. This app leverages predictive modeling techniques to provide personalized insurance cost estimates.

Factors Considered:

Smoking Status: Smoking is a significant risk factor for various health conditions, leading to higher insurance premiums for smokers compared to non-smokers.
Age: Age is a critical factor in determining insurance costs. Generally, older individuals may face higher premiums due to increased health risks associated with aging.
Number of Children: The number of children an individual has can also impact insurance premiums. More children may indicate higher family-related expenses and potential health-related costs.
BMI (Body Mass Index): BMI is a measure of body fat based on height and weight. Higher BMIs may be associated with increased health risks, leading to higher insurance premiums.
Functionality:

Input Parameters: Users input their smoking status (yes/no), age, number of children, and BMI into the app.
Prediction Calculation: The app utilizes a predictive model that takes into account the provided inputs to estimate the individual's insurance costs. This model considers historical data and correlations between smoking status, age, number of children, BMI, and insurance premiums.
Display of Results: The estimated insurance cost is then displayed to the user. This provides them with insights into how these factors contribute to their insurance expenses.
"""
)

st.success('please **go to the next pages** to get the prediction')