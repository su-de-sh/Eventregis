


import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import csv
import time
import os


HEIGHT=700
WIDTH=800
time=int(time.strftime("%Y%m%d"))


count: int=0
i: int=0
global NameofE
window=tk.Tk()
window.title("Event registration")
closing= tk.StringVar()
canvas1=tk.Canvas(window,height=HEIGHT,width=WIDTH)
canvas1.pack()

frame1=tk.Frame(window,bg="#80c1ff")
frame1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)



def correct(inp):
    if inp.isdigit():
        enterednumber = inp
        ch = enterednumber[0]

        length = len(enterednumber)

        if (ch == "0"):
            return False
        else:
            if (length<=5):
                return True
            else:
                return False
    elif inp is "":
        return True
    else:
        return False





def VerifyDT():
    try:

        SmallEvent = Event.get()
        #print(SmallEvent)
        i = 0
        nos = 0
        with open('Programsinfo.csv', 'r')as f:
            read = csv.reader(f)
            next(read)

            for row in read:
                print(row)
                i = i + 1
                name, s, c, n = row
                #print(name)
                #print(n)

                if name == SmallEvent:
                    c = c.replace('-', '')
                    C = int(c)
                    N = int(n)
                    print(C, N)


                    with open(SmallEvent + ".csv", "r")as f:
                        read = csv.reader(f)
                        next(read)
                        for line in read:
                            nos = nos + 1
                            print(nos)

                    if N - nos == 0 and C - time <= 1:
                        messagebox.showinfo("warning", "Registration1 closed")
                    elif N - nos == 0:
                        messagebox.showinfo("warning", "NO more seats available")
                    elif C - time <= 1:
                        messagebox.showinfo("warning", "Registration closed")
                    else:
                        Verify()
    except PermissionError:
        messagebox.showinfo("Warning", "Close the excel file")

def Verify():

    try:



        email=Email.get()
        SmallEvent = Event.get()




        with open(SmallEvent + ".csv", "r")as f:

            read = csv.reader(f)
            for line in read:
                if email in line[1]:

                    messagebox.showinfo("Warning", "This email address is already registered!!")
                    break

            else:
                userInfo()
    except PermissionError:
        messagebox.showinfo("Warning", "Close the excel file")

# def VerifyCancelation():
#     try:
#
#
#
#         email=Email.get()
#         SmallEvent = Event.get()
#
#
#
#
#         with open(SmallEvent + ".csv", "r")as f:
#
#             read = csv.reader(f)
#             for line in read:
#                 if email in line[1]:
#
#                     messagebox.showinfo("Warning", "This email address is already registered!!")
#                     break
#
#             else:
#                 messagebox.showinfo("Warning", "Email not Registered")
#     except PermissionError:
#         messagebox.showinfo("Warning", "Close the excel file")



def RegisterCostumer():
    global Name,Email,Refcode,Event,age

    Event= tk.StringVar()
    Name=tk.StringVar()
    Email=tk.StringVar()
    Refcode=tk.StringVar()
    age=tk.StringVar()





    # window2=tk.Toplevel(window)
    # window2.title("Costumer detail")
    # canvas2=tk.Canvas(window2,height=700,width=800)
    # canvas2.pack()

    frame2=tk.Frame(window,bg="#80c1ff").place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
    tk.Label(frame2, text="Event",bg="#80c1ff").place(relx=0.17,rely=0.1,relwidth=0.15,relheight=0.08)
    tk.Label(frame2, text="Name:",bg="#80c1ff").place(relx=0.17,rely=0.18,relwidth=0.15,relheight=0.08)
    tk.Label(frame2, text="Email:",bg="#80c1ff").place(relx=0.17,rely=0.25,relwidth=0.15,relheight=0.08)
    tk.Label(frame2, text="REF code:", bg="#80c1ff").place(relx=0.17, rely=0.32, relwidth=0.15, relheight=0.08)
    tk.Label(frame2, text="Age group...", bg="#80c1ff").place(relx=0.17, rely=0.42, relwidth=0.15, relheight=0.08)

    E4 = tk.Entry(frame2, textvariable=Event)
    E4.place(relx=0.33, rely=0.13, relwidth=0.45, relheight=0.05)

    E1=tk.Entry(frame2,textvariable=Name)
    E1.place(relx=0.33,rely=0.20,relwidth=0.45,relheight=0.05)

    E2=tk.Entry(frame2,textvariable=Email)
    E2.place(relx=0.33,rely=0.27,relwidth=0.45,relheight=0.05)
    E3=tk.Entry(frame2,textvariable=Refcode)
    E3.place(relx=0.33, rely=0.35, relwidth=0.45, relheight=0.05)

    tk.Label(frame2, text=" *must be of 5 digits and start from 10000", bg="#80c1ff",bd=0).place(relx=0.22, rely=0.40, relwidth=0.5,
                                                                               relheight=0.05)

    E5 = tk.Entry(frame2, textvariable=age)
    E5.place(relx=0.33, rely=0.45, relwidth=0.45, relheight=0.05)
    tk.Label(frame2, text=" *A for Adult and C for child", bg="#80c1ff").place(relx=0.17, rely=0.498, relwidth=0.5, relheight=0.08)



    ok_but=tk.Button(frame2,text="SUBMIT", bg='green',command=VerifyDT)
    ok_but.place(relx=0.45,rely=0.6,relwidth=0.2,relheight=0.08)
    # back_but = tk.Button(frame2, text="Back", bg='red', command=first_screen)
    # back_but.place(relx=0.1, rely=0.05, relwidth=0.15, relheight=0.05)



def userInfo():


    global count
    SmallEvent= Event.get()
    NameofC= Name.get()
    email=Email.get()
    rfcode=Refcode.get()
    a=age.get()



    if os.path.exists(SmallEvent+ ".csv"):

        try:


            with open(SmallEvent + '.csv','a',newline='')as f:
                write = csv.writer(f)
                write.writerow([NameofC, email, rfcode,a])
                messagebox.showinfo("Registered", "Registration complete!!")
        except PermissionError:
            messagebox.showinfo("Warning", "Close the excel file")

    else:
        messagebox.showinfo("Warning", "No such event exists")




def ExcelFile():

    NameofE=NOE.get()
    s = starting.get()
    c = closing.get()
    n=seat.get()


    try:

        if os.path.exists(NameofE + ".csv"):
            messagebox.showinfo("Warning", "Event already exist!!")
        else:
            file = open(NameofE + ".csv", "x")
            file.close()
            with open(NameofE + ".csv", 'a', newline='')as f:
                write = csv.writer(f)
                write.writerow(['Name', 'E-mail', 'Ref. code','Age group'])


            if os.path.exists("Programsinfo.csv"):
                with open('programsinfo.csv', 'a', newline='')as f:
                    write = csv.writer(f)
                    write.writerow([NameofE, s, c,n])
                    messagebox.showinfo("...", "Event added successfully")

            else:
                file = open("Programsinfo.csv", "x")
                file.close()
                with open('programsinfo.csv', 'a', newline='')as f:
                    write = csv.writer(f)
                    write.writerow(['Eventname', 'starting date', 'closing date','no of seat'])

                with open('programsinfo.csv', 'a', newline='')as f:
                    write = csv.writer(f)
                    write.writerow([NameofE, s, c, n])
                    messagebox.showinfo("...", "Event added successfully")
    except PermissionError:
        messagebox.showinfo("Warning", "Close the excel file!!")




def Addevent():
    global NOE, starting,closing,seat
    NOE = tk.StringVar()

    starting = tk.StringVar()
    closing= tk.StringVar()
    seat=tk.StringVar()


    frame2 = tk.Frame(window, bg="#80c1ff")
    frame2.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    tk.Label(frame2, text="Name of Event:", bg="#80c1ff").place(relx=0.25, rely=0.18, relwidth=0.15, relheight=0.08)
    tk.Label(frame2, text="Registration starting Date:", bg="#80c1ff").place(relx=0.17, rely=0.257, relwidth=0.22, relheight=0.08)
    tk.Label(frame2, text="Registration closing Date:", bg="#80c1ff").place(relx=0.17, rely=0.327, relwidth=0.22, relheight=0.08)
    tk.Label(frame2, text="NO of seat:", bg="#80c1ff").place(relx=0.17, rely=0.41, relwidth=0.2, relheight=0.08)


    E1 = tk.Entry(frame2, textvariable=NOE)
    E1.place(relx=0.4, rely=0.19, relwidth=0.32, relheight=0.05)

    E2 = tk.Entry(frame2, textvariable=starting)
    E2.place(relx=0.4, rely=0.27, relwidth=0.32, relheight=0.05)
    tk.Label(frame2, text="*eg. 2019-06-03", bg="#80c1ff").place(relx=0.72, rely=0.25, relwidth=0.2, relheight=0.08)

    E3 = tk.Entry(frame2, textvariable=closing)
    E3.place(relx=0.4, rely=0.35, relwidth=0.32, relheight=0.05)

    E4=tk.Entry(frame2, textvariable=seat)
    E4.place(relx=0.4, rely=0.43, relwidth=0.32, relheight=0.05)

    ok_but = tk.Button(frame2, text="Register", bg='green', command=ExcelFile)
    ok_but.place(relx=0.45, rely=0.6, relwidth=0.2, relheight=0.08)

    # back_but=tk.Button(frame2, text="Back", bg='red', command=first_screen)
    # back_but.place(relx=0.05, rely=0.05, relwidth=0.15, relheight=0.05)


def VerifyCancel():
    CancelingEvent = EventName.get()
    CancelingEmail = CancelEmail.get()
    with open('Programsinfo.csv', 'r')as f:
        read = csv.reader(f)
        next(read)

        for row in read:
            print(row)

            name, s, c, n = row
            # print(name)
            # print(n)

            if name == CancelingEvent:
                c = c.replace('/', '')
                C = int(c)
    if C-time<=1:
        messagebox.showinfo("Warning", "This reservation cannot be canceled now!!")

    else:
        with open(CancelingEvent+'.csv','r')as f:
            read=csv.reader(f)

            for row in read:
                if row[1] == CancelingEmail:
                    x=0
                    Cancel()
                    break
                else:
                    x=1

            if (x==1):
                messagebox.showinfo("Warning", "No seat is registered using this Email")











def Cancel():

    CancelingEvent=EventName.get()
    CancelingEmail=CancelEmail.get()

    with open(CancelingEvent+'.csv', 'r') as inp:
        reader = csv.reader(inp)

        for row in reader:
            # print(row[1])
            if row[1] == CancelingEmail:
                continue

            else:
                with open('temp1.csv', 'a', newline='') as out:
                    write = csv.writer(out)
                    write.writerow(row)

        with open(CancelingEvent+'.csv', 'w') as out:
            pass

        with open('temp1.csv', 'r') as inp:
            reader = csv.reader(inp)

            for row in reader:
                # print(row[1])

                with open(CancelingEvent+'.csv', 'a', newline='') as out:
                    write = csv.writer(out)
                    write.writerow(row)

        # with open(CancelingEvent+'.csv', 'r') as inp:
        #     reader = csv.reader(inp)
        #
        #     for row in reader:
        #         print(row[1])

    os.remove('temp1.csv')
    messagebox.showinfo("Message", "Your reservation is cancelled successfully !!")

def RegisterCancel():
    global CancelEmail,EventName
    CancelEmail=tk.StringVar()
    EventName=tk.StringVar()
    frame2 = tk.Frame(window, bg="#80c1ff")
    frame2.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    tk.Label(frame2, text="Event", bg="#80c1ff").place(relx=0.17, rely=0.18, relwidth=0.15, relheight=0.08)
    E1 = tk.Entry(frame2, textvariable=EventName)
    E1.place(relx=0.3, rely=0.19, relwidth=0.45, relheight=0.05)
    tk.Label(frame2, text="Email", bg="#80c1ff").place(relx=0.17, rely=0.23, relwidth=0.15, relheight=0.08)
    E2 = tk.Entry(frame2, textvariable=CancelEmail)
    E2.place(relx=0.3, rely=0.24, relwidth=0.45, relheight=0.05)

    ok_but = tk.Button(frame2, text="SUBMIT", bg='green', command=VerifyCancel)
    ok_but.place(relx=0.45, rely=0.6, relwidth=0.2, relheight=0.08)

def EventDetail():
    Ename=EventName.get()
    Nseat=0
    try:
        with open('Programsinfo.csv', 'r')as f:
            read = csv.reader(f)
            next(read)

            for row in read:
                print(row)
                Nseat = Nseat+ 1
                name, s, c, n = row
                # print(name)
                # print(n)

                if name == Ename:
                    N = int(n)
        AvailableSeat=N-Nseat

        frame2 = tk.Frame(window, bg="#80c1ff")
        frame2.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        tk.Label(frame2, text="Total seats: ", bg="#80c1ff",font=("arial",12)).place(relx=0.25, rely=0.18, relwidth=0.15, relheight=0.08)
        tk.Label(frame2, text=N, bg="red").place(relx=0.5, rely=0.18, relwidth=0.15, relheight=0.08)

        tk.Label(frame2, text="Booked seats: ", bg="#80c1ff",font=("arial",12)).place(relx=0.2, rely=0.32, relwidth=0.25,
                                                                                 relheight=0.03)
        tk.Label(frame2, text=Nseat, bg="Yellow",).place(relx=0.5, rely=0.29, relwidth=0.15, relheight=0.08)
        tk.Label(frame2, text="Available seats:", bg="#80c1ff",font=("arial",12)).place(relx=0.2, rely=0.4, relwidth=0.22,
                                                                                relheight=0.08)
        tk.Label(frame2, text=AvailableSeat, bg="green").place(relx=0.5, rely=0.40, relwidth=0.15, relheight=0.08)



    except PermissionError:
        messagebox.showinfo("Warning","Close the excel file first!!!")

def EventInfo():
    global EventName

    EventName = tk.StringVar()
    frame2 = tk.Frame(window, bg="#80c1ff")
    frame2.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    tk.Label(frame2, text="Event Name:", bg="#80c1ff",font=16).place(relx=0.18, rely=0.2, relwidth=0.17, relheight=0.08)
    E1 = tk.Entry(frame2, textvariable=EventName)
    E1.place(relx=0.35, rely=0.19, relwidth=0.45, relheight=0.1)

    ok_but = tk.Button(frame2, text="SUBMIT", bg='green', command=EventDetail)
    ok_but.place(relx=0.45, rely=0.6, relwidth=0.2, relheight=0.08)


button1 = tk.Button(frame1 ,compound=tk.TOP, width=10, height=10,
        text="Add New Event", bg='Yellow',font=18,command=Addevent)
button1.place(relx=0.08,rely=0.1,relwidth=0.4,relheight=0.2)
button2 = tk.Button(frame1, compound=tk.TOP, width=10,font=18, height=10,
                                text="Register for the event", bg='blue', command=RegisterCostumer)
button2.place(relx=0.08, rely=0.4, relwidth=0.4, relheight=0.2)
button3 = tk.Button(frame1, compound=tk.TOP, width=10,font=18, height=10,
                                text="Cancel Registration", bg='red', command=RegisterCancel)
button3.place(relx=0.08, rely=0.7, relwidth=0.4, relheight=0.2)

button4 = tk.Button(frame1, compound=tk.TOP, width=5,font=18, height=5,
                                text="Event Info", bg='grey', command=EventInfo)
button4.place(relx=0.55, rely=0.4, relwidth=0.4, relheight=0.2)

window.mainloop()
print(time)
