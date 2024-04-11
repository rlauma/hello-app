import streamlit as st
import pandas as pd

# Create some sample data
st.header("Triviālais nosaukums")
data = {
    'Taukskābes nosaukums': ['Taukskābes nosaukums', 'Ķīmiskā formula', 'Oglekļu atomu skaits', 'Ķēžu garums'],
    'Ķīmiskā formula': [25, 30, 35, 30],
    'Oglekļu atomu skaits': ['New York', 'London', 'Tokyo', 'Tokyo']
    
}
    
# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Remove the row indices from the DataFrame
df_display = df.copy()
df_display.index = [''] * len(df)  # Replace row indices with empty strings

# Display the table without row indices
st.table(df_display)
