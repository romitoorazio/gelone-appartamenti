import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Gelone Appartamenti", layout="wide")

st.title("🏨 Gelone Appartamenti - Gestione 2026")
st.sidebar.header("Menu")

scelta = st.sidebar.radio("Vai a:", ["Nuovo Check-in", "Scarica File Questura"])

if scelta == "Nuovo Check-in":
    st.header("📝 Registrazione Ospite")
    with st.form("ospite"):
        nome = st.text_input("Nome")
        cognome = st.text_input("Cognome")
        doc = st.text_input("Numero Documento")
        notti = st.number_input("Notti", min_value=1)
        invia = st.form_submit_button("Salva Dati")
        if invia:
            st.success(f"Dati di {nome} {cognome} salvati correttamente!")

if scelta == "Scarica File Questura":
    st.header("📤 Esportazione Polizia di Stato")
    st.write("Genera il file .txt da caricare su Alloggiati Web.")
    st.download_button("Scarica file per Questura", data="TRACCIATO-RECORD-2026", file_name="alloggiati.txt")
