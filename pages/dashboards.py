import streamlit as st
from numpy import sort
# set page configs
st.set_page_config(
    page_title="PCA Dashboards",
    layout="wide",
    page_icon = 'https://jimdo-storage.freetls.fastly.net/image/446612637/7c401e7a-6b6d-4ec8-84a5-4ab2cae82c9e.png?quality=80,90&auto=webp&disable=upscale&width=1024&height=576&trim=0,0,0,0',
)

# LOGO
st.image("https://media.licdn.com/dms/image/v2/D4E16AQGCrog5mV8nBQ/profile-displaybackgroundimage-shrink_350_1400/B4EZUAA8ZzHgAY-/0/1739462002589?e=1744848000&v=beta&t=miQyzZN82YjcYs9B_Mc-UVhaKt01dqVnPE56CnaVPbw",
        width = 250)

# title
st.title('PCA Dashboards', help = 'This page offers visualizations of the PCA Statistics for improved reporting')
st.caption('Reports are maintained by [Disciplytics, LLC](https://www.disciplytics.com/)')

# connect to snowflake
@st.cache_data(show_spinner=False)
def load_stats_data():
    sql = 'SELECT * FROM PCA_STATISTICS;'
    conn = st.connection("snowflake")
    return conn.query(sql, ttl=0, show_spinner = False)

stats_df = load_stats_data()

# query data

def query_data(df):
    df['STATE']=df['STATE'].fillna('No State Reported')
    df['CITY']=df['CITY'].fillna('No City Reported')
    df['CHURCH']=df['CHURCH'].fillna('No Church Reported')

    # BUILD STATE FILTER
    # get filter options for state
    state_options = sort(df['STATE'].unique())
    # streamlit object for state filter
    state_sel = st.multiselect('Select a State', state_options)
    st.write(state_sel)

    # BUILD CITY FILTER IF STATE IS FILTERED 
    city_sel = None
    
    if len(state_sel) > 0:
        filtered_df = df[df['STATE'].isin(state_sel)]
        city_options = sort(df['CITY'].unique())
        city_sel = st.multiselect('Select a City', city_options)
        st.write(city_sel)
        
    # BUILD CHURCH FILTER IF STATE IS FILTERED 
    if city_sel:
        filtered_df = df[(df['STATE'].isin(state_sel)) & (df['CITY'].isin(city_sel))]
        church_options = sort(df['CHURCH'].unique())
        church_sel = st.multiselect('Select a Church', church_options)
        st.write(church_sel)

    return filtered_df
filtered_df = query_data(stats_df)   

st.dataframe(filtered_df)
st.dataframe(stats_df)

