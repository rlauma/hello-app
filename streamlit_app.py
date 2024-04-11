import streamlit as st
st.header("Dzīvnieku katalogs")
st.write("This is my new app")

st.header("Vispārīgie dati")
animal = st.radio("Dzīvnieku nosaukums", ("Brūnais lācis", "Ziemeļu sikspārnis", "Eirāzijas āpsis"))
button3 = st.button("Apstiprināt")
if button3:
    if animal == "Brūnais lācis":
        st.write("Ursus arctos")
    if animal == "Ziemeļu sikspārnis":
        st.write("Eptesicus nilssoni")


