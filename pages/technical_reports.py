import streamlit as st
# set page configs
st.set_page_config(
    page_title="PCA Technical Reports",
    layout="wide",
    page_icon = 'https://jimdo-storage.freetls.fastly.net/image/446612637/7c401e7a-6b6d-4ec8-84a5-4ab2cae82c9e.png?quality=80,90&auto=webp&disable=upscale&width=1024&height=576&trim=0,0,0,0',
)

# LOGO
st.image("https://media.licdn.com/dms/image/v2/D4E16AQGCrog5mV8nBQ/profile-displaybackgroundimage-shrink_350_1400/B4EZUAA8ZzHgAY-/0/1739462002589?e=1744848000&v=beta&t=miQyzZN82YjcYs9B_Mc-UVhaKt01dqVnPE56CnaVPbw",
        width = 250)

# title
st.title('PCA Technical Reports', help='This page offers technical breakdowns of the data and findings by [Disciplytics](https://www.disciplytics.com/). Reports are indexed by Stat Year.')
st.caption('Reports are maintained by [Disciplytics, LLC](https://www.disciplytics.com/)')

with st.expander('2024 PCA Technical Report'):
        st.markdown('''    
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
