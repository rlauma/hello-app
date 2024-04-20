import streamlit as st
import pandas as pd

# Read data from the Google Sheets document
google_sheets_url = "https://docs.google.com/spreadsheets/d/1OXzGj1jhVuzCmnRkYV8v8MqisPmKkz2MDIB8vDxeVrc/export?format=xlsx"
df = pd.read_excel(google_sheets_url, sheet_name="data", usecols=[0], engine='openpyxl')

# Display the DataFrame
st.write(df)

# The rest of your code...
