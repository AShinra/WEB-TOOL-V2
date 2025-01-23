import streamlit as st
from streamlit_option_menu import option_menu

from tools import tools_main
from settings import settings_main



if __name__ == "__main__":

    st.set_page_config(layout="wide")

    with st.sidebar:

        with st.container():
            st.header(":hammer_and_wrench: MMI Web Tool V2.0", divider=True)

        with st.container(border=True):
            selected = option_menu(
                menu_title='Analyst Tools',
                options=['Home', 'Tools', 'Report Creator', 'Settings'],
                icons=['house', 'wrench', 'filetype-xlsx', 'gear'],
                key='home_sidebar',
            )
    
    if selected == 'Tools':
        tools_main()
    
    if selected == 'Settings':
        settings_main()
