from lbp import *
from euclidean_distance import *

import os
import numpy as np
import matplotlib.pyplot as plt



# parameters: all images names and images directory
# returns: list of all LBP images 
def compute_lbp_on_data_set(images, cwd):
    
    mask = np.array([[7,6,5], [0,0,4], [1,2,3]])
    mask = pow(2, mask)
    
    #execute lbp on every image in the dataset
    lbp_img = list()
    for i in range(len(images)):
        lbp_img.append(lbp(plt.imread(os.path.join(cwd, images[i])), 3, mask)) 
        #lbp_img.append(mlbp(plt.imread(os.path.join(cwd, images[i])), 3, mask))
        #lbp_img.append(circular_lbp(plt.imread(os.path.join(cwd, images[i])), 3, 2))
        
    return lbp_img

# parameters: LBP images, chosen image index and all images names 
# returns: list of 3 index
def the_3_most_similar(lbp_img, img_number, images):
    #calculate euclidean distance between the chosen image and data set
    euclidean_distances = list()
    for i in range(len(images)):
        euclidean_distances.append(euclidean_distance(lbp_img[img_number], lbp_img[i]))
        
    #get the index for the 3 most similar images
    similars = list()
    
    minim = 0
    maxim = max(euclidean_distances)
    index = 0
    for j in range(3):
        for i in range(len(images)):
            if euclidean_distances[i] > minim and euclidean_distances[i] <= maxim:
                maxim = euclidean_distances[i]
                index = i
        minim = maxim
        maxim = max(euclidean_distances)

        similars.append(index)
        
    return similars