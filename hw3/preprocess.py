import pandas as pd
import datetime as dt

# Read in dataset and create appropriate dataframe
csv_1 = pd.read_csv("raw_data/201701-hubway-tripdata.csv")
csv_2 = pd.read_csv("raw_data/201702-hubway-tripdata.csv")
csv_3 = pd.read_csv("raw_data/201703-hubway-tripdata.csv")
csv_4 = pd.read_csv("raw_data/201704-hubway-tripdata.csv")
csv_5 = pd.read_csv("raw_data/201705-hubway-tripdata.csv")
csv_6 = pd.read_csv("raw_data/201706-hubway-tripdata.csv")
csv_7 = pd.read_csv("raw_data/201707-hubway-tripdata.csv")
csv_8 = pd.read_csv("raw_data/201708-hubway-tripdata.csv")
csv_9 = pd.read_csv("raw_data/201709-hubway-tripdata.csv")
csv_10 = pd.read_csv("raw_data/201710-hubway-tripdata.csv")
csv_11 = pd.read_csv("raw_data/201711-hubway-tripdata.csv")
csv_12 = pd.read_csv("raw_data/201712-hubway-tripdata.csv")

months = [csv_1, csv_2, csv_3, csv_4, csv_5, csv_6,
          csv_7, csv_8, csv_9, csv_10, csv_11, csv_12]

# Concatonate the entire year's worth of data
df = pd.concat(months)

# Drop extenious columns
df.drop(columns=['start station name', 'start station latitude', 'start station longitude',
                 'end station name', 'end station latitude', 'end station longitude'], inplace=True)

# Separate 'Date/Time' into unique columns
temp = pd.DatetimeIndex(df['starttime'])
df['start_date'] = temp.date
df['start_time'] = temp.time

temp = pd.DatetimeIndex(df['stoptime'])
df['end_date'] = temp.date
df['end_time'] = temp.time

df.drop(columns=['starttime'], inplace=True)
df.drop(columns=['stoptime'], inplace=True)

# Write the cleaned result to CSV
df.to_csv("2017-hubway-tripdate_CLEAN.csv")
