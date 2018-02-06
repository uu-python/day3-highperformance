# Exercises: High-performance computing
Speed optimization using Numpy, Cython

## 1. Numpy exercises

#### a. Create a null vector of size 10 but the fifth value which is 1

#### b. Create a vector with values ranging from 10 to 49

#### c. Reverse a vector (first element becomes last) 

#### d. Create a 3x3 matrix with values ranging from 0 to 8

#### e. Find indices of non-zero elements from [1,2,0,0,4,0]

#### f. Create a random vector of size 30 and find the mean value

#### g. Create a 2d array with 1 on the border and 0 inside

#### h. Create a 8x8 matrix and fill it with a checkerboard pattern

#### i. Create a checkerboard 8x8 matrix using the tile function

#### j. Given a 1D array, negate all elements which are between 3 and 8, in place
```
Z = np.arange(11)
Z...
print(Z)
```

#### k. Create a random vector of size 10 and sort it
```
Z = np.random.random(10)
Z = ...
print(Z)
```

#### l. Consider two random array A anb B, check if they are equal
```
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = ...
print(equal)
```

#### m. How to convert an integer (32 bits) array into a float (32 bits) in place?
```
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z = ...
print(Z.dtype)
```

#### n. How to get the diagonal of a dot product?
```
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = ...
print(D)
```

## 2. Speed optimization using Cython
Cythonize the ```primes.py``` script (as described in the lecture notes)
