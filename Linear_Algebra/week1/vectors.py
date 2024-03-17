import numpy as np
import matplotlib.pyplot as plt
import time

# ---Vector---
x = [-1.1, 0.0, 3.6, 7.2]
print(len(x))  # 4

y = np.array([-1.1, 0.0, 3.6, 7.2])
print(y)  # [-1.1, 0. , 3.6, 7.2]

print(x[2])  # 3.6

x[2] = 2022
print(x[2])  # 2022

# ---Assignment vs. Copying---
x = [-1.1, 0.0, 3.6, 7.2]
x = y  # y는 numpy array, x에 assign. (참조를 전달)
y[2] = 0
print(x) # [-1.1, 0. , 0. , 7.2]
print(y) # [-1.1, 0. , 0. , 7.2]

y = np.array([-1.1, 0.0, 3.6, 7.2])
x = y.copy()  # y는 numpy array, x에 copy. (값을 복사)
y[2] = 0
print(x) # [-1.1, 0. , 3.6 , 7.2]
print(y) # [-1.1, 0. , 0. , 7.2]

# ---Vector equality---
x = [-1.1, 0, 3.6, 7.2]
y = x.copy()
print(x == y)  # True

x = [-1.1, 0, 3.6, 7.2]
y = x.copy()
y[2] = 2022
print(x == y)  # False

x = 2022    # Scalar
y = [2022]  # 1-Vector
print(x == y)      # False
print(x == y[0])   # True

x = 2022    # Scalar
y = np.array([2022, 2022])  # numpy array
print(x == y)      # array([True, True])

# ---Block Vector---
x = np.array([1, 1])
y = np.array([2, 2, 2])
z = np.concatenate((x, y))
print(z)  # [1 1 2 2 2]
# Caution! this is a list of vectors(Not a block vector)
x = [1, 1]
y = [2, 2, 2]
z = [x, y]
print(z)  # [[1, 1], [2, 2, 2]]

# ---Subvector---
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = x[1:4]  # 0번 인덱스 부터 시작
print(y)    # [2 3 4] 

x[1:4] = [200, 300, 400]
print(x)   # [1, 200, 300, 400, 5, 6, 7]

# 지정 인덱스 부터 To end.
x = np.array([1, 2, 3, 4, 5, 6, 7])
print(x[2:])  # array([3, 4, 5, 6, 7])
# To end -1
print(x[:-1]) # array([1, 2, 3, 4, 5, 6])
# All
print(x[:]) # array([1, 2, 3, 4, 5, 6, 7])
# from-to-update
print(x[1:5:2]) # array([2, 4])

# ---Zero vector, Ones vector---
print(np.zeros(3))  # array([0., 0., 0.])
print(np.ones(4))  # array([1., 1., 1., 1.])
print(np.random.random(4))  # 0이상 1미만 4개의 난수로 채워진 numpy array 생성

# ---Unit vector---
size = 4
unit_vectors = []
for i in range(size) :
    v = np.zeros(size)
    v[i] = 1
    unit_vectors.append(v)
print(unit_vectors)

# ---Plotting---
data = [71, 71, 68, 69, 68, 69, 68, 74, 77, 82, 85, 86, 
        88, 86, 85, 86, 84, 79, 77, 75, 73, 71, 70, 70, 69, 69, 69,
        69, 67, 68, 68, 73, 76, 77, 82, 84, 84, 81, 80, 78, 79, 78,
        73, 72, 70, 70, 68, 67]
plt.plot(data, '-bo')
plt.savefig("temperature.pdf", format = 'pdf')

# ---addition/Subtraction---
x = np.array([1, 2, 3])
y = np.array([100, 200, 300])
print(x+y)  # [101 202 303]
print(x-y)  # [-99 -198 -297]

# ---Scalar Multiplication/Division---
x = np.array([1, 2, 3])
print(100*x)  # [100, 200, 300]
print(x/100)  # [0.01, 0.02, 0.03]

# ---Linear Combination---
x = np.array([1, 2, 3])
y = np.array([100, 200, 300])
a = 0.5
b = 0.5
c = a*x + b*y
print(c)  # [50.5 101. 151.5]

x = np.array([1, 2, 3])
y = np.array([100, 200, 300])
vectors = [x, y]  # Not Block Vector, It's a List of Vectors
coefs = [0.5, 0.5, 0.5]
def linearCombination(vecs, coefs) :
    res = np.zeros(len(vecs[0]))
    for i in range(len(vecs)) : 
        res += coefs[i]*vecs[i]
    return res
print(linearCombination(vectors, coefs))  # [50.5 101. 151.5]

# ---Checking properties---
a = np.random.random(3)
b = np.random.random(3)
beta = np.random.random()
left = beta*(a+b)
right = beta*a + beta*b
print(left == right)  # array([True, True, True])

# ---Inner product---
x = np.array([1, 2, 3])
y = np.array([1, 10, 100])
print(np.inner(x, y))  # 321
print(x @ y)           # 321

# ---Complexity---
a = np.random.random(10**5)
b = np.random.random(10**5)

start = time.time()
for i in range (100) :
    a@b
end = time.time()
print("%.10f" % (end - start))

start = time.time()
for i in range (1000) :
    a@b
end = time.time()
print("%.10f" % (end - start))

start = time.time()
for i in range (10000) :
    a@b
end = time.time()
print("%.10f" % (end - start))

# ---Floating point operations
a = np.random.random()
b = np.random.random()
left = (a+b) * (a-b)
right = a**2 - b**2
print(left == right)
print(left - right)