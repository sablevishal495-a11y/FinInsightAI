import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        .block-container{
            padding-top:2rem;
            padding-bottom:2rem;
            max-width:1100px;
        }

        h1{
            text-align:center;
        }

        div.stButton > button{
            width:100%;
            border-radius:10px;
            height:50px;
            font-size:16px;
            font-weight:600;
        }

        div.stFileUploader{
            border:2px dashed #4CAF50;
            border-radius:10px;
            padding:15px;
        }

        .stChatMessage{
            border-radius:12px;
        }

        footer{
            visibility:hidden;
        }

        #MainMenu{
            visibility:hidden;
        }

        header{
            visibility:hidden;
        }

        </style>
        """,
        unsafe_allow_html=True
    )