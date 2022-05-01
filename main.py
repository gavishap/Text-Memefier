import random

import streamlit
import streamlit as st
import platform
import os

if __name__== '__main__':
    text = input("Give me a text to memify:\n")
    meme_txt=[]
    for let in text:
        low_or_high=random.randint(0,1)
        if let.isspace()==False:
            if low_or_high==0:
                meme_txt.append(let.lower())
            else:
                meme_txt.append(let.upper())
        else:
            meme_txt.append(' ')

    print(''.join(meme_txt))
    print("streamlit version: {:>30}".format(streamlit.__version__))