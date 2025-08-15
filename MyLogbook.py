import streamlit as st
from datetime import datetime

# Page title
st.title("Digital Pilot Logbook - New Flight Entry")

# Step 1: Input - Date of Flight in British format
date_input = st.text_input("Enter Date of Flight (DD/MM/YYYY)")

# Button to proceed after entering date
if st.button("Next") and date_input:
    # Validate date format
    try:
        date_obj = datetime.strptime(date_input, "%d/%m/%Y")
        # Display confirmation
        st.success(f"Date entered: {date_obj.strftime('%Y-%m-%d')}")
        # Store the date in session state for further use
        st.session_state['flight_date'] = date_obj.strftime('%Y-%m-%d')
        # Proceed to next step or input fields...
        
        # For now, just show next input prompt
        # (Further implementation will be added in subsequent steps)
    except ValueError:
        st.error("Invalid date format. Please enter as DD/MM/YYYY.")
else:
    # Wait for correct date input
    if date_input:
        # If input is not valid, show error
        try:
            datetime.strptime(date_input, "%d/%m/%Y")
        except ValueError:
            st.error("Invalid date format. Please enter as DD/MM/YYYY.")
