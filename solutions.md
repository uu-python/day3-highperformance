# Exercises: High-performance computing
Speed optimization using Numpy, Cython, MPI and GPU acceleration

## 1. Numpy exercises
Examples were taken from [http://www.labri.fr/perso/nrougier/teaching/numpy.100/](http://www.labri.fr/perso/nrougier/teaching/numpy.100/)

#### a. Create a null vector of size 10 but the fifth value which is 1
```
Z = np.zeros(10)
Z[4] = 1
print(Z)
```

#### b. Create a vector with values ranging from 10 to 49
```
Z = np.arange(10,50)
print(Z)
```

#### c. Reverse a vector (first element becomes last) 
```
Z = np.arange(50)
Z = Z[::-1]
```

#### d. Create a 3x3 matrix with values ranging from 0 to 8
```
Z = np.arange(9).reshape(3,3)
print(Z)
```

#### e. Find indices of non-zero elements from [1,2,0,0,4,0]
```
nz = np.nonzero([1,2,0,0,4,0])
print(nz)
```

#### f. Create a random vector of size 30 and find the mean value
```
Z = np.random.random(30)
m = Z.mean()
print(m
```

#### g. Create a 2d array with 1 on the border and 0 inside
```
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
```

#### h. Create a 8x8 matrix and fill it with a checkerboard pattern
```
Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)
```

#### i. Create a checkerboard 8x8 matrix using the tile function
```
Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
print(Z)
```

#### j. Given a 1D array, negate all elements which are between 3 and 8, in place
```
Z = np.arange(11)
Z...
print(Z)
```

#### k. Create a random vector of size 10 and sort it
```
Z = np.random.random(10)
Z.sort()
print(Z)
```

#### l. Consider two random array A anb B, check if they are equal
```
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.allclose(A,B)
print(equal)
```

#### m. How to convert a float (32 bits) array into an integer (32 bits) in place?
```
Z = np.arange(10, dtype=np.float32)
print(Z.dtype)
Z = Z.astype(np.int32, copy=False)
print(Z.dtype)
```

#### n. How to get the diagonal of a dot product?
```

A = np.arange(9).reshape(3,3)
B = A + 1

# Slow version
D = np.diag(np.dot(A, B))

# Fast version
D = np.sum(A * B.T, axis=1)

# Faster version
D = np.einsum("ij,ji->i", A, B).

print(D)
```

## 2. Speed optimization using Cython
Cythonize the ```primes.py``` script (as described in the lecture notes)

## 3. Start working on your coding project
