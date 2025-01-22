import streamlit as st
from streamlit_option_menu import option_menu

from tools import cleaner



if __name__ == "__main__":

    with st.sidebar:

        with st.container():
            st.header(":hammer_and_wrench: MMI Web Tool V2.0", divider=True)

        with st.container(border=True):
            selected = option_menu(
                menu_title='Main',
                options=['Home', 'Tools', 'Report Creator'],
                icons=['house', 'pc-display', 'filetype-xlsx'],
                key='home_sidebar',
            )
    
    if selected == 'Tools':
        cleaner()
