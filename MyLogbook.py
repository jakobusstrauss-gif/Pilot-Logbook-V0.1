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

# Function to display the editing interface
def edit_flight(index):
    df = st.session_state['flight_logs']
    record = df.iloc[index]

    with st.form("edit_form"):
        date_str = st.text_input("Flight Date (DD/MM/YYYY)", value=datetime.strptime(record['Date'], "%Y-%m-%d").strftime("%d/%m/%Y"))
        aircraft_type = st.text_input("Type of Aircraft", value=record['Aircraft Type'])
        registration = st.text_input("Registration", value=record['Registration'])
        pilot_in_command = st.text_input("Name of Pilot in Command", value=record['Pilot in Command'])
        role = st.selectbox("Role of Pilot", ["Dual", "PIC", "PICUS", "Co-Pilot", "Instructor"], index=["Dual", "PIC", "PICUS", "Co-Pilot", "Instructor"].index(record['Role']))
        flight_details = st.text_area("Details of Flight", value=record['Flight Details'])
        hours_flown = st.number_input("Total Hours Flown", min_value=0.1, max_value=24.0, step=0.1, value=record['Hours Flown'])
        actual_instrument_time = st.number_input("Actual Instrument Flight Time (hours)", min_value=0.0, max_value=24.0, step=0.1, value=record['Actual Instrument Time'])
        simulator_time = st.number_input("Simulator Flight Time (hours)", min_value=0.0, max_value=24.0, step=0.1, value=record['Simulator Time'])
        day_night = st.selectbox("Day or Night Flight", ["Day", "Night"], index=["Day", "Night"].index(record['Day/Night']))
        takeoffs_landings = st.number_input("Takeoffs and Landings", min_value=0, max_value=20, value=record['Takeoffs and Landings'])
        engine_type = st.selectbox("Engine Type", ["Single Engine", "Multi Engine"], index=["Single Engine", "Multi Engine"].index(record['Engine Type']))
        
        if st.form_submit_button("Save Changes"):
            try:
                date_obj = datetime.strptime(date_str, "%d/%m/%Y")
                date_formatted = date_obj.strftime("%Y-%m-%d")
                # Update the record
                st.session_state['flight_logs'].iloc[index] = {
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
                st.success("Record updated!")
            except ValueError:
                st.error("Invalid date format. Please use DD/MM/YYYY.")

# List all flights with an edit button
st.header("Existing Flights")
for idx, row in st.session_state['flight_logs'].iterrows():
    col1, col2, col3 = st.columns([0.9, 0.05, 0.05])
    with col1:
        st.write(f"{row['Date']} - {row['Aircraft Type']} ({row['Registration']})")
    with col2:
        if st.button("Edit", key=f"edit_{idx}"):
            edit_flight(idx)

# Show the current flight logs
st.header("All Logged Flights")
st.dataframe(st.session_state['flight_logs'])
