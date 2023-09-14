from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Text Editor')
root.minsize(650, 650)
root.configure(background = 'snow')

def getImg(imgName):
    return ImageTk.PhotoImage(Image.open(imgName))

def readLine(file):
    return file.readline().rstrip() 

lblFileName = Label(root, text = 'File Name:', bg = 'light blue', fg = 'black')
lblFileName.place(relx = 0.5, rely = 0.05, anchor = CENTER)

entFileName = Entry(root)
entFileName.place(relx = 0.5, rely = 0.1, anchor = CENTER)

myTxt = Text(root, height = 25, width = 60)
myTxt.place(relx = 0.5, rely = 0.3, anchor = N)

# Buttons
imgs = []
for i in range(3):
    imgs.append(getImg(f'Class158+/Icons/Icon { i }.png'))

def openFile(name):
    myTxt.delete(1.0, END)
    entFileName.delete(0, END)
    
    TEXT_FILE = open(f'Class158+/Texts/Math.txt', 'r')
    data = TEXT_FILE.read()
    print(data)
    myTxt.insert(END, data)
    TEXT_FILE.close()

def saveFile(name):
    TEXT_FILE = open(f'{ name }.txt', 'w')

btnOpen = Button(root, bg = 'snow', command = lambda: openFile('Math'))
btnOpen.place(relx = 0.425, rely = 0.2, anchor = CENTER)
btnOpen['image'] = imgs[0]

btnSave = Button(root, bg = 'snow', command = lambda: saveFile())
btnSave.place(relx = 0.5, rely = 0.2, anchor = CENTER)
btnSave['image'] = imgs[1]

btnReset = Button(root, bg = 'snow', command = lambda: saveFile())
btnReset.place(relx = 0.575, rely = 0.2, anchor = CENTER)
btnReset['image'] = imgs[2]

root.mainloop()