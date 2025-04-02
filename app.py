import streamlit as st
# set page configs
st.set_page_config(
    page_title="PCA Analytics",
    layout="wide",
    page_icon = 'https://jimdo-storage.freetls.fastly.net/image/446612637/7c401e7a-6b6d-4ec8-84a5-4ab2cae82c9e.png?quality=80,90&auto=webp&disable=upscale&width=1024&height=576&trim=0,0,0,0',
)

# title
st.title('PCA Statistics Analysis :church:', help = 'All data is from [The PCA](https://presbyteryportal.pcanet.org/Report/StatsReport)')
st.caption('App and analysis is maintained by [Disciplytics, LLC](https://www.disciplytics.com/)')


# click to learn more expander
with st.expander("2024 PCA Statistics Technical Report"):
    st.markdown('''
        ##### Welcome to the PCA Statistics Analysis App!
        If you would like to reach out to the team, please contact us [here](https://www.disciplytics.com/contact/).
    
        While you can take a tour of the analysis by clicking through the app, you can also read the technical report below.
    
        ##### Title page
        
        ##### Acknowledgements
        
        ##### Summary
        
        ##### Table of Contents
        
        ##### Introduction/Terms of Reference/Scope
        
        ##### Procedure
        
        ##### Findings
        
        ##### Conclusions
        
        ##### Recommendations
        
        ##### References/Bibliography
        
        ##### Appendices
    
    
        '''
    )
