import numpy as np
from skimage import color

def window_processing(roi, current_value, mask, window_size):

    roi = (roi > current_value).astype(int)
    roi[window_size//2, window_size//2] = 0
    
    return np.sum(roi * mask)


def lbp(img, window_size, mask):
    
    img = color.rgb2gray(img)
    h = img.shape[0]
    w = img.shape[1]
    new_img = np.zeros((h, w))
    
    for i in range(window_size, h - window_size):
        for j in range(window_size, w - window_size):
            
            roi = img[i - window_size//2 : i + window_size//2 +1, \
                      j - window_size//2 : j + window_size//2 + 1 ]
                
            current_value = img[i][j]
            new_img[i][j] = window_processing(roi, current_value, mask, window_size)
    
    return new_img


def mlbp(img, window_size, mask):
    
    img = color.rgb2gray(img)
    h = img.shape[0]
    w = img.shape[1]
    new_img = np.zeros((h, w))
    
    for i in range(window_size, h - window_size):
        for j in range(window_size, w - window_size):
            
            roi = img[i - window_size//2 : i + window_size//2 +1, \
                      j - window_size//2 : j + window_size//2 + 1 ]
                
            roi_mean = np.sum(roi)/(window_size**2)
            new_img[i][j] = window_processing(roi, roi_mean, mask, window_size)
    
    return new_img
