import numpy as np

def calculate(arr):
    if len(arr) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(arr).reshape(3,3)
    calculations = {
        'mean': [
            np.mean(arr, axis=0).astype(float).tolist(), 
            np.mean(arr, axis=1).astype(float).tolist(), 
            float(np.mean(arr))
            ],
        'variance': [
            np.var(arr, axis=0).astype(float).tolist(), 
            np.var(arr, axis=1).astype(float).tolist(), 
            float(np.var(arr))
            ],
        'standard deviation': [
            np.std(arr, axis=0).astype(float).tolist(), 
            np.std(arr, axis=1).astype(float).tolist(), 
            float(np.std(arr))
            ],
        'max': [
            np.max(arr, axis=0).astype(int).tolist(), 
            np.max(arr, axis=1).astype(int).tolist(), 
            int(np.max(arr))
            ],
        'min': [
            np.min(arr, axis=0).astype(int).tolist(), 
            np.min(arr, axis=1).astype(int).tolist(), 
            int(np.min(arr))
            ],
        'sum': [
            np.sum(arr, axis=0).astype(int).tolist(), 
            np.sum(arr, axis=1).astype(int).tolist(), 
            int(np.sum(arr))
            ]
    }
    return calculations