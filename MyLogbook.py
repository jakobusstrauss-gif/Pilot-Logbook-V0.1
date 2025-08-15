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
    st.write(f"**Airplane Registration:** {st
