#import modules
from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk
from tkinter import messagebox
import pymysql

#functions
def on_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
        return


def pass_enter(event):
     if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
        return

def hide():
    openeye.config(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\closedeye.gif")
    passwordEntry.config(show='*')
    eyebutton.config(command=show)
    return

def show():
    openeye.config(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\openeye.gif")
    passwordEntry.config(show='')
    eyebutton.config(command=hide)

def signup():
    loginpage.destroy()
    import signup_page

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fill all the required details')
    else:
        con = pymysql.connect(host='localhost', user='root', password='shreyas0601')
        mycursor = con.cursor()
        query = 'use vapourapp'
        mycursor.execute(query)
        query = 'select * from customer where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(),passwordEntry.get()))

        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid Username or Password')
            usernameEntry.delete(0,END)
            passwordEntry.delete(0,END)
            usernameEntry.insert(0, 'Username')
            passwordEntry.insert(0, 'Password')
        else:
            loginpage.destroy()
            import prodselect

def forgotpass():
    loginpage.destroy()
    import forgotpw

#gui code
loginpage=Tk()

loginpage.resizable(0,0)

loginpage.title('V4Pour Customer Login Page')

bgImage=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\banner_main.jpg")
bgLabel=Label(loginpage,image=bgImage)
bgLabel.grid(row=0,column=0)

heading=Label(loginpage,text='Welcome to V4Pour',font=('Microsoft Yahei UI Light',23,'bold'),bg='black',fg='white')
heading.place(x=500,y=50)

login_heading=Label(loginpage,text='User Login',font=('Microsoft Yahei UI Light',23,'bold'),bg='black',fg='white')
login_heading.place(x=965,y=180)

#entry fields
usernameEntry=Entry(loginpage,width=40,bd=0,font=('Microsoft Yahei UI Light',12),bg='black',fg='white')
usernameEntry.place(x=860,y=270)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',on_enter)

#creating a frame(acting as the blue underline
frame1=Frame(loginpage,width=362,height=2,bg='blue').place(x=860,y=292)

passwordEntry=Entry(loginpage,width=40,bd=0,font=('Microsoft Yahei UI Light',12),bg='black',fg='white')
passwordEntry.place(x=860,y=320)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',pass_enter)

#creating a frame(acting as the blue underline
frame2=Frame(loginpage,width=362,height=2,bg='blue').place(x=860,y=342)


openeye=PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\openeye.gif")

eyebutton=Button(loginpage,image=openeye,bd=0,bg='black',activebackground='white',cursor='hand2',command=hide,fg='white')
eyebutton.place(x=1200,y=320)

forgetbutton=Button(loginpage,text='Forgot Password?',bd=0,bg='black',activebackground='black',cursor='hand2',font=('Microsoft Yahei UI Light',8)
                    ,fg='blue',command=forgotpass)
forgetbutton.place(x=1125,y=350)

loginbutton=Button(loginpage,text='Login',bg='green',fg='white',width=10,font=('Arial',16),command=login_user,cursor='hand2')
loginbutton.place(x=978,y=390)

orlabel=Label(loginpage,text='------OR------',font=('Microsoft Yahei UI Light',11,'bold'),bg='black',fg='white')
orlabel.place(x=985,y=450)

newaccountbutton=Button(loginpage,text='Create your new V4Pour Account',bg='green',activebackground='black',
                        cursor='hand2',font=('Microsoft Yahei UI Light',16),fg='white',command=signup)
newaccountbutton.place(x=880,y=490)




loginpage.mainloop()
