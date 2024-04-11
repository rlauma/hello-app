import streamlit as st
import pandas as pd

# Create some sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Location': ['New York', 'London', 'Tokyo']
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Display the table
st.table(df)
