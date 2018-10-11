from sklearn.svm import SVC
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn import svm

digitsdataset=datasets.load_digits() #loading digits dataset
x = digitsdataset.data
y = digitsdataset.target
xtrain,xtest,ytrain,ytest=train_test_split(digitsdataset.data,digitsdataset.target,test_size=0.3,random_state=0)
clf = svm.SVC(kernel='poly',degree=4, C=1).fit(xtrain,ytrain)
y_prediction = clf.fit(xtrain,ytrain).predict(xtest)
print("Accuracy with poly kernel: "+str(metrics.accuracy_score(ytest, y_prediction)))
clfr = svm.SVC(kernel='rbf',C=1).fit(xtrain,ytrain)
y_predict = clfr.fit(xtrain,ytrain).predict(xtest)
print("Accuracy with RBF kernel: "+str(metrics.accuracy_score(ytest,y_predict)))
changes1=svm.SVC(kernel='poly',C=9,gamma=9).fit(xtrain,ytrain)
print('changes: ', changes1.score(xtest,ytest))
changes2=svm.SVC(kernel='rbf',C=5,gamma=7).fit(xtrain,ytrain)
print('changes: ', changes2.score(xtest,ytest))
