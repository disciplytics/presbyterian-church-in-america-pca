def disbursements(df):
  import streamlit as st
  import pandas as pd
  import numpy as np

  df = df.rename(columns = {
          'YEAR': 'Year',
          'ADMINISTRATION': 'Administration', 'DISCIPLESHIPMIN': 'DiscipleshipMin', 'MISSIONTONAMERICA': 'MissionToNAAmerica', 'MISSIONTOTHEWORLD': 'MissionToTheWorld', 
          'COVENANTCOLLEGE': 'CovenantCollege', 'COVENANTSEMINARY': 'CovenantSeminary', 'RIDGEHAVEN': 'Ridgehaven', 'REFORMEDUNIVERSITYMINISTRIES': 'ReformedUniversityMinistries',
          'PCAOFFICEBUILDING': 'PCAOfficeBuilding', 'OTHER': 'Other', 

          'PRESBYTERYOPERATION': 'PresbyteryOperation', 'CHRISTIANEDUCATION': 'ChristianEducation',  'HOMEMISSIONS': 'HomeMissions', 'INTERNATIONALMISSIONS': 'InternationalMissions', 'OTHERPRESBYTERYMIN': 'OtherPresbyteryMin', 

          'LOCALMINISTRIES': 'LocalMinistires', 'MERCYMINISTIRES': 'MercyMinistries', 'PCAINTERNATIONLMISSIONS': 'PCAInternationalMissions', 'PCAHOMEMISSION': 'PCAHomeMissions', 'NONPCAMISSION': 'NonPCAMissions',
          'PCASCHOOLS': 'PCASchools', 'NONPCASCHOOLS': 'NonPCASchools', 'TOTALBENEVOLENTDISBURSEMENTS': 'TotalBenevolentDisbursements', 

          'CURRENTEXPENSES': 'CurrentExpenses', 'BUILDINGFUND': 'BuildingFund',
          'TOTALALLDISBURSEMENTS': 'TotalAllDisbursements'
  }
                )

  df['Year'] = df['Year'].astype(str)
  
  totals_df = df[['Year', 'TotalBenevolentDisbursements', 'TotalAllDisbursements']].melt(id_vars=['Year'], var_name='Metric', value_name='Dollars')
  gen_assembly_df = df[['Year', 'Administration', 'DiscipleshipMin', 'MissionToNAAmerica', 'MissionToTheWorld', 'CovenantCollege', 'CovenantSeminary', 'Ridgehaven', 'ReformedUniversityMinistries', 'PCAOfficeBuilding', 'Other']].melt(id_vars=['Year'], var_name='Metric', value_name='Dollars')
  pres_df = df[['Year', 'PresbyteryOperation', 'ChristianEducation', 'HomeMissions', 'InternationalMissions', 'OtherPresbyteryMin']].melt(id_vars=['Year'], var_name='Metric', value_name='Dollars')
  cong_df = df[['Year', 'LocalMinistires', 'MercyMinistries', 'PCAInternationalMissions', 'PCAHomeMissions', 'NonPCAMissions', 'PCASchools', 'NonPCASchools']].melt(id_vars=['Year'], var_name='Metric', value_name='Dollars')
  ops_df = df[['Year', 'CurrentExpenses', 'BuildingFund']].melt(id_vars=['Year'], var_name='Metric', value_name='Dollars')

  TotalBenevolentDisbursements = df.groupby(['Year'])['TotalBenevolentDisbursements'].sum().reset_index()
  TotalAllDisbursements = df.groupby(['Year'])['TotalAllDisbursements'].sum().reset_index()

  pct_df = pd.merge(TotalBenevolentDisbursements, TotalAllDisbursements, on = 'Year', how = 'left')
  pct_df['TotalBenevolentDisbursementsPercentage'] = np.round(pct_df['TotalBenevolentDisbursements'] / pct_df['TotalAllDisbursements'], 2) * 100


  TOTALCONTRIB = df.groupby(['Year'])['TOTALCONTRIB'].sum().reset_index()
  COMM = df.groupby(['Year'])['COMM'].sum().reset_index()

  pcg_df = pd.merge(TOTALCONTRIB, COMM, on = 'Year', how = 'left')
  pcg_df['PerCapitaGiving'] = np.round(pcg_df['TOTALCONTRIB'] / pcg_df['COMM'], 0)
  
  st.subheader('Total Disbursements Trends')
  st.bar_chart(totals_df.groupby(['Year', 'Metric'])['Dollars'].sum().reset_index(), x = 'Year', y = 'Dollars', color = 'Metric', stack = False)

  st.subheader('Total Benevolent Disbursements % of All Disbursements Trends')
  st.line_chart(pct_df.groupby(['Year'])['TotalBenevolentDisbursementsPercentage'].sum().reset_index(), x = 'Year', y = 'TotalBenevolentDisbursementsPercentage')

  st.subheader('Per Capita Giving Trends')
  st.line_chart(pcg_df.groupby(['Year'])['PerCapitaGiving'].sum().reset_index(), x = 'Year', y = 'PerCapitaGiving')
  
  st.subheader('General Assembly Ministries')
  st.bar_chart(gen_assembly_df.groupby(['Year', 'Metric'])['Dollars'].sum().reset_index(), x = 'Year', y = 'Dollars', color = 'Metric', stack = False)

  st.subheader('Presbytery Ministries')
  st.bar_chart(pres_df.groupby(['Year', 'Metric'])['Dollars'].sum().reset_index(), x = 'Year', y = 'Dollars', color = 'Metric', stack = False)

  st.subheader('Congregational Ministries Trends')
  st.bar_chart(cong_df.groupby(['Year', 'Metric'])['Dollars'].sum().reset_index(), x = 'Year', y = 'Dollars', color = 'Metric', stack = False)

  st.subheader('Congregational Operations Trends')
  st.bar_chart(ops_df.groupby(['Year', 'Metric'])['Dollars'].sum().reset_index(), x = 'Year', y = 'Dollars', color = 'Metric', stack = False)
