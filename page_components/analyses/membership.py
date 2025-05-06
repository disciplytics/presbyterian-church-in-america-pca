def membership(df):
  import streamlit as st
  import pandas as pd

  df['Total Members'] = df['COMM'] + df['NON_COMM']
  df['Total Additions'] = df['PROF_CHILD'] + df['PROF_ADULT'] + df['TRANS_LETTER'] + df['REAFFIRMATION'] + df['RESTORED']
  df['Total Losses'] = df['DEATH'] + df['TRANS'] + df['REMOVED_FROM_ROLL'] + df['DISCIPLINE']
  
  df = df.rename(columns = {
          'STAT_YEAR': 'Year',
          'COMM': 'Comm', 'NON_COMM': 'NonComm', 
          'PROF_CHILD': 'ProfChild', 'PROF_ADULT': 'ProfAdult', 'TRANS_LETTER': 'TransLetter', 'REAFFIRMATION': 'Reaffirmation', 'RESTORED': 'Restored',
          'DEATH': 'Death', 'TRANS': 'Trans', 'REMOVED_FROM_ROLL': 'RemovedFromRoll', 'DISCIPLINE': 'Discipline',
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
  
