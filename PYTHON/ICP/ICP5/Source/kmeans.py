from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([1,1.5,3,5,3.5,4.5])
x2 = np.array([1,2,4,7,5,5])

plt.plot()
plt.xlim([0, 8])
plt.ylim([0, 8])
plt.title('Dataset')
plt.scatter(x1, x2)
plt.show()

plt.plot()
X = np.array(list(zip(x1, x2)))
print(X)
#X = np.array(list(zip(x1, x2))).reshape(len(X),2)
#print(X)
colors = ['b', 'g', 'r']
markers = ['o', 'v', 's']

# KMeans algorithm
kmeans_model = KMeans(n_clusters=2).fit(X)

plt.plot()
for i, l in enumerate(kmeans_model.labels_):
    plt.plot(x1[i], x2[i], color=colors[l], marker=markers[l],ls='None')
    plt.xlim([0, 8])
    plt.ylim([0, 8])

plt.show()