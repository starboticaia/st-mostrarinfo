import streamlit as st

st.title("Título")
st.header("Cabecera")
st.subheader("Subcabecera")
st.write("Texto simple con emoji :sunglasses:")
st.write("Códigos de emojis para streamlit: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/")

st.markdown("Texto usando Markdown: *negrita* **cursiva** ***negrita cursiva***")
st.markdown(":red[Texto] de :rainbow[colores] con :violet[Markdown]")

multilinea = """
Cuando deseamos escribir  
un texto multilínea  
insertamos al final  
de cada línea  
dos espacios.
"""

st.markdown(multilinea)
