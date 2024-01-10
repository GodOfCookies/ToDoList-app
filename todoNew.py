import tkinter
from tkinter import *

root = Tk()
root.title("Just Do It, Bro!")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("todo.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
            task_list.append(task)
            listbox.insert(END, task)

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("todo.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete(ANCHOR)
def openTaskFile():
    try:
        global task_list
        with open("todo.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != "\n":  # если строка не пустая
                task_list.append(task)
                listbox.insert(END, task)

    except:
        file = open("todo.txt", "w")
        file.close()


# icon
Image_icon = PhotoImage(file="Image/task.png")
root.iconphoto(False, Image_icon)

# top bar
TopImage = PhotoImage(file="Image/topbar.png")
Label(root, image=TopImage).pack()

dockImage = PhotoImage(file="Image/dock.png")
Label(root, image=dockImage, bg='#32405b').place(x=30, y=25)  # bg='#32405b' - HEX code for blue color like an image

noteImage = PhotoImage(file="Image/task.png")
Label(root, image=noteImage, bg='#32405b').place(x=340, y=19)

heading = (Label(root, text="Your tasks, bro!", font="Arial 20 bold", fg="white", bg="#32405b"))
heading.place(x=89, y=20)

# main
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font="Arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text="Add, bro!", font="arial 20 bold", padx=6, pady=8, bg="#5a95ff", fg="#fff", bd=0,
                command=addTask)
button.place(x=257, y=0)

# listbox
frame1 = Frame(root, bd=3, width=700, height=300, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=("arial", 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2",
                  selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

# delete
Delete_icon = PhotoImage(file="Image/Delete.png")
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

root.mainloop()
