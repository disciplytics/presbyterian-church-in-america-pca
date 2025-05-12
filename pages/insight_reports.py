import streamlit as st
import pydeck as pdk
from json import loads

from utils.get_analysis import analysis_layout

# set page configs
st.set_page_config(
    page_title="Community Insight Reports",
    layout="wide",
    page_icon = 'https://jimdo-storage.freetls.fastly.net/image/446612637/7c401e7a-6b6d-4ec8-84a5-4ab2cae82c9e.png?quality=80,90&auto=webp&disable=upscale&width=1024&height=576&trim=0,0,0,0',
)

# title
st.title('Community Insight Reports', help='This page offers community insights for each church. Great for ministry identification and evaluation.')
st.caption('Reports are maintained by [Disciplytics, LLC](https://www.disciplytics.com/) and community data is generated from the [American Community Survey](https://www.census.gov/programs-surveys/acs/about.html)')


    
