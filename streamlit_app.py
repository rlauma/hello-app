import streamlit as st
import pandas as pd

# Create some sample data
st.header("Triviālais nosaukums")
data = {
    'Taukskābes nosaukums': ['Taukskābes nosaukums', 'Ķīmiskā formula', 'Oglekļu atomu skaits', 'Ķēžu garums', 'Ķēžu garums'],
    'Ķīmiskā formula': [25, 30, 35, 30, 30],
    'Oglekļu atomu skaits': ['New York', 'London', 'Tokyo', 'Tokyo', 'Tokyo'],
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Set 'Taukskābes nosaukums' column as index
df.set_index('Taukskābes nosaukums', inplace=True)

# Display the table without the index column
st.table(df)
