from PIL import Image
import os

#getting the current working directory and 
#changing it to the images folder
cwd = os.path.abspath(os.getcwd())
cwd = cwd.replace("Source", "Images")

#list containing all the names of the images
images = os.listdir(cwd)

classes = ["monument", "dino", "flower", "horse", "bmw"]
IMG_PER_CLASS = 10

#resize the data set
for i in range(len(images)):
    
    img = Image.open(cwd + "/" +images[i])
    splited = images[i].split(".")
    extension = splited[len(splited) - 1]
    img.save(cwd + "/" + str(i+10) + "_" + classes[i // IMG_PER_CLASS]  \
                   + "." + extension)
    