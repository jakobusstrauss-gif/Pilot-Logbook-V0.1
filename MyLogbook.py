import streamlit as st
import pandas as pd

# Initialize session state for flight logs
if 'flight_logs' not in st.session_state:
    st.session_state['flight_logs'] = pd.DataFrame(columns=[
        'Date', 'Aircraft Type', 'Registration', 'Pilot in Command', 'Flight Details'
    ])

st.title("Pilot Flight Hours Log")

# Input form for a new flight
with st.form("log_flight_form"):
    # Manual entry in British format (DD/MM/YYYY)
    date_str = st.text_input("Flight Date (DD/MM/YYYY)", placeholder="e.g., 15/08/2025")
    aircraft_type = st.text_input("Type of Aircraft")
    registration = st.text_input("Registration")
    pilot_in_command = st.text_input("Name of Pilot in Command")
    flight_details = st.text_area("Details of Flight")
    submitted = st.form_submit_button("Add Flight")

    if submitted:
        # Validate and convert date
        from datetime import datetime
        try:
            date_obj = datetime.strptime(date_str, "%d/%m/%Y")
            date_formatted = date_obj.strftime("%Y-%m-%d")  # Store in ISO format
            # Append new log to session state
            new_entry = {
                'Date': date_formatted,
                'Aircraft Type': aircraft_type,
                'Registration': registration,
                'Pilot in Command': pilot_in_command,
                'Flight Details': flight_details
            }
            st.session_state['flight_logs'] = st.session_state['flight_logs'].append(new_entry, ignore_index=True)
            st.success("Flight logged successfully!")
        except ValueError:
            st.error("Invalid date format. Please use DD/MM/YYYY.")

# Display logged flights
st.header("Logged Flights")
st.dataframe(st.session_state['flight_logs'])
