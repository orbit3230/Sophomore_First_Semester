import numpy as np

def concat_ndarray(x1, x2, axis) :
    try :
        return np.concatenate((x1, x2), axis=axis)
    except :
        return False
    
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print(concat_ndarray(a, b, 1))
print(concat_ndarray(a, b, 0))

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7])
print(concat_ndarray(a, b, 1))
print(concat_ndarray(a, b, 0))

a = np.array([1])
b = np.array([5, 6, 7])
print(concat_ndarray(a, b, 1))
print(concat_ndarray(a, b, 0))