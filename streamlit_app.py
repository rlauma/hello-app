import streamlit as st
import pandas as pd

# Create some sample data for Brūnais lācis
data_brown_bear = { 
    'Taukskābes nosaukums': ['palmitīnskābe (16:0)', 'stearīnskābe (18:0)', 'oleīnskābe (18:1n-9)', 'linolēnskābe (18:2n-6)', 'palmitoleīnskābe (16:1n-7)'],
    'Ķīmiskā formula': ['C₁₆H₃₂O₂', 'C₁₈H₃₆O₂', 'C₁₈H₃₄O₂', 'C₁₈H₃₂O₂', 'C₁₆H₃₀O₂'],
    'Oglekļu atomu skaits': ['16', '18', '18', '18', '16'],
    'Dubultsaišu skaits': ['', '', '1', '2', '1'],
}

# Create some sample data for Eirāzijas āpsis
data_badger = { 
    'Taukskābes nosaukums': ['arahidonskābe (20:4n-6)', 'dokozaheksaēnskābe (22:6n-3)', 'heptadekānskābe (17:0)', 'stearīnskābe (18:0)', 'oleīnskābe (18:1n-9)'],
    'Ķīmiskā formula': ['C₁₆H₃₂O₂', 'C₂₂H₃₂O₂', 'C₂₂₂₂₂H₂₂₂₂O₂₂₂₂', 'C₁₈H₃₆O₂', 'C18H34O2','C18H30O2','C18H30O2','C20H30O2'],
    'Oglekļu atomu skaits': ['16', '22', 'XX', '18', '18', '18', '18', '20'],
    'Dubultsaišu skaits': ['4', '6', '?', '?', '1', '3', '3', '5'],
}

# Convert the data to DataFrames
df_brown_bear = pd.DataFrame(data_brown_bear)
df_badger = pd.DataFrame(data_badger)

# Display headers and radio button
st.title("Dzīvnieku katalogs")
st.header("Vispārīgie dati")
animal = st.radio("Dzīvnieku nosaukums", ("Brūnais lācis", "Eirāzijas āpsis"))

# Define button label based on selected animal
if animal == "Brūnais lācis":
    button_label = "Apstiprināt Brūnais lācis"
    data_selected = df_brown_bear
    image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Ursus_arctos_-_Norway_%28cropped%29.jpg/320px-Ursus_arctos_-_Norway_%28cropped%29.jpg"
    image_caption = "Brūnais lācis"
else:
    button_label = "Apstiprināt Eirāzijas āpsis"
    data_selected = df_badger
    image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Brockhaus_and_Efron_Encyclopedic_Dictionary_b79_030-0.jpg/320px-Brockhaus_and_Efron_Encyclopedic_Dictionary_b79_030-0.jpg"
    image_caption = "Eirāzijas āpsis"

button3 = st.button(button_label)

# Display animal information when button is clicked
if button3:
    st.subheader("Taukskābju īpašības")
    st.image(image_url, caption=image_caption, use_column_width=True)
    st.table(data_selected)
