import streamlit as st
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


# get filter options
state_options = stats_df['STATE'].fillna('No State Reported').unique().sort()

state_sel = st.multiselect('Select a State', state_options)
st.write(state_sel)
st.dataframe(stats_df)
