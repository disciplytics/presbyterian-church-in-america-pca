def general_data(df):
  import streamlit as st
  import pandas as pd
  
  df = df.rename(columns = {
          'STAT_YEAR': 'Year',
          'ADULT_BAPT': 'AdultBapt', 'INFANT_BAPT': 'InfantBapt', 
          'RULING_ELDERS': 'RulingElders', 'DEACONS': 'Deacons', 
          'FAMILY_UNITS': 'FamilyUnits', 
          'SUNDAY_SCHOOL_ATTEND': 'SundaySchoolAttend', 'SMALL_GROUP_ATTEND': 'SmallGroupAttend', 'EST_MORN_ATTEND': 'EstMornAttend',
  }
                )

                            
  bapt_df = df[['Year', 'AdultBapt', 'InfantBapt']].melt(id_vars=['Year'], var_name='Metric', value_name='Count')
  off_df = df[['Year', 'RulingElders', 'Deacons']].melt(id_vars=['Year'], var_name='Metric', value_name='Count')
  fam_df = df[['Year', 'FamilyUnits']].melt(id_vars=['Year'], var_name='Metric', value_name='Count')
  attend_df = df[['Year', 'SundaySchoolAttend', 'SmallGroupAttend', 'EstMornAttend']].melt(id_vars=['Year'], var_name='Metric', value_name='Count')

  st.subheader('Baptism Trends')
  st.bar_chart(bapt_df.groupby(['Year', 'Metric'])['Count'].sum().reset_index(), x = 'Year', y = 'Count', color = 'Metric', stack = False)

  st.subheader('Officer Trends')
  st.bar_chart(off_df.groupby(['Year', 'Metric'])['Count'].sum().reset_index(), x = 'Year', y = 'Count', color = 'Metric', stack = False)

  st.subheader('Family Trends')
  st.bar_chart(fam_df.groupby(['Year', 'Metric'])['Count'].sum().reset_index(), x = 'Year', y = 'Count', color = 'Metric', stack = False)
  
  st.subheader('Attendance Trends')
  st.bar_chart(attend_df.groupby(['Year', 'Metric'])['Count'].sum().reset_index(), x = 'Year', y = 'Count', color = 'Metric', stack = False)
