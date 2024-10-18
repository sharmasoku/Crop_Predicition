import numpy as np
import streamlit as st
import pickle

# Load the trained Random Forest model
pickle_in = open('RandomForest.pkl', 'rb')
RF = pickle.load(pickle_in)

# Custom HTML title with CSS for styling
st.markdown("""
    <div style="background-color: #4CAF50; padding: 10px; border-radius: 10px;">
        <h1 style="color: white; text-align: center; font-family: Arial, sans-serif;">
            CROP RECOMMENDATION 🌾
        </h1>
    </div>
""", unsafe_allow_html=True)

# Inputs for the prediction model
N = st.text_input(label="Nitrogen level of soil")
P = st.text_input(label="Phosphorus level of soil")
K = st.text_input(label="Potassium level of soil")
Temp = st.text_input(label="Temperature (°C)")
Hum = st.text_input(label="Humidity (%)")
ph = st.text_input(label="pH Value of soil")
rnfl = st.text_input(label="Rainfall in the area (mm)")


# Button for prediction
if st.button("Predict the crop"):
    try:
        data = np.array([[int(N), int(P), int(K), float(Temp), float(Hum), float(ph), float(rnfl)]])
        prediction = RF.predict(data)
        # Custom HTML to display the prediction with large green text
        st.markdown(f"""
            <div style="background-color: #DFF0D8; padding: 15px; border-radius: 10px; margin-top: 10px;">
                <h2 style="color: #3C763D; text-align: center; font-family: Arial, sans-serif;">
                    You should cultivate: <b>{prediction[0]}</b> 🌱
                </h2>
            </div>
        """, unsafe_allow_html=True)
    except:
        st.warning('Please Enter the value in above field')