import os
import numpy as np
import matplotlib.pyplot as plt
from lbp import *
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

#choosing an image and displaying it
# -10 for image number in folder
img_number = 43


basic = lbp(plt.imread(os.path.join(cwd, images[img_number])), 3, mask)
mean = mlbp(plt.imread(os.path.join(cwd, images[img_number])), 3, mask)
circ = circular_lbp(plt.imread(os.path.join(cwd, images[img_number])), 8, 1)

plt.imshow(plt.imread(os.path.join(cwd, images[img_number])))
plt.figure()
plt.imshow(basic)
plt.figure()
plt.imshow(mean)
plt.figure()
plt.imshow(circ)
plt.figure()

'''
f, axarr = plt.subplots(2,2)
axarr[0][0].set_title("(a)")
axarr[0][0].imshow(plt.imread(os.path.join(cwd, images[img_number])))

axarr[0][1].set_title("(b)")
axarr[0][1].imshow(basic)

axarr[1][0].set_title("(c)")
axarr[1][0].imshow(mean)

axarr[1][1].set_title("(d)")
axarr[1][1].imshow(circ)
    
'''  


#stop timer and print execution time
end = time.time()
print("Elapsed time [s]: " + str(end- start))