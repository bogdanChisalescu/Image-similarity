import os
from lbp import lbp
import numpy as np
import matplotlib.pyplot as plt

#getting the current working directory and 
#changing it to the images folder
cwd = os.path.abspath(os.getcwd())
cwd = cwd.replace("Source", "Images/")

#list containing all the names of the images
images = os.listdir(cwd)

print(images)

#opening an image and displaying it
img = plt.imread(os.path.join(cwd, images[1]))
plt.figure()
plt.imshow(img)

mask = np.array([[7,6,5], [0,0,4], [1,2,3]])
mask = pow(2, mask)

new_img = lbp(img, 3 , mask)
plt.figure()
plt.imshow(new_img)