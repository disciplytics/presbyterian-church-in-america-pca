import streamlit as st
# set page configs
st.set_page_config(
    page_title="PCA Analytics",
    layout="wide",
    page_icon = 'https://jimdo-storage.freetls.fastly.net/image/446612637/7c401e7a-6b6d-4ec8-84a5-4ab2cae82c9e.png?quality=80,90&auto=webp&disable=upscale&width=1024&height=576&trim=0,0,0,0',
)

# title
st.title('PCA Statistics Analysis :church:', help = 'All data is from [The PCA](https://presbyteryportal.pcanet.org/Report/StatsReport)')
st.caption('App and analysis is maintained by [Disciplytics, LLC](https://www.disciplytics.com/).')


st.markdown('''
        ##### Welcome to the PCA Statistics Analysis App!
        The goal of this app is to report the PCA statistics in a meaningful way, 
        to provide the PCA with community data from the US Census, 
        and to use advanced analytics to explain changes in key metrics.

        At [Disciplytics, LLC](https://www.disciplytics.com/), we serve the Church using data analytics and AI. 
        
        If you would like to reach out to the team, please contact us [here](https://www.disciplytics.com/contact/).
    
        Happy digging!
        '''
           )
