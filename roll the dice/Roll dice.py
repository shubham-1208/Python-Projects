import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll the Dice')

dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label_dice.configure(image=image1)
    label_dice.image = image1

label_intro = tkinter.Label(root, text="Hello from Shubham!", fg = "Black", bg = "#33FFE3", font = "Helvetica 16 bold italic")
label_intro.pack()

label_dice = tkinter.Label(root)
label_dice.pack( expand=True)

button = tkinter.Button(root, text='Roll the Dice', fg='Black', bg = "#33FFE3",command=rolling_dice)
button.pack( expand=True)

root.mainloop()