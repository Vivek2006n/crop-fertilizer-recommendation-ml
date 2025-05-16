# Crop & Fertilizer Recommendation System

A machine learning based web application for recommending suitable crops and fertilizers based on soil and weather parameters. Built using Streamlit.

---

## 🚀 Features

- 🌱 **Crop Recommendation:** Suggests the best crop based on soil nutrients and weather.
- 🧪 **Fertilizer Recommendation:** Suggests the best fertilizer based on soil, crop, and environmental data.
- 📊 **Prediction History:** View all your predictions in the current session.
- 😀 **Emoji Icons:** Visual feedback with crop and fertilizer emojis.
- 🖥️ **Easy-to-use Web Interface:** No coding required for end users.

---

## 🖼️ Screenshots



## 🛠️ How to Run

1. **Clone this repository:**
   ```
   git clone https://github.com/Vivek2006n/crop-fertilizer-recommendation-ml.git
   cd crop-fertilizer-recommendation-ml
   ```
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```
   streamlit run app.py
   ```
4. **Open the provided URL in your browser.**

---

## 📝 Input Parameters

### Crop Recommendation
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature (°C)
- Humidity (%)
- pH Value
- Rainfall (mm)

### Fertilizer Recommendation
- Temperature
- Humidity
- Moisture
- Soil Type (as number)
- Crop Type (as number)
- Nitrogen
- Potassium
- Phosphorous

---

## 📁 Files

- `app.py` — Main Streamlit app
- `crop_model.sav`, `crop_scaler.sav` — Crop ML model and scaler
- `fertilizer_model.sav`, `fertilizer_scaler.sav` — Fertilizer ML model and scaler
- `Fertilizer_recommendation.ipynb`, `Final_Week.ipynb` — Jupyter notebooks for model development
- `requirements.txt` — Python dependencies

---

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 👤 Author

- Vivek Negi  
- For internship/industry use

---

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)
