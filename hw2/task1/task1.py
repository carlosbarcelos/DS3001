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
plt.figure()
# TODO
plt.savefig('Sightings_Per_Year.png')

# Bar chart for sightings by state
plt.figure()
df['State'].value_counts().plot(kind='bar', figsize=(15,10), title='Sightings Per State')
plt.savefig('Sighting_Per_State.png')
