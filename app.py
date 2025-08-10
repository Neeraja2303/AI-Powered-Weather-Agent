import streamlit as st
from agents.yield_predictor import predict_yield
from agents.weather_agent import get_weather
from agents.soil_health_agent import soil_advice
from agents.crop_advisor import recommend_crop
from agents.optimization_agent import give_tips

st.title("🌾 AgriAid - AI Crop Yield & Farm Advisor")

st.header("Enter Your Data")
city = st.text_input("Location (City)")
rainfall = st.slider("Rainfall (mm)", 0, 300, 100)
temperature = st.slider("Temperature (°C)", 10, 45, 25)
nitrogen = st.slider("Soil Nitrogen Level", 0, 100, 50)
ph = st.slider("Soil pH Level", 4.0, 9.0, 6.5)

if st.button("🔍 Analyze"):
    st.subheader("📊 Yield Prediction")
    yield_pred = predict_yield(rainfall, temperature, nitrogen, ph)
    st.success(f"Estimated Yield: {yield_pred:.2f} kg/hectare")

    st.subheader("🌦 Weather Forecast")
    if city:
        weather = get_weather(city)
        st.info(f"{city}: {weather['desc']} | {weather['temp']}°C | {weather['humidity']}% Humidity")

    st.subheader("🧪 Soil Health Advice")
    st.warning(soil_advice(ph, nitrogen))

    st.subheader("🌱 Crop Recommendation")
    crop = recommend_crop(temperature, rainfall, 'loamy')
    st.success(f"Recommended Crop: {crop.capitalize()}")

    st.subheader("📈 Optimization Tips")
    st.info(give_tips(crop))
