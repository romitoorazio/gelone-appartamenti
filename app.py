import streamlit as st
from datetime import datetime
import urllib.parse

# --- INSERISCI IL TUO NUMERO QUI ---
TUO_NUMERO_WA = "393471234567" # Sostituisci con il tuo numero (es. 393401234567)

st.set_page_config(page_title="Gelone Check-in", page_icon="🏨")

st.title("🏨 Gelone Appartamenti")
st.subheader("Check-in Online 2026")

# Form di inserimento per l'ospite
with st.form("checkin_form"):
    st.markdown("### 📋 Dati Anagrafici")
    nome = st.text_input("Nome").upper()
    cognome = st.text_input("Cognome").upper()
    sesso = st.selectbox("Sesso", ["M", "F"])
    data_nascita = st.date_input("Data di Nascita", datetime(1990, 1, 1))
    nazionalita = st.text_input("Cittadinanza (es. ITALIA)").upper()
    luogo_nascita = st.text_input("Comune o Stato di Nascita").upper()
    
    st.markdown("### 🪪 Documento")
    tipo_doc = st.selectbox("Tipo Documento", ["CARTA IDENTITA", "PASSAPORTO", "PATENTE"])
    num_doc = st.text_input("Numero Documento").upper()
    
    st.markdown("### 🗓️ Soggiorno")
    data_arrivo = st.date_input("Data Arrivo", datetime.now())
    notti = st.number_input("Notti", min_value=1, step=1)
    
    submit = st.form_submit_button("REGISTRA E INVIA")

if submit:
    # 1. MESSAGGIO PER WHATSAPP
    testo_wa = (f"🏨 *NUOVO CHECK-IN*\n\n"
                f"👤 Ospite: {nome} {cognome}\n"
                f"📅 Arrivo: {data_arrivo}\n"
                f"🌙 Notti: {notti}\n"
                f"🪪 Doc: {num_doc}")
    url_wa = f"https://wa.me{TUO_NUMERO_WA}?text={urllib.parse.quote(testo_wa)}"
    
    # 2. GENERAZIONE FILE QUESTURA (Formato Alloggiati Web 2026)
    # Campi a lunghezza fissa obbligatoria
    riga_txt = (f"01" # Capofamiglia
                f"{data_arrivo.strftime('%d/%m/%Y')}"
                f"{str(notti).zfill(2)}"
                f"{cognome.ljust(50)[:50]}"
                f"{nome.ljust(30)[:30]}"
                f"{sesso}"
                f"{data_nascita.strftime('%d/%m/%Y')}"
                f"{luogo_nascita.ljust(9)[:9]}"
                f"{tipo_doc[:5].ljust(5)}"
                f"{num_doc.ljust(20)[:20]}")
    
    st.success("✅ Dati salvati con successo!")
    
    # TASTO WHATSAPP
    st.markdown(f'''
        <a href="{url_wa}" target="_blank">
            <button style="background-color: #25D366; color: white; width: 100%; padding: 15px; border-radius: 10px; border: none; font-size: 18px; cursor: pointer;">
                📲 INVIA DATI SU WHATSAPP
            </button>
        </a>
    ''', unsafe_allow_html=True)
    
    st.divider()
    
    # TASTO DOWNLOAD QUESTURA
    st.subheader("🛠️ Area Gestore")
    st.write("Scarica il file pronto per Alloggiati Web:")
    st.download_button(
        label="📥 SCARICA FILE .TXT PER QUESTURA",
        data=riga_txt,
        file_name=f"questura_{cognome}.txt",
        mime="text/plain"
    )
