def contributions(df):
  import streamlit as st
  import pandas as pd
  
  df = df.rename(columns = {
          'YEAR': 'Year',
          'TITHESOFFERINGS': 'TithesOfferings', 'SPECIALCAUSES': 'SpecialCauses', 
          'BUILDINGFUNDOFFERING': 'BuildingFindOffering', 'OTHERCONTRIB': 'OtherContrib', 
          'TOTALCONTRIB': 'TotalContrib', 
          'OTHERINCOME': 'OtherIncome', 'TOTALCHURCHINCOME': 'TotalChurchIncome',
  }
                )


                            
  over_df = df[['Year', 'TotalContrib', 'TotalChurchIncome']].melt(id_vars=['Year'], var_name='Metric', value_name='Dollars')
  contrib_df = df[['Year', 'TithesOfferings', 'SpecialCauses', 'BuildingFindOffering', 'OtherContrib', 'OtherIncome']].melt(id_vars=['Year'], var_name='Metric', value_name='Dollars')

  st.subheader('Church Income Trends')
  st.bar_chart(over_df.groupby(['Year', 'Metric'])['Dollars'].sum().reset_index(), x = 'Year', y = 'Dollars', color = 'Metric', stack = False)

  st.subheader('Contributions Breakdown')
  st.bar_chart(contrib_df.groupby(['Year', 'Metric'])['Dollars'].sum().reset_index(), x = 'Year', y = 'Dollars', color = 'Metric', stack = False)
