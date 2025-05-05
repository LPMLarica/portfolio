import streamlit as st
import os
from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("assets\profile_image.jpg", width=230)

with col2:
    st.title("Larissa Campos", anchor=False)
    st.write(
        "Junior FrontEnd Developer, Data Analyst and Machine Learning enthusiast"
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()



st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - Bachelor of Science in Computer Science - UNITRI (2027)
    - Fluent in Portuguese and English by Cultura Inglesa
    - 1 year of experience in FrontEnd Development
    - 2 years of experience in Unity 3D
    """
)


st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python (Scikit-learn, Pandas, streamlit), SQL, HTML, CSS, JavaScript
    - Data Visualization: PowerBi, Plotly
    - Modeling: Logistic regression, linear regression, decision trees
    - Databases: Postgres, MongoDB, MySQL
    """
)