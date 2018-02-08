import numpy as np


def n_size_ndarray_creation(n, dtype=np.int):
    result = np.arange(n**2, dtype = dtype).reshape(n, n)
    return result


def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    if type == 0 :
        result = np.zeros(shape, dtype = dtype)
    elif type == 1 :
        result = np.ones(shape, dtype = dtype)
    elif type == 99 :
        result = np.empty(shape, dtype = dtype)
    return result


def change_shape_of_ndarray(X, n_row):
    result = X.reshape(n_row, -1)
    return result


def concat_ndarray(X_1, X_2, axis):
    try :
        result = np.concatenate((X_1, X_2), axis = axis)
        return result
    except :
        return False


def normalize_ndarray(X, axis=99, dtype=np.float32):
    if axis == 99 :
        result = (X - np.mean(X)) / np.std(X)
    elif axis == 0 :
        result = (X - np.mean(X, axis = axis)) / np.std(X, axis = axis)
    elif axis == 1 :
        result = (X - np.mean(X, axis = axis).reshape(-1, 1)) / np.std(X, axis = axis).reshape(-1, 1)
    return result


def save_ndarray(X, filename="test.npy"):
    np.save(filename, X)
    return


def boolean_index(X, condition):
    result = X[eval("X" + condition)]
    return result

def find_nearest_value(X, target_value):
    result = np.min(X - target_value)
    return result


def get_n_largest_values(X, n):
    X[::-1].sort()
    result = X[:n]
    return result