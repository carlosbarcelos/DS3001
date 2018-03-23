import pandas as pd
import matplotlib.pyplot as plt

# Read in dataset and create appropriate dataframe
csv = pd.read_csv('../CAStateBuildingMetrics.csv')
df = csv.drop(columns=['Department Name', 'Property Id', 'Property Name', 'Address 1', 'City', 'State/Province',
                       'Postal Code', 'Property Area', 'Primary Property Type', 'Year Built',
                       'Natural Gas Use (therms)', 'Propane Use (kBtu)', 'Percent of Electricity that is Green Power',
                       'Total Green Power - Onsite and Offsite (kWh)', 'Site Energy Use (kBtu)', 'ENERGY STAR Score',
                       'LEED Certified', 'Location'])

# Remove missing values
for index, row in df.iterrows():
    if pd.isna(row['Water Use (All Water Sources) (kgal)']) or pd.isna(row['Electricity Use (kWh)']):
        df.drop(index, inplace=True)

# Create scatterplot for all correlation
plt.figure()
df.plot.scatter('Water Use (All Water Sources) (kgal)', 'Electricity Use (kWh)')
plt.savefig('Water_v_Electric.png')

# Calculate Person's correlation coefficient
pCorr = df.corr(method='pearson')
print('Person Correlation Coefficient: ', pCorr, '\n')


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

# Get Person's correlation coefficient and scatter plot for top five departments
for dep in top5_byName:
    temp = top5[top5['Department'] == dep]
    # Calculate Person's correlation coefficient
    pCorr = temp.corr(method='pearson')
    print('Person Correlation Coefficient '+dep+': ', pCorr, '\n')
    # Create scatterplot for all correlation
    plt.figure()
    temp.plot.scatter('Water Use (All Water Sources) (kgal)', 'Electricity Use (kWh)', title=dep)
    plt.savefig('Water_v_Electric_'+dep+'.png')