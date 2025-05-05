import streamlit as st

home_page = st.Page(
  'pages/home.py', 
  title = 'Home', 
  icon=":material/home:", 
  default=True
)

dashreport_page = st.Page(
  'pages/dashboards.py', 
  title = 'PCA Dashboard Reports', 
  icon=":material/analytics:", 
  default=False
)

map_page = st.Page(
  'pages/pca_church_map.py', 
  title = 'PCA Churches Map', 
  icon=":material/map:", 
  default=False
)


# navigation 
pg = st.navigation(
        {
            "": [home_page],
            "Data Reports": [dashreport_page, map_page],
          
        }
    )

pg.run()
