import streamlit as st

st.header('Lanzar una moneda')

number_of_tirals = st.slider("¿Número de intenos?", 1, 1000, 10)
start_button = st.button("Ejecutar")

if start_button:
    st.write(f'Experimento con {number_of_tirals} intentos en curso.')

st.write('Esta aplicación aún no es funcional. En construcción.')