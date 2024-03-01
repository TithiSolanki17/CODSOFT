from tkinter import *
from tkinter import messagebox

def addtask():
    task = entry.get()
    if task != "":
        lb.insert(END, task)
        entry.delete(0, "end")
    else:
        messagebox.showwarning("WARNING", "Please Enter a task!")

def deletetask():
    lb.delete(ANCHOR)
    messagebox.showinfo("ACTION", "Task Deleted!")

def update():
    task = entry.get()
    if task != "":
        string = ANCHOR
        lb.delete(string)
        lb.insert(END, task)
        entry.delete(0, "end")
    else:
        messagebox.showwarning("WARNING", "Please Select a Task!")


ws = Tk()
ws.geometry('500x450+500+200')
ws.title("TO-DO LIST")
ws.config(bg='orange')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none"

)
lb.pack(side=LEFT, fill=BOTH)

task = []

for item in task:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

entry = Entry(
    ws, 
    font=('Times', 24)
)

entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

at_btn =  Button(
    button_frame,
    text = 'ADD TASK',
    font = ('Times', 14),
    bg = 'green',
    padx=20,
    pady=10,
    command=addtask
)
at_btn.pack(fill=BOTH, expand=True, side=LEFT)

dt_btn = Button(
    button_frame,
    text='DELETE TASK',
    font=('Times',14),
    bg='red',
    padx=20,
    pady=10,
    command=deletetask
)
dt_btn.pack(fill=BOTH, expand=True, side=LEFT)

up_btn =  Button(
    button_frame,
    text = 'UPDATE TASK',
    font = ('Times', 14),
    bg = 'blue',
    padx=20,
    pady=10,
    command=update
)
up_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()