import streamlit as st
import pickle
import numpy as np

# Load the trained Linear Regression model
with open("model_LinearRegression.pkl", "rb") as f:
    model = pickle.load(f)

# App title and description
st.set_page_config(page_title="Insurance Cost Predictor", page_icon="💰")
st.title("💰 Insurance Cost Prediction App")
st.write("Enter the details below to estimate your medical insurance charges:")

# Input fields
age = st.number_input("Age", min_value=0, max_value=100, value=30)
bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=60.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
sex = st.selectbox("Sex", ("Female", "Male"))
smoker = st.selectbox("Smoker", ("No", "Yes"))

# Convert to numeric
sex_male = 1 if sex == "Male" else 0
smoker_yes = 1 if smoker == "Yes" else 0

# Predict
if st.button("Predict Insurance Cost 💵"):
    X = np.array([[age, bmi, children, sex_male, smoker_yes]])
    prediction = model.predict(X)[0]
    st.success(f"✅ Estimated Insurance Cost: ₹{prediction:,.2f}")

# Footer
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit and Linear Regression Model")
