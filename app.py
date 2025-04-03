import streamlit as st

home_page = st.Page(
  'pages/home.py', 
  title = 'Home', 
  icon=":material/home:", 
  default=True
)

techreport_page = st.Page(
  'pages/technical_reports.py', 
  title = 'PCA Technical Reports', 
  icon=":material/lab_profile:", 
  default=False
)

dashreport_page = st.Page(
  'pages/dashboards.py', 
  title = 'PCA Dashboard Reports', 
  icon=":material/analytics:", 
  default=False
)

# navigation 
pg = st.navigation(
        {
            "": [home_page],
            "PCA Reports": [techreport_page, dashreport_page],
          
        }
    )

pg.run()
