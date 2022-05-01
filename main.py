import random

import streamlit
import streamlit as st
import platform
import os


if __name__== '__main__':
    api = 'https://mememetext.herokuapp.com/'
    st.markdown('# Memefy any text you like')
    text = st.text_input("Give me a text to memify:\n")
    meme_txt=[]
    higher = text.upper()
    lower = text.lower()
    for i in range(len(text)):
        if i%2==0:
            meme_txt.append(lower[i])
        else:
            meme_txt.append(higher[i])
    st.write(f'Memed Word: {meme_txt}')
