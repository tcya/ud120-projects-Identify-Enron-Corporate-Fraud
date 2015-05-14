#!/usr/bin/python


"""
    starter code for the evaluation mini-project
    start by copying your trained/tested POI identifier from
    that you built in the validation mini-project

    the second step toward building your POI identifier!

    start by loading/formatting the data

"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn import tree
import sklearn.metrics as sm
from sklearn import cross_validation

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

clf = tree.DecisionTreeClassifier()
# t0 = time()
clf.fit(features_train, labels_train)
# print "training time:", round(time()-t0, 3), "s"
# t0 = time()
pred = clf.predict(features_test)
accu = sm.accuracy_score(labels_test,  [0]*29)
print accu
print map(int,labels_test)
print map(int,pred)
print sm.precision_score(labels_test,  pred)
print sm.recall_score(labels_test,  pred)
