import numpy as nmp

x = nmp.random.random_integers(0,20,size=15)
print(x)
print("Frequent value is:", nmp.bincount(x).argmax())
