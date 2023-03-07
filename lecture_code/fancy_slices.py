# Let's create an array with a large number of rows. 
# We will select slices of this array along the first dimension.
n, d = 100000, 100
a = np.random.random_sample((n, d)); aid = id(a)


# Let's select one every ten rows, using two different methods
# (array view and fancy indexing).
b1 = a[::10]
b2 = a[np.arange(0, n, 10)]
np.array_equal(b1, b2)
True
# The view refers to the original data buffer,
#  whereas fancy indexing yields a copy.
id(b1) == aid, id(b2) == aid
(True, False)
Let's compare the performance of both methods.
%timeit a[::10]
1000000 loops, best of 3: 804 ns per loop
%timeit a[np.arange(0, n, 10)]
100 loops, best of 3: 14.1 ms per loop
Fancy indexing is several orders of magnitude slower as it involves copying a large array.
