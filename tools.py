import streamlit as st



def cleaner():

    st.header(":hammer_and_wrench: TOOLS")

    with st.container(border=True):
        raw_file = st.file_uploader(label="Upload xlsx/xls raw file", type=["xlsx", "xls"], help='Raw File Uploader')

    if raw_file not in [None, '']:
        st.text_input(label='File Name', key='output_filename', help='Output File Name')
        
        if st.session_state['output_filename'] not in [None, '']:
            st.caption('Select Processes you want to run')
            with st.container(border=True):
                col1, col2, col3 = st.columns([0.35, 0.3, 0.35], vertical_alignment='center')
                with col1:
                    st.checkbox(label='Remove Duplicates', help='Remove exact duplicate rows')
                    st.checkbox(label='Remove Publications', help='Remove rows whose publications are in the remove list')
                    st.checkbox(label='Publication Tier', help='Adds a column containing publication tiering')
                with col2:
                    st.checkbox(label='ROI', help='Adds a column with computed Return of Investment')
                    st.checkbox(label='Tone', help='Adds a tonality column')
                    st.checkbox(label='Favorability', help='Adds favorability column')
                with col3:
                    st.checkbox(label='Reach', help='Adds column containg reach for online publications and blogs')
                    st.checkbox(label='Readership', help='Adds readership column for Print Media')
                    st.checkbox(label='Circulation', help='Adds Circulation column for Print Media')
                st.checkbox(label='Publication Edition', help='Adds a column containg publications edition, eg. National, Local')

            st.button(label=':arrow_forward:')




    return