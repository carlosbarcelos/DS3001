import pandas as pd
import re

# Converts a given string into its seconds form
def convertToSeconds(i, str):
    if 'sec' in str:
        return i
    if 'min' in str:
        i *= 60
    elif 'hour' in str:
        i *= 3600
    elif 'day' in str:
        i *= 86400
    elif 'week' in str:
        i *= 604800
    elif 'month' in str:
        i *= 2592000
    elif 'year' in str:
        i *= 31556952
    else:
        return 0
    return i

# Read in dataset and create appropriate dataframe
csv = pd.read_csv("UFOSightings.csv")

# Drop rows with missing values
csv['Date / Time'] = pd.to_datetime(csv['Date / Time'], errors='coerce') # Convert incorrect datetime to NA
csv.dropna(inplace=True)

# Separate 'Date/Time' into unique columns
temp = pd.DatetimeIndex(csv['Date / Time'])
csv['Date'] = temp.date
csv['Time'] = temp.time
csv.drop(columns=['Date / Time'], inplace=True)

# # Clean 'Duration' column
for index, row in csv.iterrows():
    # 1) Remove text only durations
    if row['Duration'].isalpha():
        csv.drop(index, inplace=True)

for index, row in csv.iterrows():
    # 2) Collect the upper bound of duration
    try:
        intList = [e for e in re.split("[^0-9]", row['Duration']) if e != '']
        intMax = max(map(int, intList))
    except:
        print('!!! ' + row['Duration'])
    # 3) Convert to seconds
    intMax = convertToSeconds(intMax, row['Duration'])
    if intMax == 0:
        csv.drop(index, inplace=True)
        continue
    # Finally, rewrite to the duration column
    csv['Duration'][index] = str(intMax)

# Write the cleaned result to CSV
csv.to_csv("../UFOSightings_CLEAN.csv")
