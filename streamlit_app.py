import streamlit as st
import pandas as pd
 
# Create some sample data
data_badger = { 
    'Taukskābes nosaukums': ['arahidonskābe (20:4n-6)', 'dokozaheksaēnskābe (22:6n-3)', 'heptadekānskābe (17:0)', 'stearīnskābe (18:0)', 'oleīnskābe (18:1n-9)'],
    'Ķīmiskā formula': ['C₂₀H₃₂O₂', 'C₂₂H₃₂O₂', 'C₁₇H₃₄O₂', 'C₁₈H₃₆O₂', 'C₁₈H₃₄O₂'],
    'Oglekļu atomu skaits': ['20', '22', '17', '18', '18'],
    'Dubultsaišu skaits': ['4', '6', '', '', '1'],
}
 
data_brown_bear = { 
    'Taukskābes nosaukums': ['palmitīnskābe (16:0)', 'stearīnskābe (18:0)', 'oleīnskābe (18:1n-9)', 'linolēnskābe (18:2n-6)', 'palmitoleīnskābe (16:1n-7)'],
    'Ķīmiskā formula': ['C₁₆H₃₂O₂', 'C₁₈H₃₆O₂', 'C₁₈H₃₄O₂', 'C₁₈H₃₂O₂', 'C₁₆H₃₀O₂'],
    'Oglekļu atomu skaits': ['16', '18', '18', '18', '16'],
    'Dubultsaišu skaits': ['', '', '1', '2', '1'],
}
 
# Convert the data to DataFrames
df_badger = pd.DataFrame(data_badger)
df_brown_bear = pd.DataFrame(data_brown_bear)
 
# Display headers and radio button
st.title("Dzīvnieku katalogs")
st.header("Vispārīgie dati")
animal = st.radio("Dzīvnieku nosaukums", ("Brūnais lācis", "Eirāzijas āpsis"))
 
# Define button label and data based on selected animal
if animal == "Brūnais lācis":
    button_label = "Apstiprināt"
    data_selected = df_brown_bear
elif animal == "Eirāzijas āpsis":
    button_label = "Apstiprināt"
    data_selected = df_badger
 
# Display animal information when button is clicked
if st.button(button_label):
    if animal == "Eirāzijas āpsis":
        # Display image from URL with caption
        st.image("https://rigazoo.lv/wp-content/uploads/2023/05/apsis-3.jpeg", caption="Eirāzijas āpsis (Meles meles)", use_column_width=True)
 
    # Display the header for the table with smaller text without bold
    st.markdown("<h3 style='color: black; font-size: 16px;'>Taukskābju īpašības</h3>", unsafe_allow_html=True)
 
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
    st.table(data_selected)
