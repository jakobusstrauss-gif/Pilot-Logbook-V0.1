import streamlit as st
from datetime import datetime

# Initialize session state for data
if 'flight_data' not in st.session_state:
    st.session_state['flight_data'] = {}
if 'step' not in st.session_state:
    st.session_state['step'] = 6  # Set to step 6 for this example

st.title("Edit Flight Details (Step 6)")

# Helper function to get existing data
def get_value(key):
    return st.session_state['flight_data'].get(key, '')

# Editable fields - all data pre-filled
# 1. Date of Flight
date_input = st.text_input(
    "Date of Flight (DD/MM/YYYY)", 
    value=get_value('Date', '')
)
try:
    if date_input:
        date_obj = datetime.strptime(date_input, "%d/%m/%Y")
        st.session_state['flight_data']['Date'] = date_obj.strftime('%Y-%m-%d')
except:
    pass  # invalid date input

# 2. Type of Airplane
st.text_input(
    "Type of Airplane", 
    value=get_value('Type of Airplane')
)
st.session_state['flight_data']['Type of Airplane'] = st.experimental_get_query_params().get('Type of Airplane', get_value('Type of Airplane'))

# 3. Airplane Registration
st.text_input(
    "Airplane Registration", 
    value=get_value('Airplane Registration')
)
st.session_state['flight_data']['Airplane Registration'] = st.experimental_get_query_params().get('Airplane Registration', get_value('Airplane Registration'))

# 4. Pilot In Command
st.text_input(
    "Pilot In Command", 
    value=get_value('Pilot In Command')
)
st.session_state['flight_data']['Pilot In Command'] = st.experimental_get_query_params().get('Pilot In Command', get_value('Pilot In Command'))

# 5. Details of Flight
details = st.text_area(
    "Details of Flight", 
    value=get_value('Details of Flight')
)
st.session_state['flight_data']['Details of Flight'] = details

# 6. Visual or Instrument?
flight_type = st.radio("Type of Flight", ("Visual", "Instrument"), index=0 if get_value('Flight Type') == 'Visual' else 1)
st.session_state['flight_data']['Flight Type'] = flight_type

# The user can edit these fields freely, and data is updated as they type.
# Proceed to next step via other interface or button outside this snippet.
