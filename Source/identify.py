import matplotlib.pyplot as plt
from lbp import lbp
from euclidean_distance import euclidean_distance
import time
import os
import numpy as np
from queue import PriorityQueue

#THIS FOR KEEPS ALL LBPs IN MEMORY


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

#choosing main image 
img_number = 7

#calcualting lbp for main image
main_lbp = lbp( plt.imread(os.path.join(cwd, images[img_number])), 3, mask)

f, axarr = plt.subplots(2,1)
f.suptitle("Main image")
axarr[0].imshow(plt.imread(os.path.join(cwd, images[img_number])))
axarr[1].imshow(main_lbp)

images.remove(images[img_number])


lbps = PriorityQueue()
for i in range(len(images)):
    im_lbp = lbp( plt.imread(os.path.join(cwd, images[i])), 3, mask)
    dist = euclidean_distance(im_lbp, main_lbp)
    lbps.put((dist, im_lbp, i))



for i in range(3):
    index = lbps.get()
    f, axarr = plt.subplots(2,1)
    f.suptitle("Closest image no.: " + str(i+1))
    #im_lbp = lbp( plt.imread(os.path.join(cwd, images[ index[1] ])), 3, mask)
    
    axarr[0].imshow(plt.imread(os.path.join(cwd, images[ index[2] ] )))
    axarr[1].imshow(index[1])
    

#stop timer and print execution time
end = time.time()
print("Elapsed time [s]: " + str(end- start))