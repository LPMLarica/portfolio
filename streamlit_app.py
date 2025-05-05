import streamlit as st

about_page=st.Page(
    page="views/about_me.py",
    title="About Me",
    icon= ":material/account_circle:",
    default=True
)

project_2_page=st.Page(
    page="views/chatbot.py",
    title="Chat",
    icon= ":material/smart_toy:",
)

pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [ project_2_page],
    }
)

pg.run()