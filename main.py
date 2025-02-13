import streamlit as st
import random

nomen = [
    "Erneuerung", "Fairness", "Gemeinschaft", "Energie", "Freiheit", "Frischer Wind", "Verankerung",
    "Ehrlichkeit", "Jugend", "Neudenken", "Kooperation", "Aufbruch", "Freiheit", "Fortschrittlich",
    "Verbindung", "Möglichkeit", "Klimaschutz", "Modernisieren", "Neue Horizonte", "Proaktiv",
    "Community", "Mut", "Innovationstreiber", "Menschlichkeit", "Start", "Neudenken", "Empowerment",
    "Zukunft", "Netzwerk", "Leidenschaft", "Chancengleichheit", "Wandel", "Teamgeist", "Wachstum",
    "Pionier", "Tatkraft", "Weitblick", "Innovation", "Gemeinschaft", "Nachhaltigkeit", "Trend",
    "Gemeinsam", "Fortschrittskraft", "Reform", "Partizipation", "Motivation", "Vision", "Digital",
    "Hoffnung", "Menschlichkeit", "Kreativität", "Frischer Wind", "Chancenreich", "Neugier",
    "Strahlkraft", "Offenheit", "Digitalisierung", "Power", "Verantwortungsbewusst", "Durchbruch",
    "Ambition", "Dynamisch", "Lösungen", "Transformation", "Verlässlich", "Beteiligung",
    "Zukunftsvision", "Mobilität", "Soziale Gerechtigkeit", "Erfolgsgeschichte", "Zusammenhalt",
    "Bürgernähe", "Tatendrang", "Macher", "Verantwortung", "Diversität", "Kooperation", "Veränderung",
    "Optimierung", "Neue Horizonte", "Stärke", "Aufstieg", "Zukunftsorientiert", "Antrieb", "Chance",
    "Vertrauen", "Beteiligung", "Impulse", "Mut", "Respekt", "Zielstrebig", "Erlebnis", "Gemeinsam",
    "Gerechtigkeit", "Weitblick", "Erfolg", "Soziale Innovation", "Optimismus", "Zukunft gestalten",
    "Verbindung", "Zusammenarbeit", "Weitsicht", "Nachhaltig", "Tatkraft", "Ehrlichkeit", "Fortschritt",
    "Brückenbau", "Generation", "Revolution", "Aufbruch", "Wertschätzung", "Transformation",
    "Visionär", "Empowerment", "Moderne", "Zukunftskraft", "Kreative Lösungen", "Innovationstreiber",
    "Teamgeist", "Inspirierend", "Erneuern", "Neugestalten", "Offen für Wandel", "Verantwortungsbewusst",
    "Erfolgsgeschichte", "Freiheit leben", "Vertrauensvoll", "Gemeinschaftlich", "Digitale Zukunft",
    "Lösungsorientiert", "Mitgestalten", "Neue Wege", "Weichen stellen", "Ehrgeiz", "Gemeinsamer Erfolg"
]

adverbien = [
    "jetzt", "heute", "morgen", "übermorgen", "gestern", "vorgestern", "bald", "gleich",
    "sofort", "demnächst", "neulich", "vorhin", "einst", "damals", "zuvor", "vorher",
    "nachher", "anschließend", "später", "zugleich", "bisher", "schon", "bereits", "stets",
    "immer", "oft", "manchmal", "selten", "nie", "hier", "dort", "da", "überall", "irgendwo", "nirgends", "nirgendwo",
    "woanders",
    "drinnen", "draußen", "oben", "unten", "vorne", "hinten", "daneben", "gegenüber", "entlang", "genau", "anders",
    "kaum", "sehr", "ziemlich", "äußerst", "völlig", "halbwegs",
    "teilweise", "schwerlich", "gerade", "besonders", "einfach", "leicht", "mühsam",
    "schnell", "langsam", "plötzlich", "allmählich", "stillschweigend", "laut", "leise", "deshalb", "darum", "daher",
    "folglich", "somit", "nämlich", "aus diesem Grund",
    "wegen", "trotzdem", "dennoch", "allerdings", "gleichwohl", "obwohl", "weil",
    "weswegen", "warum", "wieso", "weshalb", "immer", "nie", "oft", "manchmal", "selten", "regelmäßig", "ab und zu",
    "häufig",
    "gelegentlich", "ständing", "fortlaufend", "sporadisch", "meistens", "gewöhnlich"
]

pronomen = [
    "ich", "du", "er", "sie", "es", "wir", "ihr", "sie", "Sie", "mich", "dich", "sich", "uns", "euch", "mein", "dein",
    "sein", "ihr", "sein", "unser", "euer", "Ihr", "dieser", "diese", "dieses", "jene", "jener", "jenes", "derjenige",
    "diejenige", "dasjenige",
    "derselbe", "dieselbe", "dasselbe", "solcher", "solche", "solches", "der", "die", "das", "welcher", "welche",
    "welches", "wer", "was", "welcher", "welche", "welches", "wessen", "wem", "wen", "man", "jemand", "niemand",
    "irgendwer", "etwas", "nichts", "alle", "viele", "einige",
    "wenige", "mehrere", "manche", "jeglicher", "jegliche", "jegliches", "jeder", "jede", "jedes",
    "irgendetwas", "irgendein", "irgendeine", "irgendeines", "keiner", "keine", "keines", "einer", "eine", "eines",
    "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn"
]

verben = [
    "gehen", "laufen", "rennen", "springen", "fahren", "fliegen", "schwimmen", "steigen", "kriechen", "rollen",
    "sprechen", "sagen", "rufen", "schreien", "flüstern", "erzählen", "erklären", "fragen", "antworten", "diskutieren",
    "denken", "überlegen", "wissen", "lernen", "verstehen", "vergessen", "merken", "glauben", "zweifeln", "ahnen",
    "lieben", "hassen", "freuen", "ärgern", "fürchten", "trauern", "lachen", "weinen", "staunen", "sehnen",
    "machen", "tun", "arbeiten", "bauen", "zerstören", "reparieren", "schaffen", "gestalten", "entwickeln",
    "programmieren",
    "regnen", "schneien", "frieren", "blühen", "wachsen", "verwelken", "wehen", "brennen", "fließen", "tauen",
    "essen", "trinken", "kochen", "backen", "schmecken", "kauen", "schlucken", "nagen", "genießen", "rühren",
    "sehen", "hören", "riechen", "schmecken", "fühlen", "betrachten", "bemerken", "lauschen", "spüren", "erkunden",
    "helfen", "geben", "nehmen", "teilen", "danken", "bitten", "besuchen", "verlassen", "streiten", "versöhnen",
    "programmieren", "klicken", "scrollen", "tippen", "downloaden", "hochladen", "bearbeiten", "speichern", "hacken",
    "debuggen",
    "kaufen", "verkaufen", "bezahlen", "investieren", "verdienen", "sparen", "leihen", "spenden", "verwalten",
    "gewinnen",
    "trainieren", "tanzen", "klettern", "turnen", "boxen", "reiten", "tauchen", "schießen", "werfen", "fangen",
    "putzen",
    "waschen", "bügeln", "staubsaugen", "ordnen", "reparieren", "dekorieren", "einkaufen", "aufhängen", "kochen"
]

st.title("Willkommen zum Slogan-O-Mat!")
st.subheader("Ich schlage dir zufällige Wortkombinationen vor, um dich zu inspirieren!")
number_of_words = st.slider("Wie viele Wörter soll ich dir schreiben?", 1, 8, 3)


def generateSlogan():
    slogan = ""
    for _ in range(number_of_words):
        word = random.choice(verben + pronomen + adverbien + nomen + st.session_state.custom_words)
        while word in slogan:
            word = random.choice(verben + pronomen + adverbien + nomen)
        slogan += word
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


st.button(":game_die: Mach mir einen Slogan!", on_click=addSlogan)
st.write("")

for index, slogan in enumerate(reversed(st.session_state.slogans)):
    if index == 0:
        words = slogan.split()
        columns = st.columns(len(words))
        for col, word in zip(columns, words):  # Verteile jedes Wort auf die Spalten
            with col:
                col.button(word, on_click=addWord, args=(word,), key=f"button_{word}")

        st.divider()
    else:
        st.write(slogan)
