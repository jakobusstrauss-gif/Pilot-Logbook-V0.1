import streamlit as st
from datetime import datetime
import pandas as pd

# Load existing data
try:
    df = pd.read_csv('pilot_logbook_master.csv')
    last_entry = df.iloc[-1].to_dict()
except:
    last_entry = {}

st.title("Pilot Logbook Entry (Editable)")

# Date of Flight
date_input = st.text_input(
    "Date of Flight (DD/MM/YYYY)", 
    value=last_entry.get('Date', '')
)
try:
    if date_input:
        date_obj = datetime.strptime(date_input, "%d/%m/%Y")
        date_value = date_obj.strftime('%Y-%m-%d')
    else:
        date_value = ''
except:
    date_value = ''

# Type of Airplane
type_of_airplane = st.text_input(
    "Type of Airplane", 
    value=last_entry.get('Type of Airplane', '')
)

# Airplane Registration
registration = st.text_input(
    "Airplane Registration", 
    value=last_entry.get('Airplane Registration', '')
)

# Pilot In Command
pilot_in_command = st.text_input(
    "Pilot In Command", 
    value=last_entry.get('Pilot In Command', '')
)

# Details of Flight
details_of_flight = st.text_area(
    "Details of Flight", 
    value=last_entry.get('Details of Flight', '')
)

# 1. Visual or Instrument?
flight_type = st.radio(
    "Visual or Instrument?", 
    ("Visual", "Instrument"), 
    index=0 if last_entry.get('Flight Type') == 'Visual' else 1
)

# 2. Day or Night?
day_night = st.radio(
    "Day or Night?", 
    ("Day", "Night"), 
    index=0 if last_entry.get('Day/Night') == 'Day' else 1
)

# 3. Dual, PIC, PICUS, Co-Pilot
pilot_role = st.radio(
    "Flight Role:", 
    ("Dual", "PIC", "PICUS", "Co-Pilot"), 
    index=0 if last_entry.get('Role') == 'Dual' else 1
)

# 4. Single Engine or Multi Engine?
engine_type = st.radio(
    "Aircraft Type:", 
    ("Single Engine", "Multi Engine"),
    index=0 if last_entry.get('Engine Type') == 'Single Engine' else 1
)

# 5. Hours Flown (with two decimals)
hours_flown = st.text_input(
    "Hours Flown (e.g., 12.34)", 
    value=str(last_entry.get('Hours Flown', ''))
)

# Save data
if st.button("Save Entry"):
    # Validate hours input
    try:
        hours_float = float(hours_flown)
        hours_str = f"{hours_float:.2f}"
    except:
        hours_str = ""

    new_entry = {
        'Date': date_value,
        'Type of Airplane': type_of_airplane,
        'Airplane Registration': registration,
        'Pilot In Command': pilot_in_command,
        'Details of Flight': details_of_flight,
        'Flight Type': flight_type,
        'Day/Night': day_night,
        'Role': pilot_role,
        'Engine Type': engine_type,
        'Hours Flown': hours_str
    }
    try:
        df_existing = pd.read_csv('pilot_logbook_master.csv')
        df_existing = df_existing.append(new_entry, ignore_index=True)
        df_existing.to_csv('pilot_logbook_master.csv', index=False)
    except:
        pd.DataFrame([new_entry]).to_csv('pilot_logbook_master.csv', index=False)
    st.success("Entry saved successfully!")
