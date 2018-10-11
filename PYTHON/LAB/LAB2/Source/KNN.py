from sklearn import neighbors,datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

#digits dataset
data = datasets.load_digits()
x=data.data
y=data.target

print("Number of rows and columns in dataset : ", data.data.shape)

train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.25, random_state=10)

#k=1
knn=neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(train_x,train_y)
predict=knn.predict(test_x)
print(accuracy_score(predict,test_y))

#k for bigger values
knn=neighbors.KNeighborsClassifier(n_neighbors=50)
knn.fit(train_x,train_y)
predict=knn.predict(test_x)
print(accuracy_score(predict,test_y))

knn=neighbors.KNeighborsClassifier(n_neighbors=99)
knn.fit(train_x,train_y)
predict=knn.predict(test_x)
print(accuracy_score(predict,test_y))