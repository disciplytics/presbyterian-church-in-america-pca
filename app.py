import streamlit as st

home_page = st.Page(
  'pages/home.py', 
  title = 'Home', 
  icon=":material/home:", 
  default=True
)

report_2024_page = st.Page(
  'pages/report_2024.py', 
  title = 'Technical Reports', 
  icon=":material/lab_profile:", 
  default=False
)

# navigation 
pg = st.navigation(
        {
            "": [home_page],
            "Technical Reports": [report_2024],
          
        }
    )

pg.run()
