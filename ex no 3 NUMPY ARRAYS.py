import numpy as np

a = np.array([1, 2, 3])
print(type(a), a.shape, a[0], a[1], a[2])
a[0] = 5
print(a)

b = np.array([[1,2,3],[4,5,6]])
print(b.shape, b[0,0], b[0,1], b[1,0])

# Slicing
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b = a[:2,1:3]
print(a[0,1])
b[0,0] = 77
print(a[0,1])

# Indexing
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b = np.array([0,2,0,1])
print(a[np.arange(4), b])
a[np.arange(4), b] += 10
print(a)

# Arithmetic
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print(x + y)
print(np.add(x, y))
print(np.sum(x))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))
