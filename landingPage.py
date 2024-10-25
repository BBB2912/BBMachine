import streamlit as st
from streamlit_option_menu import option_menu
from Yolo import yoloServices
from DL import DLservices
from ML import MLservices
import os
import sys


st.markdown("""
    <div style="text-align: center ; font-size: 30px; font-weight: bold; color: black; margin-bottom: 30px;">
        BB Machine
    </div>
""", unsafe_allow_html=True)

# Create the horizontal navigation menu
selected = option_menu(
    menu_title=None,  # No title
    options=["ML", "DL", "YOLO"],  # Menu options
    icons=["robot", "cpu", "camera-video"],  # Menu icons
    menu_icon="cast",  # Icon for the menu
    default_index=0,  # Default selected option
    orientation="horizontal",  # Horizontal menu
)

# Render content based on the selected menu option
if selected == "ML":
    MLservices.show_ML_services()
elif selected == "DL":
    DLservices.show_DL_services()
elif selected == "YOLO":
    yoloServices.show_yolo_services()