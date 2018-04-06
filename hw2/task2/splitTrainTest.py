import pandas as pd
import datetime as dt

# Return the country region label based on state
NORTHEAST = ['PA','NY','NJ','CT','RI','MA','VT','NH','ME']
MIDWEST = ['ND','SD','NE','KS','MN','IA','MO','WI','IL','IN','MI','OH']
SOUTH = ['TX','OK','AR','LA','MS','AL','TN','KY','FL','GA','SC','NC','VA','WV','DC','MD','DE']
WEST = ['WA','OR','CA','ID','MT','WY','NV','UT','CO','AZ','NM']
def getRegion(state):
    if state in NORTHEAST:
        return 'northeast'
    elif state in MIDWEST:
        return 'midwest'
    elif state in SOUTH:
        return 'south'
    elif state in WEST:
        return 'west'
    else:
        return None

# Return the time of day label based on the time
def getTime(time):
    time = dt.datetime.strptime(time, '%H:%M:%S').time()
    if time < dt.time(hour=6):
        return 'night'
    elif time < dt.time(hour=12):
        return 'morning'
    elif time < dt.time(hour=18):
        return 'afternoon'
    else:
        return 'evening'

# Read in dataset and create appropriate dataframe
df = pd.read_csv("../UFOSightings_CLEAN.csv")

# Convert states into country regions
df['region_cat'] = df.apply(lambda x: getRegion(x['State']), axis=1)
df.dropna(inplace=True)

# Convert time into time of day
df['time_cat'] = df.apply(lambda x: getTime(x['Time']), axis=1)

# # Split into training- and testing-date
# Convert string to datetime
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y', errors='coerce')
df.dropna(inplace=True)
# Split by datetime
split_date = pd.datetime(2013, 12, 31)
df_training = df.loc[df['Date'] <= split_date]
df_test = df.loc[df['Date'] > split_date]
# Output to CSV
df_training.to_csv('UFOSightings_TRAIN.csv')
df_test.to_csv('UFOSightings_TEST.csv')
