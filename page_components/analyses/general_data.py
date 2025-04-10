def general_data(df):
  import streamlit as st
  import pandas as pd

  df['Total Members'] = df['COMM'] + df['NONCOMM']
  df['Total Additions'] = df['PROFCHILD'] + df['PROFADULT'] + df['TRANSLETTER'] + df['REAFFIRMATION'] + df['RESTORED']
  df['Total Losses'] = df['DEATH'] + df['TRANS'] + df['REMOVEDFROMROLL'] + df['DISCIPLINE']
  
  df = df.rename(columns = {
          'YEAR': 'Year',
          'COMM': 'Comm', 'NONCOMM': 'NonComm', 
          'PROFCHILD': 'ProfChild', 'PROFADULT': 'ProfAdult', 'TRANSLETTER': 'TransLetter', 'REAFFIRMATION': 'Reaffirmation', 'RESTORED': 'Restored',
          'DEATH': 'Death', 'TRANS': 'Trans', 'REMOVEDFROMROLL': 'RemovedFromRoll', 'DISCIPLINE': 'Discipline',
  }
                )

                            
  mems_df = df[['Year', 'Comm', 'NonComm', 'Total Members']].melt(id_vars=['Year'], var_name='Metric', value_name='Count')
  adds_df = df[['Year', 'ProfChild', 'ProfAdult', 'TransLetter', 'Reaffirmation', 'Restored']].melt(id_vars=['Year'], var_name='Metric', value_name='Count')
  loss_df = df[['Year', 'Death', 'Trans', 'RemovedFromRoll', 'Discipline']].melt(id_vars=['Year'], var_name='Metric', value_name='Count')

  st.subheader('Total Member Trends')
  st.bar_chart(mems_df.groupby(['Year', 'Metric'])['Count'].sum().reset_index(), x = 'Year', y = 'Count', color = 'Metric', stack = False)

  st.subheader('Member Additions')
  st.bar_chart(adds_df.groupby(['Year', 'Metric'])['Count'].sum().reset_index(), x = 'Year', y = 'Count', color = 'Metric', stack = False)

  st.subheader('Member Losses')
  st.bar_chart(loss_df.groupby(['Year', 'Metric'])['Count'].sum().reset_index(), x = 'Year', y = 'Count', color = 'Metric', stack = False)
