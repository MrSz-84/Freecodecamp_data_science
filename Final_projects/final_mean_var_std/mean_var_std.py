import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    arr = np.reshape(list, newshape=(3, 3))
    mean_a0 = arr.mean(axis=0).tolist()
    mean_a1 = arr.mean(axis=1).tolist()
    mean_fl = arr.flatten().mean().tolist()
    var_a0 = arr.var(axis=0).tolist()
    var_a1 = arr.var(axis=1).tolist()
    var_fl = arr.flatten().var().tolist()
    std_a0 = arr.std(axis=0).tolist()
    std_a1 = arr.std(axis=1).tolist()
    std_fl = arr.flatten().std().tolist()
    max_a0 = arr.max(axis=0).tolist()
    max_a1 = arr.max(axis=1).tolist()
    max_fl = arr.flatten().max().tolist()
    min_a0 = arr.min(axis=0).tolist()
    min_a1 = arr.min(axis=1).tolist()
    min_fl = arr.flatten().min().tolist()
    sum_a0 = arr.sum(axis=0).tolist()
    sum_a1 = arr.sum(axis=1).tolist()
    sum_fl = arr.flatten().sum().tolist()
    calculations = {'mean': [mean_a0, mean_a1, mean_fl],
                    'variance': [var_a0, var_a1, var_fl],
                    'standard deviation': [std_a0, std_a1, std_fl],
                    'max': [max_a0, max_a1, max_fl],
                    'min': [min_a0, min_a1, min_fl],
                    'sum': [sum_a0, sum_a1, sum_fl],
                    }
    return calculations


print(calculate([0,1,2,3,4,5,6,7,8]))