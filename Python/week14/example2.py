import numpy as np

def create_ndarray_type(shape, type, dtype=np.int64) :
    if type == 1 :
        return np.ones(shape, dtype)
    elif type == 'empty' :
        return np.empty(shape, dtype)
    else :
        return np.zeros(shape, dtype)
    
    
print(create_ndarray_type(shape=(2, 2), type=1))
print(create_ndarray_type(shape=(3, 3), type=99))