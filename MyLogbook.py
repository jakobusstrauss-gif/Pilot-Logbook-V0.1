import streamlit as st
from datetime import datetime

# Initialize session state for data storage
if 'flight_data' not in st.session_state:
    st.session_state['flight_data'] = {}

st.title("Digital Pilot Logbook - New Flight Entry")

# Step 1: Input - Date of Flight
date_input = st.text_input("Enter Date of Flight (DD/MM/YYYY)")

if 'flight_date' not in st.session_state:
    # Validate date input
    if st.button("Next") and date_input:
        try:
            date_obj = datetime.strptime(date_input, "%d/%m/%Y")
            st.session_state['flight_data']['Date'] = date_obj.strftime('%Y-%m-%d')
            st.success(f"Date entered: {date_obj.strftime('%Y-%m-%d')}")
        except ValueError:
            st.error("Invalid date format. Please enter as DD/MM/YYYY.")
    elif date_input:
        try:
            datetime.strptime(date_input, "%d/%m/%Y")
        except:
            st.error("Invalid date format. Please enter as DD/MM/YYYY.")
else:
    # Date has been validated, show next input
    st.write(f"**Flight Date:** {st.session_state['flight_data']['Date']}")
    # Step 2: Type of Aircraft
    aircraft_type = st.text_input("Enter Type of Airplane")
    if st.button("Next") and aircraft_type:
        st.session_state['flight_data']['Type of Airplane'] = aircraft_type
        st.success(f"Aircraft type recorded: {aircraft_type}")
