import streamlit as st
import pandas as pd
import streamlit as st

# Create some sample data
st.header("Triviālais nosaukums")
data = { 
    'Taukskābes nosaukums': ['palmitīnskābe (16:0)', 'stearīnskābe (18:0)', 'oleīnskābe (18:1n-9)', 'linolēnskābe (18:2n-6)', 'palmitoleīnskābe (16:1n-7)'],
    'Ķīmiskā formula': ['C16H32O2', 'C18H36O2', 'C18H34O2', 'C18H32O2', 'C16H30O2'],
    'Oglekļu atomu skaits': ['16', '18', '18', '18', '16'],
    'Dubultsaišu skaits': ['', '', '1', '2', '1'],
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Display headers and radio button
st.header("Dzīvnieku katalogs")
st.header("Vispārīgie dati")
animal = st.radio("Dzīvnieku nosaukums", ("Brūnais lācis", "Ziemeļu sikspārnis", "Eirāzijas āpsis"))
button3 = st.button("Apstiprināt")

# Display animal information when button is clicked
if button3:
    if animal == "Brūnais lācis":
        st.write("Ursus arctos")
    elif animal == "Ziemeļu sikspārnis":
        st.write("Eptesicus nilssoni")
    elif animal == "Eirāzijas āpsis":
        st.write("APSIS")

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
