import pandas as pd
import matplotlib.pyplot as plt

# Read in dataset and create appropriate dataframe
df = pd.read_csv("../UFOSightings_CLEAN.csv")

# Find the bounds for outliers
Q1 = df['Duration'].quantile(.25)
Q3 = df['Duration'].quantile(.75)
IQR = Q3 - Q1
# Remove the outliers
df_noOutlier = df
minOutlier = Q1 - (1.5 * IQR)
maxOutlier = Q3 + (1.5 * IQR)
df_noOutlier = df_noOutlier[df_noOutlier['Duration'] > float(minOutlier)]
df_noOutlier = df_noOutlier[df_noOutlier['Duration'] < float(maxOutlier)]

# Boxplot of the duration of UFO sightings (one boxplot per shape)
plt.figure()
df_noOutlier.boxplot(by='Shape')
plt.savefig('Duration_Per_Shape.png')

# Time series figure with the number of sightings per year (one line per shape)
sightingsDF = df[['Date', 'Shape']].copy()
sightingsDF['Year'] = sightingsDF['Date'].map(lambda x: pd.datetime.strptime(x, '%m/%d/%Y').year)
sightingsDF.drop(columns=['Date'], inplace=True)
plt.figure()
yearPV = sightingsDF.pivot_table(index='Year', columns='Shape', aggfunc=len)
yearPV.plot()
plt.savefig('Sightings_Per_Year.png')

# Bar chart for sightings by state
plt.figure(figsize=(15, 10))
df['State'].value_counts().plot(kind='bar', title='Sightings Per State')
plt.savefig('Sighting_Per_State.png')

# Normalize sightings by population
normDF = pd.read_csv("normalizeUFOSightings.csv")
normDF.drop(columns=['count', 'Population'], inplace=True)
plt.figure()
normDF.sort_values(by=['norm_count'], ascending=False).plot(x='State', y='norm_count', kind='bar', figsize=(15, 10), title='Sightings Per State (Normalized)')
plt.savefig('Sighting_Per_State(Normalized).png')
