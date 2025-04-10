def christian_schools(df):
  import streamlit as st
  import pandas as pd
  GRADESINCLUDED VARCHAR(16777216),
	TOTALENROLLMENT NUMBER(38,0),
  
  df = df.rename(columns = {
          'YEAR': 'Year',
          'GRADESINCLUDED': 'GradeIncluded', 'TOTALENROLLMENT': 'TotalEnrollment', 
  }
                )

                          

  st.subheader('Christian School Enrollment Trends')
  st.bar_chart(df.groupby(['Year', 'GradeIncluded'])['TotalEnrollment'].sum().reset_index(), x = 'Year', y = 'TotalEnrollment', color = 'GradeIncluded', stack = True)
