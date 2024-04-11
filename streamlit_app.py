import streamlit as st
import pandas as pd

# Create some sample data
data = {
    'Triviālais nosaukums': ['Taukskābes nosaukums', 'Ķīmiskā formula', 'Oglekļu atomu skaits', 'Ķēžu garums'],
    'Age': [25, 30, 35, 30],
    'Location': ['New York', 'London', 'Tokyo', 'Tokyo']
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Display the table
st.table(df)
