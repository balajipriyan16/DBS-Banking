import threading
import mysql.connector
from tkinter import *
import tkinter.ttk
import tkinter.messagebox
import random
import Config


#DATABASE CREDENTIALS#
DB_HOST = Config.DBS_HOST
DB_PASSWORD = Config.DBS_PASSWORD
DB_USER = Config.DBS_USER
DB_DATABASE = Config.DBS_DATABASE #Default Name: 'bank'


db = mysql.connector.connect(host=DB_HOST,user=DB_USER,passwd = DB_PASSWORD,
                             database = DB_DATABASE)
myc = db.cursor(buffered=True)
v = "SELECT * FROM details"
m = "SELECT * FROM transactions"
myc.execute(v)
Str = myc.fetchall()
myc.execute(m)
Str2 = myc.fetchall()
comm = "SELECT * FROM admins"
myc.execute(comm)
admin = myc.fetchall()

f = "SELECT * FROM requests"
myc.execute(f)
Req = myc.fetchall()
fg = "white"
bg="navyblue"
def advanced():
    def emplogin():
        def Search():
            global db,myc
            db = mysql.connector.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD,
                                         database=DB_DATABASE)
            myc = db.cursor(buffered=True)
            v = "SELECT * FROM details"
            m = "SELECT * FROM transactions"
            myc.execute(v)
            Str = myc.fetchall()
            def See_t():
                employee_frame2.pack_forget()
                framf = Frame(employee_main_window, width=1000, height=650, background="white")
                framf.pack()
                myc.execute(m)
                Str2 = myc.fetchall()
                ysb = Scrollbar(framf, orient=VERTICAL)
                ysb.pack(side=RIGHT, fill=Y)
                tb = Text(framf, font=("arial", 13, "bold"), width=108, height=28, yscrollcommand=ysb.set)
                tb.pack()

                def show():
                    for dat in Str2[::-1]:
                        if dat[1] == names or dat[3] == names:
                            tb.insert(END, "Date and Time: {},| From: {},| To: {},| ref: {}, |Amount: Rs {:,.2f},"
                                           "\n-------------------------------------------"
                                           "---------------------------------------"
                                           "---------------------------------------------------------------------------"
                                           "----\n".format(dat[2], dat[1], dat[3], dat[5],  float(dat[4])))
                    ysb.config(command=tb.yview)

                show()
                tb.config(state=DISABLED)

                def searchs():
                    tb.config(state=NORMAL)
                    ref = search.get()
                    if len(ref) == 0:
                        tb.delete("0.0", END)
                        show()
                    else:
                        for refs in Str2:
                            if refs[5] == ref:
                                tb.delete("0.0", END)
                                tb.insert(END,
                                          "Date and Time: {},| From: {},| To: {},| ref: {}, |Amount: Rs {:,.2f}"
                                          "\n-------------------------------------------"
                                          "---------------------------------------"
                                          "---------------------------------------------------------------------------"
                                          "----\n".format(refs[2], refs[1], refs[3], refs[5], int(refs[4])))
                    tb.config(state=DISABLED)

                search = Entry(framf, font=("arial", 15, "bold"))
                search.pack()
                search2 = Button(framf, text="Search", font=("arial", 10, "bold"), fg=fg, bg=bg, bd=2, command=searchs)
                search2.pack()
                Label(framf, text="Enter Ref no:", font=("arial", 12, "bold"), fg=fg, bg=bg).place(x=265, y=535)

                def Exit():
                    framf.destroy()
                    employee_frame2.pack()

                Exitb = Button(framf, text="Exit", font=("arial", 10, "bold"), width=5, fg=fg, bg=bg, command=Exit)
                Exitb.place(x=0, y=550)

            def update():
                global Str
                up_name = name_Entry.get()
                up_acc = acc_Entry.get()
                up_pin = pin_Entry.get()
                up_uid = Uid_Entry.get()
                up_balance = Balance_Entry.get()
                up_phno = phno_Entry.get()
                up_status = Status_Entry.get()
                up_gmail = Mail_Entry.get()
                myc.execute(
                    "UPDATE details SET id = '{}',pin = '{}',name = '{}',balance = '{}',accno = '{}',phno = '{}',state = '{}',gmail = '{}' WHERE accno = '{}'".format(
                        up_uid, up_pin, up_name, up_balance, up_acc, up_phno, up_status, up_gmail, names))
                db.commit()
                myc.execute("SELECT * FROM details")
                Str = myc.fetchall()
                name_Entry.delete(0, END)
                acc_Entry.delete(0, END)
                pin_Entry.delete(0, END)
                Uid_Entry.delete(0, END)
                Balance_Entry.delete(0, END)
                phno_Entry.delete(0, END)
                Status_Entry.delete(0, END)
                Mail_Entry.delete(0, END)
                See_trans.config(state=DISABLED)
                Update.config(state=DISABLED)
                details_l2.delete(0, END)
                delete_Button.config(state=DISABLED)
                clear_details()
                Upds = Label(employee_frame2, text="Successfully Updated!", font=("arial", 15, "bold"), fg="green",
                             bg="white")
                Upds.place(x=350, y=150)
                Upds.after(1000, lambda: Upds.destroy())

            def delete():
                global Str
                namec = details_l2.get()
                for bv in Str:
                    if bv[0] == namec or bv[4] == namec or bv[5] == namec:
                        if tkinter.messagebox.askyesno("Confirm",
                                                       "Are you Sure\nDo you want to delete this account permanently"):
                            com = "UPDATE details SET state = 'disabled' WHERE accno = '{}'".format(bv[4])
                            myc.execute(com)
                            comd = "UPDATE details SET status = 'offline' WHERE accno = '{}'".format(bv[4])
                            myc.execute(comd)
                            db.commit()
                            nooc = "SELECT * FROM details"
                            myc.execute(nooc)
                            Str = myc.fetchall()
                            tkinter.messagebox.showinfo("Deleted", "Account Has been Permanently Disabled")
                            delete_Button.config(state=DISABLED)
                            name_Entry.delete(0, END)
                            acc_Entry.delete(0, END)
                            pin_Entry.delete(0, END)
                            Uid_Entry.delete(0, END)
                            Balance_Entry.delete(0, END)
                            phno_Entry.delete(0, END)
                            Status_Entry.delete(0, END)
                            Mail_Entry.delete(0, END)
                            See_trans.config(state=DISABLED)
                            Update.config(state=DISABLED)
                            delete_Button.config(state=DISABLED)
                            clear_details()

            See_trans.config(state=NORMAL)
            Update.config(state=NORMAL)
            delete_Button.config(state=NORMAL)
            name_Entry.config(state=NORMAL)
            acc_Entry.config(state=NORMAL)
            pin_Entry.config(state=NORMAL)
            Uid_Entry.config(state=NORMAL)
            Balance_Entry.config(state=NORMAL)
            phno_Entry.config(state=NORMAL)
            Status_Entry.config(state=NORMAL)
            Mail_Entry.config(state=NORMAL)
            name_Entry.delete(0, END)
            acc_Entry.delete(0, END)
            pin_Entry.delete(0, END)
            Uid_Entry.delete(0, END)
            Balance_Entry.delete(0, END)
            phno_Entry.delete(0, END)
            Status_Entry.delete(0, END)
            Mail_Entry.delete(0, END)

            def clear_details():
                name_Entry.delete(0, END)
                acc_Entry.delete(0, END)
                pin_Entry.delete(0, END)
                Uid_Entry.delete(0, END)
                Balance_Entry.delete(0, END)
                phno_Entry.delete(0, END)
                Status_Entry.delete(0, END)
                name_Entry.config(state=DISABLED)
                acc_Entry.config(state=DISABLED)
                pin_Entry.config(state=DISABLED)
                Uid_Entry.config(state=DISABLED)
                Balance_Entry.config(state=DISABLED)
                phno_Entry.config(state=DISABLED)
                Status_Entry.config(state=DISABLED)
                Mail_Entry.config(state=DISABLED)
                See_trans.config(state=DISABLED)
                Update.config(state=DISABLED)
                delete_Button.config(state=DISABLED)
                Update.config(state=DISABLED)

            fc = 0
            for b in Str:
                name = details_l2.get()
                if len(name) == 0:
                    clear_details()
                elif b[0] == name or b[4] == name or b[5] == name:
                    fc = 1
                    names = b[4]
                    name_Entry.insert(END, b[2])
                    acc_Entry.insert(END, b[4])
                    pin_Entry.insert(END, b[1])
                    Uid_Entry.insert(END, b[0])
                    Balance_Entry.insert(END, b[3])
                    phno_Entry.insert(END, b[5])
                    Status_Entry.insert(END, b[6])
                    Mail_Entry.insert(END, b[9])
                    See_trans.config(command=See_t)
                    Update.config(command=update)
                    delete_Button.config(command=delete)
                    namela.config(fg="white")
                    Accnola.config(fg="white")
                    Pinla.config(fg="white")
                    Uidla.config(fg="white")
                    Balance.config(fg="white")
                    Phno.config(fg="white")
                    Status.config(fg="white")
                    Gmail.config(fg="white")
                    account_deleted_label.place_forget()
                    if b[8] == "offline":
                        account_deleted_label.place(x=350, y=350)
                        namela.config(fg="red")
                        Accnola.config(fg="red")
                        Pinla.config(fg="red")
                        Uidla.config(fg="red")
                        Balance.config(fg="red")
                        Phno.config(fg="red")
                        Status.config(fg="red")
                        Gmail.config(fg="red")
                        name_Entry.config(state=DISABLED)
                        acc_Entry.config(state=DISABLED)
                        pin_Entry.config(state=DISABLED)
                        Uid_Entry.config(state=DISABLED)
                        Balance_Entry.config(state=DISABLED)
                        phno_Entry.config(state=DISABLED)
                        Status_Entry.config(state=DISABLED)
                        Mail_Entry.config(state=DISABLED)
                        delete_Button.config(state=DISABLED)
                        Update.config(state=DISABLED)
            if fc == 0:
                clear_details()

        def create_Customer():
            def Create():
                try:
                    ff = int(e6.get())
                except ValueError:
                    tkinter.messagebox.showerror("Invalid", "Account Number must in Numbers!")
                else:
                    global Str
                    a = e1.get()
                    b = e2.get()
                    c = e3.get()
                    d = e4.get()
                    e = e5.get()
                    ff = str(ff)
                    m = []
                    mm = []
                    mmm = []
                    for CV in Str:
                        m.append(CV[4])
                        mm.append(CV[0])
                        mmm.append(CV[5])
                    try:
                        vbbs = int(b)
                    except ValueError:
                        tkinter.messagebox.showerror("Invalid", "Please check the mobile number")
                    else:
                        if len(a) <= 0 or len(b) <= 0 or len(c) <= 0 or len(d) <= 0 or len(e) <= 0 or len(ff) <= 0:
                            tkinter.messagebox.showerror("Invalid", "Please check all Details!")
                        elif ff in m or d in mm or b in mmm:
                            tkinter.messagebox.showerror("Invalid",
                                                         "Account Number/ Userid/ Mobile \nHas been already registered")
                        elif c[::] == "@gmail.com":
                            tkinter.messagebox.showerror("Invalid", "Please check the Mail!")
                        elif len(b) > 10:
                            tkinter.messagebox.showerror("Invalid", "Please check the mobile number")
                        else:
                            create = "INSERT INTO details(name,phno,gmail,id,pin,accno,balance,state,state2,status) values('{}','{}','{}','{}','{}','{}','100','active','a','online')".format(
                                a, b, c, d, e, ff)
                            myc.execute(create)
                            db.commit()
                            myc.execute("SELECT * FROM details")
                            Str = myc.fetchall()
                            e1.config(state=DISABLED)
                            e2.config(state=DISABLED)
                            e3.config(state=DISABLED)
                            e4.config(state=DISABLED)
                            e5.config(state=DISABLED)
                            e6.config(state=DISABLED)
                            Label(CCf, text="Customer Created!", fg="green", bg="white",
                                  font=("arial", 15, "bold")).place(x=0, y=420)
                            tkinter.messagebox.showinfo("Success", "Customer Created!")
                            bo.config(state=DISABLED)

            employee_frame2.pack_forget()
            CCf = Frame(employee_main_window, width=1000, height=650)
            CCf.pack()

            def Exx():
                CCf.destroy()
                employee_frame2.pack()

            Button(CCf, text="Exit", font=("arial", 11, "bold"), fg=fg, bg=bg, command=Exx).place(x=0, y=560)
            Label(CCf, text="Name:", font=("arial", 22, "bold"), fg=fg, bg=bg).place(x=0, y=0)
            Label(CCf, text="Phone:", font=("arial", 22, "bold"), fg=fg, bg=bg).place(x=0, y=70)
            Label(CCf, text="Mail:", font=("arial", 22, "bold"), fg=fg, bg=bg).place(x=0, y=100 + 30)
            Label(CCf, text="Userid:", font=("arial", 22, "bold"), fg=fg, bg=bg).place(x=0, y=150 + 30 + 20)
            Label(CCf, text="Password:", font=("arial", 18, "bold"), fg=fg, bg=bg).place(x=0, y=200 + 30 + 20 + 10)
            Label(CCf, text="Accno:", font=("arial", 22, "bold"), fg=fg, bg=bg).place(x=0, y=250 + 30 + 20 + 10 + 10)
            e1 = Entry(CCf, font=("arial", 22, "bold"), bd=5)
            e1.place(x=115, y=0)
            e2 = Entry(CCf, font=("arial", 22, "bold"), bd=5)
            e2.place(x=115, y=70)
            e3 = Entry(CCf, font=("arial", 22, "bold"), bd=5)
            e3.place(x=115, y=100 + 30)
            e4 = Entry(CCf, font=("arial", 22, "bold"), bd=5)
            e4.place(x=115, y=150 + 30 + 20)
            e5 = Entry(CCf, font=("arial", 22, "bold"), bd=5)
            e5.place(x=115, y=200 + 30 + 20 + 10)
            e6 = Entry(CCf, font=("arial", 22, "bold"), bd=5)
            e6.place(x=115, y=250 + 30 + 20 + 10 + 10)

            def generate():
                Rnumber = random.randint(111111, 999999)
                e6.delete(0, END)
                e6.insert(END, str(Rnumber))

            Button(CCf, text="Generate number", font=("arial", 15, "bold"), fg=fg, bg=bg, command=generate).place(
                x=115 + 250 + 50 + 50, y=250 + 30 + 20 + 10 + 10)
            bo = Button(CCf, text="Create Customer", font=("arial", 13, "bold"), fg=fg, bg=bg, command=Create)
            bo.place(x=0, y=385)

        def show_customers():
            global Str

            def showC():
                textbox.config(state=NORMAL)
                textbox.delete("0.0", END)
                if entry.get() == "":
                    showd()
                else:
                    for C in Str:
                        if C[4] == entry.get() or C[0] == entry.get() or C[2] in entry.get() or C[6] == entry.get():
                            textbox.insert(END,
                                           f"Name:{C[2]} | Account Number: {C[4]} | AccStatus: {C[6]}\n------------------------------------------------------------------------------------------\n")
                textbox.config(state=DISABLED)

            employee_frame2.pack_forget()
            Cframe = Frame(employee_main_window, width=1000, height=650)
            Cframe.pack()
            textbox = Text(Cframe, font=("consolas", 15, "bold"), width=90, height=23)
            textbox.place(x=0, y=0)

            def showd():
                textbox.delete("0.0", END)
                for ib in Str:
                    if ib[8] == "offline":
                        pass
                    else:
                        textbox.insert(END,
                                       f"Name:{ib[2]} | Account Number: {ib[4]} | AccStatus: {ib[6]}\n------------------------------------------------------------------------------------------\n")

            showd()
            textbox.config(state=DISABLED)

            def showda():
                textbox.config(state=NORMAL)
                textbox.delete("0.0", END)
                for ib in Str:
                    if ib[8] == "offline":
                        textbox.insert(END,
                                       f"Name:{ib[2]} | Account Number: {ib[4]} | AccStatus: {ib[6]}\n------------------------------------------------------------------------------------------\n")
                textbox.config(state=DISABLED)

            Button(Cframe, font=("arial", 10, "bold"), text="See deleted Accounts", fg=fg, bg=bg, command=showda).place(
                x=0, y=533)
            Label(Cframe, font=("arial", 12, "bold"), text="Enter Accno or\nId\nor status:", fg=fg, bg=bg).place(x=200,
                                                                                                                 y=533)
            entry = Entry(Cframe, font=("arial", 12, "bold"), bd=3)
            entry.place(x=330, y=533)
            Button(Cframe, font=("arial", 10, "bold"), text="Submit", fg=fg, bg=bg, command=showC).place(x=525, y=533)

            def Exit():
                Cframe.destroy()
                employee_frame2.pack()

            Button(Cframe, font=("arial", 10, "bold"), text="Exit", fg=fg, bg=bg, command=Exit).place(x=0, y=565)

        def make_all_disabled():
            global Str
            if tkinter.messagebox.askokcancel("Confirm", "Are you sure\n Do your want to make all accounts disabled?"):
                myc.execute("UPDATE details SET state2 = 'd'")
                db.commit()
                myc.execute("SELECT * FROM details")
                Str = myc.fetchall()
                tkinter.messagebox.showinfo("Done", "All Account Are Temporarily disabled")
                maa.config(state=NORMAL)
                mad.config(state=DISABLED)

        def make_all_active():
            global Str
            if tkinter.messagebox.askokcancel("Confirm", "Are you sure\n Do your want to make all accounts Enabled"):
                myc.execute("UPDATE details SET state2 = 'a'")
                db.commit()
                myc.execute("SELECT * FROM details")
                Str = myc.fetchall()
                tkinter.messagebox.showinfo("Done", "All Accounts Active")
                mad.config(state=NORMAL)
                maa.config(state=DISABLED)

        def show_requests():
            global Req
            myc.execute(f)
            Req = myc.fetchall()
            employee_frame2.pack_forget()
            reqframe = Frame(employee_main_window, width=1000, height=650)
            reqframe.pack()
            listbox = Listbox(reqframe, font=("arial", 22, "bold"), height=15, width=30)
            listbox.place(x=0, y=0)
            for R in Req:
                listbox.insert(listbox.size(), R[1])

            def Seer():
                def CcD():
                    coms = "DELETE FROM requests WHERE sno = {}".format(sno)
                    myc.execute(coms)
                    db.commit()
                    myc.execute(f)
                    Req = myc.fetchall()
                    try:
                        listbox.delete(listbox.curselection())
                        if listbox.size() == 0:
                            cv.config(state=DISABLED)
                        tkinter.messagebox.showinfo("Deleted", "The Request has been deleted!")
                        Newf.destroy()
                        reqframe.pack()
                    except tkinter.TclError:
                        tkinter.messagebox.showerror("oops!!", "Please Go back and Select and\n Try again")

                def Cc():
                    Newf.destroy()
                    reqframe.pack()

                try:
                    v = listbox.get(listbox.curselection())
                except tkinter.TclError:
                    tkinter.messagebox.showerror("Invalid", "Please Select Any requests")
                else:
                    reqframe.pack_forget()
                    Newf = Frame(employee_main_window, width=1000, height=650)
                    Newf.pack()
                    Rtb = Text(Newf, font=("consolas", 15, "bold"))
                    Rtb.pack()
                    for F in Req:
                        if F[1] == v:
                            sno = F[0]
                            Rtb.insert(END,
                                       "Date and Time: {}\n--------------------------------------------------------------------------------\nFrom Account Number: {}\n--------------------------------------------------------------------------------\nMessage:-\n----------\n{}".format(
                                           F[1], F[2], F[3]))
                    Rtb.config(state=DISABLED)
                    Button(Newf, text="Delete", command=CcD, font=("arial", 12, "bold"), fg=fg, bg=bg).pack(side=LEFT)
                    Button(Newf, text="Back", command=Cc, font=("arial", 12, "bold"), fg=fg, bg=bg).pack(side=LEFT)

            cv = Button(reqframe, text="Check", font=("arial", 15, "bold"), fg=fg, bg=bg, command=Seer)
            cv.place(x=0, y=540)
            if listbox.size() == 0:
                cv.config(state=DISABLED)

            def CCc():
                reqframe.destroy()
                employee_frame2.pack()

            Button(reqframe, text="Exit", font=("arial", 12, "bold"), fg=fg, bg=bg, command=CCc).place(x=80, y=540)

        # admin main
        try:
            for g in admin:
                if g[2] == Empuname.get() and g[1] == Emppassword.get():
                    employee_frame.destroy()
                    employee_frame2 = Frame(employee_main_window, width=1000, height=650)
                    employee_frame2.pack()
                    account_deleted_label = Label(employee_frame2, text="Account Deleted", font=("arial", 20, "bold"),
                                                  fg="red", bg="white")
                    Label(employee_frame2, text="Welcome {}".format(g[0]), fg=fg, bg=bg,
                          font=("arial", 22, "bold")).place(x=0, y=0)
                    Label(employee_frame2, text="Enter Customer Id or Account Number or phone Number:", fg=fg, bg=bg,
                          font=("arial", 22, "bold")).place(x=0, y=50)
                    details_l2 = Entry(employee_frame2, font=("arial", 20, "bold"), bd=5)
                    details_l2.place(x=0, y=100)
                    Button(employee_frame2, text="Search", fg=fg, bg=bg, font=("arial", 10, "bold"),
                           command = lambda : threading.Thread(target=Search).start()).place(x=315, y=110)
                    namela = Label(employee_frame2, text="Name:", fg=fg, bg=bg, font=("arial", 15, "bold"))
                    namela.place(x=0, y=0 + 110 + 50)
                    Accnola = Label(employee_frame2, text="Accno:", fg=fg, bg=bg, font=("arial", 15, "bold"))
                    Accnola.place(x=0, y=50 + 100 + 50)
                    Pinla = Label(employee_frame2, text="Pin:", fg=fg, bg=bg, font=("arial", 15, "bold"))
                    Pinla.place(x=0, y=100 + 110 + 40)
                    Uidla = Label(employee_frame2, text="Id:", fg=fg, bg=bg, font=("arial", 15, "bold"))
                    Uidla.place(x=0, y=150 + 110 + 40)
                    Balance = Label(employee_frame2, text="Balance:", fg=fg, bg=bg, font=("arial", 15, "bold"))
                    Balance.place(x=0, y=200 + 110 + 50)
                    Phno = Label(employee_frame2, text="Phone:", fg=fg, bg=bg, font=("arial", 15, "bold"))
                    Phno.place(x=0, y=250 + 110 + 50)
                    Status = Label(employee_frame2, text="Status:", fg=fg, bg=bg, font=("arial", 15, "bold"))
                    Status.place(x=0, y=250 + 110 + 50 + 50)
                    Gmail = Label(employee_frame2, text="Mail id:", fg=fg, bg=bg, font=("arial", 15, "bold"))
                    Gmail.place(x=0, y=250 + 110 + 50 + 50 + 50)
                    name_Entry = Entry(employee_frame2, font=("arial", 15, "bold"), bd=4)
                    name_Entry.delete(0, END)
                    name_Entry.place(x=75, y=0 + 110 + 50)
                    name_Entry.config(state=DISABLED)
                    acc_Entry = Entry(employee_frame2, font=("arial", 15, "bold"), bd=4)
                    acc_Entry.delete(0, END)
                    acc_Entry.place(x=75, y=50 + 100 + 50)
                    acc_Entry.config(state=DISABLED)
                    pin_Entry = Entry(employee_frame2, font=("arial", 15, "bold"), bd=4)
                    pin_Entry.delete(0, END)
                    pin_Entry.place(x=75, y=100 + 110 + 40)
                    pin_Entry.config(state=DISABLED)
                    Uid_Entry = Entry(employee_frame2, font=("arial", 15, "bold"), bd=4)
                    Uid_Entry.delete(0, END)
                    Uid_Entry.place(x=75, y=150 + 110 + 40)
                    Uid_Entry.config(state=DISABLED)
                    Balance_Entry = Entry(employee_frame2, font=("arial", 15, "bold"), bd=4)
                    Balance_Entry.delete(0, END)
                    Balance_Entry.place(x=75 + 5, y=200 + 110 + 50)
                    Balance_Entry.config(state=DISABLED)
                    phno_Entry = Entry(employee_frame2, font=("arial", 15, "bold"), bd=4)
                    phno_Entry.delete(0, END)
                    phno_Entry.place(x=75, y=250 + 110 + 50)
                    phno_Entry.config(state=DISABLED)
                    Status_Entry = tkinter.ttk.Combobox(employee_frame2, font=("arial", 15, "bold"))
                    Status_Entry["values"] = ("active", "disabled")
                    Status_Entry.delete(0, END)
                    Status_Entry.place(x=75, y=250 + 110 + 50 + 50)
                    Status_Entry.config(state=DISABLED)
                    Mail_Entry = Entry(employee_frame2, font=("arial", 15, "bold"), bd=4,width=30)
                    Mail_Entry.delete(0, END)
                    Mail_Entry.place(x=75, y=250 + 110 + 50 + 50 + 50)
                    Mail_Entry.config(state=DISABLED)
                    See_trans = Button(employee_frame2, text="See Transactions", font=("arial", 15, "bold"), fg=fg,
                                       bg=bg)
                    See_trans.place(x=420, y=250 + 110 + 50 + 50)
                    See_trans.config(state=DISABLED)
                    Update = Button(employee_frame2, text="Update", font=("arial", 15, "bold"), fg=fg, bg=bg)
                    Update.place(x=420, y=250 + 110 + 50 + 50 + 50)
                    Update.config(state=DISABLED)
                    delete_Button = Button(employee_frame2, text="Delete", font=("arial", 15, "bold"), fg=fg, bg=bg)
                    delete_Button.place(x=420 + 100, y=250 + 110 + 50 + 50 + 50)
                    delete_Button.config(state=DISABLED)
                    Button(employee_frame2, text="Add New Customer", command=create_Customer,
                           font=("arial", 15, "bold"), fg=fg, bg=bg).place(x=520 + 100, y=250 + 110 + 50 + 50 + 50)
                    Button(employee_frame2, text="Requests", font=("arial", 15, "bold"), fg=fg, bg=bg,
                           command=show_requests).place(x=420 + 100 + 100, y=250 + 110 + 50 + 50)
                    Button(employee_frame2, text="See all Customers", font=("arial", 15, "bold"), fg=fg, bg=bg,
                           command=show_customers).place(x=420 + 100 + 100, y=250 + 110 + 50)
                    mad = Button(employee_frame2, text="Make all Disabled", font=("arial", 15, "bold"), fg=fg, bg=bg,
                                 command=make_all_disabled)
                    mad.place(x=420 + 100 + 50 + 50, y=250 + 110)
                    maa = Button(employee_frame2, text="Make all Active", font=("arial", 15, "bold"), fg=fg, bg=bg,
                                 command=make_all_active)
                    maa.place(x=420 + 25, y=250 + 110 + 50)
                    maa.config(state=DISABLED)
                    for bn in Str:
                        if bn[7] == "d":
                            maa.config(state=NORMAL)
                            mad.config(state=DISABLED)

                    def Exitc():
                        employee_main_window.destroy()
                        exit()

                    Button(employee_frame2, text="Exit", font=("arial", 10, "bold"), fg=fg, bg=bg, command=Exitc).place(
                        x=0, y=573)
        except ValueError:
            tkinter.messagebox.showerror("Invalid password", "Please check the password")
    employee_main_window = Tk()
    employee_main_window.title("DBS Admin")
    employee_main_window.iconbitmap("./Assets/logo.ico")
    employee_main_window.config(background="white")
    employee_frame = Frame(employee_main_window, width=1000, height=650)
    employee_frame.pack()
    unamel = Label(employee_frame, text="Username or\nID", font=("arial", 13, "bold"), fg=fg, bg=bg)
    unamel.place(x=15 + 53 + 100 + 60, y=345)
    unamels = Label(employee_frame, text="Password", font=("arial", 14, "bold"), fg=fg, bg=bg)
    unamels.place(x=20 + 50 + 100 + 60, y=390 + 13)
    Empuname = Entry(employee_frame, font=("arial", 20, "bold"), bd=5)
    Empuname.place(x=175 + 100 + 60, y=345)
    Emppassword = Entry(employee_frame, font=("arial", 20, "bold"), bd=5, show="●")
    Emppassword.place(x=175 + 100 + 60, y=390)
    Admin = Label(employee_frame, text="DBS Bank\nAdmin Interface", font=("consolas", 60, "bold"), fg=fg, bg=bg,
                  width=23)
    Admin.place(x=0, y=90)
    Submit_button = Button(employee_frame, text="Login", font=("arial", 13, "bold"), fg=fg, bg=bg, width=8,
                           command=emplogin)
    Submit_button.place(x=175 + 50 + 50 + 100 + 50, y=445)
    w = 1000
    h = 600
    screen_w = employee_main_window.winfo_screenwidth()
    screen_h = employee_main_window.winfo_screenheight()
    x = (screen_w / 2) - (w / 2)
    y = (screen_h / 2) - (h / 2)
    x = x - 75
    y = y - 25
    employee_main_window.geometry(f"{w}x{h}+{int(x)}+{int(y)}")
    employee_main_window.resizable(False, False)
    employee_main_window.mainloop()
advanced()