import streamlit as st
from page_components.utils.query_data import query_data
from page_components.analyses.membership import membership

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
# load the data
stats_df = load_stats_data()
# provide option to query data
try:
    report_df = st.dataframe(query_data(stats_df))
except:
    report_df = stats_df.copy()

# begin data viz
mem_tab, gen_tab, school_tab, contrib_tab, disburs_tab = st.tabs(['Membership', 'General Data', 'Christian Schools', 'Contributions', 'Disbursements'])

with mem_tab:
    membership(report_df)
    
