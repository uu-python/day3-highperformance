# Exercises for Day 3
Numpy and inheritance

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

## 2. Speed optimization using Numpy
Revisit the ```matmult.py``` example from yesterday and improve its performance using Numpy.

## 3. Examples on classes and inheritance in Python

#### a. Create a "Person" class which takes firstname and lastname as arguments to the constructor (```___init___```) and define a method that returns the full name of the person as a combined string.

#### b. Create a "Student" class which inherits from the "Person" class, takes the subject area as an additional argument to the constructor and define a method that prints the full name and the subject area of the student.

#### c. You should be able now to use your "Student" class like this:
```
In [1]: from classroom import Student
In [2]: me = Student('Benedikt', 'Daurer', 'physics') 
In [3]: me.printNameSubject() 
Benedikt Daurer, physics
```

#### d. Create a "Teacher" class which also inherits from "Person", takes the name of the course (e.g. Python programming) as an argument and define a method that prints the full name of the teacher and the course he teaches. 

