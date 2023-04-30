import tkinter
from tkinter import *
from tkinter import messagebox


# Graphical User Interface
window = Tk()
window.title('login')
window.geometry('925x500+300+200')
window.configure(bg="#fff")
window.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()
    
    if username=='georgius.mario.m@gmail.com' and password=='1234':
        screen=Toplevel(window)
        screen.title('APP')
        screen.geometry('925x500+300+200')
        screen.config(bg="white")
        
        Label(screen,text="Login Suscessfully",bg='#fff',font=('Calibri(body)',50,'bold')).pack(expand=True)
        screen.mainloop()
    
    elif username!='admin' and password!='1234':
        messagebox.showerror('Invalid','Username and password not recognized')

# Frame
frame=Frame(window,width=350,height=350,bg="White")
frame.place(x=480,y=70)

# Heading
heading=Label(frame, text='Sign In',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

# User
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')


user = Entry(frame, width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame, width=295,height=2,bg='black').place(x=25,y=107)#line

# Password
def on_enter(e):
    code.delete(0, 'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code = Entry(frame, width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
Frame(frame, width=295,height=2,bg='black').place(x=25,y=177)#line


# Button
Button(frame, width=39,pady=7,text='sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)

# sign up ?
label=Label(frame,text="Don't have account ?", fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

# sign up button
sign_up = Button(frame,width=6,text='Sign up', border=0,bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=215,y=270)

# Image 
img = PhotoImage(file='formlogin.png')  
Label(window,image=img,bg='white').place(x=50,y=107)

#End
window.mainloop()