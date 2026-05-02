import streamlit as st
import pandas as pd
import joblib

import os
import joblib

BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "random_forest_model.pkl")

model = joblib.load(model_path)

st.title("Hotel Booking Cancellation Prediction System")

st.write("Enter booking details below:")

lead_time = st.number_input("Lead Time", min_value=0)

adr = st.number_input("Average Daily Rate (ADR)", min_value=0.0)

total_guests = st.number_input("Total Guests", min_value=1)

total_stay = st.number_input("Total Stay Duration", min_value=1)

previous_cancellations = st.number_input(
    "Previous Cancellations",
    min_value=0
)

booking_changes = st.number_input(
    "Booking Changes",
    min_value=0
)

hotel = st.selectbox(
    "Hotel Type",
    ["Resort Hotel", "City Hotel"]
)

customer_type = st.selectbox(
    "Customer Type",
    [
        "Transient",
        "Contract",
        "Transient-Party",
        "Group"
    ]
)

hotel_map = {
    "Resort Hotel": 1,
    "City Hotel": 0
}

customer_map = {
    "Transient": 2,
    "Contract": 0,
    "Transient-Party": 3,
    "Group": 1
}

input_data = pd.DataFrame({
    'hotel': [hotel_map[hotel]],
    'lead_time': [lead_time],
    'arrival_date_month': [0],
    'stays_in_weekend_nights': [0],
    'stays_in_week_nights': [0],
    'adults': [2],
    'children': [0],
    'babies': [0],
    'meal': [0],
    'market_segment': [0],
    'distribution_channel': [0],
    'is_repeated_guest': [0],
    'previous_cancellations': [previous_cancellations],
    'booking_changes': [booking_changes],
    'deposit_type': [0],
    'days_in_waiting_list': [0],
    'customer_type': [customer_map[customer_type]],
    'adr': [adr],
    'total_guests': [total_guests],
    'total_stay': [total_stay],
    'is_family': [1 if total_guests > 2 else 0]
})

if st.button("Predict"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Booking is likely to be canceled.")
    else:
        st.success("Booking is likely to be retained.")
