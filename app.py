import streamlit as st

home_page = st.Page(
  'pages/home.py', 
  title = 'Home', 
  icon=":material/home:", 
  default=True
)

report_page = st.Page(
  'pages/tech_reports.py', 
  title = 'PCA Technical Reports', 
  icon=":material/lab_profile:", 
  default=False
)

# navigation 
pg = st.navigation(
        {
            "": [home_page],
            "Technical Reports": [report_page],
          
        }
    )

pg.run()
