import streamlit as st
import requests

st.set_page_config(page_title="Car Price Prediction", page_icon="🚗", layout="centered")

API_URL = (
    "https://car-prediction-lpfl.onrender.com/predict"
    or "http://127.0.0.1:8000/predict"
)  

st.title("🚗 Car Price Prediction")
st.caption(
    "It sends data to FastAPI backend and shows predicted selling price."
)

# --- Inputs 
car_name = st.text_input("Car_Name (e.g. swift, ritz, sx4)")

year = st.number_input("Year", step=1)

present_price = st.number_input(
    "Present_Price (in lakhs)", min_value=0.0, step=0.1
)

kms_driven = st.number_input("Kms_Driven", min_value=0, step=1000)

fuel_type = st.selectbox("Fuel_Type", ["Petrol", "Diesel", "CNG"])

seller_type = st.selectbox("Seller_Type", ["Dealer", "Individual"])

transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# Owner is numeric in your dataset (0,1,3). Map UI labels to int.
owner_label = st.selectbox(
    "Owner", ["0 (First Owner)", "1 (Second Owner)", "3 (Third Owner)"]
)
owner = int(owner_label.split()[0])

payload = {
    "Car_Name": str(car_name),
    "Year": int(year),
    "Present_Price": float(present_price),
    "Kms_Driven": int(kms_driven),
    "Fuel_Type": str(fuel_type),
    "Seller_Type": str(seller_type),
    "Transmission": str(transmission),
    "Owner": int(owner),
}

st.write("### Details sent:")
st.json(payload)

if st.button("Predict Price 💰"):
    try:
        res = requests.post(API_URL, json=payload, timeout=20)
        if res.status_code == 200:
            data = res.json()

            # adjust keys based on your API response
            # common patterns: {"prediction": 3.45} or {"predicted_price": 3.45}
            pred = data.get("prediction", data.get("predicted_price", None))

            if pred is None:
                st.warning(
                    "API responded but prediction key not found. Full response below:"
                )
                st.json(data)
            else:
                st.success(f"✅ Predicted Selling Price: **₹ {pred:.2f} lakhs**")
        else:
            st.error(f"❌ API Error {res.status_code}")
            st.code(res.text)
    except requests.exceptions.RequestException as e:
        st.error("❌ Could not connect to API. Is FastAPI running?")
        st.code(str(e))

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0e1117;
        color: #9e9e9e;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        z-index: 100;
    }
    </style>

    <div class="footer">
        🚗 Car Price Prediction App | Developed by: Sahil Bhatti
    </div>
    """,
    unsafe_allow_html=True
)
