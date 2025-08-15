import streamlit as st
from datetime import datetime
import pandas as pd

# Initialize or load the master dataset
try:
    df_master = pd.read_csv('pilot_logbook_master.csv')
except FileNotFoundError:
    df_master = pd.DataFrame()

st.title("Digital Pilot Logbook - New Entry (Editable)")

# Initialize a dict to hold current data
current_data = {}

# Input fields for all data with existing data pre-filled
date_input = st.text_input(
    "Date of Flight (DD/MM/YYYY)", 
    value=current_data.get('Date', '')
)
try:
    # If a date is entered, validate and store in standard format
    if date_input:
        date_obj = datetime.strptime(date_input, "%d/%m/%Y")
        current_data['Date'] = date_obj.strftime('%Y-%m-%d')
except:
    pass  # If invalid, keep the string as entered

# Type of Airplane
current_data['Type of Airplane'] = st.text_input(
    "Type of Airplane", value=current_data.get('Type of Airplane', '')
)

# Airplane Registration
current_data['Airplane Registration'] = st.text_input(
    "Airplane Registration", value=current_data.get('Airplane Registration', '')
)

# Pilot In Command
current_data['Pilot In Command'] = st.text_input(
    "Pilot In Command", value=current_data.get('Pilot In Command', '')
)

# Details of Flight
current_data['Details of Flight'] = st.text_area(
    "Details of Flight", value=current_data.get('Details of Flight', '')
)

# Visual or Instrument
current_data['Flight Type'] = st.radio(
    "Visual or Instrument?", 
    ("Visual", "Instrument"), 
    index=0 if current_data.get('Flight Type', '') == 'Visual' else 1
)

# Now, display all other fields, for example:
# Instrument Flight Time
current_data['Navaid Type'] = st.text_input(
    "Type of Navaid", value=current_data.get('Navaid Type', '')
)
current_data['Navaid Place'] = st.text_input(
    "Place of Navaid", value=current_data.get('Navaid Place', '')
)
current_data['Actual IMC Hours'] = st.number_input(
    "Hours flown under actual IMC", value=float(current_data.get('Actual IMC Hours', 0.0)), format="%.2f"
)
current_data['Simulator Hours'] = st.number_input(
    "Hours flown in Simulator", value=float(current_data.get('Simulator Hours', 0.0)), format="%.2f"
)
current_data['Total Simulator Hours'] = st.number_input(
    "Total hours flown in simulator", value=float(current_data.get('Total Simulator Hours', 0.0)), format="%.2f"
)

# Hours flown in Single Engine
current_data['SE Day/Night'] = st.radio(
    "Single Engine - Day or Night?", ("Day", "Night"), index=0 if current_data.get('SE Day/Night', '') == 'Day' else 1
)
current_data['SE Type'] = st.selectbox(
    "Single Engine Type", ("Dual", "PIC", "PICUS", "Co-Pilot"), 
    index=0 if current_data.get('SE Type', '') == 'Dual' else 1
)
current_data['SE Hours'] = st.number_input(
    "Hours flown in Single Engine", value=float(current_data.get('SE Hours', 0.0)), format="%.2f"
)

# Hours flown in Multi Engine
current_data['ME Day/Night'] = st.radio(
    "Multi Engine - Day or Night?", ("Day", "Night"), index=0 if current_data.get('ME Day/Night', '') == 'Day' else 1
)
current_data['ME Type'] = st.selectbox(
    "Multi Engine Type", ("Dual", "PIC", "PICUS", "Co-Pilot"), 
    index=0 if current_data.get('ME Type', '') == 'Dual' else 1
)
current_data['ME Hours'] = st.number_input(
    "Hours flown in Multi Engine", value=float(current_data.get('ME Hours', 0.0)), format="%.2f"
)

# Takeoffs and Landings
current_data['Takeoff/Night'] = st.radio(
    "Takeoffs/Night?", ("Day", "Night"), index=0 if current_data.get('Takeoff/Night', '') == 'Day' else 1
)
current_data['Takeoffs'] = st.number_input(
    "Number of Takeoffs", value=int
