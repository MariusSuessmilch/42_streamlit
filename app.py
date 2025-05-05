import streamlit as st

st.title("Streamlit Demo: Grundkonzepte")
st.markdown("""
Diese App demonstriert die wichtigsten Streamlit-Konzepte:
- **Text-Elemente**
- **Eingabe-Elemente**
- **Sidebar**
- **Session State**

Zu jedem Bereich siehst du ein Beispiel und den ausgeführten Code.
""")

# 1. Text-Elemente
st.header("1. Text-Elemente")
st.write("Text-Elemente dienen dazu, Inhalte und Überschriften anzuzeigen.")
with st.echo():
    st.title("Das ist ein Titel")
    st.header("Das ist eine Überschrift")
    st.markdown("**Das ist fetter Text mit Markdown.**")
    st.write("Das ist ein normaler Text.")

# 2. Eingabe-Elemente
st.header("2. Eingabe-Elemente")
st.write("Eingabe-Elemente ermöglichen die Interaktion mit Nutzern.")
with st.echo():
    name = st.text_input("Wie heißt du?")
    age = st.slider("Wie alt bist du?", 0, 100, 25)
    st.write(f"Hallo, {name}! Du bist {age} Jahre alt.")

# 3. Sidebar
st.header("3. Sidebar")
st.write("Die Sidebar eignet sich für Navigation oder Einstellungen.")
with st.echo():
    st.sidebar.title("Sidebar Beispiel")
    option = st.sidebar.selectbox("Wähle eine Option", ["A", "B", "C"])
    st.sidebar.write(f"Du hast {option} gewählt.")

# 4. Session State
st.header("4. Session State")
st.write("Mit Session State kannst du Werte zwischen Interaktionen speichern.")
with st.echo():
    if 'counter' not in st.session_state:
        st.session_state.counter = 0

    if st.button("Zähler erhöhen"):
        st.session_state.counter += 1

    st.write(f"Zählerstand: {st.session_state.counter}")