import numpy as np

def normalize_ndarray(X, axis, dtype=np.float64):
    if axis == 1 :
        # mean -> numpy array for mean values of each row & resize from row vector to vector
        mean = np.mean(X, axis=1).reshape(-1, 1)
        # std -> numpy array for std values of each row & resize from row vector to vector
        std = np.std(X, axis=1).reshape(-1, 1)
        # vectorized operation
        Z = (X - mean) / std
    elif axis == 0 :
        # mean -> numpy array for mean values of each column
        mean = np.mean(X, axis=0)
        # std -> numpy array for std values of each column
        std = np.std(X, axis=0)
        # vectorized operation
        Z = (X - mean) / std
    elif axis == 'all' :
        # mean -> mean value of all elements (scarlar)
        mean = np.mean(X)
        # std -> std value of all elements (scarlar)
        std = np.std(X)
        # vectorized operation
        Z = (X - mean) / std
        
    # type conversion
    return Z.astype(dtype)
        
        
X = np.arange(12, dtype=np.int64).reshape(6, 2)
print(normalize_ndarray(X, 'all'))
print()
print(normalize_ndarray(X, 1))
print()
print(normalize_ndarray(X, 0))
print()

Y = np.random.randint(0, 1000, size=12, dtype=np.int64).reshape(6, 2)
print(normalize_ndarray(Y, 'all'))
print()
print(normalize_ndarray(Y, 1))
print()
print(normalize_ndarray(Y, 0))
print()