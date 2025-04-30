import streamlit as st
import pydeck as pdk
from json import loads
from pandas import to_numeric, pivot_table
import altair as alt

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
                first_geo_name_sel = st.selectbox(f"Base {first_geo_sel} Selection: ", first_geo_name_options['GEO_NAME'], index = 0)
        
        with second:
            # get geographical rel levels
            second_geo_rel_options = conn.query(f"SELECT DISTINCT RELATED_GEO_NAME FROM  DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA ORDER BY RELATED_GEO_NAME ASC;", ttl=0, show_spinner = False)
            second_geo_rel_sel = st.pills("Select Compare State:", second_geo_rel_options['RELATED_GEO_NAME'], selection_mode="single", key =5,  default = 'Ohio')
                
            # get geographical levels
            second_geo_options = conn.query("SELECT DISTINCT LEVEL FROM  DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA;", ttl=0, show_spinner = False)
            second_geo_sel = st.pills("Select Compare Geographical Levels: ", second_geo_options['LEVEL'], selection_mode="single", key = 6,  default = 'County')
                
            if second_geo_sel:
                # get geographical names
                second_geo_name_options = conn.query(f"SELECT DISTINCT GEO_NAME FROM  DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA WHERE LEVEL = '{second_geo_sel}' AND RELATED_GEO_NAME = '{second_geo_rel_sel}' ORDER BY GEO_NAME ASC;", ttl=0, show_spinner = False)
                second_geo_name_sel = st.selectbox(f"Compare {second_geo_sel} Selection: ", second_geo_name_options['GEO_NAME'], index = 1)
        
        # connect to snowflake
        @st.cache_data(show_spinner=f"Generating comparative analysis for {first_geo_name_sel}, {first_geo_rel_sel} and {second_geo_name_sel}, {second_geo_rel_sel}.")
        def load_acs_data(state_base, state_compare, geo_base, geo_compare):
            if state_base == state_compare and geo_base == geo_compare:
                sql = f"SELECT * FROM DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA WHERE RELATED_GEO_NAME = '{state_base}' AND GEO_NAME = '{geo_base}';"
                
            elif state_base == state_compare and geo_base != geo_compare:
                sql = f"SELECT * FROM DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA WHERE RELATED_GEO_NAME = '{state_base}' AND GEO_NAME IN ('{geo_base}', '{geo_compare}');"

            elif state_base != state_compare and geo_base == geo_compare:
                sql = f"SELECT * FROM DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA WHERE RELATED_GEO_NAME IN ('{state_base}', '{state_compare}') AND GEO_NAME = '{geo_base}';"

            elif state_base != state_compare and geo_base != geo_compare:
                sql = f"SELECT * FROM DISCIPLYTICS_APP.COMMUNITY_DATA.ACS_5YR_DATA WHERE RELATED_GEO_NAME IN  ('{state_base}', '{state_compare}') AND GEO_NAME IN ('{geo_base}', '{geo_compare}');"
                
            return conn.query(sql, ttl=0, show_spinner = False)

    except:
        st.write('Make the above selections.') 
        # load the data
    if first_geo_rel_sel and second_geo_rel_sel and first_geo_name_sel and second_geo_name_sel:
        acs_df_comp = load_acs_data(
                            first_geo_rel_sel,
                            second_geo_rel_sel,
                            first_geo_name_sel, 
                            second_geo_name_sel
                                    )

        with first:
                # convert to dictionary
            geojson_dict_first = loads(acs_df_comp[acs_df_comp['GEO_NAME'] == first_geo_name_sel].head(1)['GEOJSON_VALUES'].reset_index(drop=True)[0])
                    
                # create the GeoJson layer
            geojson_layer_first = pdk.Layer(
                        "GeoJsonLayer",
                        geojson_dict_first,
                        opacity=0.3,
                        stroked=False,
                        filled=True,
                        extruded=True,
                        wireframe=True,
                        get_elevation="20",
                        get_fill_color="[137, 207, 240]",
                        get_line_color=[255, 255, 255],
                    )
                    
            INITIAL_VIEW_STATE_FIRST = pdk.ViewState(latitude=geojson_dict_first['coordinates'][0][0][1], longitude=geojson_dict_first['coordinates'][0][0][0], zoom=9, max_zoom=16, pitch=45, bearing=0)
                    
                # create the pydeck using the geojson layer
            r_first = pdk.Deck(layers=[ geojson_layer_first ], map_style=None, initial_view_state=INITIAL_VIEW_STATE_FIRST)
                # display the pydeck
            st.pydeck_chart(r_first)

        with second:
                # convert to dictionary
            geojson_dict_second = loads(acs_df_comp[acs_df_comp['GEO_NAME'] == second_geo_name_sel].head(1)['GEOJSON_VALUES'].reset_index(drop=True)[0])
                    
                # create the GeoJson layer
            geojson_layer_second = pdk.Layer(
                        "GeoJsonLayer",
                        geojson_dict_second,
                        opacity=0.3,
                        stroked=False,
                        filled=True,
                        extruded=True,
                        wireframe=True,
                        get_elevation="20",
                        get_fill_color="[137, 207, 240]",
                        get_line_color=[255, 255, 255],
                    )
                    
            INITIAL_VIEW_STATE_SECOND = pdk.ViewState(latitude=geojson_dict_second['coordinates'][0][0][1], longitude=geojson_dict_second['coordinates'][0][0][0], zoom=9, max_zoom=16, pitch=45, bearing=0)
                    
                # create the pydeck using the geojson layer
            r_second = pdk.Deck(layers=[ geojson_layer_second ], map_style=None, initial_view_state=INITIAL_VIEW_STATE_SECOND)
                # display the pydeck
            st.pydeck_chart(r_second)


        def get_analysis(data, variables):
            ''' pass the dataframe with the analysis data and the variables to do the analysis on. '''
            data = data[data['VARIABLE'].isin(variables)]
            
            data['Value'] = to_numeric(data['VALUE'])
            data = data.rename(columns={'VARIABLE_NAME': 'Variable', 'GEO_NAME': 'Area'})
            
            data = data.pivot_table('Value', ['Area'], 'MEASUREMENT_TYPE').reset_index()

            st.dataframe(data)
    
            error = alt.Chart().mark_errorbar(ticks=True).encode(
                y=alt.Y("Estimate:Q").scale(zero=False).title(""),
                yError=("Margin of Error:Q"),
                x=alt.X("Area:N"),
                color=alt.value("#4682b4")
            )
    
            bar = alt.Chart().mark_bar().encode(
                alt.Y("Estimate:Q"),
                alt.X("Area:N"),
            ).properties(width=300,height=150)
            
            st.altair_chart(alt.layer(bar, error, data=data))


        st.markdown('### Income Reports')
        st.markdown('\n\n')
        st.markdown('##### Income Inequality: Gini Index')
        st.caption('Click here to learn more about this metric: [Gini Index](https://www.census.gov/topics/income-poverty/income-inequality/about/metrics/gini-index.html)')
        
        get_analysis(acs_df_comp, ['B19083_001M_5YR', 'B19083_001E_5YR'])

        st.markdown('\n\n')
        st.markdown('##### Household Income')
        
        get_analysis(acs_df_comp, ['B19202_001E_5YR_2023','B19202_001M_5YR_2023','B19013_001E_5YR_2023','B19013_001M_5YR_2023','B19113_001E_5YR_2023','B19113_001M_5YR_2023'])


        

        
        st.dataframe(acs_df_comp)
