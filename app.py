import streamlit as st
import pandas as pd
from database import session, ColorPalette, FontPair
from simple_model import load_data, train_simple_model

# Puslapio nustatymai
st.set_page_config(page_title="DI Dizaino Asistentas", layout="centered")

st.title("🎨 DI Vizualinio Identiteto Generatorius")
st.write("Iveskite norima emocija ir DI parinks spalvas bei sriftus.")

# 1. Gauname duomenis is DB
df = load_data()

# 2. Vartotojo ivestis
emotion_input = st.selectbox("Pasirinkite nuotaika:", df['emotion'].unique())

if st.button("Generuoti"):
    # Kvieciame musu modeli
    result = train_simple_model(df, emotion_input)
    st.success(f"Modelio rezultatas: {result}")
    
    # Isgauname spalvas is DB tam tikrai emocijai vizualizacijai
    palette = session.query(ColorPalette).filter_by(emotion=emotion_input).first()
    
    if palette:
        st.subheader(f"Rekomenduojama palete '{emotion_input}':")
        
        # Sukuriame spalvu kvadratus naudojant HTML/CSS
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"<div style='background-color:{palette.hex_1}; height:100px; border-radius:10px; border: 1px solid #ddd;'></div>", unsafe_allow_html=True)
            st.code(palette.hex_1)
        with col2:
            st.markdown(f"<div style='background-color:{palette.hex_2}; height:100px; border-radius:10px; border: 1px solid #ddd;'></div>", unsafe_allow_html=True)
            st.code(palette.hex_2)
        with col3:
            st.markdown(f"<div style='background-color:{palette.hex_3}; height:100px; border-radius:10px; border: 1px solid #ddd;'></div>", unsafe_allow_html=True)
            st.code(palette.hex_3)

        # Pridedame sriftu rekomendacija
        font = session.query(FontPair).filter_by(emotion=emotion_input).first()
        if font:
            st.divider()
            st.subheader("Rekomenduojami sriftai:")
            st.write(f"**Antrastems:** {font.headline_font}")
            st.write(f"**Tekstui:** {font.body_font}")
            st.info(f"Kategorija: {font.category}")

# Komentaras: Streamlit leidzia sukurti interaktyvius elementus be sudetingo HTML/JS