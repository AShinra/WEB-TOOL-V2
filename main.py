import streamlit as st


with st.sidebar:

    with st.container(border=True):
        st.text_input(label="USERNAME", key="_user")
        st.text_input(label="PASSWORD", key="_pass")
        st.button(label="SIGN IN")


    