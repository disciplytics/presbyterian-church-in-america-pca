def membership(df):
  import streamlit as st
  import pandas as pd

  df['Total Members'] = df['COMM'] + df['NONCOMM']

  df = df.rename(columns = {'COMM': 'Comm', 'NONCOMM': 'NonComm', 'YEAR': 'Year'})
                            
  df = df[['Year', 'Comm', 'NonComm', 'Total Members']].melt(id_vars=['Year'], var_name='Metric', value_name='Count')

  st.bar_chart(df.groupby(['Year', 'Metric'])['Count'].sum().reset_index(), x = 'Year', y = 'Count', color = 'Metric', stack = False)
