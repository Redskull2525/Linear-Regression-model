import streamlit as st
import pickle
import numpy as np

# -------------------- Load the Trained Model --------------------
with open("model_LinearRegression.pkl", "rb") as f:
    model = pickle.load(f)

# -------------------- Page Configuration --------------------
st.set_page_config(
    page_title="Insurance Cost Predictor",
    page_icon="💰",
    layout="wide"
)

# -------------------- Sidebar: Developer Info --------------------
st.sidebar.markdown(
    """
    <style>
        .sidebar-title {
            font-size: 22px;
            font-weight: bold;
            color: #27AE60; /* Bright green */
            text-align: center;
            margin-bottom: 15px;
        }
        .contact-info {
            font-size: 16px;
            line-height: 1.8;
        }
        .contact-info b {
            color: #E74C3C; /* Bright red for labels */
        }
        .contact-info a {
            color: #2ECC71; /* Green for links */
            text-decoration: none;
            font-weight: bold;
        }
        .contact-info a:hover {
            color: #F1C40F; /* Yellow on hover */
            text-decoration: underline;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <div class="sidebar-title">👨‍💻 Developer Info</div>
    <div class="contact-info">
        <b>Name:</b> <span style="color:#E74C3C;">Abhishek Shelke</span><br>
        <b>Email:</b> <a href="mailto:abhishekshelke3535@gmail.com">abhishekshelke3535@gmail.com</a><br>
        <b>Phone:</b> <a href="tel:+918530997939">+91 85309 97939</a><br>
        <b>GitHub:</b> <a href="https://github.com/Redskull2525" target="_blank">github.com/Redskull2525</a><br>
        <b>LinkedIn:</b> <a href="https://www.linkedin.com/in/abhishek-s-b98895249" target="_blank">linkedin.com/in/abhishek-s-b98895249</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("---")
st.sidebar.markdown("💡 *Developed with ❤️ using Streamlit and Linear Regression Model*")

# -------------------- Main Page --------------------
st.title("💰 Insurance Cost Prediction App")
st.write("Enter the details below to estimate your **medical insurance charges**:")

# Input fields
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=0, max_value=100, value=30)
    bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=60.0, value=25.0)
    children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
with col2:
    sex = st.selectbox("Sex", ("Female", "Male"))
    smoker = st.selectbox("Smoker", ("No", "Yes"))

# Convert to numeric
sex_male = 1 if sex == "Male" else 0
smoker_yes = 1 if smoker == "Yes" else 0

# Predict
st.markdown("---")
if st.button("🔮 Predict Insurance Cost"):
    X = np.array([[age, bmi, children, sex_male, smoker_yes]])
    prediction = model.predict(X)[0]
    st.success(f"✅ Estimated Insurance Cost: ₹{prediction:,.2f}")

# -------------------- Footer --------------------
st.markdown("---")
st.caption("© 2025 Abhishek Shelke | Built with Streamlit 💻")
