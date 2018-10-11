from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from matplotlib.pyplot import plot
#loading dataset digits
svmdatasets=datasets.load_iris()

x=svmdatasets.data
y=svmdatasets.target

#spliting the data as testing data = 20%, training data = 80%
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#Applying SVC with Linear kernel
model1 = svm.SVC(kernel='linear')
model1.fit(x_train,y_train)
y_prediction=model1.predict(x_test)
print("Linear Kernel:" + str(accuracy_score(y_test,y_prediction)))

#Applying SVC with RBF kernel
model2 = svm.SVC(kernel='rbf')
model2.fit(x_train,y_train)
y_pred=model2.predict(x_test)
print("RBF kernel:" + str(accuracy_score(y_test,y_pred)))