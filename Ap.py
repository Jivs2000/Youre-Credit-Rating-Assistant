import streamlit as st
import pandas as pd


st.title("Creditworthiness Prediction App")

# User inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
ed = st.selectbox("Education Level (1=Low, 5=High)", list(range(1, 6)))
employ = st.slider("Years of Employment", 0, 40, 5)
address = st.slider("Years at Address", 0, 40, 5)
income = st.number_input("Annual Income (in thousands)", min_value=0, value=50)

# --- Simple rule-based scoring ---
score = 0

# Age
if age >= 25 and age <= 60:
    score += 10

# Education
score += ed * 2

# Employment
score += employ * 0.5

# Address Stability
score += address * 0.2

# Income
if income >= 50:
    score += 10
elif income >= 30:
    score += 5




# --- Classification ---
if score >= 40:
    decision = "High Credit Worthiness"
elif score >= 25:
    decision = "Moderate Credit Worthiness"
else:
    decision = "Low Credit Worthiness"

st.markdown(f"### Credit Score: {score:.1f}")
st.markdown(f"## Credit Worthiness: **{decision}**")
