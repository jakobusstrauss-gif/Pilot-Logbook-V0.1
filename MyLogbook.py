import streamlit as st
from datetime import datetime

# Initialize session state for tracking step and data
if 'step' not in st.session_state:
    st.session_state['step'] = 1
if 'flight_data' not in st.session_state:
    st.session_state['flight_data'] = {}

st.title("Digital Pilot Logbook - New Flight Entry")

# Step 1: Enter Date of Flight
if st.session_state['step'] == 1:
    date_input = st.text_input("Enter Date of Flight (DD/MM/YYYY)")
    if st.button("Next"):
        try:
            date_obj = datetime.strptime(date_input, "%d/%m/%Y")
            st.session_state['flight_data']['Date'] = date_obj.strftime('%Y-%m-%d')
            st.session_state['step'] = 2
        except:
            st.error("Invalid date format. Please enter as DD/MM/YYYY.")

# Step 2: Enter Type of Airplane
elif st.session_state['step'] == 2:
    st.write(f"**Flight Date:** {st.session_state['flight_data']['Date']}")
    aircraft_type = st.text_input("Enter Type of Airplane")
    if st.button("Next") and aircraft_type:
        st.session_state['flight_data']['Type of Airplane'] = aircraft_type
        st.session_state['step'] = 3

# Additional steps can be added similarly
# For example, to proceed further, add:
# elif st.session_state['step'] == 3:
#     ... and so on

# Final step: review and save data
if st.session_state['step'] > 2:
    st.write("Current collected data:")
    for key, value in st.session_state['flight_data'].items():
        st.write(f"**{key}:** {value}")

    # Save to CSV, or add a "Submit" button to finalize the entry
    if st.button("Save Entry"):
        # Here, you would save the data to a CSV or database
        st.success("Data saved successfully!")
        # Reset session state for new entry if needed
        st.session_state['step'] = 1
        st.session_state['flight_data'] = {}
