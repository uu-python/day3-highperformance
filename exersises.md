# Exercises for Day 3
Inheritance, Numpy, MPI and GPU

## 1. Examples on classes and inheritance in Python

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


## 2. Numpy exercises

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

## 3. Speed optimization using Numpy
Revisit the ```matmult.py``` example from yesterday and improve its performance using Numpy.

## 4. MPI parallelization

#### a. Write a simple MPI script ```mpi_ranks.py``` that prints the rank of the different processes when running 
```
mpirun python mpi_ranks.py
```

#### b. Write a small script ```mpi_sum.py``` which calculates the sum over all ranks and prints the result from the process with rank 0.
Hint: Have a look at the tutorials from the mpi4py documentation page: [https://mpi4py.scipy.org/docs/usrman/tutorial.html](https://mpi4py.scipy.org/docs/usrman/tutorial.html)


## 5. GPU Computing
In this exercise we'll test the speed advantage of CuPy over NumPy in different circunstances.
We'll use Google Colab as a way to run GPU code.
Go to [https://colab.research.google.com](https://colab.research.google.com) and create a new notebook.
By default notebooks don't have GPU capabilities. To turn on the GPU go to Edit -> Notebook settings -> Hardware accelerator -> GPU

You can now run `!nvidia-smi` and should be able to see something like:
```
Tue Mar  7 12:19:49 2023       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.85.12    Driver Version: 525.85.12    CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla T4            Off  | 00000000:00:04.0 Off |                    0 |
| N/A   49C    P0    25W /  70W |      0MiB / 15360MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```
in this case showing a Tesla T4 GPU available, although in your case the hardware might be different.

You can now import cupy and numpy to compare them.
Use `%timeit` to compare the time to do a 2D Fourier transform on arrays of size 128x128, 256x256, 512x512, 1024x1024 and 2048x2048, between numpy and cupy.
At what sizes does cupy outperform?
What happens now if you set the datatype of the array to `numpy.float32`?

