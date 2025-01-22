import streamlit as st


with st.sidebar:

    with st.container():
        col1, col2 = st.columns([1,5])
        with col1:
            st.image("data:image/png;base64,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",use_container_width=True)
        with col2:
            st.header("MMI Web Tool V2.0")

    with st.container(border=True):
        st.text_input(label="USERNAME", key="_user")
        st.text_input(label="PASSWORD", key="_pass")
        st.button(label="SIGN IN")

users = st.secrets['USERS']

for _user, _pass in users.item():
    st.write(_user)
    st.write(_pass)
    