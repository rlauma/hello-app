import streamlit as st
import pandas as pd





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
