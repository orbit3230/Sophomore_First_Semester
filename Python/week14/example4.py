import numpy as np

def find_nearest(x, target_value) :
    return x[np.argmin(np.abs(x - target_value))]
    
X = np.random.uniform(0, 1, 100)
target_value = 0.3
print(find_nearest(X, target_value))

target_value = 0.4
print(find_nearest(X, target_value))