def membership(df):
  import streamlit as st
  import pandas as pd

  df['Total Members'] = df['COMM'] + df['NONCOMM']
  df['Total Additions'] = df['PROFCHILD'] + df['PROFADULT'] + df['TRANSLETTER'] + df['REAFFIRMATION'] + df['RESTORED']

  df = df.rename(columns = {
          'YEAR': 'Year',
          'COMM': 'Comm', 'NONCOMM': 'NonComm', 
          'PROFCHILD': 'ProfChild', 'PROFADULT': 'ProfAdult', 'TRANSLETTER': 'TransLetter', 'REAFFIRMATION': 'Reaffirmation', 'RESTORED': 'Restored',
  
  }
                )
                            
  mems_df = df[['Year', 'Comm', 'NonComm', 'Total Members']].melt(id_vars=['Year'], var_name='Metric', value_name='Count')
  adds_df = df[['Year', 'ProfChild', 'ProfAdult', 'TransLetter', 'Reaffirmation', 'Restored', 'Total Additions']].melt(id_vars=['Year'], var_name='Metric', value_name='Count')

  st.subheader('Total Member Trends')
  st.bar_chart(mems_df.groupby(['Year', 'Metric'])['Count'].sum().reset_index(), x = 'Year', y = 'Count', color = 'Metric', stack = False)

  st.subheader('Member Additions')
  st.bar_chart(adds_df.groupby(['Year', 'Metric'])['Count'].sum().reset_index(), x = 'Year', y = 'Count', color = 'Metric', stack = False)
  
