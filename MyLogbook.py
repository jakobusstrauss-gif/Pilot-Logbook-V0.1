import streamlit as st
from datetime import datetime
import pandas as pd

# Load existing data or create new DataFrame
try:
    df = pd.read_csv('pilot_logbook_master.csv')
except:
    df = pd.DataFrame(columns=[
        'Date', 'Type of Airplane', 'Airplane Registration', 'Pilot In Command',
        'Details of Flight', 'Day', 'Night', 'Role', 'Engine Type'
    ])

# Use last entry for pre-fill
last_entry = df.iloc[-1] if not df.empty else {}

st.title("Pilot Logbook Entry with Day/Night Hours Rule (Editable)")

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

# 1. Day or Night
day_night_selection = st.radio(
    "Day or Night?", 
    ("Day", "Night"), 
    index=0 if last_entry.get('Day') == 'Yes' else 1
)

# 2. Hours Flown (single input, saved into Day or Night column depending on selection)
hours_input = st.text_input(
    "Hours Flown (e.g., 12.34)",
    value=str(last_entry.get('Hours Flown', ''))
)
try:
    hours_value = float(hours_input)
    hours_formatted = f"{hours_value:.2f}"
except:
    hours_value = 0.0
    hours_formatted = "0.00"

# Save button
if st.button("Save Entry"):
    # Initialize row with previous data or empty
    new_record = {
        'Date': date_value,
        'Type of Airplane': type_of_airplane,
        'Airplane Registration': registration,
        'Pilot In Command': pilot_in_command,
        'Details of Flight': details_of_flight,
        'Role': '',  # Placeholder
        'Engine Type': ''  # Placeholder
        # 'Day' and 'Night' columns to be filled below
    }

    # Prepare Day/Night
    if day_night_selection == 'Day':
        new_record['Day'] = hours_formatted
        new_record['Night'] = ''
    else:
        new_record['Day'] = ''
        new_record['Night'] = hours_formatted

    # Read existing CSV and append new record
    try:
        df_existing = pd.read_csv('pilot_logbook_master.csv')
        df_existing = df_existing.append(new_record, ignore_index=True)
        df_existing.to_csv('pilot_logbook_master.csv', index=False)
    except:
        pd.DataFrame([new_record]).to_csv('pilot_logbook_master.csv', index=False)
    st.success("Entry saved successfully!")
