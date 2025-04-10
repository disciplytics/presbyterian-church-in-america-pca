def query_data(df):
    from numpy import sort
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
        city_options = sort(filtered_df['CITY'].unique())
        city_sel = st.multiselect('Select a City', city_options)
        st.write(city_sel)
        
    # BUILD CHURCH FILTER IF STATE IS FILTERED 
    if city_sel:
        filtered_df = df[(df['STATE'].isin(state_sel)) & (df['CITY'].isin(city_sel))]
        church_options = sort(filtered_df['CHURCH'].unique())
        church_sel = st.multiselect('Select a Church', church_options)
        st.write(church_sel)

    return filtered_df
