import numpy as np


def calculate(numbers):
    if len(numbers) < 9:
        raise ValueError("List must contain nine numbers.")
    matrix = np.array([numbers[:3], numbers[3:6], numbers[6:10]])  # turn list into 3x3 matrix
    results = {}
    results['mean'] = [np.ndarray.tolist(matrix.mean(axis=0)),  # mean of axis 0, axis 1, and flattened
                      np.ndarray.tolist(matrix.mean(axis=1)),
                      matrix.flatten().mean()]
    results['variance'] = [np.ndarray.tolist(matrix.var(axis=0)),
                          np.ndarray.tolist(matrix.var(axis=1)),
                          matrix.flatten().var()]
    results['standard deviation'] = [np.ndarray.tolist(matrix.std(axis=0)),
                                    np.ndarray.tolist(matrix.std(axis=1)),
                                    matrix.flatten().std()]
    results['max'] = [np.ndarray.tolist(matrix.max(axis=0, initial=None)),
                     np.ndarray.tolist(matrix.max(axis=1, initial=None)),
                     matrix.flatten().max(initial=None)]
    results['min'] = [np.ndarray.tolist(matrix.min(axis=0, initial=None)),
                     np.ndarray.tolist(matrix.min(axis=1, initial=None)),
                     matrix.flatten().min(initial=None)]
    results['sum'] = [np.ndarray.tolist(matrix.sum(axis=0)),
                     np.ndarray.tolist(matrix.sum(axis=1)),
                     matrix.flatten().sum()]
    return results


