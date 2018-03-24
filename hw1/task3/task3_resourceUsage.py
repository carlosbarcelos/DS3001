import pandas as pd
import sklearn as sk

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

# = 1 - Resource Usage Only
df1 = csv.drop(columns=['Department', 'Department Name', 'Property Id', 'Address 1', 'City', 'State/Province',
                           'Postal Code', 'Property Area', 'Primary Property Type', 'Year Built',
                           'Percent of Electricity that is Green Power', 'Total Green Power - Onsite and Offsite (kWh)',
                           'ENERGY STAR Score', 'LEED Certified', 'Location'])
# Handle missing values
df1.fillna(df1.mean(), inplace=True)

#Get comparison row/index
for index, row in df1.iterrows():
    if row['Property Name'] == 'MENDOTA MAINTENANCE STATION':
        search_row = row
        idx = index
        break
#
# == 1.1 - Euclidean Distance
# Find the Euclidean Distance for the desired property
ans_1_1 = sk.metrics.pairwise_distances(df1.drop(columns=['Property Name']), metric='manhattan')[index]
# Sort the results making sure to capture the original Property Name and position
sizeList = list(range(0, ans_1_1.size+1))
ans_1_1_tuple = list(zip(sizeList, ans_1_1))
ans_1_1_sorted = ascending_sort(ans_1_1_tuple)

print('Euclidean Distance yields these as the most similar properties :\n' +
      df1['Property Name'][ans_1_1_sorted[1][0]] + '\n' +
      df1['Property Name'][ans_1_1_sorted[2][0]] + '\n' +
      df1['Property Name'][ans_1_1_sorted[3][0]] + '\n')

# == 1.2 - Manhattan Distance
# Find the Manhattan Distance for the desired property
ans_1_2 = sk.metrics.pairwise_distances(df1.drop(columns=['Property Name']), metric='manhattan')[index]
# Sort the results making sure to capture the original Property Name and position
sizeList = list(range(0, ans_1_2.size+1))
ans_1_2_tuple = list(zip(sizeList, ans_1_2))
ans_1_2_sorted = ascending_sort(ans_1_2_tuple)

print('Manhattan Distance yields these as the most similar properties :\n' +
      df1['Property Name'][ans_1_2_sorted[1][0]] + '\n' +
      df1['Property Name'][ans_1_2_sorted[2][0]] + '\n' +
      df1['Property Name'][ans_1_2_sorted[3][0]] + '\n')

# == 1.3 - Cosine Similarity
# Find the cosine similarity for the desired property
ans_1_3 = sk.metrics.pairwise_distances(df1.drop(columns=['Property Name']), metric='cosine')[index]
# Sort the results making sure to capture the original Property Name and position
sizeList = list(range(0, ans_1_3.size+1))
ans_1_3_tuple = list(zip(sizeList, ans_1_3))
ans_1_3_sorted = ascending_sort(ans_1_3_tuple)

print('Cosine Similarity yields these as the most similar properties :\n' +
      df1['Property Name'][ans_1_3_sorted[1][0]] + '\n' +
      df1['Property Name'][ans_1_3_sorted[2][0]] + '\n' +
      df1['Property Name'][ans_1_3_sorted[3][0]] + '\n')

# = 2   - Property Variables Only
# == 2.1 - Euclidean Distance
# == 2.2 - Manhattan Distance
# == 2.3 - Cosine Similarity

