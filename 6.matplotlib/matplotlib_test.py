import matplotlib.pyplot as pl
import numpy as np

x = np.array([1,2,3,4,5,6,7,8])
y = np.array([2,3,4,5,1,4,5,8])

data3 = np.ones([2, 3])
data4 = np.array([[1, 2, 3], [4, 5, 6]])
print(data3+data4)
print(data3 * data4)
pl.bar(x,y,0.5,alpha=0.5,color='r')
pl.plot(x,y,"b")
#pl.show()


