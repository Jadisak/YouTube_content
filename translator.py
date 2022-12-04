from tkinter import *
from tkinter import ttk
import googletrans
import textblob
from langdetect import detect
from langcodes import *

root = Tk()
root.geometry('1000x700')
root.title('Translator')

def translate():
    translatedText.delete('1.0', END)
    try:
        for key, value in languages.items():
            if value == originalCombo.get():
                from_language_key = key
                
        for key, value in languages.items():
            if value == translatedCombo.get():
                to_language_key = key
        words = textblob.TextBlob(originalText.get('1.0', END))
        words = words.translate(from_lang = from_language_key, to = to_language_key)
        translatedText.insert('1.0', words)
    except Exception as e:
        print(e)

languages = googletrans.LANGUAGES
language_list = list(languages.values())

originalText = Text(root, width=20, height=15, font=('Helvetica', 5))
originalText.grid(row=0, column=0, padx=30, pady=20)

translatedText = Text(root, width=20, height=15, font=('Helvetica', 5))
translatedText.grid(row=0, column=2, padx=30, pady=20)

btn = Button(root, text='Translate', background='#000',foreground = '#fff', font=('Helvetica', 5), command=translate)
btn.grid(row=0, column=1, padx=10, pady=10)

originalCombo = ttk.Combobox(root, width=12, value=language_list)
originalCombo.grid(row=1, column=0)

translatedCombo = ttk.Combobox(root, width=12, value=language_list)
translatedCombo.grid(row=1, column=2)


root.mainloop()