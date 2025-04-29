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

single_tab, compare_tab = st.tabs(['Single Area', 'Compare Two Areas'])

with single_tab:
    try:
        # get geographical rel levels
        geo_rel_options = conn.query(f"SELECT DISTINCT RELATED_GEO_NAME FROM  DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA ORDER BY RELATED_GEO_NAME ASC;", ttl=0, show_spinner = False)
        geo_rel_sel = st.pills("State: Select One to Get Started", geo_rel_options['RELATED_GEO_NAME'], selection_mode="single", default = 'Ohio', key = 1)
        
        # get geographical levels
        geo_options = conn.query("SELECT DISTINCT LEVEL FROM  DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA;", ttl=0, show_spinner = False)
        geo_sel = st.pills("Geographical Levels: Select One to drill down", geo_options['LEVEL'], selection_mode="single", default = 'City', key = 2)
        
        if geo_sel:
            # get geographical names
            geo_name_options = conn.query(f"SELECT DISTINCT GEO_NAME FROM  DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA WHERE LEVEL = '{geo_sel}' AND RELATED_GEO_NAME = '{geo_rel_sel}' ORDER BY GEO_NAME ASC;", ttl=0, show_spinner = False)
            geo_name_sel = st.selectbox(f"{geo_sel} Selection", geo_name_options['GEO_NAME'], index=0)

    
        # connect to snowflake
        @st.cache_data(show_spinner=f"Generating community analysis for {geo_name_sel}, {geo_rel_sel}.")
        def load_acs_data_single(level, state, geo):
            sql = f"SELECT * FROM DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA WHERE LEVEL = '{level}' AND RELATED_GEO_NAME = '{state}' AND GEO_NAME = '{geo}';"
            return conn.query(sql, ttl=0, show_spinner = False)
        # load the data
        if geo_sel and geo_rel_sel:
            acs_df = load_acs_data_single(geo_sel, geo_rel_sel, geo_name_sel)
    
        # convert to dictionary
        geojson_dict = loads(acs_df.head(1)['GEOJSON_VALUES'][0])
            
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
        
        st.dataframe(acs_df)
    except:
        st.write('Make the above selections.')


with compare_tab:
    first, second = st.columns(2)
    try:
        with first:
            # get geographical rel levels
            first_geo_rel_options = conn.query(f"SELECT DISTINCT RELATED_GEO_NAME FROM  DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA ORDER BY RELATED_GEO_NAME ASC;", ttl=0, show_spinner = False)
            first_geo_rel_sel = st.pills("Select Base State: ", first_geo_rel_options['RELATED_GEO_NAME'], selection_mode="single", default = 'Ohio', key = 3)
            
            # get geographical levels
            first_geo_options = conn.query("SELECT DISTINCT LEVEL FROM  DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA;", ttl=0, show_spinner = False)
            first_geo_sel = st.pills("Select Base Geographical Levels: ", first_geo_options['LEVEL'], selection_mode="single", default = 'County', key = 4)
            
            if first_geo_sel:
                # get geographical names
                first_geo_name_options = conn.query(f"SELECT DISTINCT GEO_NAME FROM  DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA WHERE LEVEL = '{first_geo_sel}' AND RELATED_GEO_NAME = '{first_geo_rel_sel}' ORDER BY GEO_NAME ASC;", ttl=0, show_spinner = False)
                first_geo_name_sel = st.selectbox(f"Base {first_geo_sel} Selection", first_geo_name_options['GEO_NAME'], index = 0)
    except:
        st.write('Make the above selections.') 
        
    with second:
        # get geographical rel levels
        second_geo_rel_options = conn.query(f"SELECT DISTINCT RELATED_GEO_NAME FROM  DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA ORDER BY RELATED_GEO_NAME ASC;", ttl=0, show_spinner = False)
        second_geo_rel_sel = st.pills("Select Compare State", second_geo_rel_options['RELATED_GEO_NAME'], selection_mode="single", key =5,  default = 'Ohio')
            
        # get geographical levels
        second_geo_options = conn.query("SELECT DISTINCT LEVEL FROM  DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA;", ttl=0, show_spinner = False)
        second_geo_sel = st.pills("Select Compare Geographical Levels:", second_geo_options['LEVEL'], selection_mode="single", key = 6,  default = 'County')
            
        if second_geo_sel:
            # get geographical names
            second_geo_name_options = conn.query(f"SELECT DISTINCT GEO_NAME FROM  DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA WHERE LEVEL = '{second_geo_sel}' AND RELATED_GEO_NAME = '{second_geo_rel_sel}' ORDER BY GEO_NAME ASC;", ttl=0, show_spinner = False)
            second_geo_name_sel = st.selectbox(f"Compare {second_geo_sel} Selection", second_geo_name_options['GEO_NAME'], index = 1)
    
    # connect to snowflake
    @st.cache_data(show_spinner=f"Generating comparative analysis for {first_geo_name_sel}, {first_geo_rel_sel} and {second_geo_name_sel}, {second_geo_rel_sel}.")
    def load_acs_data(level, state, geo):
        sql = f"SELECT * FROM DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA WHERE LEVEL IN ({level}) AND RELATED_GEO_NAME '{state}' AND GEO_NAME = ({geo});"
        return conn.query(sql, ttl=0, show_spinner = False)
    # load the data
    if first_geo_sel and first_geo_rel_sel and second_geo_sel and second_geo_rel_sel and first_geo_name_sel and second_geo_name_sel:
        acs_df = load_acs_data(
                        first_geo_sel + ',' + second_geo_sel, 
                        first_geo_rel_sel + ',' + second_geo_rel_sel,
                        first_geo_name_sel + ',' + second_geo_name_sel
                                )
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
