def contributions(df):
  import streamlit as st
  import pandas as pd
  
  df = df.rename(columns = {
          'STAT_YEAR': 'Year',
          'TITHES_OFFERINGS': 'TithesOfferings', 'SPECIAL_CAUSES': 'SpecialCauses', 
          'BUILDING_FUND_OFFERING': 'BuildingFindOffering', 'OTHER_CONTRIB': 'OtherContrib', 
          'TOTAL_CONTRIB': 'TotalContrib', 
          'OTHER_INCOME': 'OtherIncome', 'TOTAL_CHURCH_INCOME': 'TotalChurchIncome',
  }
                )


                            
  over_df = df[['Year', 'TotalContrib', 'TotalChurchIncome']].melt(id_vars=['Year'], var_name='Metric', value_name='Dollars')
  contrib_df = df[['Year', 'TithesOfferings', 'SpecialCauses', 'BuildingFindOffering', 'OtherContrib', 'OtherIncome']].melt(id_vars=['Year'], var_name='Metric', value_name='Dollars')

  st.subheader('Church Income Trends')
  st.bar_chart(over_df.groupby(['Year', 'Metric'])['Dollars'].sum().reset_index(), x = 'Year', y = 'Dollars', color = 'Metric', stack = False)

  st.subheader('Contributions Breakdown')
  st.bar_chart(contrib_df.groupby(['Year', 'Metric'])['Dollars'].sum().reset_index(), x = 'Year', y = 'Dollars', color = 'Metric', stack = False)
