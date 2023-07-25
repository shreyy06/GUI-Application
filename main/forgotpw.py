from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def on_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
        return


def pass_enter(event):
    if newpasswordEntry.get() == 'New Password':
        newpasswordEntry.delete(0, END)
        return

def confirmpassword_enter(event):
    if confirmpasswordEntry.get()=='Confirm Password':
        confirmpasswordEntry.delete(0,END)
        return

def change_password():
    if usernameEntry.get()=='' or newpasswordEntry.get()=='' or confirmpasswordEntry.get()=='':
        messagebox.showerror('Error','Fill all the required details')
    if newpasswordEntry.get()!=confirmpasswordEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    else:
        con = pymysql.connect(host='localhost', user='root', password='shreyas0601',database='vapourapp')
        mycursor = con.cursor()
        query = 'select * from customer where username=%s'
        mycursor.execute(query, (usernameEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Incorrect Username')
        else:
            query='update customer set password=%s where username=%s'
            mycursor.execute(query,(newpasswordEntry.get(),usernameEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success!','Password reset successfull')
            forgotpage.destroy()
            import loginpage




forgotpage=Tk()

forgotpage.resizable(0,0)

forgotpage.title('Password Reset')

bgImage=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\forgotbg.jpg")
bgLabel=Label(forgotpage,image=bgImage)
bgLabel.grid(row=0,column=0)

frame=Frame(forgotpage,bg='black')
frame.place(x=130,y=10)

heading=Label(frame,text='Forgot Password?',font=('Microsoft Yahei UI Light',14,'bold'),bg='black',fg='white')
heading.grid(row=0,column=0,sticky='s')

usernameEntry=Entry(frame,width=20,font=('Microsoft Yahei UI Light',14),bg='black',fg='white')
usernameEntry.grid(row=1,column=0,sticky='s',padx=10,pady=10)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',on_enter)

newpasswordEntry=Entry(frame,width=20,font=('Microsoft Yahei UI Light',14),bg='black',fg='white')
newpasswordEntry.grid(row=2,column=0,sticky='s',padx=10,pady=10)
newpasswordEntry.insert(0,'New Password')
newpasswordEntry.bind('<FocusIn>',pass_enter)

confirmpasswordEntry=Entry(frame,width=20,font=('Microsoft Yahei UI Light',14),bg='black',fg='white')
confirmpasswordEntry.grid(row=3,column=0,sticky='s',padx=10,pady=10)
confirmpasswordEntry.insert(0,'Confirm Password')
confirmpasswordEntry.bind('<FocusIn>',confirmpassword_enter)

confirmButton=Button(frame,text='Confirm',bg='green',fg='white',width=10,font=('Arial',14),cursor='hand2',command=change_password)
confirmButton.grid(row=4,column=0,padx=10,pady=10,sticky='s')





forgotpage.mainloop()