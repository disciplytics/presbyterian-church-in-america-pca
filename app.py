import streamlit as st

home_page = st.Page(
  'pages/home.py', 
  title = 'Home', 
  icon=":material/home:", 
  default=True
)

community_insight_page = st.Page(
  'pages/insight_reports.py', 
  title = 'PCA Insight Reports', 
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
            "Data Reports": [dashreport_page, community_insight_page],
          
        }
    )

pg.run()
