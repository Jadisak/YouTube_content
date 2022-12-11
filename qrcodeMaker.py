from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import asksaveasfilename
import qrcode

root = Tk()
root.geometry('1000x1000')
root.title('QR Code Maker')

def makeQR():
    dataQR = data.get()
    qr = qrcode.make(dataQR)
    path = asksaveasfilename(filetypes=[('Image', '*jpg'), ('All','*')])
    qr.save(path)
    img = Image.open(path)
    photo = ImageTk.PhotoImage(img)
    lbl.config(image = photo)

topFrame = Frame(root, borderwidth = 5)
topFrame.pack(padx=10, pady=20)

data = StringVar()
dataEntry = Entry(topFrame, textvariable = data, bg='#fff')
dataEntry.grid(row=0, column=0, padx=10, pady=20)

Button(topFrame, text='Make QR', bg='#46abf2', fg='#fff', command = makeQR).grid(row=0, column=1, padx=10, pady=20)

lbl = Label(root)
lbl.pack(padx=10, pady=20)

root.mainloop()