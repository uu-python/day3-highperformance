import numpy as np

a = np.random.random((1000000))
b = list(a)
%timeit a.sum()
%timeit sum(b)

