import numpy as np

def calculate(array):
    if len(array) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(array).reshape(3, 3)
    
    operations = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }

    calculations = {}
    for key, func in operations.items():
        calculations[key] = [
            func(matrix, axis=0).tolist(),
            func(matrix, axis=1).tolist(),
            func(matrix).item()
        ]
    
    return calculations