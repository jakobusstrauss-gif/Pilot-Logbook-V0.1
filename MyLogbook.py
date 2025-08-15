import streamlit as st
from datetime import datetime

# Initialize session state
if 'flight_data' not in st.session_state:
    st.session_state['flight_data'] = {}
if 'step' not in st.session_state:
    st.session_state['step'] = 1

st.title("Digital Pilot Logbook - New Flight Entry")

# Helper function to get value with default
def get_value(key, default=''):
    return st.session_state['flight_data'].get(key, default)

# Step 1: Date of Flight
if st.session_state['step'] == 1:
    date_input = st.text_input("Enter Date of Flight (DD/MM/YYYY)", value=get_value('Date', ''))
    if st.button("Next") and date_input:
        try:
            date_obj = datetime.strptime(date_input, "%d/%m/%Y")
            st.session_state['flight_data']['Date'] = date_obj.strftime('%Y-%m-%d')
            st.session_state['step'] = 2
        except:
            st.error("Invalid date format. Please enter as DD/MM/YYYY.")

# Step 2: Type of Airplane
elif st.session_state['step'] == 2:
    st.write(f"**Flight Date:** {get_value('Date')}")
    aircraft_type = st.text_input("Enter Type of Airplane", value=get_value('Type of Airplane', ''))
    if st.button("Next") and aircraft_type:
        st.session_state['flight_data']['Type of Airplane'] = aircraft_type
        st.session_state['step'] = 3

# Step 3: Airplane Registration
elif st.session_state['step'] == 3:
    st.write(f"**Flight Date:** {get_value('Date')}")
    st.write(f"**Type of Airplane:** {get_value('Type of Airplane')}")
    registration = st.text_input("Enter Airplane Registration", value=get_value('Airplane Registration', ''))
    if st.button("Next") and registration:
        st.session_state['flight_data']['Airplane Registration'] = registration
        st.session_state['step'] = 4

# Step 4: Pilot In Command
elif st.session_state['step'] == 4:
    st.write(f"**Flight Date:** {get_value('Date')}")
    st.write(f"**Type of Airplane:** {get_value('Type of Airplane')}")
    st.write(f"**Airplane Registration:** {get_value('Airplane Registration')}")
    pilot_in_command = st.text_input("Enter Pilot In Command", value=get_value('Pilot In Command', ''))
    if st.button("Next") and pilot_in_command:
        st.session_state['flight_data']['Pilot In Command'] = pilot_in_command
        st.session_state['step'] = 5

# Step 5: Details of Flight
elif st.session_state['step'] == 5:
    # Show all previous data
    st.write(f"**Flight Date:** {get_value('Date')}")
    st.write(f"**Type of Airplane:** {get_value('Type of Airplane')}")
    st.write(f"**Airplane Registration:** {get_value('Airplane Registration')}")
    st.write(f"**Pilot In Command:** {get_value('Pilot In Command')}")
    # Editable textarea for flight details
    details = st.text_area("Enter Details of Flight", value=get_value('Details of Flight', ''))
    if st.button("Next") and details:
        st.session_state['flight_data']['Details of Flight'] = details
        st.session_state['step'] = 6

# Additional steps can follow similarly...

# Final review and save
if st.session_state['step'] > 5:
    st.write("Current data (editable):")
    for key, value in st.session_state['flight_data'].items():
        if key != 'Date':  # Date is already stored in 'Date'
            new_value = st.text_input(f"{key}", value=value)
            st.session_state['flight_data'][key] = new_value
    if st.button("Save Entry"):
        # Here, you'd typically write to CSV or database
        st.success("Data saved successfully!")
        # Reset for new entry
        st.session_state['step'] = 1
        st.session_state['flight_data'] = {}
