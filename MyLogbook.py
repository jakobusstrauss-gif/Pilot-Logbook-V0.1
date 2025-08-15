import streamlit as st
import pandas as pd
from datetime import datetime

# Load existing master sheet or create a new one
try:
    df_master = pd.read_csv('pilot_logbook_master.csv')
except FileNotFoundError:
    df_master = pd.DataFrame()

st.title("Digital Pilot Logbook")

# Function to round hours to 2 decimal places
def round_hours(hours):
    return round(hours, 2)

# Define the form for new flight entry
with st.form("flight_log_form"):
    st.header("Enter Flight Details")
    
    # 1. Date of flight (British format dd/mm/yyyy)
    flight_date = st.text_input("Date of Flight (DD/MM/YYYY)")
    
    # 2. Type of Airplane
    aircraft_type = st.text_input("Type of Airplane")
    
    # 3. Airplane Registration
    registration = st.text_input("Airplane Registration")
    
    # 4. Pilot In Command Name
    pilot_name = st.text_input("Pilot In Command Name")
    
    # 5. Details of Flight
    flight_details = st.text_area("Details of Flight")
    
    # 6. Instrument Flight Time Section
    st.subheader("Instrument Flight Time")
    navaid_type = st.text_input("Type of Navaid")
    navaid_place = st.text_input("Place of Navaid")
    actual_imc_hours = st.number_input("Hours flown under actual IMC", min_value=0.0, format="%.2f")
    simulator_hours = st.number_input("Hours flown in Simulator", min_value=0.0, format="%.2f")
    
    # 7. Total hours flown in simulator
    total_sim_hours = st.number_input("Total hours flown in simulator (for this flight)", min_value=0.0, format="%.2f")
    
    # 8. Hours in Single Engine Aircraft
    st.subheader("Single Engine Aircraft")
    se_day_night = st.radio("Day or Night", ("Day", "Night"))
    se_type = st.radio("Type", ("Dual", "PIC", "PICUS", "Co-Pilot"))
    se_hours = st.number_input("Hours flown in Single Engine", min_value=0.0, format="%.2f")
    
    # 9. Hours in Multi Engine Aircraft
    st.subheader("Multi Engine Aircraft")
    me_day_night = st.radio("Day or Night", ("Day", "Night"))
    me_type = st.radio("Type", ("Dual", "PIC", "PICUS", "Co-Pilot"))
    me_hours = st.number_input("Hours flown in Multi Engine", min_value=0.0, format="%.2f")
    
    # 10. Takeoffs and Landings
    st.subheader("Takeoffs and Landings")
    takeoff_type = st.radio("Type of Takeoff/Landing", ("Day", "Night"))
    takeoffs = st.number_input("Number of Takeoffs", min_value=0, step=1)
    landings = st.number_input("Number of Landings", min_value=0, step=1)
    
    # 11. Remarks
    remarks = st.text_area("Remarks")
    
    # Submit button
    submitted = st.form_submit_button("Submit Entry")
    
    if submitted:
        # Validate date
        try:
            date_obj = datetime.strptime(flight_date, "%d/%m/%Y")
            date_str = date_obj.strftime("%Y-%m-%d")
        except:
            st.error("Invalid date format. Please enter as DD/MM/YYYY.")
            st.stop()
        
        # Create record dictionary
        record = {
            "Date": date_str,
            "Type of Airplane": aircraft_type,
            "Registration": registration,
            "Pilot Name": pilot_name,
            "Flight Details": flight_details,
            "Navaid Type": navaid_type,
            "Navaid Place": navaid_place,
            "Actual IMC Hours": round_hours(actual_imc_hours),
            "Simulator Hours": round_hours(simulator_hours),
            "Total Simulator Hours": round_hours(total_sim_hours),
            "SE Day/Night": se_day_night,
            "SE Type": se_type,
            "SE Hours": round_hours(se_hours),
            "ME Day/Night": me_day_night,
            "ME Type": me_type,
            "ME Hours": round_hours(me_hours),
            "Takeoff/Night": takeoff_type,
            "Takeoffs": takeoffs,
            "Landings": landings,
            "Remarks": remarks
        }
        
        # Append the new record to the master DataFrame
        df_master = df_master.append(record, ignore_index=True)
        
        # Save to CSV file
        df_master.to_csv('pilot_logbook_master.csv', index
