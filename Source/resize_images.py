from PIL import Image
import os

#getting the current working directory and 
#changing it to the images folder
cwd = os.path.abspath(os.getcwd())
cwd = cwd.replace("Source", "Images")

#list containing all the names of the images
images = os.listdir(cwd)

#resize the data set
for i in range(len(images)):
    img = Image.open(cwd + "/" +images[i])
    img = img.resize((384, 256))
    name = images[i].split(".")
    img.save(cwd + "/" + str(i+10) + "." + str( name[len(name)-1] ))
