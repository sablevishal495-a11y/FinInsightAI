import streamlit as st


def show_message(message):

    if message["role"] == "user":

        with st.chat_message("user"):

            st.markdown(message["content"])

    else:

        with st.chat_message("assistant"):

            st.markdown(message["content"])

            if "sources" in message:

                pages = sorted(
                    {
                        str(source["page"])
                        for source in message["sources"]
                        if "page" in source
                    },
                    key=int
                )

                if pages:

                    st.markdown("#### 📚 Source Pages")

                    cols = st.columns(len(pages))

                    for i, page in enumerate(pages):

                        cols[i].success(f"Page {page}")