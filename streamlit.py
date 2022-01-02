import pandas as pd
import streamlit as st


option = st.sidebar.selectbox(('Choose a Data'), ("Years" , "Production", "Certificate", "Stars"))


if option == "Years":
    st.write('#### Movie Years')
    year = pd.read_csv('Database/year.csv')
    year = year['Year'].value_counts()
    st.area_chart(year)
    st.table(year)

elif option == "Production":
    st.write('#### Movies Productions')
    production = pd.read_csv('Database/production.csv')
    production = production['Production'].value_counts()
    st.area_chart(production)
    st.table(production)

elif option == "Certificate":
    st.write('#### Movie Certificate')
    certificate = pd.read_csv('Database/certificate.csv')
    certificate = certificate['Certificate'].value_counts()
    st.bar_chart(certificate)
    st.table(certificate)

elif option == "Stars":
    st.write('#### Movie Stars')
    stars = pd.read_csv('Database/stars.csv')
    stars = stars['Stars'].value_counts()
    st.bar_chart(stars)
    st.table(stars)






hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        button[title="View fullscreen"] {
        display: none;
        }
        button[title="View fullscreen"]:hover {
        display: none;
        }
        summary{
            display: none;
        }
        summary:hover{
            display: none;
        }
        </style>
        """
st.markdown(hide_st_style, unsafe_allow_html=True)


