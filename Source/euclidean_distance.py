import numpy as np

def euclidean_distance(img1, img2):
    return np.sqrt(np.sum(np.power(img1 - img2, 2)))

