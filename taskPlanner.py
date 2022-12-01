from tkinter import *

root = Tk()
root.title('Task Planner')
root.geometry('1000x1500')
root.config(bg='#000')

def addTask():
    newWindow = Tk()
    newWindow.geometry('1000x600')
    newWindow.config(bg='#000')
    
    def addIt():
        task_to_add = taskToAdd.get('1.0', 'end-1c')
        taskList.insert(END, '•'+task_to_add)
        newWindow.destroy()
    
    taskToAdd = Text(newWindow, bg='#000', fg='#fff', insertbackground='#fff', width=100, height=5)
    taskToAdd.pack(padx=10, pady=20)
    
    Button(newWindow,text='Add It' , bg='#000', fg='#fff', command = addIt).pack(padx=10, pady=20)
    
    newWindow.mainloop()

taskList = Listbox(root, background='#000', foreground='#fff', height=20, width=100)
taskList.pack(padx=10, pady=20)

Button(root, text='Add Task', bg='#000', fg='#fff', command=addTask).pack(padx=10, pady=20)

root.mainloop()