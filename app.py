import streamlit as st

home_page = st.Page(
  'pages/home.py', 
  title = 'home', 
  icon=":material/home:", 
  default=True
)

# navigation 
pg = st.navigation(
        {
            "": [home_page],
          
        }
    )

pg.run()
