import tkinter
import PIL
import csv
import random
from PIL import Image
from PIL import ImageTk
from dataclasses import dataclass

@dataclass
class Entity:
    name: str
    cyrillicName: str
    imagePath: str
    image: PIL.ImageTk.PhotoImage

def changeImages():
    global imagesIndex
    if imagesIndex >= len(entities):
        imagesIndex = 0
    labelImage.config(image=entities[imagesIndex].image)
    labelImage.image = entities[imagesIndex].image
    imagesIndex += 1
    labelCyrillicName.config(text="")

def getMetadata ():
    data = []
    with open("metadata.txt", mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            data.append(row)
    return data

def viewCyrillic():
    labelCyrillicName.config(text=entities[imagesIndex-1].cyrillicName)

def randomizeImages():
    global entities
    global imagesIndex

    random.shuffle(entities)
    imagesIndex = 0
    labelImage.config(image=entities[imagesIndex].image)
    labelImage.image = entities[imagesIndex].image
    imagesIndex += 1
    labelCyrillicName.config(text="")

def addImage():
    print ("Add Image")

def randomizeEntities (entities):
    random.shuffle(entities)
    return entities

def loadImages (path):
    images = []
    metadata = getMetadata ()
    for line in metadata:
        image = Image.open(path + str(line[2]))
        image = image.resize((300, 300), Image.Resampling.LANCZOS)
        hoto_image = ImageTk.PhotoImage(image)
        entity = Entity (line[0], line[1], line[2], hoto_image)
        images.append(entity)
    images = randomizeEntities (images)
    return images

def getImagesDirectory():
    out = "images/"
    with open("config", "r") as config:
        for line in config:
            if line.split("=")[0] == "imagesDirectory":
                out = line.split("=")[1]
    return out

imagesDirectory = getImagesDirectory()

root = tkinter.Tk()
root.title("RUWOLER")
root.geometry("500x420")

entities = loadImages("images/")
imagesIndex = 0

labelImage = tkinter.Label(root, image=entities[imagesIndex].image)
labelImage.pack(pady=1)
imagesIndex += 1

labelCyrillicName = tkinter.Label(root, text="", bg="lightblue", height=1, width=30)
labelCyrillicName.pack(pady=5)

frame1 = tkinter.Frame(root)
frame1.pack(pady=1)

frame2 = tkinter.Frame(root)
frame2.pack(pady=1)

buttonViewCyrillic = tkinter.Button(frame1, text="View Cyrillic", command=viewCyrillic, width=17)
buttonViewCyrillic.grid(row=0, column=1, padx=10)

buttonChangeImage = tkinter.Button(frame2, text="Change Image", command=changeImages, width=17)
buttonChangeImage.grid(row=0, column=1, padx=10)

buttonRandomize = tkinter.Button(frame2, text="Randomize Images", command=randomizeImages, width=17)
buttonRandomize.grid(row=0, column=0, padx=10)

# not implemented
buttonAddImage = tkinter.Button(frame2, text="Add Image", command=addImage, width=17)
buttonAddImage.grid(row=0, column=2, padx=10)
# ---

root.mainloop()
