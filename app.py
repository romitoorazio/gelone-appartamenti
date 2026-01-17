import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse

st.set_page_config(page_title="Gelone Appartamenti", layout="wide")

# --- CONFIGURAZIONE ---
TUO_NUMERO_WHATSAPP = "393XXXXXXXXX" # <--- METTI IL TUO NUMERO QUI (con 39 davanti)

st.title("🏨 Gelone Appartamenti - Check-in 2026")

menu = ["Nuovo Check-in", "Genera File Questura"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Nuovo Check-in":
    st.header("📝 Registrazione Ospite")
    with st.form("form_ospite"):
        nome = st.text_input("Nome")
        cognome = st.text_input("Cognome")
        nascita = st.date_input("Data di Nascita", datetime(1990, 1, 1))
        documento = st.text_input("Tipo e Num. Documento (es. CI CA12345)")
        data_arrivo = st.date_input("Data Arrivo", datetime.now())
        notti = st.number_input("Notti", min_value=1, step=1)
        
        st.warning("Cliccando 'Salva' i dati verranno preparati per l'invio su WhatsApp.")
        submit = st.form_submit_button("SALVA E INVIA")

        if submit:
            # Creazione del messaggio per WhatsApp
            testo_msg = f"*NUOVO CHECK-IN*\n\n" \
                        f"*Ospite:* {nome} {cognome}\n" \
                        f"*Nato il:* {nascita}\n" \
                        f"*Documento:* {documento}\n" \
                        f"*Arrivo:* {data_arrivo}\n" \
                        f"*Notti:* {notti}\n" \
                        f"*Tassa Soggiorno:* €{notti*2:.2f}"
            
            msg_encoded = urllib.parse.quote(testo_msg)
            whatsapp_url = f"https://wa.me{TUO_NUMERO_WHATSAPP}?text={msg_encoded}"
            
            st.success(f"Dati pronti per l'invio!")
            st.markdown(f'''
                <a href="{whatsapp_url}" target="_blank">
                    <button style="background-color: #25D366; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-size: 16px;">
                        ✅ Invia Dati su WhatsApp
                    </button>
                </a>
                ''', unsafe_allow_html=True)

if choice == "Genera File Questura":
    st.header("📤 Export per Polizia di Stato")
    st.write("Usa i dati ricevuti su WhatsApp per compilare il file txt quando avrai le credenziali.")
    st.info("Oggi è il 17 Gennaio 2026: ricorda di inviare le schedine entro 24 ore.")
