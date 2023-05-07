from tkinter import *

from pathlib import Path
from PIL import ImageTk, Image
import os
import glob

# Create the main window
root = Tk()
root.geometry("1024x600")
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/pi/Desktop/Cardigo3/build\assets\frame1")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def deleter():
    path=glob.glob('/home/pi/Desktop/Cardigo3/build/*.jpg')
    for file in path:
        if os.path.isfile(file):
            os.remove(file)

def destroy():
    deleter()
    root.destroy()

# Load the image using the Image module from PIL
img = Image.open('download.jpg')
button_image_10 = PhotoImage(
    file=relative_to_assets("abutton_9.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: destroy(),
    relief="flat"
)
button_10.place(
    x=5.0,
    y=5.0,
    width=37.0,
    height=37.0
)
# Create a PhotoImage object from the image
photo = ImageTk.PhotoImage(img)

# Create a label and set the PhotoImage object as its image
label = Label(root, image=photo)

# Pack the label to display it in the window
label.pack()

# Run the main loop
root.attributes("-fullscreen", True)

root.mainloop()
