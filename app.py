import streamlit as st
import pickle

# Load model & encoders
model = pickle.load(open("model.pkl", "rb"))
le_time = pickle.load(open("time_encoder.pkl", "rb"))
le_weather = pickle.load(open("weather_encoder.pkl", "rb"))
le_delay = pickle.load(open("delay_encoder.pkl", "rb"))

st.title("Transit Delay Predictor 🚍")

time = st.selectbox("Select Time", ["Morning", "Afternoon", "Evening", "Night"])
weather = st.selectbox("Select Weather", ["Clear", "Rain"])

if st.button("Predict"):
    time_encoded = le_time.transform([time])[0]
    weather_encoded = le_weather.transform([weather])[0]

    prediction = model.predict([[time_encoded, weather_encoded]])
    result = le_delay.inverse_transform(prediction)

    st.success(f"Prediction: {result[0]}")