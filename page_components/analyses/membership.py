def membership(df):
  import streamlit as st

  st.bar_chart(df.groupby(['YEAR'])['COMM'].sum().reset_index, x = 'YEAR', y = 'COMM')
