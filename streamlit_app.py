import streamlit as st
import pandas as pd

# Create some sample data
st.header("Triviālais nosaukums")
data = { 
    'Taukskābes nosaukums': ['palmitīnskābe (16:0)', 'stearīnskābe (18:0)', 'oleīnskābe (18:1n-9)', 'linolēnskābe (18:2n-6)', 'palmitoleīnskābe (16:1n-7)'],
    'Ķīmiskā formula': ['C₁₆H₃₂O₂', 'C₁₈H₃₆O₂', 'C₁₈H₃₄O₂', 'C₁₈H₃₂O₂', 'C₁₆H₃₀O₂'],
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

    # Display image from URL with caption
    st.image("https://rigazoo.lv/wp-content/uploads/2023/05/apsis-3.jpeg", caption="Eirāzijas āpsis (Meles meles)", use_column_width=True, unsafe_allow_html=True)

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
