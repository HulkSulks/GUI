import tkinter
import random
from tkinter import messagebox


root = tkinter.Tk()

root.geometry("200x500")

Tasks = []


Title = tkinter.Label(root, text="To Do List")
Title.pack()

label_DIS = tkinter.Label(root, text="")
label_DIS.pack()


def List_update():
    Clear_LB()
    for Task in Tasks:
        ListBox.insert("end", Task)

def Clear_LB():
    ListBox.delete(0, "end")

def add_task():
     Task = Text.get()
     if Task != "":
        Tasks.append(Task)
        List_update()
     else:
        label_DIS["text"]="Please enter a task."
        Text.delete(0,'end')

def Delete_All():
    global Tasks
    ASKYESORNO = messagebox.askyesno("Warning!", "Do you want to Delete all tasks?")
    Tasks = []
    List_update()


def Delete():
    Task = ListBox.get("active")

    if Task in Tasks:
        Tasks.remove(Task)
    List_update()

def Random_Task():
    Task = random.choice(Tasks)
    label_DIS["text"]= Task

def TT_NO_Tasks():
    No_TASKS = len(Tasks)
    message = "Number of tasks are: %s"%No_TASKS
    label_DIS["text"] = message




Text = tkinter.Entry(root, width=15)
Text.pack()

Add_Task_Button = tkinter.Button(root, text="Add Task", command=add_task)
Add_Task_Button.pack()

Delete_all_Button = tkinter.Button(root, text="Delete All", command=Delete_All)
Delete_all_Button.pack()

Delete_Button = tkinter.Button(root, text="Delete", command=Delete)
Delete_Button.pack()

Random_Button = tkinter.Button(root, text="Choose Random Task", command=Random_Task)
Random_Button.pack()

No1_Task_Button = tkinter.Button(root, text="Total no of tasks", command=TT_NO_Tasks)
No1_Task_Button.pack()



ListBox = tkinter.Listbox(root)
ListBox.pack()

root.mainloop()
