import streamlit as st
st.title("Dzīvnieku katalogs")


st.header("Start of the Checkbox Section")
like = st.checkbox("Do you like this app?")
button2 = st.button("Submit")
if button2:
    if like:
        st.write("Thanks. I like it too.")
    else:
        st.write("I'm sorry. You have bad tastes.")

st.header("Start of the Radio Button Section")
animal = st.radio("What animal is your favorite?", ("Lion", "Tiger", "Bear"))
button3 = st.button("Submit Animal")
if button3:
    st.write(animal)
    if animal == "Lion":
        st.write("ROAR!")

st.header("Start of the Selectbox Section")
animal2 = st.selectbox("What animal is your favorite?", ("Lion", "Tiger", "Bear"))
button4 = st.button("Submit Animal 2")
if button4:
    st.write(animal2)
    if animal2 == "Lion":
        st.write("ROAR!")


st.header("Start of the Multiselect Section")
options = st.multiselect("What animals do you like?",
["Lion", "Tiger", "Bear"])
button5 = st.button("Print Animals")
if button5:
    st.write(options)


def run_sentiment_analysis(txt):
    st.write(f"Analysis Done. {txt}")

txt = st.text_area('Text to analyze', '''It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair''')
st.write('Sentiment:', run_sentiment_analysis(txt))
