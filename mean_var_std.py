# To find mean,variance,standard deviation ,min,max,sum from series of element in a list

import numpy as np


def Calculate(array):
    try:
        a=array.reshape((3,3))
    except ValueError:
        print("List must contain nine numbers.")
    # mean
    mean1=np.mean(a,axis=0)
    mean2=np.mean(a,axis=1)
    mean=np.mean(a)

    # variance
    var1=np.var(a,axis=0)
    var2=np.var(a, axis=1)
    var =np.var(a)

    # standard deviation
    std1=np.std(a, axis=0)
    std2=np.std(a,axis=1)
    std=np.std(a)

    #maximum
    max1=np.max(a,axis=0)
    max2=np.max(a,axis=1)
    max=np.max(a)

    # minimum
    min1 = np.min(a, axis=0)
    min2 = np.min(a, axis=1)
    min = np.min(a)

    # sum
    sum1=np.sum(a,axis=0)
    sum2 = np.sum(a, axis=1)
    sum = np.sum(a)

    return {'mean': [mean1, mean2, mean],
  'variance': [var1, var2, var],
  'standard deviation': [std1, std2, std],
  'max': [max1,max2,max],
  'min': [min1,min2,min],
  'sum': [sum1,sum2,sum]}

print(Calculate(np.array(range(9))))



