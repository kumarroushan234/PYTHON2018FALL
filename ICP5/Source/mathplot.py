import numpy as np
import matplotlib.pyplot as plt
x=np.array([2.9,6.7,4.9,7.9,9.8,6.9,6.1,6.2,6,5.1,4.7,4.4,5.8])
y=np.array([4,7.4,5,7.2,7.9,6.1,6,5.8,5.2,4.2,4,4.4,5.2])
meanx=np.mean(x)
meany=np.mean(y)
num=np.sum((x-meanx)*(y-meany))
den=np.sum(pow((x-meanx),2))
slope=num/den
intercept=meany-(slope*meanx)
print("slope",slope)
print("intercept",intercept)
val=(slope*x)+intercept
plt.plot(x,val)
plt.scatter(x,y)
plt.show()