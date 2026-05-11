import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

# Load model & encoders
model = pickle.load(open("model.pkl", "rb"))
le_time = pickle.load(open("time_encoder.pkl", "rb"))
le_weather = pickle.load(open("weather_encoder.pkl", "rb"))
le_traffic = pickle.load(open("traffic_encoder.pkl", "rb"))
le_day = pickle.load(open("day_encoder.pkl", "rb"))
le_delay = pickle.load(open("delay_encoder.pkl", "rb"))

# Page config
st.set_page_config(
    page_title="Transit Delay Predictor",
    page_icon="🚍",
    layout="centered"
)

# Sidebar
st.sidebar.title("🚍 About Project")

st.sidebar.info(
    """
    This machine learning project predicts whether a public transit vehicle 
    will face delays based on:

    - Time of day
    - Weather condition
    - Traffic level
    - Day type

    Model Used:
    Random Forest Classifier
    """
)

# Title
st.title("🚍 Transit Delay Predictor")

st.markdown(
    "Predict whether public transport will face delays based on travel conditions."
)

st.divider()

# Input section
st.subheader("📋 Enter Trip Details")

col1, col2 = st.columns(2)

with col1:
    time = st.selectbox(
        "🕒 Time of Day",
        ["Morning", "Afternoon", "Evening", "Night"]
    )

    weather = st.selectbox(
        "🌦️ Weather Condition",
        ["Clear", "Rain"]
    )

with col2:
    traffic = st.selectbox(
        "🚗 Traffic Level",
        ["Low", "Medium", "High"]
    )

    day = st.selectbox(
        "📅 Day Type",
        ["Weekday", "Weekend"]
    )

st.divider()

# Prediction
if st.button("🔍 Predict Delay"):

    try:

        # Encode input
        input_data = pd.DataFrame([[
            le_time.transform([time])[0],
            le_weather.transform([weather])[0],
            le_traffic.transform([traffic])[0],
            le_day.transform([day])[0]
        ]], columns=["Time", "Weather", "Traffic", "Day"])

        # Prediction
        prediction = model.predict(input_data)

        result = le_delay.inverse_transform(prediction)[0]

        # Confidence score
        probability = model.predict_proba(input_data)

        confidence = max(probability[0]) * 100

        # Output message
        if result == "Yes":
            st.error("⚠️ Delay Expected")
        else:
            st.success("✅ No Major Delay Expected")

        # Confidence display
        st.info(f"📊 Confidence: {confidence:.2f}%")

        # Confidence interpretation
        if confidence > 85:
            st.success("Model is highly confident about this prediction.")

        elif confidence > 70:
            st.warning("Model confidence is moderate.")

        else:
            st.error("Prediction confidence is low.")

    except Exception as e:
        st.error(f"Error: {e}")

# Dataset preview
if st.checkbox("Show Dataset Sample"):

    data = pd.read_csv("transit_data.csv")

    st.dataframe(data.head(10))

# Feature importance chart
if st.checkbox("Show Feature Importance"):

    features = ["Time", "Weather", "Traffic", "Day"]

    importance = model.feature_importances_

    fig, ax = plt.subplots()

    ax.bar(features, importance)

    ax.set_ylabel("Importance")

    ax.set_title("Feature Importance")

    st.pyplot(fig)