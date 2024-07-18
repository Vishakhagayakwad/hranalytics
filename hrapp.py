
import streamlit as st
import pickle
import numpy as np

# Load the trained XGBoost model and scaler
with open('hr.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('schr.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Create the web app
st.title('Salary Prediction App')

# Input fields
age = st.number_input('Age', min_value=0, max_value=120, value=30)
education = st.selectbox('Education Level', ['High School or less', 'Intermediate', 'Graduation', 'PG'])
experience_months = st.number_input('Months of Experience', min_value=0, max_value=600, value=60)  # Assuming max experience is 50 years

# Convert education to numeric encoding
education_mapping = {'High School or less': 0, 'Intermediate': 1, 'Graduation': 2, 'PG': 3}
education_encoded = education_mapping[education]

# Prepare the feature vector
features = np.array([[age, education_encoded, experience_months]], dtype=np.float64)

# Scale the features
features_scaled = scaler.transform(features)

# Predict salary
predicted_salary = model.predict(features_scaled)

# Display the result
st.write(f"Predicted Salary: ${predicted_salary[0]:,.2f}")
