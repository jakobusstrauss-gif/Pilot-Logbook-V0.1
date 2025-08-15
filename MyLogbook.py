import streamlit as st
import pandas as pd

# Initialize session state for flight logs
if 'flight_logs' not in st.session_state:
    st.session_state['flight_logs'] = pd.DataFrame(columns=[
        'Date', 'Aircraft Type', 'Registration', 'Pilot in Command', 'Flight Details',
        'Hours Flown', 'Day/Night', 'Engine Type'
    ])

st.title("Pilot Flight Hours Log")

# Input form for a new flight
with st.form("log_flight_form"):
    # Date input
    date_str = st.text_input("Flight Date (DD/MM/YYYY)", placeholder="e.g., 15/08/2025")
    
    # Flight details
    aircraft_type = st.text_input("Type of Aircraft")
    registration = st.text_input("Registration")
    pilot_in_command = st.text_input("Name of Pilot in Command")
    flight_details = st.text_area("Details of Flight")
    
    # Flight specifics
    hours_flown = st.number_input("Hours Flown", min_value=0.1, max_value=24.0, step=0.1)
    day_night = st.selectbox("Day or Night Flight", ["Day", "Night"])
    engine_type = st.selectbox("Engine Type", ["Single Engine", "Multi Engine"])
    
    submitted = st.form_submit_button("Add Flight")
    
    if submitted:
        from datetime import datetime
        try:
            date_obj = datetime.strptime(date_str, "%d/%m/%Y")
            date_formatted = date_obj.strftime("%Y-%m-%d")  # ISO format
            # Append new log to session state
            new_entry = {
                'Date': date_formatted,
                'Aircraft Type': aircraft_type,
                'Registration': registration,
                'Pilot in Command': pilot_in_command,
                'Flight Details': flight_details,
                'Hours Flown': hours_flown,
                'Day/Night': day_night,
                'Engine Type': engine_type
            }
            st.session_state['flight_logs'] = st.session_state['flight_logs'].append(new_entry, ignore_index=True)
            st.success("Flight logged successfully!")
        except ValueError:
            st.error("Invalid date format. Please use DD/MM/YYYY.")

# Display logged flights
st.header("Logged Flights")
st.dataframe(st.session_state['flight_logs'])
