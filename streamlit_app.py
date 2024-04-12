import streamlit as st
import pandas as pd

# Create sample data for each animal
data_brown_bear = { 
    'Taukskābes nosaukums': ['ursodeoksikolskābe', 'chenodeoksikolskābe', 'kholelāts', 'holīns', 'tā'],
    'Ķīmiskā formula': ['C₂₄H₄₀O₄', 'C₂₄H₄₀O₅', 'C₂₄H₄₀O₄', 'C₅H₁₄NO⁺', '??'],
    'Oglekļa atomu skaits': ['24', '24', '24', '-', '-'],
    'Dubultsaišu skaits': ['1', '1', '1', '-', '-'],
}
df_brown_bear = pd.DataFrame(data_brown_bear)

data_bat = { 
    'Taukskābes nosaukums': ['zīds', 'pūkas', 'tā'],
    'Ķīmiskā formula': ['C₂₈H₅₄O₂', 'C₁₆H₃₀O₂', '??'],
    'Oglekļa atomu skaits': ['28', '16', '-'],
    'Dubultsaišu skaits': ['0', '0', '-'],
}
df_bat = pd.DataFrame(data_bat)

data_badger = { 
    'Taukskābes nosaukums': ['pūkas', 'metīlsinapīnskābe', 'tā'],
    'Ķīmiskā formula': ['C₁₆H₃₀O₂', 'C₁₁H₁₄O₂', '??'],
    'Oglekļa atomu skaits': ['16', '11', '-'],
    'Dubultsaišu skaits': ['0', '0', '-'],
}
df_badger = pd.DataFrame(data_badger)

# Display headers and radio button
st.title("Dzīvnieku katalogs")
st.header("Vispārīgie dati")
animal = st.radio("Dzīvnieku nosaukums", ("Brūnais lācis", "Ziemeļu sikspārnis", "Eirāzijas āpsis"))

# Define button label based on selected animal
if animal == "Brūnais lācis":
    button_label = "Apstiprināt Brūnais lācis"
elif animal == "Ziemeļu sikspārnis":
    button_label = "Apstiprināt Ziemeļu sikspārnis"
else:
    button_label = "Apstiprināt Eirāzijas āpsis"

button3 = st.button(button_label)

# Display animal information when button is clicked
if button3:
    if animal == "Brūnais lācis":
        st.subheader("Taukskābju īpašības")
        st.write("Ursus arctos")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Ursus_arctos_-_Norway_%28cropped%29.jpg/320px-Ursus_arctos_-_Norway_%28cropped%29.jpg", caption="Brūnais lācis", use_column_width=True)
        st.table(df_brown_bear)
    elif animal == "Ziemeļu sikspārnis":
        st.subheader("Taukskābju īpašības")
        st.write("Eptesicus nilssoni")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Gray_bat_Raymond_Skillern.jpg/320px-Gray_bat_Raymond_Skillern.jpg", caption="Ziemeļu sikspārnis", use_column_width=True)
        st.table(df_bat)
    else:
        st.subheader("Taukskābju īpašības")
        st.write("Meles meles")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Brockhaus_and_Efron_Encyclopedic_Dictionary_b79_030-0.jpg/320px-Brockhaus_and_Efron_Encyclopedic_Dictionary_b79_030-0.jpg", caption="Eirāzijas āpsis", use_column_width=True)
        st.table(df_badger)
