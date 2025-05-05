# Streamlit Demo: Grundkonzepte

Willkommen zu diesem kleinen Streamlit-Projekt! Diese App zeigt dir die wichtigsten Grundfunktionen von Streamlit – einer beliebten Bibliothek, mit der du ganz einfach eigene Web-Apps mit Python bauen kannst.

## Was ist Streamlit?
Streamlit ist ein Werkzeug, mit dem du Python-Code in interaktive Webseiten verwandeln kannst. Du brauchst dafür keine Vorkenntnisse in Webentwicklung.

## Was zeigt diese Demo-App?
In der Datei `app.py` findest du Beispiele und Erklärungen zu:

1. **Seiteneinstellungen (`st.set_page_config`)**: Damit kannst du den Namen und das Icon deiner App festlegen. Das sorgt für einen schöneren und professionelleren Auftritt im Browser.
2. **Text-Elemente**: So kannst du Überschriften, normalen Text und formatierte Texte anzeigen.
3. **Eingabe-Elemente**: Damit kann der Nutzer z.B. seinen Namen eingeben oder einen Regler verschieben.
4. **Sidebar**: Eine Seitenleiste für Einstellungen oder Navigation.
5. **Session State**: So kannst du Werte speichern, die auch nach einer Nutzeraktion erhalten bleiben (z.B. ein Zähler).

## Wie starte ich die App?

1. **Virtuelle Umgebung (empfohlen):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install streamlit
   ```
2. **App starten:**
   ```bash
   streamlit run app.py
   ```

Die App öffnet sich im Browser. Du kannst die Elemente ausprobieren und den Code dazu direkt sehen.

## Für wen ist das gedacht?
Dieses Projekt ist für Schüler:innen und alle, die neu im Programmieren sind. Du brauchst nur ein bisschen Python-Grundwissen. Alles andere lernst du beim Ausprobieren!

Viel Spaß beim Entdecken von Streamlit! 🚀