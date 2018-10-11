import matplotlib.pyplot as mat
import seaborn as sb
from sklearn import datasets,metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import imp

data=datasets.load_iris()
x=data.data
y=data.target

iris = sb.load_dataset("iris")
sb.pairplot(iris, height=1.0)
mat.show()

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)

naive=GaussianNB()
naive.fit(x_train,y_train)
y_pred = naive.predict(x_test)

print("Accuracy : ",metrics.accuracy_score(y_test, y_pred))