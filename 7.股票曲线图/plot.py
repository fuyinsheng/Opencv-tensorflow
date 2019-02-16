import numpy as np
import matplotlib.pyplot as pl
date = np.array([i for i in range(1,16)])
priceBegin = np.array([19.59,19.51,\
                       20.98,18.67,18.52,19,\
                     18.64,18.2,
\
                       18.73,18.84,18.42,\
                       18.2,18.55,\
                       19.02,18.78])
priceEnd = np.array([19.45,19.83,

                     20.6,20.56,

                     18.69,18.56,

                     19.18,18.68,

                     18.38,18.8,
 
                    18.94,18.39,
 
                    18.16,18.7,18.68])

priceHeight = np.array([20.23,19.
9,21.97,20.56,18.93,
 
                      19.09,19.32,18.78,
 
                       19.04,19,19.37,

                        18.4,18.59,

                        19.18,19.27])

priceLow = np.array([19.33,19,20.56,18.5,18.42
,18.51,18.54,18.07,18.34,18.6,18.4,18.18,18.1,18.6,18.68])


for i in range(1,15):
	dateOne = np.zeros([2])
	dateOne[0] = i;
	dateOne[1] = i
	
	priceOne = np.zeros([2])
	priceOne[0] = priceBegin[i]
	priceOne[1] = priceEnd[i]
	priceMaxMin = np.zeros([2])
	priceMaxMin[0] = priceHeight[i]
	priceMaxMin[1]= priceLow[i]
	if priceOne[0] > priceOne[1]:
		pl.plot(dateOne, priceOne, 'g', lw=8)
		pl.plot(dateOne,priceMaxMin,color='g',lw=1)

	else :	
		pl.plot(dateOne, priceOne, 'r', lw=8)
		pl.plot(dateOne,priceMaxMin,color='r',lw=1)

pl.show()



