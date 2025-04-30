def analysis_layout(data):
      from pandas import to_numeric, pivot_table
      import altair as alt
      import streamlit as st

      def get_analysis(data, variables):
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
                      x=alt.X("Variable:N", axis=alt.Axis(labelLimit=300)).title(""),
                      color=alt.value("#4682b4")
                  )
          
            bar = alt.Chart().mark_point(filled=True,color="black").encode(
                      alt.Y("Estimate:Q"),
                      alt.X("Variable:N", axis=alt.Axis(labelLimit=300)).title(""),
                  ).properties(width=300,height=200)
      
            st.altair_chart(alt.layer(bar, error, data=data).facet(column='Area:N'))
            
      st.markdown('### Income Reports')
      st.markdown('\n\n')
      st.markdown('##### Income Inequality: Gini Index')
      st.caption('Click here to learn more about this metric: [Gini Index](https://www.census.gov/topics/income-poverty/income-inequality/about/metrics/gini-index.html)')
        
      get_analysis(data, ['B19083_001M_5YR', 'B19083_001E_5YR'])

      st.markdown('\n\n')
      st.markdown('##### Household Income')
        
      get_analysis(data, ['B19202_001E_5YR_2023','B19202_001M_5YR_2023','B19013_001E_5YR_2023','B19013_001M_5YR_2023','B19113_001E_5YR_2023','B19113_001M_5YR_2023'])
        
      st.dataframe(data)
