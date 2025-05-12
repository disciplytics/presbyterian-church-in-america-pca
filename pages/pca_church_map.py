import streamlit as st
from numpy import sort
# set page configs
st.set_page_config(
    page_title="PCA Churches Map",
    layout="wide",
    page_icon = 'https://jimdo-storage.freetls.fastly.net/image/446612637/7c401e7a-6b6d-4ec8-84a5-4ab2cae82c9e.png?quality=80,90&auto=webp&disable=upscale&width=1024&height=576&trim=0,0,0,0',
)

# title
st.title('PCA Church Map', help = 'All data is from [The PCA Directory](https://presbyteryportal.pcanet.org/ac/directory/)')
st.caption('App and analysis is maintained by [Disciplytics, LLC](https://www.disciplytics.com/)')

# connect to snowflake
@st.cache_data(show_spinner=False)
def load_directory_data():
    sql = 'SELECT * FROM PCA_CHURCH_DIRECTORY;'
    conn = st.connection("snowflake")
    df =  conn.query(sql, ttl=0, show_spinner = False)
    # rename data
    rename_dict = {
            'CHURCH_NAME': 'Church Name',
            'CITY': 'City',
            'STATE': 'State',
            'PHONE': 'Phone',
            'EMAIL': 'Email',
            'WEBSITE': 'Website',
            'PRESBYTERY': 'Presbytery',
            'PASTOR': 'Pastor',
            'MAILING_ADDRESS': 'Mailing Address',
            'MEETING_ADDRESS': 'Meeting Address',
            'FAX': 'Fax',
            'MEETING_ADDRESSES': 'Meeting Addresses',
            'ATTN': 'Attn',
            'STREET': 'Street',
            'ZIP': 'Zip',
            #'GCODE',
            #'LATITUDE',
            #'LONGIvTUDE'
    }

    df = df.rename(columns = rename_dict)
    return df[['Church Name', 'State', 'City', 'Pastor', 'Presbytery', 'Meeting Address', 'Website', 'LATITUDE', 'LONGITUDE']]
    
# load the data
directory_df = load_directory_data()

state_sel = st.selectbox('Select a State', sort(directory_df['State'].unique()), None)

if state_sel:
    map_df = directory_df[(directory_df['LATITUDE'].isna()==False) 
                        & (directory_df['State']==state_sel)]
else:
    map_df = directory_df[(directory_df['LATITUDE'].isna()==False)] 
    
st.markdown('#### Church Map')
st.map(map_df)

st.markdown('#### Church Directory')
st.dataframe(map_df.drop(columns=['LATITUDE', 'LONGITUDE']).set_index(['Church Name']))
