import streamlit as st

# Set the text color to black
st.markdown('<style>div.stMarkdown { color: black }</style>', unsafe_allow_html=True)

# Display some text
import pandas as pd

# Create some sample data
st.header("Triviālais nosaukums")

# Display some text

data = { 
    'Taukskābes nosaukums': ['palmitīnskābe (16:0)', 'stearīnskābe (18:0)', 'oleīnskābe (18:1n-9)', 'linolēnskābe (18:2n-6)', 'palmitoleīnskābe (16:1n-7)'],
    'Ķīmiskā formula': ['C16H32O2', 'C18H36O2', 'C18H34O2', 'C18H32O2', 'C16H30O2'],
    'Oglekļu atomu skaits': ['16', '18', '18', '18', '16'],
    'Dubultsaite': ['16', '18', '1', '2', '1'],
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Set the CSS style for the table to make text color black
table_style = """
    <style>
    .dataframe tbody tr th {
        color: black;
    }
    .dataframe tbody tr td {
        color: black;
    }
    </style>
"""
st.write(table_style, unsafe_allow_html=True)

# Display the table
st.table(df)
