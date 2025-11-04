# 🏥 Medical Cost Prediction with Linear Regression

This repository contains a machine learning project focused on predicting **individual medical insurance costs** using several key health and demographic features. The project utilizes a **Linear Regression** model, complete with rigorous data cleaning, feature engineering, and a live web application for interactive predictions.

-----

## ✨ Live Demo

You can interact with the live application deployed on Streamlit Cloud here:

[](https://linear-regression-model-medical-cost.streamlit.app/)

**[Visit the Live App](https://linear-regression-model-medical-cost.streamlit.app/)**

-----

## 🎯 Project Goal

The primary objective is to accurately model the relationship between a set of independent variables (like age, BMI, smoking status) and the dependent variable (**insurance charges**).

The project follows a standard machine learning workflow:

1.  **Exploratory Data Analysis (EDA):** Initial inspection of data distributions and feature correlations.
2.  **Data Cleaning:** Removal of duplicate records and treatment of **BMI outliers** using the Interquartile Range (IQR) method.
3.  **Feature Engineering:** Conversion of categorical variables (like `sex` and `smoker`) into numerical format using **One-Hot Encoding**.
4.  **Model Training:** Fitting a Scikit-learn **`LinearRegression`** model.
5.  **Model Evaluation:** Assessing performance using **$R^2$ Score** and **Mean Squared Error (MSE)**.
6.  **Deployment:** Deploying the trained model via a **Streamlit** web interface.

-----

## ⚙️ Model and Features

### Selected Features (Independent Variables, X)

The model was trained using the following features, which showed the strongest correlation with medical charges:

  * `age`
  * `bmi` (Body Mass Index, cleaned of outliers)
  * `children`
  * `sex_male` (Dummy variable)
  * `smoker_yes` (Dummy variable, typically the strongest predictor)

### Performance Summary

The model's ability to generalize to unseen data was evaluated using the test set (20% of data).

| Metric | Training Set | Testing Set (Unseen Data) | Description |
| :--- | :--- | :--- | :--- |
| **$R^2$ Score** | (To be filled from results) | (To be filled from results) | Represents the proportion of the variance in charges predictable from the features. Scores closer to 1 are better. |
| **MSE** | (To be filled from results) | (To be filled from results) | Measures the average squared difference between actual and predicted charges. Lower scores are better. |

-----

## 📁 Repository Structure

```
Linear-Regression-model/
├── insurance.csv           # The original dataset used for training
├── model_training.py       # Main script for data processing and model training (your commented code)
├── app.py                  # Streamlit script for the web application
├── model_LinearRegression.pkl # The saved, trained model object
└── README.md               # This file
```

-----

## 💻 Technical Stack

| Category | Tools/Libraries | Purpose |
| :--- | :--- | :--- |
| **Language** | Python | Primary programming language. |
| **Data Handling** | Pandas, NumPy | Data cleaning, manipulation, and numerical operations. |
| **Machine Learning** | Scikit-learn | Model building (`LinearRegression`), data splitting, and evaluation. |
| **Visualization** | Matplotlib, Seaborn | Exploratory Data Analysis (EDA) and visualizing correlations. |
| **Deployment** | Streamlit | Creating the interactive web application. |
| **Persistence** | `pickle` | Saving the trained model object. |

-----

## 🚀 Local Setup and Run

To run this project locally, follow these steps:

### 1\. Clone the repository

```bash
git clone https://github.com/Redskull2525/Linear-Regression-model
cd Linear-Regression-model
```

### 2\. Prepare the dataset

Ensure the `insurance.csv` file is present in the root directory.

### 3\. Create a virtual environment and install dependencies

It is highly recommended to use a virtual environment.

```bash
# Create environment
python -m venv venv

# Activate environment (Linux/macOS)
source venv/bin/activate

# Activate environment (Windows)
.\venv\Scripts\activate

# Install all necessary libraries
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```

### 4\. Run the main script (Training)

Execute the training script to clean the data, train the model, and generate the `model_LinearRegression.pkl` file.

```bash
python model_training.py
```

### 5\. Run the Streamlit Application

Execute the Streamlit command to launch the web interface.

```bash
streamlit run app.py
```

The application will open in your web browser, typically at `http://localhost:8501`.
