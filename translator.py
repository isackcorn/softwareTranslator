import streamlit as st
from deep_translator import GoogleTranslator

st.title("Переводчик")
source_text = st.text_area("Введите Ваш текст:")
translate = st.button("Перевести")
if translate:
    translatedText = GoogleTranslator(source='auto', target='ru').translate( source_text )
    st.write(translatedText)