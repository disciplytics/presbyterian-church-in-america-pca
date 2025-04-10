def christian_schools(df):
  import streamlit as st
  import pandas as pd
  
  df = df.rename(columns = {
          'YEAR': 'Year',
          'GRADESINCLUDED': 'GradeIncluded', 'TOTALENROLLMENT': 'TotalEnrollment', 
  }
                )

                          

  st.subheader('Christian School Enrollment Trends')
  st.write('*P=Presch, K=Kindergarten, E=Elem, M=Middle, H=HighSch')
  st.bar_chart(df.groupby(['Year', 'GradeIncluded'])['TotalEnrollment'].sum().reset_index(), x = 'Year', y = 'TotalEnrollment', color = 'GradeIncluded', stack = True)
