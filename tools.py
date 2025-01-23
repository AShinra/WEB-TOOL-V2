import streamlit as st
from streamlit_option_menu import option_menu
from processes import clean_file


def tools_main():

    with st.container(border=True):
        selected = option_menu(
            menu_title='Tools',
            options=['Process Raw', 'Tool2', 'Tool3'],
            # icons=['house', 'wrench', 'filetype-xlsx'],
            key='tools_main',
            orientation='horizontal'
        )
    
    if selected=='Process Raw':
        cleaner()
        


def cleaner():

    with st.container(border=True):
        raw_file = st.file_uploader(label="Upload xlsx/xls raw file", type=["xlsx", "xls"], help='Raw File Uploader')

    if raw_file not in [None, '']:
        with st.container(border=True):
            st.text_input(label='File Name', key='output_filename', help='Output File Name')
        
        if st.session_state['output_filename'] not in [None, '']:
            st.caption('Select Columns to Add')
            with st.container(border=True):
                col1, col2, col3 = st.columns([0.35, 0.3, 0.35], vertical_alignment='top')
                with col1:
                    st.checkbox(label='Publication Tier', key='pub_tier', help='Adds a column containing publication tiering')
                    st.checkbox(label='ROI', key='roi', help='Adds a column with computed Return of Investment')
                    st.checkbox(label='Tone', key='tone', help='Adds a tonality column')
                with col2:
                    st.checkbox(label='Reach', key='reach', help='Adds column containg reach for online publications and blogs')
                    st.checkbox(label='Readership', key='readership', help='Adds readership column for Print Media')
                    st.checkbox(label='Circulation', key='circulation', help='Adds Circulation column for Print Media')
                with col3:
                    st.checkbox(label='Favorability', key='favorability', help='Adds favorability column')
                    st.checkbox(label='Publication Edition', key='pub_edition', help='Adds a column containg publications edition, eg. National, Local')                    
                    
            button_clean = st.button('Clean Raw File')


            if button_clean:
                df = clean_file(raw_file)

                # check which columns to add
                if st.session_state['pub_tier']:
                    df['Publication Tier'] = ''
                
                if st.session_state['roi']:
                    df['ROI'] = 0
                
                if st.session_state['tone']:
                    df['Tone'] = ''
                
                if st.session_state['reach']:
                    df['Monthly Reach'] = 0
                
                if st.session_state['readership']:
                    df['Readership'] = 0
                
                if st.session_state['circulation']:
                    df['Circulation'] = 0
                
                if st.session_state['favorability']:
                    df['Favorability'] = ''
                
                if st.session_state['pub_edition']:
                    df['Publication Edition'] = ''

                for i in df.index:
                    if st.session_state['roi']:
                        hit = df.at[i, 'Mention']/10
                        df.at[i, 'ROI'] = (1+hit)*df.at[i, 'PR Value']

                st.dataframe(df)


                

            

            





    return