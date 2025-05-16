import streamlit as st
import numpy as np
import pickle

# --- Emoji dictionaries for crops and fertilizers ---
crop_emoji = {
    "Rice": "🌾", "Maize": "🌽", "Jute": "🧵", "Cotton": "🧶", "Coconut": "🥥",
    "Papaya": "🍈", "Orange": "🍊", "Apple": "🍎", "Muskmelon": "🍈", "Watermelon": "🍉",
    "Grapes": "🍇", "Mango": "🥭", "Banana": "🍌", "Pomegranate": "🍎", "Lentil": "🌱",
    "Blackgram": "🌱", "Mungbean": "🌱", "Mothbeans": "🌱", "Pigeonpeas": "🌱",
    "Kidneybeans": "🌱", "Chickpea": "🌱", "Coffee": "☕"
}
fert_emoji = {
    "Urea": "🧪", "DAP": "🧴", "14-35-14": "🧫", "28-28": "🧬", "17-17-17": "⚗️",
    "20-20": "🧯", "10-26-26": "🧲"
}

# --- Session state for prediction history ---
if "crop_history" not in st.session_state:
    st.session_state.crop_history = []
if "fert_history" not in st.session_state:
    st.session_state.fert_history = []

# Load Crop Model and Scaler
crop_model = pickle.load(open('crop_model.sav', 'rb'))
crop_scaler = pickle.load(open('crop_scaler.sav', 'rb'))

# Load Fertilizer Model and Scaler
fertilizer_model = pickle.load(open('fertilizer_model.sav', 'rb'))
fertilizer_scaler = pickle.load(open('fertilizer_scaler.sav', 'rb'))

# Crop dictionary
crop_dict = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 
    6: "Papaya", 7: "Orange", 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 
    11: "Grapes", 12: "Mango", 13: "Banana", 14: "Pomegranate", 15: "Lentil", 
    16: "Blackgram", 17: "Mungbean", 18: "Mothbeans", 19: "Pigeonpeas", 
    20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
}

# Fertilizer dictionary
fert_dict = {
    1: 'Urea', 2: 'DAP', 3: '14-35-14', 4: '28-28', 5: '17-17-17', 6: '20-20', 7: '10-26-26'
}

st.title("Crop & Fertilizer Recommendation System")

option = st.sidebar.selectbox("Choose Recommendation", ("Crop", "Fertilizer"))

if option == "Crop":
    st.header("Crop Recommendation")
    N = st.number_input("Nitrogen (N)", min_value=0)
    P = st.number_input("Phosphorus (P)", min_value=0)
    K = st.number_input("Potassium (K)", min_value=0)
    temperature = st.number_input("Temperature (°C)")
    humidity = st.number_input("Humidity (%)")
    ph = st.number_input("pH Value")
    rainfall = st.number_input("Rainfall (mm)")

    if st.button("Recommend Crop"):
        features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        transformed = crop_scaler.transform(features)
        pred = crop_model.predict(transformed)
        crop_name = crop_dict.get(pred[0], "Unknown")
        emoji = crop_emoji.get(crop_name, "🌱")
        st.success(f"Recommended Crop: {emoji} **{crop_name}**")
        # Add to history
        st.session_state.crop_history.append({
            "Nitrogen": N, "Phosphorus": P, "Potassium": K,
            "Temperature": temperature, "Humidity": humidity,
            "pH": ph, "Rainfall": rainfall, "Crop": f"{emoji} {crop_name}"
        })

    # Show history
    if st.session_state.crop_history:
        st.subheader("Prediction History")
        st.table(st.session_state.crop_history)

elif option == "Fertilizer":
    st.header("Fertilizer Recommendation")
    Temparature = st.number_input("Temperature")
    Humidity = st.number_input("Humidity")
    Moisture = st.number_input("Moisture")
    Soil_Type = st.number_input("Soil Type (as number)")
    Crop_Type = st.number_input("Crop Type (as number)")
    Nitrogen = st.number_input("Nitrogen")
    Potassium = st.number_input("Potassium")
    Phosphorous = st.number_input("Phosphorous")

    if st.button("Recommend Fertilizer"):
        features = np.array([[Temparature, Humidity, Moisture, Soil_Type, Crop_Type, Nitrogen, Potassium, Phosphorous]])
        transformed = fertilizer_scaler.transform(features)
        pred = fertilizer_model.predict(transformed)
        fert_name = fert_dict.get(pred[0], "Unknown")
        emoji = fert_emoji.get(fert_name, "🧪")
        st.success(f"Recommended Fertilizer: {emoji} **{fert_name}**")
        # Add to history
        st.session_state.fert_history.append({
            "Temperature": Temparature, "Humidity": Humidity, "Moisture": Moisture,
            "Soil Type": Soil_Type, "Crop Type": Crop_Type,
            "Nitrogen": Nitrogen, "Potassium": Potassium, "Phosphorous": Phosphorous,
            "Fertilizer": f"{emoji} {fert_name}"
        })

    # Show history
    if st.session_state.fert_history:
        st.subheader("Prediction History")
        st.table(st.session_state.fert_history)