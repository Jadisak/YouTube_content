from tkinter import *
from langcodes import *
from langdetect import detect

root = Tk()
root.geometry('1000x800')
root.title('DetectLang')
root.config(bg='#121212')

def check():
    if my_text.compare('end-1c', '==', '1.0'):
        my_label.config(text='Hey, put some text man!!')
    else:
        code = detect(my_text.get('1.0', END))
        my_result = Language.make(language=code).display_name()
        my_label.config(text=f'Your text is {my_result}')

my_text = Text(root, bg='#1d1b1f', fg='#fff', insertbackground='#fff', width=50, height=10)
my_text.pack(padx=10, pady=20)

Button(root, text='Detect', bg='#000', fg='#00ff00', command=check).pack(padx=10, pady=20)

my_label = Label(root, bg='#121212', fg='#fff')
my_label.pack(padx=10, pady=20)

root.mainloop()