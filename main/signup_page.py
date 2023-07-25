import email
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def on_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
        return


def pass_enter(event):
     if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
        return

def email_enter(event):
    if emailEntry.get()=='Email':
        emailEntry.delete(0,END)
        return

def confirmpassword_enter(event):
    if confirmpasswordEntry.get()=='Confirm Password':
        confirmpasswordEntry.delete(0,END)
        return

def hide():
    openeye.config(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\closedeye.gif")
    passwordEntry.config(show='*')
    confirmpasswordEntry.config(show='*')
    eyebutton.config(command=show)
    return

def show():
    openeye.config(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\openeye.gif")
    passwordEntry.config(show='')
    confirmpasswordEntry.config(show='')
    eyebutton.config(command=hide)

def login_page():
    signupPage.destroy()
    import loginpage

def clear():
    usernameEntry.delete(0,END)
    emailEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmpasswordEntry.delete(0,END)
    return


def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()==''or confirmpasswordEntry.get()=='':
        messagebox.showerror('Error','Fill all the required details')
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='shreyas0601')
            mycursor = con.cursor()
            query ='use vapourapp'
            mycursor.execute(query)
            query ='create table customer(ID int auto_increment primary key not null,username varchar(100),password varchar(20),email varchar(50))'
            mycursor.execute(query)
        except:
            query = 'use vapourapp'
            mycursor.execute(query)
        query='select * from customer where username=%s'
        mycursor.execute(query,(usernameEntry.get()))

        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Error','Username Already exists')
        else:
            query = 'insert into customer(username,password,email) values(%s,%s,%s)'
            mycursor.execute(query, (usernameEntry.get(), passwordEntry.get(), emailEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success!', 'You are now a V4Pour Verified Customer')
            clear()
            signupPage.destroy()
            import loginpage





signupPage=Tk()
signupPage.resizable(0,0)
signupPage.title('New Account')

bgImage=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\banner_main.jpg")
bgLabel=Label(signupPage,image=bgImage)
bgLabel.grid(row=0,column=0)

heading=Label(signupPage,text='Welcome to V4Pour',font=('Microsoft Yahei UI Light',23,'bold'),bg='black',fg='white')
heading.place(x=500,y=50)

frame=Frame(signupPage,bg='black')
frame.place(x=810,y=180)

signup_heading=Label(frame,text='Create your new V4Pour Account',font=('Microsoft Yahei UI Light',15,'bold'),bg='black',fg='white')
signup_heading.grid(row=0,column=0,sticky='s')

usernameEntry=Entry(frame,width=40,font=('Microsoft Yahei UI Light',12),bg='black',fg='white')
usernameEntry.grid(row=1,column=0,sticky='w',padx=25,pady=25)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',on_enter)


emailEntry=Entry(frame,width=40,font=('Microsoft Yahei UI Light',12),bg='black',fg='white')
emailEntry.grid(row=2,column=0,sticky='w',padx=25,pady=25)
emailEntry.insert(0,'Email')
emailEntry.bind('<FocusIn>',email_enter)



passwordEntry=Entry(frame,width=40,font=('Microsoft Yahei UI Light',12),bg='black',fg='white')
passwordEntry.grid(row=3,column=0,sticky='w',padx=25,pady=25)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',pass_enter)

openeye=PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\openeye.gif")

eyebutton=Button(frame,image=openeye,bd=0,bg='black',activebackground='white',cursor='hand2',command=hide,fg='black')
eyebutton.grid(row=3,column=2)

confirmpasswordEntry=Entry(frame,width=40,font=('Microsoft Yahei UI Light',12),bg='black',fg='white')
confirmpasswordEntry.grid(row=4,column=0,sticky='w',padx=25,pady=25)
confirmpasswordEntry.insert(0,'Confirm Password')
confirmpasswordEntry.bind('<FocusIn>',confirmpassword_enter)

#checkButton=Checkbutton(frame,bd=0,bg='black',fg='white',width=10,text='I agree to all Terms and Conditions',font=('Microsoft Yahei UI Light',12))
#checkButton.grid(row=5,column=0,pady=25)

createButton=Button(frame,bd=0,text='Create',bg='green',fg='white',width=10,font=('Arial',16),cursor='hand2',command=connect_database)
createButton.grid(row=5,column=0,pady=25,sticky='s')

alreadylabel=Label(frame,text='Already have a V4Pour Account?',font=('Microsoft Yahei UI Light',12,'italic'),bg='black',fg='white')
alreadylabel.grid(row=6,column=0,pady=10,sticky='s')

loginbutton=Button(frame,text='Login',bg='green',fg='white',width=10,font=('Arial',16),command=login_page,cursor='hand2')
loginbutton.grid(row=7,column=0,pady=10,sticky='s')










signupPage.mainloop()

















# window=Toplevel()
    # window.title('Bill')
    # bgImage = ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\billbg.jpg")
    # bgLabel = Label(window, image=bgImage)
    # bgLabel.grid(row=0, column=0)
    #
    # heading = Label(window, text='Your Bill',font=('Microsoft Yahei UI Light', 18, 'bold'), bg='black',
    #                 fg='white')
    # heading.place(x=200,y=10)

    # billheading = Label(window,text=data,font=('Microsoft Yahei UI Light', 18, 'bold'), bg='black',
    #                 fg='white')
    # billheading.place(x=200, y=60)
    # csgoprice=IntVar()
    # total=IntVar()
    # if csgocheck.get()=='CSGO-2':
    #     total= '3.99'
    # else:
    #     total= '0'
    # if csgocheck.get()=='CSG0-2'and valocheck.get()=='Valorant':
    #     total=''
    # total=Label(window, text=total,font=('Microsoft Yahei UI Light', 18, 'bold'), bg='black',
    #                 fg='white')
    # total.place(x=200,y=80)
    #
    # window.mainloop()
