eimport streamlit as st
st.title("Dzīvnieku katalogs")


st.header("Vispārīgie dati")
animal = st.radio("Dzīvnieku nosaukums", ("Brūnais lācis", "Ziemeļu sikspārnis", "Eirāzijas āpsis"))
button3 = st.button("Apstiprināt")
if button3:
    st.write(animal)
    if animal == "Brūnais lācis":
        st.write("Ursus arctos")
        if animal == "Ziemeļu sikspārnis":
        st.write("Eptesicus nilssoni")
        if animal == "Eirāzijas āpsis":
        st.write("Meles meles")










st.header("Start of the Selectbox Section")
animal2 = st.selectbox("What animal is your favorite?", ("Lion", "Tiger", "Bear"))
button4 = st.button("Submit Animal 2")
if button4:
    st.write(animal2)
    if animal2 == "Lion":
        st.write("ROAR!")



