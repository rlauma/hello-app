import streamlit as st
import pandas as pd

# Create sample data for each animal
data_brown_bear = { 
    'Dzīvnieka nosaukums': ['Brūnais lācis'],
    'Suga': ['Ursus arctos'],
    'Barība': ['Omnivors'],
    'Dzīvesvieta': ['Ziemeļi'],
}

data_bat = { 
    'Dzīvnieka nosaukums': ['Ziemeļu sikspārnis'],
    'Suga': ['Eptesicus nilssoni'],
    'Barība': ['Insektofāgs'],
    'Dzīvesvieta': ['Ziemeļi'],
}

data_badger = { 
    'Dzīvnieka nosaukums': ['Eirāzijas āpsis'],
    'Suga': ['Meles meles'],
    'Barība': ['Omnivors'],
    'Dzīvesvieta': ['Visās teritorijas'],
}

# Convert the data to DataFrames
df_brown_bear = pd.DataFrame(data_brown_bear)
df_bat = pd.DataFrame(data_bat)
df_badger = pd.DataFrame(data_badger)

# Display headers and radio button
st.title("Dzīvnieku katalogs")
st.header("Vispārīgie dati")
animal = st.radio("Dzīvnieku nosaukums", ("Brūnais lācis", "Ziemeļu sikspārnis", "Eirāzijas āpsis"))
button3 = st.button("Apstiprināt")

# Display animal information when button is clicked
if button3:
    if animal == "Brūnais lācis":
        st.table(df_brown_bear)
        st.image("https://www.nps.gov/subjects/bears/images/Brown-bear-Katmai.jpg", caption="Brūnais lācis (Ursus arctos)", use_column_width=True)
    elif animal == "Ziemeļu sikspārnis":
        st.table(df_bat)
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Eptesicus_nilssoni_%28Norway%29.jpg/800px-Eptesicus_nilssoni_%28Norway%29.jpg", caption="Ziemeļu sikspārnis (Eptesicus nilssoni)", use_column_width=True)
    elif animal == "Eirāzijas āpsis":
        st.table(df_badger)
        st.image("https://rigazoo.lv/wp-content/uploads/2023/05/apsis-3.jpeg", caption="Eirāzijas āpsis (Meles meles)", use_column_width=True)
