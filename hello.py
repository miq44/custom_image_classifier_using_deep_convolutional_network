import numpy as np

a = np.arange(15).reshape(3,5)
#print(a.itemsize)

b = np.array([4,5,1])
#print(type(b))

c = np.zeros((4,5))
#print(c)

one = np.ones((2,3,5) , dtype = np.float)
#print(one)

random = np.empty((3,5) )
#print(random)

rng = np.arange(10,15,1)

dim = np.arange(20).reshape(4,5)

large = np.arange(10000)

a = np.array([20,30,40,50])
b = np.arange(4)

res = b-a
res = b**2

res = np.sign(res)
res = res>10
last =res
array = [5,3,5,6]
last = np.array(array).reshape(2,2)

a = np.array([2,3,4,5,6,7,1,0]).reshape(4,2)
b= np.arange(6).reshape(2,3)

res = a.dot(b)
res = np.dot(a,b)
last =res
last = np.random.random((2,3))

a = np.random.random((2,3))
last = a.sum()
last = a.min()

b = np.arange(12).reshape(3,4)

last = b.sum(axis=0)
last = b.sum(axis = 1)
last = b.cumsum(axis=0)


a = np.arange(3)
print(a)
a = np.sqrt(a)
last =a
print(last)