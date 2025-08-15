import streamlit as st
import pandas as pd
import uuid
from datetime import datetime

# Define columns for the logbook
columns = [
    "Date", "Type", "Reg", "PIC", "Details of Flight", "Nav Aids", "Place",
    "Actual Time", "FSTD Time", "SE", "ME", "FSTD", "FSTD Actual Time",
    "Day Dual", "PIC (SE Day)", "PICUS (SE Day)", "Co-Pilot (SE Day)",
    "Night Dual (SE)", "PIC (SE Night)", "PICUS (SE Night)", "Co-Pilot (SE Night)",
    "Day Dual (ME)", "PIC (ME Day)", "PICUS (ME Day)", "Co-Pilot (ME Day)",
    "Night Dual (ME)", "PIC (ME Night)", "PICUS (ME Night)", "Co-Pilot (ME Night)",
    "Day", "Night", "Remarks"
]

# Initialize session state for log entries
if 'log_entries' not in st.session_state:
    st.session_state['log_entries'] = []

st.title("Digital Pilot Logbook")

# Helper function to convert DD-MM-YYYY to YYYY-MM-DD
def convert_date_format(date_str):
    try:
        return datetime.strptime(date_str, '%d-%m-%Y').strftime('%Y-%m-%d')
    except ValueError:
        return date_str  # Return original string if format doesn't match

# Input form for new log entry
with st.form("entry_form"):
    st.header("Add New Flight Log Entry")
    input_data = {}

    col1, col2, col3 = st.columns(3)
    input_data["Date"] = col1.text_input("Date (DD-MM-YYYY)")
    input_data["Type"] = col2.text_input("Aircraft Type")
    input_data["Reg"] = col3.text_input("Aircraft Registration")
    
    col4, col5 = st.columns(2)
    input_data["PIC"] = col4.text_input("Pilot In Command")
    input_data["Details of Flight"] = col5.text_input("Details of Flight")
    
    input_data["Nav Aids"] = st.text_input("Navigation Aids Used")
    input_data["Place"] = st.text_input("Place of Navigation Aids")
    
    col6, col7 = st.columns(2)
    input_data["Actual Time"] = col6.number_input("Actual Time", min_value=0.0, step=0.01)
    input_data["FSTD Time"] = col7.number_input("FSTD Time", min_value=0.0, step=0.01)
    
    col8, col9, col10 = st.columns(3)
    input_data["SE"] = col8.number_input("SE", min_value=0.0, step=0.01)
    input_data["ME"] = col9.number_input("ME", min_value=0.0, step=0.01)
    input_data["FSTD"] = col10.number_input("FSTD", min_value=0.0, step=0.01)
    
    input_data["FSTD Actual Time"] = st.number_input("FSTD Actual Time", min_value=0.0, step=0.01)
    
    col11, col12, col13 = st.columns(3)
    input_data["Day Dual"] = col11.number_input("Day Dual", min_value=0.0, step=0.01)
    input_data["PIC (SE Day)"] = col12.number_input("PIC (SE Day)", min_value=0.0, step=0.01)
    input_data["PICUS (SE Day)"] = col13.number_input("PICUS (SE Day)", min_value=0.0, step=0.01)
    
    col14, col15, col16 = st.columns(3)
    input_data["Co-Pilot (SE Day)"] = col14.number_input("Co-Pilot (SE Day)", min_value=0.0, step=0.01)
    input_data["Night Dual (SE)"] = col15.number_input("Night Dual (SE)", min_value=0.0, step=0.01)
    input_data["PIC (SE Night)"] = col16.number_input("PIC (SE Night)", min_value=0.0, step=0.01)
    
    col17, col18, col19 = st.columns(3)
    input_data["PICUS (SE Night)"] = col17.number_input("PICUS (SE Night)", min_value=0.0, step=0.01)
    input_data["Co-Pilot (SE Night)"] = col18.number_input("Co-Pilot (SE Night)", min_value=0.0, step=0.01)
    input_data["Day Dual (ME)"] = col19.number_input("Day Dual (ME)", min_value=0.0, step=0.01)
    
    col20, col21, col22 = st.columns(3)
    input_data["PIC (ME Day)"] = col20.number_input("PIC (ME Day)", min_value=0.0, step=0.01)
    input_data["PICUS (ME Day)"] = col21.number_input("PICUS (ME Day)", min_value=0.0, step=0.01)
    input_data["Co-Pilot (ME Day)"] = col22.number_input("Co-Pilot (ME Day)", min_value=0.0, step=0.01)
    
    col23, col24, col25 = st.columns(3)
    input_data["Night Dual (ME)"] = col23.number_input("Night Dual (ME)", min_value=0.0, step=0.01)
    input_data["PIC (ME Night)"] = col24.number_input("PIC (ME Night)", min_value=0.0, step=0.01)
    input_data["PICUS (ME Night)"] = col25.number_input("PICUS (ME Night)", min_value=0.0, step=0.01)
    
    col26, col27 = st.columns(2)
    input_data["Co-Pilot (ME Night)"] = col26.number_input("Co-Pilot (ME Night)", min_value=0.0, step=0.01)
    input_data["Day"] = col27.number_input("Takeoffs and Landings Day", min_value=0, step=1)

    col28, col29 = st.columns(2)
    input_data["Night"] = col28.number_input("Takeoffs and Landings Night", min_value=0, step=1)
    input_data["Remarks"] = col29.text_input("Remarks")

    # Submit button
    submitted = st.form_submit_button("Add Entry")
    if submitted:
        # Convert date format
        input_data["Date"] = convert_date_format(input_data["Date"])
        # Append the input data to the session state list
        st.session_state['log_entries'].append(input_data)
        st.success("Entry added successfully!")

# Display all entries in a table
if st.session_state['log_entries']:
    df_entries = pd.DataFrame(st.session_state['log_entries'])

    # Display the table
    st.dataframe(df_entries)

    # Add an export button to download the data as CSV
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(df_entries)

    st.download_button(
        label="Download logbook as CSV",
        data=csv,
        file_name='pilot_logbook.csv',
        mime='text/csv',
    )




