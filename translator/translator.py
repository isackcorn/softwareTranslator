import streamlit as st
from deep_translator import GoogleTranslator
from langs import languages

st.title("Переводчик")
lang = st.selectbox("Язык, на который необходимо перевести текст:", languages)
source_text = st.text_area("Введите Ваш текст:")
translate = st.button("Перевести")
if translate:
    translatedText = GoogleTranslator(source='auto', target=lang).translate( source_text )
    st.write(translatedText)