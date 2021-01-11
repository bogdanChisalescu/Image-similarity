import os
import numpy as np
import matplotlib.pyplot as plt
from lbp import *
from euclidean_distance import euclidean_distance
import time
from shutil import copyfile
from final_interface_v2 import Panel
import re
#start timer
start = time.time()


#getting the current working directory and 
#changing it to the images folder
cwd = os.path.abspath(os.getcwd())
cwd = cwd.replace("Source", "Images/")

#list containing all the names of the images
global images
images = os.listdir(cwd)

mask = np.array([[6,7,0], [5,0,1], [4,3,2]])
mask = pow(2, mask)

#execute lbp on every image in the dataset

#avem nevoie de o alta functie ce face lbp, pentru a o apela in gui
def lbp_imagines(images):
    lbp_img = list()
    for i in range(len(images)):
        lbp_img.append(lbp(plt.imread(os.path.join(cwd, images[i])), 3, mask))
        #lbp_img.append(mlbp(plt.imread(os.path.join(cwd, images[i])), 3, mask))
        #lbp_img.append(circular_lbp(plt.imread(os.path.join(cwd, images[i])), 3, 2))

    return lbp_img

#choosing an image and displaying it
# -10 for image number in folder
#creare legatura gui cu lbp
panel=Panel()
global img_path_selectata
img_path_selectata=panel.img_path
def Img_number(img_path_selectata):
    #extrag numarul din filename
    img_number=re.search('[0-9][0-9]', img_path_selectata) # cauta 2 numere alaturate
    img_number=int(img_number.group())-10
    print(img_number)
    #return img_number

#trebuie sa returnam valoarea img_path

#f, axarr = plt.subplots(2,1)
#axarr[0].imshow(plt.imread(img_path))
#axarr[1].imshow(lbp_img[img_number]) # group(), selecteaza match-ul



#calculate euclidean distance between the chosen image and data set
lbp_img=lbp_imagines(images)
euclidean_distances = list()
for i in range(len(images)):
    euclidean_distances.append(euclidean_distance(lbp_img[Img_number(img_path_selectata)], lbp_img[i]))
    

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
    
    f, axarr = plt.subplots(2,1)
    f.suptitle('Image closest no.: ' + str(j+1))
    axarr[0].imshow(plt.imread(os.path.join(cwd, images[index])))
    axarr[1].imshow(lbp_img[index])

    #salvare poze
    img_path_src=os.path.join(cwd, images[index])
    img_path_dest=os.path.join('D:\Facultate\IOM\Image-similarity\LBP_img\\', '{j}.jpg').format(j=j+1)
    copyfile(img_path_src, img_path_dest)

    plt.show()
    print(index)
    


#stop timer and print execution time
end = time.time()
print("Elapsed time [s]: " + str(end- start))