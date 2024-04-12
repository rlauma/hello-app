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
    'Ķīmiskā formula': ['C₂₀H₃₂O₂', 'C₂₂H₃₂O₂', 'C₁₇H₃₄O₂', 'C₁₈H₃₆O₂', 'C₁₈H₃₄O₂'],
    'Oglekļu atomu skaits': ['20', '22', '17', '18', '18'],
    'Dubultsaišu skaits': ['4', '6', '', '', '1'],
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
    image_url = "https://rigazoo.lv/wp-content/uploads/2023/05/apsis-3.jpeg","
    image_caption = "Eirāzijas āpsis"

button3 = st.button(button_label)

# Display animal information when button is clicked
if button3:
    st.subheader("Taukskābju īpašības")
    st.image(image_url, caption=image_caption, use_column_width=True)
    st.table(data_selected)
