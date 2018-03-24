import pandas as pd
import matplotlib.pyplot as plt

# Read in dataset and create appropriate dataframe
csv = pd.read_csv('../CAStateBuildingMetrics.csv')
df = csv.drop(columns=['Department Name', 'Property Id', 'Property Name', 'Address 1', 'City', 'State/Province',
                   'Postal Code', 'Property Area', 'Primary Property Type', 'Year Built', 'Electricity Use (kWh)',
                   'Natural Gas Use (therms)', 'Propane Use (kBtu)', 'Percent of Electricity that is Green Power',
                   'Total Green Power - Onsite and Offsite (kWh)', 'Site Energy Use (kBtu)', 'ENERGY STAR Score',
                   'LEED Certified', 'Location'])

# Remove missing values
df.dropna(inplace=True)

# All buildings
# Calculate central tendency for all departments
print('Mean: ', df.mean(), '\n')
print('Median: ', df.median(), '\n')
print('Mode: ', df.mode(), '\n')
# Create boxplot for all buildings
plt.figure()
df.boxplot(by='Department')
plt.savefig('All_Buildings.png')


# # Find the top five departments based on number of associated buildings
top5 = df
top5['count'] = top5.groupby('Department')['Department'].transform(pd.Series.value_counts)
top5.sort_values('count', inplace=True, ascending=False)
# Discover the top five departments
top5_byName = []
cnt = 0
for index, row in top5.iterrows():
    if row['Department'] not in top5_byName:
        top5_byName.append(row['Department'])
        cnt += 1
    if cnt == 5:
        break
# Remove all other departments
for index, row in top5.iterrows():
    if row['Department'] not in top5_byName:
        top5.drop(index, inplace=True)
top5.drop(columns=['count'], inplace=True) # Clean up

print('The top departments are: ', top5_byName, '\n')
# Calculate central tendency for top 5 departments
print('Mean by department: ', top5.groupby('Department').mean(), '\n')
print('Median by department: ', top5.groupby('Department').median(), '\n')
print('Mode by department: ', top5.groupby('Department').agg(pd.Series.mode), '\n')

# Create boxplot for top 5 departments
plt.figure()
top5.boxplot(by='Department')
plt.savefig('Top_5_Buildings.png')


# # Find the top five departments based on number of associated buildings (without outliers)
# Find the bounds for outliers
Q1 = top5.quantile(.25)
Q3 = top5.quantile(.75)
IQR = Q3 - Q1
# Remove the outliers
top5_noOutlier = top5
minOutlier = Q1 - (1.5 * IQR)
maxOutlier = Q3 + (1.5 * IQR)
top5_noOutlier = top5_noOutlier[top5_noOutlier['Water Use (All Water Sources) (kgal)'] > float(minOutlier)]
top5_noOutlier = top5_noOutlier[top5_noOutlier['Water Use (All Water Sources) (kgal)'] < float(maxOutlier)]
# Calculate central tendency for top 5 departments without outliers
print('Mean by department without outliers: ', top5_noOutlier.groupby('Department').mean(), '\n')
print('Median by department without outliers: ', top5_noOutlier.groupby('Department').median(), '\n')
print('Mode by department without outliers: ', top5_noOutlier.groupby('Department').agg(pd.Series.mode), '\n')
# Create boxplot for top 5 departments without outliers
plt.figure()
top5_noOutlier.boxplot(by='Department')
plt.savefig('Top_5_Buildings_No_Outliers.png')
