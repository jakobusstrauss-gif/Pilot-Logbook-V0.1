import streamlit as st
from datetime import datetime
import pandas as pd

# Try to load existing data.csv; if not, create empty DataFrame with relevant columns
try:
    df = pd.read_csv('pilot_logbook_master.csv')
except:
    df = pd.DataFrame(columns=[
        'Date', 'Type of Airplane', 'Airplane Registration', 'Pilot In Command',
        'Details of Flight', 'Flight Type', 'Day/Night', 'Role', 'Engine Type',
        'Visual Hours', 'Instrument Hours'
    ])

# Get last entry for pre-filling
last_entry = df.iloc[-1] if not df.empty else {}

st.title("Pilot Logbook Entry with Rules")

# Date
date_input = st.text_input("Date of Flight (DD/MM/YYYY)", value=last_entry.get('Date', ''))
try:
    if date_input:
        date_obj = datetime.strptime(date_input, "%d/%m/%Y")
        date_value = date_obj.strftime('%Y-%m-%d')
    else:
        date_value = ''
except:
    date_value = ''

# Basic info
type_of_airplane = st.text_input("Type of Airplane", value=last_entry.get('Type of Airplane', ''))
registration = st.text_input("Airplane Registration", value=last_entry.get('Airplane Registration', ''))
pilot_in_command = st.text_input("Pilot In Command", value=last_entry.get('Pilot In Command', ''))
details_of_flight = st.text_area("Details of Flight", value=last_entry.get('Details of Flight', ''))

# Flight type: Visual or Instrument
flight_type = st.radio(
    "Visual or Instrument?", 
    ("Visual", "Instrument"), 
    index=0 if last_entry.get('Flight Type') == 'Visual' else 1
)

# Hours Flown input
hours_input = st.text_input("Hours Flown (e.g., 12.34)", value=str(last_entry.get('Hours Flown', '')))
try:
    input_hours = float(hours_input)
    hours_formatted = f"{input_hours:.2f}"
except:
    input_hours = 0.0
    hours_formatted = "0.00"

# Logic for hours depending on flight type
visual_hours = 0.0
instrument_hours_total = 0.0

# Load existing data to calculate total instrument hours
if 'Instrument Hours' in df.columns:
    instrument_hours_total = sum(df['Instrument Hours'].dropna().astype(float))

if st.button("Save Entry"):
    # Save hours in appropriate column(s)
    new_row = {
        'Date': date_value,
        'Type of Airplane': type_of_airplane,
        'Airplane Registration': registration,
        'Pilot In Command': pilot_in_command,
        'Details of Flight': details_of_flight,
        'Flight Type': flight_type,
        'Day/Night': 'Day',  # Placeholder for later
        'Role': '',          # Placeholder for later
        'Engine Type': '',   # Placeholder for later
        'Visual Hours': None,
        'Instrument Hours': None
    }
    # Assign hours based on selection
    if flight_type == 'Visual':
        new_row['Visual Hours'] = hours_formatted
        new_row['Instrument Hours'] = None
    else:
        # Add to total instrument hours
        instrument_hours_total += input_hours
        new_row['Visual Hours'] = None
        new_row['Instrument Hours'] = f"{instrument_hours_total:.2f}"

    # Append to existing CSV
    try:
        existing_df = pd.read_csv('pilot_logbook_master.csv')
        existing_df = existing_df.append(new_row, ignore_index=True)
        existing_df.to_csv('pilot_logbook_master.csv', index=False)
    except:
        pd.DataFrame([new_row]).to_csv('pilot_logbook_master.csv', index=False)
    st.success("Entry saved successfully!")
