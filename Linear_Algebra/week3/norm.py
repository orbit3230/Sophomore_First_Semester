import numpy as np
import matplotlib.pyplot as plt
import math

# ---Norm---
x = np.array([2, -1, 2])
print(np.linalg.norm(x))

# ---Triangular inequality---
x = np.random.random(10)
y = np.random.random(10)
left = np.linalg.norm(x+y)
right = np.linalg.norm(x) + np.linalg.norm(y)
print(left, "<=", right)

# ---RMS value---
t = np.arange(0, 1.01, 0.1)  # 0.0, 0.1, 0.2, ... 1.0
x = np.cos(8*t) - 2*np.sin(11*t)  # 임의로 변형
print("t: ", t)
print("x: ", x)

rms = lambda x: np.linalg.norm(x)/np.sqrt(len(x))
print("rms: ", rms(x))

plt.plot(t, x)
plt.plot(t, np.mean(x)*np.ones(len(x)))
plt.plot(t, (np.mean(x)+rms(x))*np.ones(len(x)), 'g')
plt.plot(t, (np.mean(x)-rms(x))*np.ones(len(x)), 'g')
plt.savefig("rms.pdf", format = 'pdf')

# ---Chebyshev inequality---
x = np.array([0, 1, 1, 1, 1, 1, 1, 10])
cheb_bound = lambda x,a : math.floor(sum(x**2)/a**2) # np.linalg.norm(x)**2 ?
a = 9

print("value of a: ", a)
print("vector x: ", x)
print("Chebyshev bound: ", cheb_bound(x, a))
print("number of values >= a: ", sum(abs(x) >= a))

# ---Distance---
u = np.array([1.8, 2.0, -3.7, 4.7])
v = np.array([0.6, 2.1, 1.9, -1.4])
w = np.array([2.0, 1.9, -4.0, 4.6])

print("dist(u, v): ", np.linalg.norm(u-v))
print("dist(u, w): ", np.linalg.norm(u-w))
print("dist(v, w): ", np.linalg.norm(v-w))

# ---Nearest neighbor---
nn = lambda x, z : z[np.argmin([np.linalg.norm(x-y) for y in z])]
z = ([2,1], [7,2], [5.5,4], [4,8], [1,5], [9,6])
x = np.array([5,6])
print("Nearest from [5,6]: ", nn(x,z))
print("Nearest from [3,3]: ", nn(np.array([3,3]), z))

# ---Demeaning a vector---
de_mean = lambda x: x - sum(x) / len(x)
x = np.array([1, -2.2, 3])
print("avg. of x: ", np.mean(x))
demeaned_x = de_mean(x)
print('y        : ', demeaned_x)
print('avg. of x_tilde: ', math.ceil(np.mean(demeaned_x)))

# ---Standard deviation---
x = np.random.random(100)
de_mean = lambda x: x - sum(x)/len(x)
demeaned_x = de_mean(x)

st_dev1 = lambda x: np.linalg.norm(demeaned_x)/(len(x)**0.5)
print("st_dev1 - rms_of_demeaned_x: ", st_dev1(x))
st_dev2 = lambda x: np.linalg.norm(x - sum(x)/len(x))/(len(x)**0.5)
print("st_dev2: ", st_dev2(x))

# ---Angle---
angle = lambda x,y : np.arccos(x @ y / (np.linalg.norm(x)*np.linalg.norm(y)))
a = np.array([1, 2, -1])
b = np.array([2, 0, -3])
print("angle    : ", angle(a, b))
print("in degree : ", angle(a, b) * (360/(2*np.pi)))

# ---Correlation coefficient---
def corr_coef(a, b) :
    x = a - sum(a)/len(a)
    y = b - sum(b)/len(b)
    denom = (np.linalg.norm(x)*np.linalg.norm(y))
    return (x @ y) / denom

a = np.array([4.4, 9.4, 15.4, 12.4, 10.4, 1.4, -4.6, -5.6, -0.6, 7.4])
b = np.array([6.2, 11.2, 14.2, 14.2, 8.2, 2.2, -3.8, -4.8, -1.8, 4.2])
print("case1: ", corr_coef(a, b))

a = np.array([4.1, 10.1, 15.1, 13.1, 7.1, 2.1, -2.9, -5.9, 0.1, 7.1])
b = np.array([5.5, -0.5, -4.5, -3.5, 1.5, 7.5, 13.5, 14.5, 11.5, 4.5])
print("case1: ", corr_coef(a, b))

a = np.array([-5.0, 0.0, 5.0, 8.0, 13.0, 11.0, 1.0, 6.0, 4.0, 7.0])
b = np.array([5.8, 0.8, 7.8, 9.8, 0.8, 11.8, 10.8, 5.8, -0.2, -3.2])
print("case1: ", corr_coef(a, b))