import pandas as pd
import numpy as np
import os 

train_df = pd.read_csv('Highway-Rail_Grade_Crossing_Accident_Data.csv',
                       dtype={'Other Railroad Code': str, 'Other Railroad Name': str, 'Other Incident Number': str, 'Division': str, 'Subdivision': str, 
                              'Vehicle Direction Code': str, 'Equipment Involved Code': str, 'Hazmat Involvement': str, 'Hazmat Released by': str, 'Hazmat Released Name': str, 'Hazmat Released Quantity': str,
                              'Hazmat Released Measure': str, 'Equipment Type Code': str, 'Track Class': str, 'Train Direction Code': str, 'Crossing Warning Expanded 5': str,
                              'Crossing Warning Expanded 6': str, 'Crossing Warning Expanded 7': str, 'Signaled Crossing Warning Code': str, 'Crossing Warning Explanation Code': str,
                              'Crossing Warning Explanation': str, 'Roadway Condition Code': str, 'Roadway Condition': str, 'Crossing Warning Location Code': str, 'User Gender': str,
                              'Video Taken': str, 'Video Used': str, 'Special Study 1': str, 'Special Study 2': str, 'Narrative': str, 'Railroad Type': str, 'Whistle Ban': str})



code_list = []
def col_finder():
       column_list = list(train_df.columns)
       for column in column_list:
              if 'Code' in column:
                     code_list.append(column)
              elif 'Maintenance' in column:
                     code_list.append(column)
              elif 'Crossing Warning Expanded' in column:
                     code_list.append(column)
              else:
                     continue
       return 

col_finder()

train_df = train_df.drop(code_list, axis=1)

train_df = train_df.drop(['Report Year', 'Incident Year', 'Incident Month', 'Other Incident Number', 'Other Incident Year', 'Other Incident Month',
                          'Form 54 Filed', 'Video Taken', 'Video Used', 'Special Study 1', 'Special Study 2', 'Report Key', 'Narrative', 'Total Killed Form 55A',
                            'Total Injured Form 55A', 'Maintainance Incident Number', 'Crossing Warning Explanation', 'Other Railroad Name', 'Division', 'Subdivision',
                            'Roadway Condition', 'Number People On Train', 'Whistle Ban'], axis=1)




#pd.set_option('display.max_columns', None)

#train_main = train_df[['Incident Number', 'Railroad Name', 'Highway Name', 'City Name', 'County Name', 'State Name', 'Date', 'Time']].copy()
#
#train_time = train_df[['Incident Number', 'Date', 'Time', 'Month', 'Day', 'Hour', 'Minute', 'AM/PM']].copy()
#
#train_detail = train_df[['Incident Number', 'Public/Private', 'Highway User', 'Estimated Vehicle Speed', 'Vehicle Direction', 'Highway User Position', 'Equipment Involved', 'Railroad Car Unit Position']].copy()
#
#train_hazmat = train_df[['Incident Number', 'Hazmat Involvement Code', 'Hazmat Involvement', 'Hazmat Released by Code', 'Hazmat Released by', 'Hazmat Released Name', 'Hazmat Released Quantity', 'Hazmat Released Measure']].copy()
#
#train_weather = train_df[['Incident Number', 'Visibility Code', 'Visibility', 'Weather Condition Code', 'Weather Condition']].copy()
#
#train_detail2 = train_df[['Incident Number', 'Equipment Type Code', 'Equipment Type', 'Track Type Code', 'Track Type', 'Track Name', 'Number of Cars', 'Train Speed', 'Train Direction', 'Number People On Train']].copy()
#
#train_user = train_df[['Incident Number', 'User Age', 'User Gender', 'Highway User Action Code', 'Highway User Action', 'Driver Condition Code', 'Driver Condition', 'Driver In Vehicle']]



#def csv_maker():
#       directory = 'train_datasets'
#       parent_directory = 'C:/Data Projects/Trains/'
#       pathway = os.path.join(parent_directory, directory)
#       #os.mkdir(pathway)

#       for df in df_list:
#              df_name = df.name
#              df.to_csv(fr'C:/Data Projects/Trains/train_datasets/{df_name}.csv'.format(df_name=df_name), index=False)



bins= [0, 26, 51, 76, 110]
labels = ['< 26','26 - 50','51 - 75','76 - 100']
train_df['Age Category'] = pd.cut(train_df['User Age'], bins=bins, labels=labels, right=False)

train_df.to_csv(r'C:/Data Projects/Trains/train_datasets/train_df.csv', index=False)