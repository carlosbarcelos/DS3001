import pandas as pd
from sklearn import tree
from sklearn.metrics import classification_report

# Read in dataset and create appropriate dataframe
csv_train = pd.read_csv("UFOSightings_TRAIN.csv")
csv_test = pd.read_csv("UFOSightings_TEST.csv")

# # Create decision tree using GINI impurity
# Convert to numerical using one hot endcoding
df_train = csv_train[['Shape', 'region_cat', 'time_cat']]
df_train = pd.get_dummies(df_train, columns=['region_cat', 'time_cat'], prefix=['region', 'time'])

df_test = csv_test[['Shape', 'region_cat', 'time_cat']]
df_test = pd.get_dummies(df_test, columns=['region_cat', 'time_cat'], prefix=['region', 'time'])

# Create the decision tree
X_train = df_train.drop(columns=['Shape'])
Y_train = df_train['Shape']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, Y_train)
# Illustrate decision tree based on training set
tree.export_graphviz(clf, out_file='tree.dot',
                     feature_names=df_train.drop(columns=['Shape']).columns,
                     class_names=Y_train)

# Report classification accuracy using test set
X_test = df_test.drop(columns=['Shape'])
Y_test = df_test['Shape']
Y_predict = clf.predict(X_test)
report = classification_report(Y_test, Y_predict)
print(report)
