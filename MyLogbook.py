import streamlit as st
import pandas as pd

# Define columns
columns = [
    "Date (Brit format)", "Aircraft Type", "Aircraft Registration", "Pilot In Command",
    "Flight Details", "Navigation Aids Used", "Place of Navigation Aids",
    "Time under Actual IMC", "Time in FST in IMC", "Time as Instructor in Single Engine",
    "Time as Instructor in Multi Engine", "Time in FST as Instructor",
    "Total Time in FST", "Day Dual in Single Engine", "Day PIC in Single Engine",
    "Day PIC under Supervision", "Day Co-pilot in Single Engine", "Night Dual in Single Engine",
    "Night PIC in Single Engine", "Night PIC under Supervision", "Night Co-pilot in Single Engine",
    "Day Dual in Multi Engine", "Day PIC in Multi Engine", "Day PIC under Supervision",
    "Day Co-pilot in Multi Engine", "Night Dual in Multi Engine", "Night PIC in Multi Engine",
    "Night PIC under Supervision", "Night Co-pilot in Multi Engine",
    "Takeoffs and Landings Day", "Takeoffs and Landings Night", "Remarks"
]

# Initialize session state for logs
if 'log_entries' not in st.session_state:
    st.session_state['log_entries'] = []

st.title("Digital Pilot Logbook")

# Form for new entry
with st.form("entry_form"):
    st.header("Add New Flight Log Entry")
    input_data = {}
    col1, col2, col3 = st.columns(3)
    input_data["Date (Brit format)"] = col1.text_input("Date (DD/MM/YYYY)")
    input_data["Aircraft Type"] = col2.text_input("Aircraft Type")
    input_data["Aircraft Registration"] = col3.text_input("Aircraft Registration")
    
    col4, col5 = st.columns(2)
    input_data["Pilot In Command"] = col4.text_input("Pilot In Command")
    input_data["Flight Details"] = col5.text_input("Details of Flight")
    
    input_data["Navigation Aids Used"] = st.text_input("Navigation Aids Used")
    input_data["Place of Navigation Aids"] = st.text_input("Place of Navigation Aids")
    input_data["Time under Actual IMC"] = st.number_input("Time in Actual IMC (hours)", min_value=0.0, step=0.1)
    input_data["Time in FST in IMC"] = st.number_input("Time in FST in IMC (hours)", min_value=0.0, step=0.1)
    input_data["Time as Instructor in Single Engine"] = st.number_input("Time as Instructor in Single Engine (hours)", min_value=0.0, step=0.1)
    input_data["Time as Instructor in Multi Engine"] = st.number_input("Time as Instructor in Multi Engine (hours)", min_value=0.0, step=0.1)
    input_data["Time in FST as Instructor"] = st.number_input("Time in FST as Instructor (hours)", min_value=0.0, step=0.1)
    input_data["Total Time in FST"] = st.number_input("Total Time in FST (hours)", min_value=0.0, step=0.1)
    input_data["Day Dual in Single Engine"] = st.number_input("Day Dual in Single Engine (hours)", min_value=0.0, step=0.1)
    input_data["Day PIC in Single Engine"] = st.number_input("Day PIC in Single Engine (hours)", min_value=0.0, step=0.1)
    input_data["Day PIC under Supervision"] = st.number_input("Day PIC under Supervision (hours)", min_value=0.0, step=0.1)
    input_data["Day Co-pilot in Single Engine"] = st.number_input("Day Co-pilot in Single Engine (hours)", min_value=0.0, step=0.1)
    input_data["Night Dual in Single Engine"] = st.number_input("Night Dual in Single Engine (hours)", min_value=0.0, step=0.1)
    input_data["Night PIC in Single Engine"] = st.number_input("Night PIC in Single Engine (hours)", min_value=0.0, step=0.1)

