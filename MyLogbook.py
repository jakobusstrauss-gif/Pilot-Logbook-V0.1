import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize session state for flight logs
if 'flight_logs' not in st.session_state:
    st.session_state['flight_logs'] = pd.DataFrame(columns=[
        'Date', 'Aircraft Type', 'Registration', 'Pilot in Command', 'Role', 'Flight Details',
        'Hours Flown', 'Actual Instrument Time', 'Simulator Time', 'Day/Night', 'Takeoffs and Landings', 'Engine Type'
    ])

st.title("Pilot Flight Hours Log")

# Set default values for input fields
default_date = datetime.now().strftime("%d/%m/%Y")
default_hours = 1.0
default_takeoffs = 1

# Input form for a new flight
with st.form("log_flight_form"):
    date_str = st.text_input("Flight Date (DD/MM/YYYY)", value=default_date)
    aircraft_type = st.text_input("Type of Aircraft")
    registration = st.text_input("Registration")
    pilot_in_command = st.text_input("Name of Pilot in Command")
    role = st.selectbox("Role of Pilot", ["Dual", "PIC", "PICUS", "Co-Pilot", "Instructor"])
    flight_details = st.text_area("Details of Flight")
    hours_flown = st.number_input("Total Hours Flown", min_value=0.1, max_value=24.0, step=0.1, value=default_hours)
    actual_instrument_time = st.number_input("Actual Instrument Flight Time (hours)", min_value=0.0, max_value=24.0, step=0.1)
    simulator_time = st.number_input("Simulator Flight Time (hours)", min_value=0.0, max_value=24.0, step=0.1)
    day_night = st.selectbox("Day or Night Flight", ["Day", "Night"])
    takeoffs_landings = st.number_input("Takeoffs and Landings", min_value=0, max_value=20, value=default_takeoffs)
    engine_type = st.selectbox("Engine Type", ["Single Engine", "Multi Engine"])
    submitted = st.form_submit_button("Add Flight")

    if submitted:
        try:
            date_obj = datetime.strptime(date_str, "%d/%m/%Y")
            date_formatted = date_obj.strftime("%Y-%m-%d")
            new_entry = {
                'Date': date_formatted,
                'Aircraft Type': aircraft_type,
                'Registration': registration,
                'Pilot in Command': pilot_in_command,
                'Role': role,
                'Flight Details': flight_details,
                'Hours Flown': hours_flown,
                'Actual Instrument Time': actual_instrument_time,
                'Simulator Time': simulator_time,
                'Day/Night': day_night,
                'Takeoffs and Landings': takeoffs_landings,
                'Engine Type': engine_type
            }
            # Append to the DataFrame
            new_row = pd.DataFrame([new_entry])
            st.session_state['flight_logs'] = pd.concat([st.session_state['flight_logs'], new_row], ignore_index=True)
            st.success("Flight logged successfully!")
        except ValueError:
            st.error("Invalid date format. Please use DD/MM/YYYY.")

# Reset input fields after submission is handled (handled automatically in Streamlit)

# Display logged flights
st.header("Logged Flights")
st.dataframe(st.session_state['flight_logs'])
