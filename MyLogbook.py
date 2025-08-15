import streamlit as st
from datetime import datetime

# Initialize session state
if 'step' not in st.session_state:
    st.session_state['step'] = 1
if 'flight_data' not in st.session_state:
    st.session_state['flight_data'] = {}

st.title("Digital Pilot Logbook - New Flight Entry")

# Step 1: Enter Date of Flight
if st.session_state['step'] == 1:
    date_input = st.text_input("Enter Date of Flight (DD/MM/YYYY)")
    if st.button("Next") and date_input:
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

# Step 3: Enter Airplane Registration
elif st.session_state['step'] == 3:
    st.write(f"**Flight Date:** {st.session_state['flight_data']['Date']}")
    st.write(f"**Type of Airplane:** {st.session_state['flight_data']['Type of Airplane']}")
    registration = st.text_input("Enter Airplane Registration")
    if st.button("Next") and registration:
        st.session_state['flight_data']['Airplane Registration'] = registration
        st.session_state['step'] = 4

# Step 4: Enter Pilot In Command
elif st.session_state['step'] == 4:
    st.write(f"**Flight Date:** {st.session_state['flight_data']['Date']}")
    st.write(f"**Type of Airplane:** {st.session_state['flight_data']['Type of Airplane']}")
    st.write(f"**Airplane Registration:** {st.session_state['flight_data']['Airplane Registration']}")
    pilot_in_command = st.text_input("Enter Pilot In Command")
    if st.button("Next") and pilot_in_command:
        st.session_state['flight_data']['Pilot In Command'] = pilot_in_command
        st.session_state['step'] = 5

# Step 5: Details of Flight
elif st.session_state['step'] == 5:
    # Show previous data
    st.write(f"**Flight Date:** {st.session_state['flight_data']['Date']}")
    st.write(f"**Type of Airplane:** {st.session_state['flight_data']['Type of Airplane']}")
    st.write(f"**Airplane Registration:** {st.session_state['flight_data']['Airplane Registration']}")
    st.write(f"**Pilot In Command:** {st.session_state['flight_data']['Pilot In Command']}")
    # Input for Details of Flight
    flight_details = st.text_area("Enter Details of Flight")
    if st.button("Next") and flight_details:
        st.session_state['flight_data']['Details of Flight'] = flight_details
        st.session_state['step'] = 6

# After this, further steps can be added similarly...

# Review and Save
if st.session_state['step'] > 5:
    st.write("Current collected data:")
    for key, value in st.session_state['flight_data'].items():
        st.write(f"**{key}:** {value}")

    if st.button("Save Entry"):
        # Save to CSV or database here
        st.success("Data saved successfully!")
        # Reset for new entry
        st.session_state['step'] = 1
        st.session_state['flight_data'] = {}
