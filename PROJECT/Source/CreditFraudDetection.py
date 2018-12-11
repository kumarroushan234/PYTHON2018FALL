# Anamolie Detection for bank transactions.
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# importing the necessary packages
import numpy as np
import pandas as pds
import seaborn as sbn
# Load the dataset from the .csv file using pandas
dataset = pds.read_csv ("creditcard.csv")
print(dataset.columns)#exploring the data set
print(dataset.shape)
print(dataset.describe ())#checking what al elements are there
#data = data_from_csv.sample (frac=0.1, random_state=1)
#print(data.shape)
# plot histogram of each parameter
dataset.hist (figsize=(20, 20))
plt.show ()
print("------------------------------------------------------------------------")
# Determine number of fraud and valid cases in dataset
fraud = dataset[dataset['Class'] == 1]
valid = dataset[dataset['Class'] == 0]
outlier_fraction = len (fraud) / float (len (valid))
print("------------------------------------------------------------------------")
print(outlier_fraction)
print("Fraud Cases: {}".format (len (fraud)))
print("Valid Cases: {}".format (len (valid)))
# Correlation Matrix
corrmat = dataset.corr ()
figure = plt.figure (figsize=(12, 9))
data1 = dataset.sample (frac=0.1, random_state=1)
sbn.heatmap (corrmat, vmax=.8, square=True)
plt.show ()
corrmat1=data1.corr()
figure1 = plt.figure (figsize=(12, 9))
# importing seaborn library and using corr plot plotting the heat map
sbn.heatmap(corrmat1, vmax= 1.0, square=False)
#Showing the plot by plotting it
plt.show()
# Get all the columns from the dataframe
columns = dataset.columns.tolist ()
# filter the columns to remove data we donot want
columns = [c for c in columns if c not in ["Class"]]
# Store the variable we'll be predicting on
target = "Class"
X = dataset[columns]
Y = dataset[target]
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.25)
# print the shapes of X and Y
#print(X_train)
#print(Y_train)
print(X.shape)
print(Y.shape)
from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
# define a random state
state = 1
# define the outlier detection methods
classifiers = {
    "Isolation Forest": IsolationForest (max_samples=len (X),
                                         contamination=outlier_fraction,
                                         random_state=state),
    "Local Outlier Factor": LocalOutlierFactor (
        n_neighbors=20,#nearest neighbours discovering
        contamination=outlier_fraction)
}
# fit the model using the length of the fraud transactions.
n_outliers = len (fraud)
for i, (clf_name, clf) in enumerate (classifiers.items ()):

    # fit the data and tagging  outlier functions
    if clf_name == "Local Outlier Factor":
        y_pred = clf.fit_predict (X)
        scores_pred = clf.negative_outlier_factor_
    else:
        clf.fit (X)
        scores_pred = clf.decision_function (X)
        y_pred = clf.predict (X)
    # Reshaping the prediction value to 0 for valid and 1 for fraud
    y_pred[y_pred == 1] = 0
    y_pred[y_pred == -1] = 1
    n_errors = (y_pred != Y).sum ()
    # Run Classification Metrics
print("{0}: {1}".format (clf_name, n_errors))
print(accuracy_score (Y, y_pred))
print(classification_report (Y, y_pred))