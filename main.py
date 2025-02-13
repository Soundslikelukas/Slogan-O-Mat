import streamlit as st
import random
import words

word_collection = words.words


st.title("Willkommen zum Slogan-O-Mat!")
st.write(
    "Ich schlage dir zufällige Wörter vor, um dich für einen Slogan zu inspirieren! Wenn du möchtest, dass ich es dir öfter vorschlage, klicke einfach auf das Wort. Du kannst ein Wort auch mehrmals anklicken, dann verwende ich es noch häufiger.")
number_of_words = st.slider("Wie viele Wörter soll ich dir schreiben?", 1, 8, 3)
st.divider()

def getRandomWord():
    return random.choice(word_collection + st.session_state.custom_words)


def generateSlogan():
    slogan = ""
    for _ in range(number_of_words):
        randWord = getRandomWord()
        while randWord in slogan:
            randWord = getRandomWord()
        slogan += randWord
        slogan += " "
    return slogan


if "slogans" not in st.session_state:
    st.session_state.slogans = []

if "custom_words" not in st.session_state:
    st.session_state.custom_words = []


def addSlogan():
    newSlogan = generateSlogan()
    st.session_state.slogans.append(newSlogan)


def addWord(word):
    for i in range(10):
        st.session_state.custom_words.append(word)
    st.toast(f'**{word}** als Favorit hinzugefügt!', icon='🌱')


st.button(":game_die: Gib mir Wörter!", on_click=addSlogan)
st.write("")

for index, slogan in enumerate(reversed(st.session_state.slogans)):
    if index == 0:
        words = slogan.split()
        columns = st.columns(len(words))
        for col, word in zip(columns, words):  # Verteile jedes Wort auf die Spalten
            with col:
                if word in st.session_state.custom_words:
                    col.button(word, on_click=addWord, args=(word,), key=f"button_{word}", type="primary",
                               use_container_width=True)
                else:
                    col.button(word, on_click=addWord, args=(word,), key=f"button_{word}", type="secondary",
                               use_container_width=True)

        st.divider()
        st.write("**Dein persönlicher Wort-Verlauf:**")
    else:
        st.write(slogan)
