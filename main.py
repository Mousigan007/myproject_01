import streamlit as st
from streamlit_option_menu import option_menu

# Fixed: Added quotes around string
st.title("my live application")

with st.sidebar:
    # Fixed: Added quotes and changed 'option' to 'options'
    data = option_menu(
        menu_title="my apps",
        options=["home", "About", "Services"],
    )
