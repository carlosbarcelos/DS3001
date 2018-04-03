import pandas as pd
import pydotplus
from sklearn import tree
import pydot
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import graphviz
from sklearn import preprocessing
from sklearn.feature_extraction import DictVectorizer
import collections
import networkx as nx
import matplotlib.pyplot as plt

# Read in dataset and create appropriate dataframe
csv_train = pd.read_csv("UFOSightings_TRAIN.csv")
csv_test = pd.read_csv("UFOSightings_TEST.csv")

# # Create decision tree using GINI impurity
cat = ['Shape', 'region_cat', 'time_cat']
df_train = csv_train[cat]

le = preprocessing.LabelEncoder()
A = le.fit_transform(df_train['Shape'])
B = le.fit_transform(df_train['region_cat'])
C = le.fit_transform(df_train['time_cat'])
BC = list(map(lambda x,y:[x,y],B,C))
# print()

clf = tree.DecisionTreeClassifier()
clf = clf.fit(BC, A)
tree.export_graphviz(clf, out_file='tree.dot')

# Report classification accuracy using test set
# TODO

# Illustrate decision tree based on training set
# TODO
