from tkinter import *
import openai

root = Tk()
root.geometry('1000x1500')
root.title('AskMe')

def search():
    openai.api_key='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'
    prompt = question.get()
    if prompt.lower()=='exit' or prompt.lower()=='quit':
        exit()
    else:
        response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        max_tokens = 2000
        )
        myText.insert(END, response['choices'][0]['text'])

Label(root, text='AskMe', font=('Helvetica', 13)).pack(padx=10, pady=20)

myText = Text(root, bg='#fff', fg='#000', insertbackground ='#fff', height=20)
myText.pack(padx=10, pady=20)

frameInput = Frame(root, borderwidth=6)
frameInput.pack(padx=10, pady=20, side=BOTTOM)

question = StringVar()
Entry(frameInput, textvariable = question, font=('Helvetica', 10)).grid(row=0, column=0, padx=(0, 10))

Button(frameInput, text='Submit', bg='#000', fg='#fff', command=search).grid(row=0, column=1, padx=(10, 0))

root.mainloop()