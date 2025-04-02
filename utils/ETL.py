## SCRIPT LOADS THE DATA FOR ANALYSIS

import pandas as pd
from pandas.api.types import is_integer_dtype
from pandas.api.types import is_float_dtype
from pandas.api.types import is_string_dtype

# EXTRACT

# function loads raw data and transforms it into a table
def load_data(data_year: str):
    
    load_path = f"raw_data\{data_year}_stats.xlsx"
    data = pd.read_excel(load_path)
    data.columns = data.loc[1]
    data = data.iloc[2:-2]
    return data

# load data for each year, clean, and save as a csv
years = ['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']

analysis_data = pd.DataFrame()
for i in years:
    analysis_data = pd.concat([analysis_data, load_data(i)])
    
    
# TRANSFORM

# retain needed columns
needed_columns = [
    'City', 
    'St', 
    'Church', 
    'Pastor',
    
    'Stat Year', 
    
    # Members
    'Comm', 
    'Non Comm', 
    #'Total', 
    
    # Additions
    'Prof Child', 
    'Prof Adult',
    'Trans Letter', 
    'Reaffir-mation', 
    'Re-stored', 
    #'Total', 
    
    # Losses
    'Death',
    'Trans', 
    "Rem'v fr Roll", 
    'Discipl', 
    #'Total', 
    
    # General Data
    'Adult Bapt', 
    'Infant Bapt', 
    'Ruling Elders', 
    'Deacons', 
    'Family Units',
    'Sunday School Attend', 
    'Small Group Attend', 
    'Est Morn Attend',
    
    #Christian School
    # Grades Included Key
    #*P=Presch, K=Kindergarten, E=Elem, M=Middle, H=HighSch	
    'Grades *Included', 
    'Total Enrollment', 
    
    # Contributions
    'Tithes & Offerings',
    'Special\nCauses', 
    'Building Fund Offering', 
    'Other Contrib',
    'Total Contrib', 
    'Other Income', 
    'Total Church Income', 
    
    # Benevolent Disbursements: General Assembly Ministries
    'Admini-stration', 
    'Disciple-ship Min.', 
    'Mission to N. America',
    'Mission to the World', 
    'Covenant College', 
    'Covenant Seminary',
    'Ridge\nHaven', 
    'Reformed University Ministries', 
    'PCA Office Building',
    'Other', 
    #'Total', 
    
    # Benevolent Disbursements: Presbytery Ministries
    'Presbytery Operation', 
    'Christian Education',
    'Home Missions', 
    "Internat'l\nMissions", 
    'Other Pres-bytery Min',
    #'Total', 

    # Benevolent Disbursements: Congregational Ministries
    'Local Ministries', 
    'Mercy Ministires',
    "PCA Internat'l\nMissions", 
    'PCA Home Mission', 
    'Non-PCA Mission',
    'PCA Schools', 
    'Non-PCA Schools', 
    #'Total',
    
    'TOTAL Benevolent Disbursements', 
    
    # Congregational Operational Disbursements
    'Current Expenses', 
    'Building Fund',
    
    # sum('TOTAL Benevolent Disbursements', 'Current Expenses', 'Building Fund')
    'GRAND TOTAL: All Disbursements', 
    
    # 'TOTAL Benevolent Disbursements' / 'GRAND TOTAL: All Disbursements'
    'Benevol/\nGrand Total',
    
    # 'Total Contrib' / 'Comm'
    'Per Capita Giving'
    ]

analysis_data = analysis_data[needed_columns]

# rename columns
rename_mapping = {
    #'City', 
    'St': 'State', 
    #'Church', 
    #'Pastor',
    #'Stat Year', 
    
    # Members
    #'Comm', 
    #'Non Comm', 
    
    # Additions
    #'Prof Child', 
    #'Prof Adult',
    #'Trans Letter', 
    'Reaffir-mation': 'Reaffirmation', 
    'Re-stored': 'Restored', 
    
    # Losses
    #'Death',
    #'Trans', 
    "Rem'v fr Roll": "Removed From Roll", 
    'Discipl': 'Discipline', 
    
    # General Data
    #'Adult Bapt', 
    #'Infant Bapt', 
    #'Ruling Elders', 
    #'Deacons', 
    #'Family Units',
    #'Sunday School Attend', 
    #'Small Group Attend', 
    #'Est Morn Attend',
    
    #Christian School
    # Grades Included Key
    #*P=Presch, K=Kindergarten, E=Elem, M=Middle, H=HighSch	
    'Grades *Included': 'Grades Included', 
    #'Total Enrollment', 
    
    # Contributions
    #'Tithes & Offerings',
    'Special\nCauses': 'Special Causes', 
    #'Building Fund Offering', 
    #'Other Contrib',
    #'Total Contrib', 
    #'Other Income', 
    #'Total Church Income', 
    
    # Benevolent Disbursements: General Assembly Ministries
    'Admini-stration': 'Administration', 
    'Disciple-ship Min.': 'Discipleship Min.', 
    #'Mission to N. America',
    #'Mission to the World', 
    #'Covenant College', 
    #'Covenant Seminary',
    'Ridge\nHaven': 'Ridge Haven', 
    #'Reformed University Ministries', 
    #'PCA Office Building',
    #'Other', 
    
    # Benevolent Disbursements: Presbytery Ministries
    #'Presbytery Operation', 
    #'Christian Education',
    #'Home Missions', 
    "Internat'l\nMissions": "Internat'l Missions", 
    'Other Pres-bytery Min': 'Other Presbytery Min',

    # Benevolent Disbursements: Congregational Ministries
    #'Local Ministries', 
    #'Mercy Ministires',
    "PCA Internat'l\nMissions": "PCA Internat'l Missions", 
    #'PCA Home Mission', 
    #'Non-PCA Mission',
    #'PCA Schools', 
    #'Non-PCA Schools', 
    
    'TOTAL Benevolent Disbursements': 'Total Benevolent Disbursements', 
    
    # Congregational Operational Disbursements
    #'Current Expenses', 
    #'Building Fund',
    
    # sum('TOTAL Benevolent Disbursements', 'Current Expenses', 'Building Fund')
    'GRAND TOTAL: All Disbursements': 'Total All Disbursements', 
    
    # 'TOTAL Benevolent Disbursements' / 'GRAND TOTAL: All Disbursements'
    'Benevol/\nGrand Total': 'Benevol Grand Total',
    
    # 'Total Contrib' / 'Comm'
    #'Per Capita Giving'
    
}
analysis_data.rename(columns=rename_mapping, inplace=True)

# infer data types
analysis_data = analysis_data.convert_dtypes()

# replace missing data
for i in analysis_data.columns:
    if is_string_dtype(analysis_data[i]):
        analysis_data[i] = analysis_data[i].fillna(f'No {i} Reported')
    elif is_integer_dtype(analysis_data[i]) or is_float_dtype(analysis_data[i]):
        analysis_data[i] = analysis_data[i].fillna(0)
        
# LOAD
    
analysis_data.to_csv('analysis_data\data.csv', index=False)
