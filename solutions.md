# Exercises: Numpy and inheritance

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
Z[(3 < Z) & (Z <= 8)] *= -1
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

#### m. How to convert an integer (32 bits) array into a float (32 bits) in place?
```
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
A = Z.view(np.float32)
A[:] = Z[:]
print(A.dtype)
print(A.__array_interface__['data'][0] == Z.__array_interface__['data'][0])
print(np.alltrue(A == np.arange(10,dtype=np.int32)))
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

## 2. Speed optimization using Numpy
Revisit the ```matmult.py``` example from yesterday and improve its performance using Numpy.
See ```matmult_numpy.py``` for a possible solution.

## 3. Examples on classes and inheritance in Python

#### a. Create a "Person" class which takes firstname and lastname as arguments to the constructor (```___init___```) and define a method that returns the full name of the person as a combined string.
see ```classroom.py```

#### b. Create a "Student" class which inherits from the "Person" class, takes the subject area as an additional argument to the constructor and define a method that prints the full name and the subject area of the student.
see ```classroom.py```

#### c. You should be able now to use your "Student" class like this:
```
In [1]: from classroom import Student
In [2]: me = Student('Benedikt', 'Daurer', 'physics') 
In [3]: me.printNameSubject() 
Benedikt Daurer, physics
```

#### d. Create a "Teacher" class which also inherits from "Person", takes the name of the course (e.g. Python programming) as an argument and define a method that prints the full name of the teacher and the course he teaches. 
see ```classroom.py```
