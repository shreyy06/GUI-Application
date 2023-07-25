import os
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import os
import random

def on_enter(event):
    if usernameEntry.get()=='Enter your name':
        usernameEntry.delete(0,END)
        return

def goback():
    prodselect.destroy()
    import loginpage

def backtologin():
    messagebox.showinfo('Thank you for choosing V4Pour!','You can find your bill in bills.txt!')
    prodselect.destroy()
    import loginpage

def billwindow():
        billno = IntVar()
        billno = random.randint(0000, 9999)
        billnostr=str(billno)
        con = pymysql.connect(host='localhost', user='root', password='shreyas0601',database='vapourapp')
        mycursor = con.cursor()
        query='insert into games (CSGO2,Valorant,Minecraft,Apex_Legends,Fifa,GTAV,Genshin_Impact,Elden_Ring,id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        mycursor.execute(query,(csgocheck.get(),valocheck.get(),minecheck.get(),apexcheck.get(),fifacheck.get(),gtacheck.get(),genshincheck.get(),eldencheck.get(),billno))
        con.commit()
        print(csgocheck.get(),valocheck.get(),minecheck.get(),apexcheck.get(),fifacheck.get(),gtacheck.get(),genshincheck.get(),eldencheck.get())
        messagebox.showinfo('Success!','Bill Generated')
        total=IntVar()
        discount=IntVar()
        discount=1
        total=(csgocheck.get()+valocheck.get()+minecheck.get()+apexcheck.get()+fifacheck.get()+gtacheck.get()+genshincheck.get()+eldencheck.get())-discount
        print(total)
        totalstr=str(total)
        csgostr=str(csgocheck.get())
        valostr = str(valocheck.get())
        minestr = str(minecheck.get())
        apexstr = str(apexcheck.get())
        fifastr = str(fifacheck.get())
        gtastr = str(gtacheck.get())
        genshinstr = str(genshincheck.get())
        eldenstr = str(eldencheck.get())
        os.remove(r"C:\Users\Admin\OneDrive\Desktop\bills.txt")
        f=open(r"C:\Users\Admin\OneDrive\Desktop\bills.txt",'w')
        data=('--------V4Pour- All things Gaming--------\nBill No -'+billnostr+'\nCSGO2 -$'+csgostr+'\nValorant -$'+valostr+'\nMinecraft -$'+minestr+'\nApex Legends -$'+apexstr+'\nFIFA 23 -$'+fifastr+'\nGTA-V -$'+gtastr+'\nGenshin Impact -$'+genshinstr+'\nElden Ring -$'+eldenstr+'\nYour total after discount -$'+totalstr+'\n------Thank you for choosing V4Pour------')
        f.write(data)
        f.close()



        window=Toplevel()
        window.title('Bill')
        window.resizable(0,0)
        bgImage = ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\billbg.jpg")
        bgLabel = Label(window, image=bgImage)
        bgLabel.grid(row=0, column=0)
        frame=Frame(window,bg='black')
        frame.place(x=160,y=5)

        heading = Label(frame, text='Your Bill',font=('Microsoft Yahei UI Light',15, 'bold'), bg='green',
                        fg='white')
        heading.grid(row=0,column=0,sticky='s',pady=10)

        csgoheading = Label(frame, text='CSGO2 -$'+csgostr, font=('Microsoft Yahei UI Light', 12, 'bold'),bg='black',
                        fg='white')
        csgoheading.grid(row=1,column=0,sticky='s',pady=10)

        valoheading = Label(frame, text='Valorant -$'+valostr, font=('Microsoft Yahei UI Light', 12, 'bold'), bg='black',
                            fg='white')
        valoheading.grid(row=2,column=0,sticky='s',pady=10)

        mineheading = Label(frame, text='Minecraft -$'+minestr, font=('Microsoft Yahei UI Light', 12, 'bold'), bg='black',
                            fg='white')
        mineheading.grid(row=3,column=0,sticky='s',pady=10)

        apexheading = Label(frame, text='Apex Legends -$'+apexstr, font=('Microsoft Yahei UI Light', 12, 'bold'), bg='black',
                            fg='white')
        apexheading.grid(row=4,column=0,sticky='s',pady=10)

        fifaheading = Label(frame, text='FIFA 23 -$'+fifastr, font=('Microsoft Yahei UI Light', 12, 'bold'), bg='black',
                            fg='white')
        fifaheading.grid(row=5,column=0,sticky='s',pady=10)

        gtaheading = Label(frame, text='GTA-V -$'+gtastr, font=('Microsoft Yahei UI Light', 12, 'bold'), bg='black',
                            fg='white')
        gtaheading.grid(row=6,column=0,sticky='s',pady=10)

        genshinheading = Label(frame, text='Genshin Impact -$'+genshinstr, font=('Microsoft Yahei UI Light', 12, 'bold'), bg='black',
                            fg='white')
        genshinheading.grid(row=7,column=0,sticky='s',pady=10)

        eldenheading = Label(frame, text='Elden Ring -$'+eldenstr, font=('Microsoft Yahei UI Light',12, 'bold'), bg='black',
                            fg='white')
        eldenheading.grid(row=8,column=0,sticky='s',pady=10)

        totalheading = Label(frame,text='Your total after discount -$'+totalstr,font=('Microsoft Yahei UI Light',15, 'bold'), bg='green',
                        fg='white')
        totalheading.grid(row=9,column=0,sticky='s',pady=10)


        proceedButton = Button(frame, text='Proceed', font=('Microsoft Yahei UI Light', 12, 'bold'),
                               bg='green',
                               fg='white', cursor='hand2', command=backtologin)
        proceedButton.grid(row=10, column=0, sticky='s', pady=10)










        window.mainloop()

        return





prodselect=Tk()

prodselect.resizable(0,0)

prodselect.title('Product Selection Window')

bgImage=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\bg.jpg")
bgLabel=Label(prodselect,image=bgImage)
bgLabel.grid(row=0,column=0)

frame=Frame(prodselect,bg='black')
frame.place(x=0,y=100)

heading=Label(prodselect,text='Select your desired V4Pour Games',font=('Microsoft Yahei UI Light',23,'bold'),bg='black',fg='white')
heading.place(x=400,y=50)

csgo2=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\csgo2.jpg")

csgoButton=Button(frame,image=csgo2,bd=0,bg='black',activebackground='white',fg='black')
csgoButton.grid(row=0,column=0,pady=25,padx=5,sticky='w')

csgocheck=IntVar()

csgoCheckbutton=Checkbutton(frame,text='CS-GO2($3.99)',bd=0,bg='black',fg='blue',font=('Microsoft Yahei UI Light',14)
                            ,variable=csgocheck,cursor='hand2',offvalue='',onvalue='4')
csgoCheckbutton.grid(row=1,column=0,pady=10,padx=15,sticky='s')

valo=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\valo.jpg")

valoButton=Button(frame,image=valo,bd=0,bg='black',activebackground='white',fg='black')
valoButton.grid(row=0,column=1,pady=25,padx=10,sticky='w')

valocheck=IntVar()

valoCheckbutton=Checkbutton(frame,text='Valorant($6.99)',bd=0,bg='black',fg='blue',font=('Microsoft Yahei UI Light',14)
                            ,variable=valocheck,cursor='hand2',offvalue='',onvalue='7')
valoCheckbutton.grid(row=1,column=1,pady=10,padx=10,sticky='s')

mine=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\minecraft.jpg")

mineButton=Button(frame,image=mine,bd=0,bg='black',activebackground='white',fg='black')
mineButton.grid(row=0,column=2,pady=25,padx=10,sticky='w')

minecheck=IntVar()

mineCheckbutton=Checkbutton(frame,text='Minecraft($5.99)',bd=0,bg='black',fg='blue',font=('Microsoft Yahei UI Light',14)
                            ,variable=minecheck,cursor='hand2',offvalue='',onvalue='6')
mineCheckbutton.grid(row=1,column=2,pady=10,padx=15,sticky='s')

apex=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\apex.jpg")

apexButton=Button(frame,image=apex,bd=0,bg='black',activebackground='white',fg='black')
apexButton.grid(row=0,column=3,pady=25,padx=10,sticky='w')

apexcheck=IntVar()

apexCheckbutton=Checkbutton(frame,text='Apex Legends($2.99)',bd=0,bg='black',fg='blue',font=('Microsoft Yahei UI Light',14)
                            ,variable=apexcheck,cursor='hand2',offvalue='',onvalue='3')
apexCheckbutton.grid(row=1,column=3,pady=10,padx=10,sticky='s')

fifa=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\fifa23.jpg")

fifaButton=Button(frame,image=fifa,bd=0,bg='black',activebackground='white',fg='black')
fifaButton.grid(row=2,column=0,pady=25,padx=5,sticky='w')

fifacheck=IntVar()

fifaCheckbutton=Checkbutton(frame,text='Fifa 23($9.99)',bd=0,bg='black',fg='blue',font=('Microsoft Yahei UI Light',14)
                            ,variable=fifacheck,cursor='hand2',offvalue='',onvalue='10')
fifaCheckbutton.grid(row=3,column=0,pady=10,padx=15,sticky='s')

gta=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\gtaV.jpg")

gtaButton=Button(frame,image=gta,bd=0,bg='black',activebackground='white',fg='black')
gtaButton.grid(row=2,column=1,pady=25,padx=10,sticky='w')

gtacheck=IntVar()

gtaCheckbutton=Checkbutton(frame,text='GTA-V($10.99)',bd=0,bg='black',fg='blue',font=('Microsoft Yahei UI Light',14)
                            ,variable=gtacheck,cursor='hand2',offvalue='0',onvalue='11')
gtaCheckbutton.grid(row=3,column=1,pady=10,padx=10,sticky='s')

genshin=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\genshin.jpg")

genshinButton=Button(frame,image=genshin,bd=0,bg='black',activebackground='white',fg='black')
genshinButton.grid(row=2,column=2,pady=25,padx=10,sticky='w')

genshincheck=IntVar()

genshinCheckbutton=Checkbutton(frame,text='Genshin Impact($4.99)',bd=0,bg='black',fg='blue',font=('Microsoft Yahei UI Light',14)
                            ,variable=genshincheck,cursor='hand2',offvalue='0',onvalue='5')
genshinCheckbutton.grid(row=3,column=2,pady=10,padx=15,sticky='s')

elden=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\Vapour App\elden.jpg")

eldenButton=Button(frame,image=elden,bd=0,bg='black',activebackground='white',fg='black')
eldenButton.grid(row=2,column=3,pady=25,padx=10,sticky='w')

eldencheck=IntVar()

eldenCheckbutton=Checkbutton(frame,text='Elden Ring($4.99)',bd=0,bg='black',fg='blue',font=('Microsoft Yahei UI Light',14)
                            ,variable=eldencheck,cursor='hand2',offvalue='0',onvalue='5')
eldenCheckbutton.grid(row=3,column=3,pady=10,padx=10,sticky='s')

gobackButton=Button(frame,text='Go back',bg='green',fg='white',width=10,font=('Arial',16),command=goback)
gobackButton.grid(row=4,column=1,pady=20,sticky='s')

checkoutButton=Button(frame,text='Checkout',bg='green',fg='white',width=10,font=('Arial',16),command=billwindow)
checkoutButton.grid(row=4,column=2,pady=20,sticky='s')


















prodselect.mainloop()