def get_analysis(data, variables):
      from pandas import to_numeric, pivot_table
      import altair as alt
      ''' pass the dataframe with the analysis data and the variables to do the analysis on. '''
      data = data[data['VARIABLE'].isin(variables)]
            
      data['Value'] = to_numeric(data['VALUE'])
      data = data.rename(columns={'SERIES_LEVEL_1': 'Variable', 'GEO_NAME': 'Area'})
            
      data = data.pivot_table('Value', ['Area', 'Variable'], 'MEASUREMENT_TYPE').reset_index()

      data['Margin of Error'] = data['Margin of Error'].fillna(method='bfill')

      data = data.dropna(subset=['Estimate'])
                
      error = alt.Chart().mark_errorbar(ticks=True).encode(
                y=alt.Y("Estimate:Q").scale(zero=False).title(""),
                yError=("Margin of Error:Q"),
                x=alt.X("Variable:N", axis=alt.Axis(labelAngle=45, labelLimit=400)).title(""),
                color=alt.value("#4682b4")
            )
    
      bar = alt.Chart().mark_point(filled=True,color="black").encode(
                alt.Y("Estimate:Q"),
                alt.X("Variable:N", axis=alt.Axis(labelAngle=45, labelLimit=400)).title(""),
            ).properties(width=300,height=250)

      st.altair_chart(alt.layer(bar, error, data=data).facet(column='Area:N'))
