pip install openpyxl
import streamlit as st
import pandas as pd

# Title for the app
st.title('Excel File Uploader')

# File uploader widget
file = st.file_uploader('Upload Excel file', type=['xls', 'xlsx'])

# If a file is uploaded
if file is not None:
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file)
    
    # Display the DataFrame
    st.write(df)
