import numpy as np
from skimage import color
import time

def window_processing(roi, current_value, mask, window_size):

    roi = (roi > current_value).astype(int)
    roi[window_size//2, window_size//2] = 0
    
    return np.sum(roi * mask)



def lbp(img, window_size, mask):
    
    #start timer
    start = time.time()
    
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
    
    #stop timer and print execution time
    end = time.time()
    print("Time spent in circular lbp [s]: " + str(end- start))
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


def circular_lbp(img, P: int, R: int):
    
    #start timer
    start = time.time()
    
    # P = number of points on the circle
    # R = radius
    
    img = color.rgb2gray(img)
    h = img.shape[0]
    w = img.shape[1]
    new_img = np.zeros((h, w))
    
    #to avoid border issues
    edge_limit = R + 1 + 1
    
    #array from 0 to P-1
    k = np.arange(P)
    
    powers = 2**k
    
    for i in range(edge_limit, h - edge_limit):
        for j in range(edge_limit, w - edge_limit):
            
            #intesity level of central pixel
            vc = img[i][j]
            
            #coordinates of points along the circle
            xk = i + R * np.cos((2*np.pi*k) / P)
            yk = j - R * np.sin((2*np.pi*k) / P)
            
            vk = np.ones((P,1))
            #for small values of P should not be to costly
            #RUNNING THIS I SEE THAT IT ACTUALLY IS !
            for index in range(P):
                if (np.modf(xk[index])[0] == 0 and np.modf(yk[index])[0] == 0):
                    vk[index] = img[int(xk[index])][int(yk[index])]
                else:
                    
                    x = xk[index]
                    y = yk[index]
                    
                    whole_x = int(np.modf(x)[1])
                    whole_y = int(np.modf(y)[1])
                    
                    f00 = img[whole_x][whole_y]
                    f01 = img[whole_x][whole_y + 1]
                    f10 = img[whole_x + 1][whole_y]
                    f11 = img[whole_x + 1][whole_y + 1]
                    
                    vk[index] = f00*(1-x)*(1-y) + \
                                f10*x*(1-y) + f01*(1-x)*y + \
                                f11*x*y
            
            boolean = (vk - vc) >= 0
            new_img[i][j] = np.sum( boolean.astype(int) * powers)
            
    
    #stop timer and print execution time
    end = time.time()
    print("Time spent in circular lbp [s]: " + str(end- start))
    return new_img
            
            
    
    
    
    
    
    
    


