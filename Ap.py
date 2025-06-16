import streamlit as st
import pandas as pd
import joblib

# Load model
try:
    model = joblib.load("credit_model.pkl")
except FileNotFoundError:
    st.error("❌ Model file 'credit_model.pkl' not found. Please make sure it's in the same folder.")
    st.stop()

st.title("Creditworthiness Prediction App")

# User inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
ed = st.selectbox("Education Level (1=Low, 5=High)", list(range(1, 6)))
employ = st.slider("Years of Employment", 0, 40, 5)
address = st.slider("Years at Address", 0, 40, 5)
income = st.number_input("Annual Income (in thousands)", min_value=0, value=50)
dti = st.number_input("Debt to Income Ratio", min_value=0.0, value=10.0)
cdr = st.number_input("Credit to Debt Ratio", min_value=0.0, value=1.5)
othdebt = st.number_input("Other Debt", min_value=0.0, value=3.0)

# Predict button
if st.button("Assess Creditworthiness"):
    input_df = pd.DataFrame([[age, ed, employ, address, income, dti, cdr, othdebt]],
                            columns=['age', 'ed', 'employ', 'address', 'income',
                                     'Debt to Income Ratio', 'Credit to Debt Ratio', 'othdebt'])

    try:
        prediction = model.predict(input_df)[0]
        if prediction == 1:
            st.error("⚠️ Result: Not Creditworthy (Default Likely)")
        else:
            st.success("✅ Result: Creditworthy (Low Risk)")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")