def general_data(df):
  import streamlit as st
  import pandas as pd
  
  df = df.rename(columns = {
          'YEAR': 'Year',
          'ADULTBAPT': 'AdultBapt', 'INFANTBAPT': 'InfantBapt', 
          'RULINGELDERS': 'RulingElders', 'DEACONS': 'Deacons', 
          'FAMILYUNITS': 'FamilyUnits', 
          'SUNDAYSCHOOLATTEND': 'SundaySchoolAttend', 'SMALLGROUPATTEND': 'SmallGroupAttend', 'ESTMORNATTEND': 'EstMornAttend',
  }
                )

                            
  bapt_df = df[['Year', 'AdultBapt', 'InfantBapt']].melt(id_vars=['Year'], var_name='Metric', value_name='Count')
  off_df = df[['Year', 'RulingElders', 'Deacons', 'FamilyUnits']].melt(id_vars=['Year'], var_name='Metric', value_name='Count')
  attend_df = df[['Year', 'SundaySchoolAttend', 'SmallGroupAttend', 'EstMornAttend']].melt(id_vars=['Year'], var_name='Metric', value_name='Count')

  st.subheader('Baptism Trends')
  st.bar_chart(bapt_df.groupby(['Year', 'Metric'])['Count'].sum().reset_index(), x = 'Year', y = 'Count', color = 'Metric', stack = False)

  st.subheader('Officer Trends')
  st.bar_chart(off_df.groupby(['Year', 'Metric'])['Count'].sum().reset_index(), x = 'Year', y = 'Count', color = 'Metric', stack = False)

  st.subheader('Attendance Trends')
  st.bar_chart(attend_df.groupby(['Year', 'Metric'])['Count'].sum().reset_index(), x = 'Year', y = 'Count', color = 'Metric', stack = False)
