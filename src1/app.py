from pickle import load
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import numpy as np

#carga el modelo
model = load(open("../models/logistic_regression.sav", "rb"))

ed = ["Primaria","Secundaria","Terciaria"]
mes = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
yn = ["Si","No"]

st.set_page_config(page_title="Campaña de Marketing Bancaria", page_icon="\U0001F3E0", layout="wide")

with st.container():
    st.title("🏡 Campaña de Marketing Bancaria 🏙️")
    st.write("Esta aplicación permite predecir si una persona esta dispuesta a hacer un depósito de largo plazo o no.")

with st.container():
    st.subheader("🔍 Ingresa las características del cliente")
    col1 = st.columns(1)[0]
    with col1:
        education = st.selectbox('Educación',["Primaria","Secundaria","Terciaria"])
        balance = st.number_input('Ingresa el balance:')
        housing = st.selectbox('🏚️ Casa Propia',["Si","No"])
        loan = st.selectbox('Préstamo',["Si","No"])
        month = st.selectbox('Month',["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"])
        duration = st.number_input('Ingresa la duración:', min_value=0)
        campaign = st.slider("Campaña", 0, 5,1)
        pdays = st.number_input('ingresa los pdays:', min_value=-10)
        previous = st.number_input('ingresa los días previos:', min_value=0)

with st.container():
    st.markdown("---")
    if st.button("Predecir"):
        input_data = np.array([[ed.index(education),balance,yn.index(housing),yn.index(loan),mes.index(month),duration,campaign,pdays,previous]])
        prediction = model.predict(input_data)[0]
        if prediction == 0:
            pred = 'NO'
        elif prediction == 1:
            pred = 'SI'
        st.success(f"✨ Cliente potencia de depósito de largo plazo: {pred}")


st.markdown("---")