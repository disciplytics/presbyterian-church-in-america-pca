import streamlit as st
import pydeck as pdk
from json import loads
# set page configs
st.set_page_config(
    page_title="Community Insight Reports",
    layout="wide",
    page_icon = 'https://jimdo-storage.freetls.fastly.net/image/446612637/7c401e7a-6b6d-4ec8-84a5-4ab2cae82c9e.png?quality=80,90&auto=webp&disable=upscale&width=1024&height=576&trim=0,0,0,0',
)

# title
st.title('Community Insight Reports', help='This page offers community insights for each church. Great for ministry identification and evaluation.')
st.caption('Reports are maintained by [Disciplytics, LLC](https://www.disciplytics.com/) and community data is generated from the [American Community Survey](https://www.census.gov/programs-surveys/acs/about.html)')

# connect to snowflake
conn = st.connection("snowflake")

# get geographical rel levels
geo_rel_options = conn.query(f"SELECT DISTINCT RELATED_GEO_NAME FROM  DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA ORDER BY RELATED_GEO_NAME ASC;", ttl=0, show_spinner = False)
geo_rel_sel = st.pills("State: Select One to Get Started", geo_rel_options['RELATED_GEO_NAME'], selection_mode="single")

# get geographical levels
geo_options = conn.query("SELECT DISTINCT LEVEL FROM  DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA;", ttl=0, show_spinner = False)
geo_sel = st.pills("Geographical Levels: Select One to drill down", geo_options['LEVEL'], selection_mode="single")

if geo_sel:
    # get geographical names
    geo_name_options = conn.query(f"SELECT DISTINCT GEO_NAME FROM  DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA WHERE LEVEL = '{geo_sel}' AND RELATED_GEO_NAME = '{geo_rel_sel}' ORDER BY GEO_NAME ASC;", ttl=0, show_spinner = False)
    geo_name_sel = st.selectbox(f"{geo_sel} Selection", geo_name_options['GEO_NAME'])


# connect to snowflake
@st.cache_data(show_spinner=f"Generating community analysis for {geo_name_sel}, {geo_rel_sel}.")
def load_acs_data(level, state, geo):
    sql = f"SELECT * FROM DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA WHERE LEVEL = '{level}' AND RELATED_GEO_NAME = '{state}' AND GEO_NAME = '{geo}' LIMIT 10;"
    return conn.query(sql, ttl=0, show_spinner = False)
# load the data
if geo_sel and geo_rel_sel:
    acs_df = load_acs_data(geo_sel, geo_rel_sel, geo_name_sel)
    
    st.dataframe(acs_df)
'''
conn = st.connection("snowflake")
# get geojson for selected area
geojson_sql = "SELECT DISTINCT GEOJSON_VALUES FROM DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA WHERE GEO_NAME IN ('Warren County') "
geojson = conn.query(geojson_sql, ttl=0)

# convert to dictionary
geojson_dict = loads(geojson['GEOJSON_VALUES'][0])

# create the GeoJson layer
geojson_layer = pdk.Layer(
    "GeoJsonLayer",
    geojson_dict,
    opacity=0.3,
    stroked=False,
    filled=True,
    extruded=True,
    wireframe=True,
    get_elevation="20",
    get_fill_color="[137, 207, 240]",
    get_line_color=[255, 255, 255],
)

INITIAL_VIEW_STATE = pdk.ViewState(latitude=geojson_dict['coordinates'][0][0][1], longitude=geojson_dict['coordinates'][0][0][0], zoom=9, max_zoom=16, pitch=45, bearing=0)

# create the pydeck using the geojson layer
r = pdk.Deck(layers=[ geojson_layer ], map_style=None, initial_view_state=INITIAL_VIEW_STATE)

# display the pydeck
st.pydeck_chart(r)


# get geojson for selected area
geojson_sql = "SELECT GEOJSON_VALUES FROM DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA WHERE GEO_NAME = '44883' LIMIT 1"
geojson = conn.query(geojson_sql, ttl=0)

# convert to dictionary
geojson_dict = loads(geojson['GEOJSON_VALUES'][0])

# create the GeoJson layer
geojson_layer = pdk.Layer(
    "GeoJsonLayer",
    geojson_dict,
    opacity=0.3,
    stroked=False,
    filled=True,
    extruded=True,
    wireframe=True,
    get_elevation="20",
    get_fill_color="[137, 207, 240]",
    get_line_color=[255, 255, 255],
)

INITIAL_VIEW_STATE = pdk.ViewState(latitude=geojson_dict['coordinates'][0][0][1], longitude=geojson_dict['coordinates'][0][0][0], zoom=9, max_zoom=16, pitch=45, bearing=0)

# create the pydeck using the geojson layer
r = pdk.Deck(layers=[ geojson_layer ], map_style=None, initial_view_state=INITIAL_VIEW_STATE)

# display the pydeck
st.pydeck_chart(r)
'''
