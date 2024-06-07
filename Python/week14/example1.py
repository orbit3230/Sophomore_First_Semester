import numpy as np

def power_of_n_matrix(n, dtype=np.int64) :
    return np.array([[i*n + j for j in range(n)] for i in range(n)], dtype=dtype)

print(power_of_n_matrix(5))