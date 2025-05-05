import streamlit as st
# set page configs
st.set_page_config(
    page_title="PCA Churches Map",
    layout="wide",
    page_icon = 'https://jimdo-storage.freetls.fastly.net/image/446612637/7c401e7a-6b6d-4ec8-84a5-4ab2cae82c9e.png?quality=80,90&auto=webp&disable=upscale&width=1024&height=576&trim=0,0,0,0',
)

# title
st.title('PCA Church Map', help = 'All data is from [The PCA Directory](https://presbyteryportal.pcanet.org/ac/directory/)')
st.caption('App and analysis is maintained by [Disciplytics, LLC](https://www.disciplytics.com/)')
