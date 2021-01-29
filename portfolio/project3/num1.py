import numpy as np
import sys
import time


#memory convinent
'''
list = range(1000)

array = np.arange(1000)

print(sys.getsizeof(5) * 1000)

print(array.size * array.itemsize)

'''

# time taken

s = 1000000

a = list(range(s))
b = list(range(s))

st = time.time()
result = [a[i] + b[i] for i in range(s)]
print('list time =',(time.time() - st) * 1000)

ar1 = np.arange(s)
ar2 = np.arange(s)

st = time.time()
ar3 = ar1 + ar2
print('array time =', (time.time() - st) * 1000)