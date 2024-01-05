import streamlit as st
import spacy
from spacy import displacy

nlp = spacy.load("pl_core_news_sm")


sentence_5 = ['Myślę, że firmy takie jak Enron chciały Andersona, ponieważ były skłonne naginać zasady i działać w szarej strefie.',
 'To ich gówniany prawnik wpadł w szał Bonanzy, kiedy stało się jasne, że Enron upadnie.',
 'Zapewnia nieograniczoną przestrzeń dyskową, przeciąganie i zmniejszanie profesjonalizmu witryny, obsługę domen na całym świecie, kontrolę cPanel, dostęp do FTP, a także wiele więcej.',
 "Większość ludzi na studiach MBA myśli, że będzie Steve'em Jobsem.",
 ', ale Steve Jobs to ludzie, którzy zakładają firmę, zamiast iść na studia MBA.']

st.title("Named Entity Recognition Demo")

for sentence in sentence_5:
    sentence_doc = nlp(sentence)
    html = displacy.render(sentence_doc, style="ent", page=False, options={"colors": {"ORG": "#7aecec", "PERSON": "#aa9cfc", "LOC": "#bfeeb7"}})

    svg = html[html.find("<svg"):html.find("</svg>") + 6]

    # st.markdown(sentence, unsafe_allow_html=True)
    st.markdown(html, unsafe_allow_html=True)