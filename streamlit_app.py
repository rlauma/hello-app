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
    if animal == "Eirāzijas āpsis":
        st.write("Meles meles")

selected_data = st.sidebar.selectbox('Select a dataset', data().dataset_id)
title_data = data()[ data()['dataset_id'] == selected_data]['title']

st.header('Datasets')
st.subheader('List of dataset')
with st.expander('Show list of dataset'):
    st.write(data())

st.subheader(f'Selected data (`{selected_data}`)')
st.info(title_data)
st.write(data(selected_data))
