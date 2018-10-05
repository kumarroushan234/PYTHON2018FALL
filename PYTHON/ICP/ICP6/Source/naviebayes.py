#import packages for datasets,metrics,Gaussian NB model and test for training data
from sklearn import datasets,metrics
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split

#load the iris datasets
irisdatasets=datasets.load_iris()
#load the irisdatasets column values
x=irisdatasets.data
y=irisdatasets.target

#split the data for training and testing cross validation
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
#define the model
model=GaussianNB(priors=None)
#fit the training data into model
model.fit(x_train,y_train)
#prints the probability of training data
#print(model.score(x_train,y_train))
def __init__(self, priors=None, var_smoothing=1e-9):
    self.priors = priors
    self.var_smoothing = var_smoothing
 #define to predict the test data
y_pred = model.predict(x_test)
#calc accuracy
print("Accuracy : ",metrics.accuracy_score(y_test, y_pred))
