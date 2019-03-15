#Exercise 4

#import numpy package
import numpy as np

#txt file into numpy array
data = np.loadtxt("precip_data.txt", skiprows=1, usecols=2)

prec_min = data.min()
print("The minimum precipitation is " + str(prec_min))

prec_max = data.max()
print("The maximum precipitation is " + str(prec_max))

prec_mean = data.mean()
print("The mean precipitation is " + str(prec_mean))





