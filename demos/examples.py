import streamlit as st
#import cv2
import numpy as np
import time
import random
from demos import orchestrator



def show():

    
    # Add a name field

    #name_input = st.text_input(
    #    "Vul je naam in 👇",
    #    placeholder="naam",
    #    key= key
    #)
    #name = name_input.lower()

    #st.markdown("""---""")
    picture = st.camera_input("Selfie tijd...", key="1")



    filters_to_funcs = {
        "No filter": none,
        "Invert": invert,
        "HDR": hdr,
        "Sketch": sketch,
        "Grayscale": gray
    }


    #if "name" not in st.session_state:
    #    st.session_state["name"] = name

    st.session_state["picture"] = picture


    #st.write(st.session_state)
