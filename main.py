"""
Streamlit Cheat Sheet

App to summarise streamlit docs v1.25.0

There is also an accompanying png and pdf version

https://github.com/daniellewisDL/streamlit-cheat-sheet

v1.25.0
03 June 2024
"""

import streamlit as st
from pathlib import Path
import base64

# Initial page config

st.set_page_config(
    page_title='My own cheat sheet',
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    cs_sidebar()
    cs_body()

    return None


# Thanks to streamlitopedia for the following code snippet

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


# sidebar

def cs_sidebar():
    st.sidebar.markdown(
        '''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://streamlit.io/)'''.format(
            img_to_bytes("logomark_website.png")), unsafe_allow_html=True)
    st.sidebar.header('Streamlit cheat sheet')

    st.sidebar.markdown('''
<small>Das ist mein Cheatsheet</small>
    ''', unsafe_allow_html=True)

    st.sidebar.markdown('__Install and import__')

    st.sidebar.code('$ pip install streamlit')

    st.sidebar.markdown('__Command line__')
    st.sidebar.code('''
$ streamlit --help
$ streamlit run your_script.py
$ streamlit docs
$ streamlit --version
    ''')

    st.sidebar.markdown(
        '<small>Learn more about [streamlit experimental features](https://docs.streamlit.io/library/advanced-features/prerelease#beta-and-experimental-features)</small>',
        unsafe_allow_html=True)

    st.sidebar.markdown('''<hr>''', unsafe_allow_html=True)
    st.sidebar.markdown(
        '''<small>[Cheat sheet v1.25.0](https://github.com/daniellewisDL/streamlit-cheat-sheet)  | Juni 2024 | [Mai](https://github.com/phuong-mai-mai)</small>''',
        unsafe_allow_html=True)

    return None


##########################
# Main body of cheat sheet
##########################

def cs_body():
    col1, col2 = st.columns(2)

    #######################################
    # COLUMN 1
    #######################################

    # Display text

    col1.subheader('Git commands')
    col1.code('''
              git checkout main
    ''')

    # Display data

    col1.subheader('Other code')
    col1.code('''

    ''')

    #######################################
    # COLUMN 2
    #######################################

    # Display interactive widgets

    col2.subheader('Other code')
    col2.code('''

    ''')

    col2.code('''

    ''')
    col2.code('''

              ''')

    # Build chat-based apps

    col2.subheader('More Code')
    col2.code('''
    
''')

    col2.markdown(
        '<small>Learn how to [build chat-based apps](https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps)</small>',
        unsafe_allow_html=True)

    return None


# Run main()

if __name__ == '__main__':
    main()