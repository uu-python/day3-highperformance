import numpy as np

a = np.zeros([10])
a[4] = 5
#print(a)

b = np.arange(10,50)
#print(b)

c = b[::-1]
#print(c)

d = np.arange(0,9).reshape(3,3)
#print(d)

e1 = np.array([1,2,0,0,4,0])
e2 = e1 != 0
#print(e1[e2])

f = np.random.rand(30)
#print(np.mean(f))

g = np.ones(9).reshape(3,3)
g[1][1] = 0
#print(g)

h = np.zeros([8,8])
h[::2,::2] = 1
h[1::2,1::2] = 1
#print(h)

i = np.tile([[1,0],[0,1]],(4,4))
#print(i)

j = np.arange(11)
j[3:9] *= -1
#print(j)

k = np.random.random(10)
k = np.sort(k)
#print(k)

l1 = np.random.randint(0,2,5)
l2 = np.random.randint(0,2,5)
equal = np.array_equal(l1,l2)
#print(equal)

m = np.arange(10, dtype=np.int32)
#print(m.dtype)
m = m.astype(np.float32)
#print(m.dtype)

n1 = np.arange(9).reshape(3,3)
n2 = n1 + 1
n3 = np.dot(n1,n2)
n4 = np.diagonal(n3)
#print(n4)
