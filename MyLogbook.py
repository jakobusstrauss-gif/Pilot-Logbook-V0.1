import streamlit as st
from datetime import datetime
import pandas as pd

# Load existing data or create new DataFrame with columns for role hours
try:
    df = pd.read_csv('pilot_logbook_master.csv')
except:
    df = pd.DataFrame(columns=[
        'Date', 'Type of Airplane', 'Airplane Registration', 'Pilot In Command',
        'Details of Flight', 'Day', 'Night', 'Dual', 'PIC', 'PICUS', 'Co-Pilot'
    ])

# Use last entry to pre-fill
last_entry = df.iloc[-1] if not df.empty else {}

st.title("Pilot Logbook Entry with Role-specific Hours (Editable)")

# Date
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
day_night = st.radio(
    "Day or Night?", 
    ("Day", "Night"), 
    index=0 if last_entry.get('Day') == 'Day' else 1
)

# 2. Role: Dual, PIC, PICUS, Co-Pilot
role = st.radio(
    "Role:", 
    ("Dual", "PIC", "PICUS", "Co-Pilot"), 
    index=0 if last_entry.get('Role') == 'Dual' else 1
)

# 3. Hours Flown (single input for the role)
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
    # Initialize record with all columns
    new_record = {
        'Date': date_value,
        'Type of Airplane': type_of_airplane,
        'Airplane Registration': registration,
        'Pilot In Command': pilot_in_command,
        'Details of Flight': details_of_flight,
        'Day': '',      # will be populated based on selection
        'Night': '',    # will be populated based on selection
        'Dual': '',
        'PIC': '',
        'PICUS': '',
        'Co-Pilot': ''
    }

    # Assign hours into Day or Night depending on selection
    if day_night == 'Day':
        new_record['Day'] = hours_formatted
        new_record['Night'] = ''
    else:
        new_record['Day'] = ''
        new_record['Night'] = hours_formatted

    # Assign hours into specific role column
    role_columns = ['Dual', 'PIC', 'PICUS', 'Co-Pilot']
    for col in role_columns:
        if col == role:
            new_record[col] = hours_formatted
        else:
            new_record[col] = ''

    # Append to existing CSV
    try:
        df_existing = pd.read_csv('pilot_logbook_master.csv')
        df_existing = df_existing.append(new_record, ignore_index=True)
        df_existing.to_csv('pilot_logbook_master.csv', index=False)
    except:
        pd.DataFrame([new_record]).to_csv('pilot_logbook_master.csv', index=False)

    st.success("Entry saved successfully!")
