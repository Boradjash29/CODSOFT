from tkinter import *
from tkinter import messagebox

def newtask():
    task = my_entry.get()
    if task !="":
        ln.insert(END, task)
        my_entry.delete(0,"end")
        feedback_label.config(text="Task added successfully!", fg="green")
        
    else:
        messagebox.showwarning("warning","Please enter some task.")
        
def deletetask(event=None):
    if ln.curselection():
        selection = ln.curselection()[0]
        task = ln.get(selection)
        if messagebox.askyesno("Confurmation",f"Are you sue you want to delete '{task}' ?"):
            ln.delete(selection)
            feedback_label.config(text="Task deleted successfully!",fg="green")
        else :
            feedback_label.config(text="Please select a task to delete.",fg="red") 
               
def clear_input(event=None):
    my_entry.delete(0,END)

def add_task_shortcut(event):
    if event.state ==4 and event.keysym == "Return":
        newtask()


def delete_task_shortcut(event):
    if event.keysym == "Delete":
        deletetask()               
    
    
ws = Tk()
ws.geometry('500x500+400+200')
ws.title('TO-DO-LIST')
ws.config(bg='#333333')
ws.resizable(width=False ,height=False)

frame =Frame(ws)
frame.pack(pady=10)

ln = Listbox(
    frame,
    width=25,
    height=8,
    font=('Helvitica',18,'italic'),
    bd=0,
    fg='#080808',
    highlightthickness=0,
    selectbackground='#8fbc8f',
    activestyle="none",
)

ln.pack(side=LEFT,fill = BOTH)

task_list =[]

for item in task_list:
    ln.insert(END,item)
    
sb =Scrollbar(frame)
sb.pack(side=RIGHT,fill =BOTH)

ln.config(yscrollcommand =sb.set)
sb.config(command =ln.yview)

my_entry =Entry(
    ws,
    font=('Helvetivca',24,'italic')
)    

my_entry.pack(pady=20)
my_entry.focus()

button_frame =Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('Helvetica',16,'bold italic'),
    bg='#3D59AB',
    padx =20,
    pady=10,
    command=newtask
)

addTask_btn.pack(fill=BOTH,expand=True,side=LEFT)
addTask_btn.bind("<Enter>", lambda event : addTask_btn.config(bg='#2E4482',fg='white'))
addTask_btn.bind("<Leave>", lambda event : addTask_btn.config(bg='#3D59AB',fg='black'))

delTask_btn =Button(
    button_frame,
    text='Delete Task',
    font=('Helvetica' , 16,'bold italic'),
    bg ='#59868B',
    padx=20,
    pady=10,
    command=deletetask
)
delTask_btn.pack(fill=BOTH,expand=True,side=LEFT)
delTask_btn.bind("<Enter>", lambda event: delTask_btn.config(bg='#4f726c',fg='white'))
delTask_btn.bind("<Leave>" , lambda event : delTask_btn.config(bg='#59868b',fg ='black'))

feedback_label =Label(ws,text="",font=('Helvetica',12),bg='#333333',fg='green')
feedback_label.pack()

my_entry.bind("<FocusIn>",clear_input)

ws.bind("<Control-Return>",add_task_shortcut)
ws.bind("<Delete>",delete_task_shortcut)

ws.mainloop()
          
    