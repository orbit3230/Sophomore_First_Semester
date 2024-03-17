import numpy as np
import matplotlib.pyplot as plt
import import_ipynb
from houseSalesData import house_sales_data

# ---Function---
def func(x) :
    res = x[0] + x[1] - x[3]**2
    return res

x = np.array([-1, 0, 1, 10])
print(func(x))  # -101

func = lambda x: x[0] + x[1] - x[3]**2
x = np.array([-1, 0, 1, 10])
print(func(x))  # -101

# ---Superposition---
a = np.random.random(3)
x = np.random.random(3)
y = np.random.random(3)

def func(a, x, y) :
    alpha = np.random.uniform()
    beta = np.random.uniform()
    return np.inner(a, alpha*x + beta*y) == alpha*np.inner(a, x) + beta*np.inner(a, y)

print(func(a, x, y))  # True (if random function is linear)

# ---practice---
func = lambda x: sum(x)/len(x)
v1 = [1, 2, 3, 4, 5]
v2 = [-1, 0, 1]
print(func(v1))  # 3.0
print(func(v2))  # 0.0

print(np.mean(v1))  # 3.0
print(np.mean(v2))  # 0.0

# Regression model
D = house_sales_data()
price = D['price']
area = D['area']
beds = D['beds']
v = 54.4017  # offset
beta = np.array([147.7251, -18.8534])  # parameter
predicted = v + beta[0]*area + beta[1]*beds
plt.scatter(price, predicted)
plt.plot((0,800), (0,800), ls="--", c='r')
plt.ylim(0, 800)
plt.xlim(0, 800)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.savefig("predicted_price.pdf", format = 'pdf')