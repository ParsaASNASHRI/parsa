from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('400x400')
root.title('form')

#function=================
def Exit_():
    result=messagebox.askyesno('Exit',' Are you sure:')
    if result==True:
        root.destroy()

def run():
    score=int(ent_score.get())
    if 15<score<=20:
        messagebox.showinfo('score','your score is:very good')
    elif 10<score<=15:
         messagebox.showinfo('score','your score is:good')
    elif 5<score<=10:
        messagebox.showinfo('score','your score is:bad')
    elif 0<=score<=5:
        messagebox.showinfo('score','your score is:very bad')
    else:
         messagebox.showinfo('score','your score is:not valid')
       

lbl_name=Label(root,text='name:',font='tahoma 15')
lbl_name.place(x=80,y=80)

lbl_score=Label(root,text='score:',font='tahoma 15')
lbl_score.place(x=80,y=120)

ent_welcome=Entry(root,font='tahoma 15')
ent_welcome.place(x=140,y=85)

ent_score=Entry(root,font='tahoma 15')
ent_score.place(x=140,y=125)

btn_Exit=Button(root,text='Exit',font='tahoma 15',command=Exit_)
btn_Exit.place(x=100,y=250)

btn_run=Button(root,text='run',font='tahoma 15',command=run)
btn_run.place(x=200,y=250)

root.mainloop()