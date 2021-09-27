
# Biblioteka numeryczna NumPy
import numpy as np
import math
import time

array1 = np.array([1,2,3,4,5], dtype="int16")
array2 = np.array([5,7,1,10,15], dtype="int16")
array3 = np.array([ [1,2,3], [4,5,6], [7,8,9] ], dtype="int16")

print(array1+array2)
print(array1*2)
print(array2-5)

# Pierwiastkowanie na liscie z wykorzystaniem Math
ts1 = time.time()
for i in range(10):
    result = [math.sqrt(x) for x in range(1,1_000_000) ]
ts2 = time.time()
print(ts2-ts1)

ts1 = time.time()
for i in range(10):
    result = np.sqrt(np.arange(1, 1_000_000))
ts2 = time.time()
print(ts2-ts1)

