#collective.py
#example to run: mpiexec -n 4 python collective.py 10000
import numpy
import sys
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = int(sys.argv[1])

x = numpy.linspace(start=float(rank)/size, stop=float(1+rank)/size, num=n//size, endpoint=False)
cosx = numpy.cos(x)

#initializing variables. mpi4py requires that we pass numpy objects.
integral = numpy.zeros(1)
total = numpy.zeros(1)

# perform local computation. Each process integrates its own interval
integral[0] = numpy.sum(cosx)*1.0/n
print("Estimate of integral of cos(x) from %f to %f is %f" % (float(rank)/size, float(1+rank)/size, integral))
# communication
# root node receives results with a collective "reduce"
comm.Reduce(integral, total, op=MPI.SUM, root=0)

# root process prints results
if comm.rank == 0:
    print("With n=%d our estimate of the integral from 0 to 1 of cos(x) is %f" % (n, total))
    print("Exact integral (sin(1)) is %f" % (numpy.sin(1.0)))
