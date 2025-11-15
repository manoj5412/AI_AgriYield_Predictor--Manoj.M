import streamlit as st
import pandas as pd
import pickle

# --- PAGE CONFIG ---
st.set_page_config(page_title="Smart Crop Yield Prediction", page_icon="🌾", layout="centered")

# --- TITLE ---
st.title("🌾 Smart Crop Yield Prediction System")
st.write("Predict your crop yield based on soil, weather, and region data")

# --- LOAD MODEL ---
try:
    model = pickle.load(open("models/xgb_yield_model.pkl", "rb"))
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Model loading failed: {e}")
    st.stop()

# --- INPUT SECTION ---
st.header("📊 Enter Crop & Environmental Details")

col1, col2 = st.columns(2)
with col1:
    state = st.selectbox("State", ["Tamil Nadu", "Kerala", "Karnataka", "Andhra Pradesh", "Telangana"])
    if state == "Tamil Nadu":
        district = st.selectbox("District", ["Coimbatore", "Thanjavur", "Erode", "Salem", "Madurai"])
    else:
        district = "DefaultDistrict"  # Auto-fill for other states
    season = st.selectbox("Season", ["Kharif", "Rabi", "Summer", "Winter", "Whole Year"])
    crop = st.selectbox("Crop", ["Rice", "Maize", "Sugarcane", "Cotton", "Wheat"])
    year = st.number_input("Year", min_value=2000, max_value=2030, value=2024)

with col2:
    area = st.number_input("Area (in hectares)", min_value=0.1, value=10.0)
    production = st.number_input("Production (in tons)", min_value=0.1, value=8.0)
    N = st.number_input("Nitrogen (N)", min_value=0.0, value=60.0)
    P = st.number_input("Phosphorus (P)", min_value=0.0, value=50.0)
    K = st.number_input("Potassium (K)", min_value=0.0, value=40.0)
    temperature = st.number_input("Temperature (°C)", value=25.0)
    humidity = st.number_input("Humidity (%)", value=70.0)
    ph = st.number_input("Soil pH", value=6.5)
    rainfall = st.number_input("Rainfall (mm)", value=200.0)

# --- CREATE INPUT DATAFRAME ---
input_data = pd.DataFrame([{
    'State': state,
    'District': district,
    'Year': year,
    'Season': season,
    'Crop': crop,
    'Area': area,
    'Production': production,
    'N': N,
    'P': P,
    'K': K,
    'temperature': temperature,
    'humidity': humidity,
    'ph': ph,
    'rainfall': rainfall
}])

# --- FEATURE ENGINEERING (same as training) ---
input_data['crop_encoded'] = input_data['Crop'].astype('category').cat.codes
input_data['N_by_P'] = input_data['N'] / (input_data['P'] + 1)
input_data['K_by_N'] = input_data['K'] / (input_data['N'] + 1)
input_data['rain_temp_ratio'] = input_data['rainfall'] / (input_data['temperature'] + 1)
input_data['ph_humidity_interaction'] = input_data['ph'] * input_data['humidity']
input_data['nutrient_sum'] = input_data['N'] + input_data['P'] + input_data['K']
input_data['nutrient_balance'] = abs(input_data['N'] - input_data['P']) + abs(input_data['K'] - input_data['P'])
input_data['rainfall_ph_interaction'] = input_data['rainfall'] * input_data['ph']
input_data['State_enc'] = input_data['State'].astype('category').cat.codes
input_data['District_enc'] = input_data['District'].astype('category').cat.codes
input_data['N_P_ratio'] = input_data['N'] / (input_data['P'] + 1)
input_data['K_N_ratio'] = input_data['K'] / (input_data['N'] + 1)
input_data['humidity_ph_interaction'] = input_data['humidity'] * input_data['ph']
input_data['temp_squared'] = input_data['temperature'] ** 2

# --- Convert categorical columns ---
for col in ['State', 'District', 'Season', 'Crop']:
    input_data[col] = input_data[col].astype('category')

# --- PREDICT BUTTON ---
if st.button("🌾 Predict Yield"):
    try:
        # Directly predict with DataFrame (no DMatrix)
        prediction = model.predict(input_data)
        yield_value = float(prediction[0])

        st.success(f"🌾 Predicted Crop Yield: {yield_value:.2f} tons/hectare")

        st.markdown("### 🌱 Prediction Summary")
        st.write(f"🗺️ **State:** {state}")
        st.write(f"📍 **District:** {district}")
        st.write(f"☀️ **Season:** {season}")
        st.write(f"🌾 **Crop:** {crop}")
        st.write(f"📈 **Predicted Yield:** {yield_value:.2f} tons/hectare")

    except Exception as e:
        st.error(f"⚠️ Error while predicting: {e}")






