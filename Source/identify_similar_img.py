import os
import numpy as np
import matplotlib.pyplot as plt
from lbp import lbp
from euclidean_distance import euclidean_distance
import time

#start timer
start = time.time()

#getting the current working directory and 
#changing it to the images folder
cwd = os.path.abspath(os.getcwd())
cwd = cwd.replace("Source", "Images/")

#list containing all the names of the images
images = os.listdir(cwd)

mask = np.array([[7,6,5], [0,0,4], [1,2,3]])
mask = pow(2, mask)

#execute lbp on every image in the dataset
lbp_img = list()
for i in range(len(images)):
    lbp_img.append(lbp(plt.imread(os.path.join(cwd, images[i])), 3, mask)) 

#choosing an image and displaying it
img_number = 10
img = plt.imread(os.path.join(cwd, images[img_number]))
plt.figure()
plt.imshow(img)

#calculate euclidean distance between the chosen image and data set
euclidean_distances = list()
for i in range(len(images)):
    euclidean_distances.append(euclidean_distance(lbp_img[img_number], lbp_img[i]))
    
#print the 3 most similar images
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
    
    plt.figure()
    plt.imshow(plt.imread(os.path.join(cwd, images[index])))
    
    print(index)

#stop timer and print execution time
end = time.time()
print("Elapsed time [s]: " + str(end- start))