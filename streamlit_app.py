import streamlit as st
import pandas as pd

# Create some sample data
st.header("Triviālais nosaukums")
data = {

    'Taukskābes nosaukums': ['palmitīnskābe (16:0)', 'stearīnskābe (18:0)', 'oleīnskābe (18:1n-9)', 'linolēnskābe (18:2n-6)', 'palmitoleīnskābe (16:1n-7)'],
    'Ķīmiskā formula': ['C16H32O2', 'C18H36O2', 'C18H34O2', 'C18H32O2', 'C16H30O2'],

    
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Set 'Taukskābes nosaukums' column as index
df.set_index('Taukskābes nosaukums', inplace=True)

# Display the table without the index column
st.table(df)
