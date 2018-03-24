import pandas as pd
import sklearn.metrics as sk

def ascending_sort(A):
    '''
        Given a disordered list of pairs, rearrange the integers in descending order using bubble sort algorithm.
        Input: A:  a list, such as  [(0,2),(1,0.5),(2,1.)]
                   For (n,m) where n is the node and m is the value
        Output: a sorted list
    '''
    for i in range(len(A)):
        for k in range( len(A) - 1, i, -1):
            if ( A[k][1] < A[k-1][1] ):
                temp = A[k]
                A[k] = A[k-1]
                A[k-1] = temp
    # Return the list of sorted nodes
    sorted_touple = list(zip([item[0] for item in A], [item[1] for item in A]))
    return sorted_touple

# Read in dataset and create appropriate dataframe
csv = pd.read_csv('../CAStateBuildingMetrics.csv')

# = Part 2 - Resource Usage Only
df = csv.drop(columns=['Department', 'Property Id', 'Address 1', 'State/Province', 'Postal Code', 'Year Built',
                        'Electricity Use (kWh)', 'Natural Gas Use (therms)', 'Propane Use (kBtu)',
                        'Water Use (All Water Sources) (kgal)', 'Percent of Electricity that is Green Power',
                        'Total Green Power - Onsite and Offsite (kWh)', 'Site Energy Use (kBtu)', 'ENERGY STAR Score',
                        'LEED Certified', 'Location'])

# Handle missing values
df.dropna(inplace=True)

# Transform catagorical data to nominal data
df_trans = pd.get_dummies(df, columns=['Department Name', 'City', 'Primary Property Type'], prefix=['dept', 'city', 'type'])

#Get comparison row/index
for index, row in df.iterrows():
    if row['Property Name'] == 'MENDOTA MAINTENANCE STATION':
        search_row = row
        idx = index
        break

# == 2.1 - Euclidean Distance
# Find the Euclidean Distance for the desired property
ans_2_1 = sk.pairwise_distances(df_trans.drop(columns=['Property Name']), metric='euclidean')[index]
# Sort the results making sure to capture the original Property Name and position
sizeList = list(range(0, ans_2_1.size+1))
ans_2_1_tuple = list(zip(sizeList, ans_2_1))
ans_2_1_sorted = ascending_sort(ans_2_1_tuple)

print('Euclidean Distance yields these as the most similar properties :\n' +
      df_trans['Property Name'][ans_2_1_sorted[1][0]] + '\n' +
      df_trans['Property Name'][ans_2_1_sorted[2][0]] + '\n' +
      df_trans['Property Name'][ans_2_1_sorted[3][0]] + '\n')

# == 2.2 - Manhattan Distance
# Find the Manhattan Distance for the desired property
ans_2_2 = sk.pairwise_distances(df_trans.drop(columns=['Property Name']), metric='manhattan')[index]
# Sort the results making sure to capture the original Property Name and position
sizeList = list(range(0, ans_2_2.size+1))
ans_2_2_tuple = list(zip(sizeList, ans_2_2))
ans_2_2_sorted = ascending_sort(ans_2_2_tuple)

print('Manhattan Distance yields these as the most similar properties :\n' +
      df_trans['Property Name'][ans_2_2_sorted[1][0]] + '\n' +
      df_trans['Property Name'][ans_2_2_sorted[2][0]] + '\n' +
      df_trans['Property Name'][ans_2_2_sorted[3][0]] + '\n')

# == 2.3 - Cosine Similarity
# Find the cosine similarity for the desired property
ans_2_3 = sk.pairwise_distances(df_trans.drop(columns=['Property Name']), metric='cosine')[index]
# Sort the results making sure to capture the original Property Name and position
sizeList = list(range(0, ans_2_3.size+1))
ans_2_3_tuple = list(zip(sizeList, ans_2_3))
ans_2_3_sorted = ascending_sort(ans_2_3_tuple)

print('Cosine Similarity yields these as the most similar properties :\n' +
      df_trans['Property Name'][ans_2_3_sorted[1][0]] + '\n' +
      df_trans['Property Name'][ans_2_3_sorted[2][0]] + '\n' +
      df_trans['Property Name'][ans_2_3_sorted[3][0]] + '\n')
