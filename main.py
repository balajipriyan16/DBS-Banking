import mysql.connector
from tkinter import *
import tkinter.messagebox
import random
import socket
from fpdf import FPDF
from tkinter import filedialog
from time import strftime,sleep
import smtplib
import Config

#DATABASE CREDENTIALS#
DB_HOST = Config.DBS_HOST
DB_PASSWORD = Config.DBS_PASSWORD
DB_USER = Config.DBS_USER
DB_DATABASE = Config.DBS_DATABASE #Default Name: bank

#Mail Credentials (for sending mails)
Mail_Sender = "your-mail"
Mail_Password = "your-app password"


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
#####################

def welcome():
    global Str,Str2
    def interface():
        def main():
            def showb():
                global db,myc
                balance.config(text="PLEASE WAIT")
                balance.config(state=DISABLED)
                db = mysql.connector.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD,
                                             database=DB_DATABASE)
                myc = db.cursor(buffered=True)
                balances.place(x=0, y=175 + 75)
                myc.execute("SELECT * FROM details")
                Str = myc.fetchall()
                for i in Str:
                    if i[0] == un or i[4] == un and i[1] == ps:
                        newb = float(i[3])
                        balances.config(text="Rs: {:,.2f}".format(newb))
                balance.config(text="Click to view Balance", state=ACTIVE)
                balance.config(state=ACTIVE)
            def pinchange():
                db = mysql.connector.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD,
                                             database=DB_DATABASE)
                myc = db.cursor(buffered=True)
                v = "SELECT * FROM details"
                m = "SELECT * FROM transactions"
                myc.execute(v)
                Str = myc.fetchall()
                myc.execute(m)
                Str2 = myc.fetchall()
                def finish():
                    def finish2():
                        global Str
                        newpss = newpin.get()
                        for i in Str:
                            if i[0] == un or i[4] == un and i[1] == oldp:
                                accnod = i[4]
                                myc.execute("UPDATE details SET pin = '{}' WHERE accno = '{}'".format(newpss,accnod))
                                db.commit()
                                myc.execute("SELECT * FROM details")
                                Str = myc.fetchall()
                                tkinter.messagebox.showinfo("Success","Your Password Has been Changed Successfully\nPlease Exit!")
                                newl = Label(fram3, text="Password changed", font=("arial", 25, "bold"),fg="green")
                                newl.place(x=200, y=405)
                                newsub.config(state=DISABLED)
                                newpin.config(state=DISABLED)
                    oldp = oldpin.get()
                    xaxis = 200
                    for i in Str:
                        if i[0] == un or i[4] == un and i[1] == oldp:
                            oldpin.config(state=DISABLED)
                            sub.config(state=DISABLED)
                            Label(fram3, text="Enter your New Password", bg=bg, fg=fg,font=("arial", 25, "bold")).place(x=xaxis, y=155+100)
                            newpin = Entry(fram3, font=("arial", 25, "bold"), bd=5,show="●")
                            def showd():
                                newpin.config(show="")
                                newpin.after(1000, lambda: newpin.config(show="●"))
                            ssbd = Button(fram3, text="Show password", font=("arial", 10, "bold"), command=showd)
                            ssbd.place(x=575, y=120+200)
                            newpin.place(x=xaxis, y=310)
                            newsub = Button(fram3, font=("arial", 10, "bold"), text="submit", command=finish2,fg=fg,bg=bg)
                            newsub.place(x=xaxis, y=365)
                fram2.pack_forget()
                fram3 = Frame(window, width=1000, height=650)
                fram3.pack()
                def time():
                    string = strftime('%X\n%d - %b - %y')
                    label.config(text=string)
                    label.after(1000, time)
                def Exit():
                    label.destroy()
                    fram3.destroy()
                    fram2.pack()
                label = Label(window, font=("arial", 20, "bold"), background=bg, foreground=fg)
                label.place(x=830,y=0)
                time()
                Label(fram3, text="Enter your old password", bg=bg, fg=fg,font=("arial",25, "bold")).place(x=200,y=10+10+65)
                oldpin = Entry(fram3,font=("arial",25,"bold"),bd=5,show="●")
                oldpin.place(x=200,y=55+10+65)
                def show():
                    oldpin.config(show="")
                    oldpin.after(1000,lambda :oldpin.config(show="●") )
                ssb = Button(fram3,text="Show password",font=("arial",10,"bold"),command=show)
                ssb.place(x=200+250+50+75,y=55+10+65+20)
                sub = Button(fram3,font=("arial",10,"bold"),text="submit",command=finish,fg=fg,bg=bg)
                sub.place(x=200,y=105+10+65)
                exitb = Button(fram3,font=("arial",10,"bold"),text="Exit",fg=fg,bg=bg,command=Exit)
                exitb.place(x=0,y=570)
            def logout():
                tlabel.destroy()
                l23 = Label(fram2, text="Thank you for using DBS\nbanking services", bg=bg, fg=fg,font=("arial", 40, "bold"),width=40, height=10)
                l23.pack()
                def nexts():
                    window.destroy()
                    welcome()
                l23.after(1500,nexts)
            def transfer():

                Transfer.config(state=DISABLED)
                def t2():
                    def Exits():
                        label.destroy()
                        frame5.destroy()
                        fram2.pack()
                        balance.invoke()
                        Transfer.config(state=ACTIVE)
                    def nexc():
                        def nexcv():
                            subbs.config(state=DISABLED)
                            foundss = 0
                            global Str
                            global Str2
                            pin = Ams.get()
                            if pin == ps:
                                global db, myc
                                db = mysql.connector.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD,
                                                             database=DB_DATABASE)
                                myc = db.cursor(buffered=True)
                                v = "SELECT * FROM details"
                                m = "SELECT * FROM transactions"
                                myc.execute(v)
                                Str = myc.fetchall()
                                myc.execute(m)
                                for ig in Str:
                                    if ig[0] == bname or ig[4] == bname:
                                        for n in Str:
                                            if n[0] == un or n[4] == un and n[1] == ps:
                                                try:
                                                    ahb = float(n[3])
                                                    bb = float(ig[3])
                                                    ta = float(Am.get())
                                                    if ta <= 0:
                                                        foundss = 0
                                                    else:
                                                        bfas = bb + ta
                                                        ahfas = ahb - ta
                                                        beneficiary_acount_number = ig[4]
                                                        account_holder_accno = n[4]
                                                        beneficiary_name = ig[2]
                                                        account_holder_name = n[2]
                                                        Transferred_amount = str(Am.get())
                                                        if ahfas <= 0:
                                                            foundss = 2
                                                        else:
                                                            a = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
                                                            b = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
                                                            c = "1 2 3 4 5 6 7 8 9 0".split()
                                                            ch = random.choices(a, k=2)
                                                            cha = random.choices(b, k=2)
                                                            chaa = random.choices(c, k=2)
                                                            refs = ch + chaa + cha
                                                            ref = "".join(random.sample(refs,len(refs)))
                                                            myc.execute("UPDATE details SET balance = '{}' WHERE accno = '{}'".format(str(ahfas), account_holder_accno))
                                                            myc.execute("UPDATE details SET balance = '{}' WHERE accno = '{}'".format(str(bfas), str(beneficiary_acount_number)))
                                                            string = strftime('%d/%m/%y, %X')
                                                            myc.execute("INSERT INTO transactions (F,Ti,T,Amount,ref) VALUES ('{}','{}','{}','{}','{}')".format(n[4], string, ig[4], Transferred_amount, ref))
                                                            db.commit()
                                                            myc.execute("SELECT * FROM details")
                                                            Str = myc.fetchall()
                                                            myc.execute(m)
                                                            Str2 = myc.fetchall()
                                                            foundss = 1
                                                            subbss = Label(frame5, text="Transaction Successful\nPlease Exit!",
                                                                            fg="green", font=("arial", 15, "bold"))
                                                            subbss.place(x=150, y=300 + 100 + 40)
                                                            tkinter.messagebox.showinfo("Success","Transaction Successful")
                                                            Transfer.config(state=ACTIVE)
                                                            string = strftime('%d/%m/%y, %X')
                                                            t1 = string[:8]
                                                            t2 = string[10:]
                                                            def save():
                                                                a = filedialog.asksaveasfilename(
                                                                    filetypes=[("All files", ".*")],)
                                                                if len(a) == 0:
                                                                    pass
                                                                else:
                                                                    pdf = FPDF()
                                                                    pdf.add_page()
                                                                    pdf.set_font("arial", size=25)
                                                                    pdf.image("./Assets/dbs.png")
                                                                    pdf.text(15, 65, t1)
                                                                    pdf.text(15, 77, t2)
                                                                    pdf.text(140, 70, ref)
                                                                    pdf.text(15, 112, account_holder_accno)
                                                                    pdf.text(150, 112, beneficiary_acount_number)
                                                                    pdf.text(15, 150, account_holder_name)
                                                                    pdf.text(15, 190, beneficiary_name)
                                                                    pdf.text(15, 227, Transferred_amount)
                                                                    if a[-1:-5:-1] == "fdp.":
                                                                        pdf.output(f"{a}", "F")
                                                                        prints.config(text="Recipt Saved!")
                                                                        prints.config(state=DISABLED)
                                                                    else:
                                                                        pdf.output(f"{a}.pdf", "F")
                                                                        prints.config(text="Recipt Saved!")
                                                                        prints.config(state=DISABLED)
                                                            prints = Button(frame5,text="Save recipt!",fg="white",bg=bg,
                                                                            font=("arial",13,"bold"),command=save)
                                                            prints.place(x=150, y=300 + 100 + 40+50+10)
                                                except ValueError:
                                                    foundss = 3
                            if foundss == 0:
                                subbss = Label(frame5, text="Please Exit!",
                                               fg="red", font=("arial",15, "bold"))
                                subbss.place(x=150, y=300 + 100 + 40)
                                tkinter.messagebox.showerror("Failed","Transaction Failed\nplease Try again later")
                                Transfer.config(state=ACTIVE)
                            elif foundss == 2:
                                subbsss = Label(frame5, text="Insufficient balance!",
                                               fg="red", font=("arial", 15, "bold"))
                                subbsss.place(x=150, y=300 + 100 + 40)
                                tkinter.messagebox.showerror("Insufficient balance!", "Insufficient balance!\nplease exit")
                                Transfer.config(state=ACTIVE)
                            elif foundss == 3:
                                subbsss = Label(frame5, text="Please check the Amount!",
                                                fg="red", font=("arial", 15, "bold"))
                                subbsss.place(x=150, y=300 + 100 + 40)
                                tkinter.messagebox.showerror("Error!",
                                                             "Something went wrong\nplease exit")
                                Transfer.config(state=ACTIVE)
                            Ams.config(state=DISABLED)

                        if len(Am.get()) == 0:
                            inp = Label(frame5,text="Enter the Amount!",font=("arial",15,"bold"),fg="red",bg="white")
                            inp.place(x=65, y=302)
                            inp.after(1000,lambda:inp.destroy())
                        else:
                            Am.config(state=DISABLED)
                            subb.config(state=DISABLED)
                            asbs = Label(frame5, text="Enter Password:-", bg=bg, fg=fg, font=("arial", 18, "bold"))
                            asbs.place(x=0, y=305+40)
                            Ams = Entry(frame5, font=("arial", 18, "bold"), bd=5,show="●")
                            Ams.place(x=0, y=350+40)
                            subbs = Button(frame5, text="Submit", bg=bg,
                                          fg=fg, font=("arial", 10, "bold"), command=nexcv)
                            subbs.place(x=0, y=440)
                    bname = tE.get()
                    founds = 0
                    for ic in Str:
                        if uid == bname or uno == bname:
                            pass
                        elif ic[0] == bname or ic[4] == bname:
                            if ic[6] == "disabled" or ic[8] == "deleted":
                                pass
                            else:
                                tE.delete(0,END)
                                founds = 1
                                fram2.pack_forget()
                                frame5 = Frame(window,width=1000,height=650)
                                frame5.pack()
                                def time():
                                    string = strftime('%X\n%d - %b - %y')
                                    label.config(text=string)
                                    label.after(1000, time)
                                label = Label(window, font=("arial", 20, "bold"), background=bg, foreground=fg)
                                label.place(x=830, y=0)
                                time()
                                namel = Label(frame5, text="Name: {}".format(ic[2]), bg=bg, fg=fg,
                                              font=("arial", 30, "bold"))
                                namel.place(x=0, y=0)
                                namel2 = Label(frame5, text="Account no: {}".format(ic[4]), bg=bg, fg=fg,
                                               font=("arial", 30, "bold"))
                                namel2.place(x=0, y=65)
                                namel2d = Label(frame5, text="Phone: {}".format(ic[5]), bg=bg, fg=fg,
                                               font=("arial", 30, "bold"))
                                namel2d.place(x=0, y=100+30)
                                Eb = Button(frame5,text="Exit", bg=bg, fg=fg,font=("arial",13, "bold"),command=Exits)
                                Eb.place(x=0,y=560)
                                asb = Label(frame5, text="Enter Amount:-", bg=bg, fg=fg,font=("arial", 18, "bold"))
                                asb.place(x=0, y=305-100)
                                Am = Entry(frame5,font=("arial", 18, "bold"),bd=5)
                                Am.place(x=0,y=350-100)
                                subb = Button(frame5,text="Submit",bg=bg,
                                              fg=fg, font=("arial",10, "bold"),command=nexc)
                                subb.place(x=0,y=300)
                                tE.destroy()
                                Transfers.destroy()
                                sb.destroy()
                    if founds == 0:
                        tkinter.messagebox.showerror("Invalid","Invalid Account Number")
                        sbs = Label(fram2, text="Invalid username / Acc Number", bg="white",
                                    fg="red", font=("arial", 12, "bold"))
                        sbs.place(x=225, y=430 + 40)
                        sbs.after(1000, lambda: sbs.destroy())
                Transfers = Label(fram2, text="Beneficiary username / account number", bg=bg,
                                  fg=fg, font=("arial", 18, "bold"))
                Transfers.place(x=200, y=350)
                tE = Entry(fram2,font=("arial", 18, "bold"),bd=5)
                tE.place(x=200+25, y=350+35)
                sb = Button(fram2,text="Submit",bg=bg,
                                  fg=fg, font=("arial",10, "bold"),command=t2)
                sb.place(x=225,y=350+35+35+10)
            def t_history():
                global db, myc
                history.config(text="PLEASE WAIT",state=DISABLED)
                db = mysql.connector.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD,
                                             database=DB_DATABASE)
                myc = db.cursor(buffered=True)
                v = "SELECT * FROM details"
                m = "SELECT * FROM transactions"
                myc.execute(v)
                Str = myc.fetchall()
                myc.execute(m)
                Str2 = myc.fetchall()
                fram2.pack_forget()
                framf = Frame(window, width=1000, height=650, background="white")
                framf.pack()
                myc.execute(m)
                Str2 = myc.fetchall()
                ysb = Scrollbar(framf, orient=VERTICAL)
                ysb.pack(side=RIGHT, fill=Y)
                tb = Text(framf,font=("arial",13,"bold"),width=108,height=28,yscrollcommand=ysb.set)
                tb.pack()
                def show():
                    for dat in Str2[::-1]:
                        if  dat[1] == uno or dat[3] == uno:
                            tb.insert(END,"Date and Time: {},| From: {},| To: {},| ref: {}, |Amount: Rs {:.2f}"
                                          "\n-------------------------------------------"
                                          "---------------------------------------"
                                          "---------------------------------------------------------------------------"
                                          "----\n".format(dat[2],dat[1],dat[3],dat[5],float(dat[4])))
                    ysb.config(command=tb.yview)
                show()
                tb.config(state=DISABLED)
                def searchs():
                    tb.config(state=NORMAL)
                    ref = search.get()
                    if len(ref) == 0:
                        tb.delete("0.0",END)
                        show()
                    else:
                        for refs in Str2:
                            if refs[5] == ref:
                                tb.delete("0.0", END)
                                tb.insert(END,"Date and Time: {},| From: {},| To: {},| ref: {}, |Amount: Rs {:,.2f},"
                                          "\n-------------------------------------------"
                                          "---------------------------------------"
                                          "---------------------------------------------------------------------------"
                                          "----\n".format(refs[2],refs[1],refs[3],refs[5],int(refs[4])))
                    tb.config(state=DISABLED)
                search = Entry(framf, font=("arial", 15, "bold"))
                search.pack()
                search2 = Button(framf,text="Search", font=("arial", 10, "bold"), fg=fg, bg=bg,bd=2,command=searchs)
                search2.pack()
                Label(framf,text="Enter Ref no:", font=("arial", 12, "bold"), fg=fg, bg=bg).place(x=265,y=535)
                def Exit():
                    history.config(state=ACTIVE,text="Transaction History")
                    history.config(activebackground=bg,activeforeground=fg)
                    framf.destroy()
                    fram2.pack()
                Exitb = Button(framf, text="Exit", font=("arial", 10, "bold"), width=5, fg=fg, bg=bg, command=Exit)
                Exitb.place(x=0,y=550)
            def Request():
                global db, myc
                global Req
                db = mysql.connector.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD,
                                             database=DB_DATABASE)
                myc = db.cursor(buffered=True)
                v = "SELECT * FROM details"
                m = "SELECT * FROM transactions"
                myc.execute(v)
                Str = myc.fetchall()
                myc.execute(m)
                Str2 = myc.fetchall()
                def submit():
                    string = strftime('%X, %d - %b - %y')
                    req = text_box.get("1.0",END)
                    if len(req) <= 1:
                        tkinter.messagebox.showerror("Invalid","Request/Message Cannot Be Empty!!")
                    else:
                        myc.execute("INSERT INTO requests(Ti,Fr,Msg) values('{}','{}','{}')".format(string,user_number,req))
                        db.commit()
                        myc.execute(f)
                        Req = myc.fetchall()
                        text_box.config(state=DISABLED)
                        submit.config(state=DISABLED)
                        tkinter.messagebox.showinfo("Request Submitted","Your Request Has been submitted!\nPlease Exit")
                        Label(framt,text="Request Successfully Submitted!\nPlease Exit!",font=("arial",15,"bold"),fg="Green",bg="white").place(x=250,y=500)
                fram2.pack_forget()
                framt = Frame(window, width=1000, height=650, background="white")
                framt.pack()
                text_box = Text(framt,bd=5,font=("consolas",18,"bold"),height=15,width=76)
                text_box.place(x=0,y=60)
                Label(framt,text="Enter your Request Here:",fg=fg,bg=bg,font=("arial",25,"bold")).place(x=0,y=0)
                submit = Button(framt,text="Submit",font=("arial",14,"bold"),fg=fg,bg=bg,command=submit)
                submit.place(x=0,y=500)
                def Ext():
                    framt.destroy()
                    fram2.pack()
                exitb = Button(framt,text="exit",font=("arial",13,"bold"),fg=fg,bg=bg,width=5,command=Ext)
                exitb.place(x=0,y=550)
            def getr():
                global db, myc
                global Str2

                fram2.pack_forget()

                def SURESSs():
                    if tkinter.messagebox.askyesno("Are you Sure", "Are you Sure\nDo you Want To Exit?"):
                        fram35.destroy()
                        window.destroy()
                        exit(0)

                window.protocol("WM_DELETE_WINDOW", SURESSs)

                def Exit():
                    window.protocol("WM_DELETE_WINDOW", SURE)
                    fram35.destroy()
                    fram2.pack()
                db = mysql.connector.connect(host=DB_HOST,user=DB_USER,passwd = DB_PASSWORD,
                             database = DB_DATABASE)
                myc = db.cursor(buffered=True)
                v = "SELECT * FROM details"
                m = "SELECT * FROM transactions"
                myc.execute(v)
                Str = myc.fetchall()
                myc.execute(m)
                Str2 = myc.fetchall()
                def nextsd():
                    def last():
                        found = 0
                        for dat in Str2:
                            if dat[5] == oldpins.get():
                                a = filedialog.asksaveasfilename(filetypes=[("All files", ".*")])
                                if len(a) == 0:
                                    found = 1
                                else:
                                    found = 1
                                    t1 = dat[2][:8]
                                    t2 = dat[2][10:]
                                    account_holder_accno = dat[1]
                                    beneficiary_acount_number = dat[3]
                                    Transferred_amount = dat[4]
                                    ref = oldpins.get()
                                    pdf = FPDF()
                                    pdf.add_page()
                                    pdf.set_font("arial", size=25)
                                    pdf.image("./Assets/dbs.png")
                                    pdf.text(15, 65, t1)
                                    pdf.text(15, 77, t2)
                                    pdf.text(140, 70, ref)
                                    pdf.text(15, 112, account_holder_accno)
                                    pdf.text(150, 112, beneficiary_acount_number)
                                    pdf.text(15, 150, account_holder_name)
                                    pdf.text(15, 190, beneficiary_name)
                                    pdf.text(15, 227, Transferred_amount)
                                    pdf.output("a.pdf")
                                    def saved():
                                        sub.config(state=DISABLED)
                                        tkinter.messagebox.showinfo("Saved", "Receipt Saved!")
                                    if a[-1:-5:-1] == "fdp.":
                                        pdf.output(f"{a}", "F")
                                        saved()
                                    else:
                                        pdf.output(f"{a}.pdf", "F")
                                        saved()
                        if found == 0:
                            tkinter.messagebox.showerror("Invalid", "Invalid Ref Number")
                    for jj in Str:
                        for jjd in Str2:
                            if jjd[-1] == oldpins.get():
                                if jjd[3] == jj[4]:
                                    beneficiary_name = jj[2]
                                if jjd[1] == jj[4]:
                                    account_holder_name = jj[2]
                    last()
                fram35 = Frame(window, width=1000, height=650)
                fram35.pack()
                oldl = Label(fram35, text="Enter Ref no: ", bg=bg, fg=fg,font=("arial", 25, "bold"))
                oldl.place(x=200, y=10 + 10 + 65)
                oldpins = Entry(fram35, font=("arial", 25, "bold"), bd=5)
                oldpins.place(x=200, y=55 + 10 + 65)
                sub = Button(fram35, font=("arial", 10, "bold"), text="Print Receipt", command=nextsd, fg=fg, bg=bg)
                sub.place(x=200, y=105 + 10 + 65)
                exitb = Button(fram35, font=("arial", 15, "bold"), text="Exit", fg=fg, bg=bg,
                               command=Exit)
                exitb.place(x=0, y=560)
            def seepro():

                def SURESS():
                    if tkinter.messagebox.askyesno("Are you Sure", "Are you Sure\nDo you Want To Exit?"):
                        profile_frame.destroy()
                        window.destroy()
                        exit(0)

                window.protocol("WM_DELETE_WINDOW", SURESS)
                def Ed():
                    profile_frame.destroy()
                    fram2.pack()
                    window.protocol("WM_DELETE_WINDOW", SURE)


                fram2.pack_forget()
                profile_frame = Frame(window, width=1000, height=650, background="white")
                profile_frame.pack()
                for iff in Str:
                    if iff[0] == un or iff[4] == un and iff[1] == ps:
                        Label(profile_frame,text="Name: {}".format(iff[2]),font=("arial",22,"bold"),fg=fg,bg=bg).place(x=0,y=0)
                        Label(profile_frame,text="Accno: {}".format(iff[4]),font=("arial",22,"bold"),fg=fg,bg=bg).place(x=0,y=50)
                        Label(profile_frame, text="Phone Number: {}".format(iff[5]), font=("arial", 22, "bold"), fg=fg,bg=bg).place(x=0,y=100)
                        Label(profile_frame, text="Userid: {}".format(iff[0]), font=("arial", 22, "bold"), fg=fg,bg=bg).place(x=0,y=150)
                        Label(profile_frame, text="Mail id: {}".format(iff[9]), font=("arial", 22, "bold"), fg=fg,bg=bg).place(x=0,y=200)
                        Label(profile_frame, text="Status: {}".format(iff[6]), font=("arial", 22, "bold"), fg=fg,bg=bg).place(x=0,y=250)
                EB = Button(profile_frame,text="Exit",fg=fg,bg=bg,font=("arial",12,"bold"),command=Ed)
                EB.place(x=0,y=565)
            #customer main interface
            global db, myc
            db = mysql.connector.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD,
                                         database=DB_DATABASE)
            myc = db.cursor(buffered=True)
            v = "SELECT * FROM details"
            m = "SELECT * FROM transactions"
            myc.execute(v)
            Str = myc.fetchall()
            myc.execute(m)
            Str2 = myc.fetchall()
            window.resizable(True,True)
            for i in Str:
                if i[0] == un or i[4] == un and i[1] == ps:
                    l.destroy()
                    fram2 = Frame(window,width=1000,height=650,background="white")
                    fram2.pack()
                    Label(fram2,text="Welcome {}".format(i[2]),bg=bg,fg=fg,font=("arial",30,"bold")).place(x=0,y=0)
                    Button(fram2,text="Get Receipts",font=("arial",15,"bold"),fg=fg,bg=bg,
                           command=getr).place(x=855,y=190)
                    Button(fram2,text="See profile",font=("arial",15,"bold"),fg=fg,bg=bg,
                           command=seepro).place(x=855,y=190+50)
                    Send_Request = Button(fram2, text="Contact Bank",font=("arial", 15, "bold"), fg=fg, bg=bg, command=Request)
                    Send_Request.place(x=850, y=140)
                    Label(fram2, text="Account no: {}".format(i[4]), bg=bg, fg=fg, font=("arial", 30, "bold")).place(x=0,y=65+25)
                    pinchange = Button(fram2, text="Change password", bg=bg,fg=fg, font=("arial", 15, "bold"), command=pinchange,activeforeground=fg,activebackground=bg)
                    pinchange.place(x=0,y=125+50)
                    history = Button(fram2, text="Transaction History",bg=bg, fg=fg,
                                     font=("arial", 18, "bold"),
                                     command=t_history)
                    history.place(x=750,y=80)

                    def SURE():
                        if tkinter.messagebox.askyesno("Are you Sure","Are you Sure\nDo you Want To Exit?"):
                            fram2.destroy()
                            exit(0)
                    window.protocol("WM_DELETE_WINDOW",SURE)


                    logouts = Button(fram2,text="Logout",bg=bg,fg=fg, font=("arial", 15, "bold"),command=logout)
                    logouts.place(x=0,y=550)
                    uid = i[0]
                    uno = i[4]
                    user_number = i[4]
                    Transfer = Button(fram2,image=img,command=transfer)
                    Transfer.place(x=0,y=350)
                    def ne(event):
                        Transfer.config(background="red")
                    def xe(event):
                        Transfer.config(background=bg)
                    Transfer.bind("<Enter>",ne)
                    Transfer.bind("<Leave>",xe)
                    balances = Label(fram2, font=("arial", 19, "bold"), bd=5,relief=RAISED, bg=bg, fg=fg)
                    def time():
                        string = strftime('%X\n%d - %b - %y')
                        tlabel.config(text=string)
                        tlabel.after(1000, time)
                    tlabel = Label(fram2, font=("arial",20,"bold"), bg=bg, fg=fg)
                    tlabel.place(x=830, y=0)
                    time()
                    balance = Button(fram2, activebackground=bg, text="Click to view balance", bg=bg, fg=fg,
                                     font=("arial", 10, "bold"), command=showb,
                                     activeforeground=fg)
                    balance.place(x=0, y=175 + 75 + 50)
                    def ccd(r):
                        balance.config(fg="red")
                    def ccsd(e):
                        balance.config(fg=fg)
                    balance.bind("<Enter>", ccd)
                    balance.bind("<Leave>", ccsd)
        un = uname.get()
        ps = password.get()
        uname.delete(0, END)
        password.delete(0, END)
        uname.focus_set()
        found = 0
        for i in Str:
            if i[0] == un or i[4] == un and i[1] == ps:
                ssl = i[4]
                if i[7] == "d":
                    found = 11
                    tkinter.messagebox.showinfo("Maintenance","Sorry we are updating our servers,\nplease Try again after sometime\nThank you for your cooperation\nDBS bank")
                elif i[8] == "offline":
                    pass
                elif i[6] == "disabled":
                    global Req
                    found = 1
                    if tkinter.messagebox.askokcancel("Disabled","Your account Has been Disabled!\nContact Bank?"):
                        def submit():
                            string = strftime('%X, %d - %b - %y')
                            req = text_box.get("1.0", END)
                            if len(req) <= 1:
                                Sucls = Label(framt, text="Request Cannot be Empty",font=("arial", 15, "bold"), fg="Red", bg="white")
                                Sucls.place(x=250, y=500)
                                Sucls.after(1000, lambda: Sucls.destroy())
                            else:
                                myc.execute("INSERT INTO requests(Ti,Fr,Msg) values('{}','{}','{}')".format(string,ssl,req))
                                db.commit()
                                myc.execute(f)
                                Req = myc.fetchall()
                                tkinter.messagebox.showinfo("Submitted", "Your Request Has been submitted!")
                                text_box.config(state=DISABLED)
                                submit.config(state=DISABLED)
                                Label(framt, text="Request Successfully Submitted!\nPlease Exit!",font=("arial", 15, "bold"), fg="Green", bg="white").place(x=250, y=500)
                        frame.destroy()
                        framt = Frame(windows, width=1000, height=650, background="white")
                        framt.pack()
                        text_box = Text(framt, bd=5, font=("consolas", 18, "bold"), height=15, width=76)
                        text_box.place(x=0, y=60)
                        Label(framt, text="Enter your Request Here:", fg=fg, bg=bg, font=("arial", 25, "bold")).place(x=0, y=0)
                        submit = Button(framt, text="Submit", font=("arial", 14, "bold"), fg=fg, bg=bg, command=submit)
                        submit.place(x=0, y=500)
                        def Ext():
                            windows.destroy()
                            welcome()
                        exitb = Button(framt, text="exit", font=("arial", 13, "bold"), fg=fg, bg=bg, width=5,command=Ext)
                        exitb.place(x=0, y=550)
                    else:
                        windows.destroy()
                        welcome()
                else:
                    windows.destroy()
                    window = Tk()
                    img = PhotoImage(file="./Assets/Symbol.png")
                    window.title("DBS Banking")
                    window.iconbitmap("./Assets/logo.ico")
                    window.config(background="white")
                    window.config(bg="white")
                    window.resizable(False, False)
                    l = Label(window,text="Please wait...",bg=bg,fg=fg,font=("arial",40,"bold"),width=40,height=10)
                    l.pack()
                    l.after(1000,main)
                    found = 1
                    w = 1000
                    h = 600
                    screen_w = window.winfo_screenwidth()
                    screen_h = window.winfo_screenheight()
                    x = (screen_w / 2) - (w / 2)
                    y = (screen_h / 2) - (h / 2)
                    x = x - 75
                    y = y - 25
                    window.geometry(f"{w}x{h}+{int(x)}+{int(y)}")
                    window.mainloop()
        if found == 0 :
            tkinter.messagebox.showerror("invalid", "invalid username / password")
            windows.destroy()
            welcome()
        elif found == 11:
            windows.destroy()
            welcome()
    windows = Tk()
    windows.title("DBS Banking")
    windows.iconbitmap("./Assets/logo.ico")
    windows.config(background="white")
    windows.config(bg="white")
    windows.resizable(False, False)
    frame = Frame(windows)
    frame.place(x=248,y=65)
    image = PhotoImage(file="./Assets/DBS logo.gif")
    label = Label(frame,image=image)
    label.pack()
    Label(frame,text="Username\n or accno",font=("arial",12,"bold"),fg=fg,bg=bg).place(x=0,y=331)
    Label(frame, text="Password", font=("arial", 12, "bold"), fg=fg, bg=bg).place(x=2, y=330+45+10)
    uname = Entry(frame,font=("arial",20,"bold"),bd=5)
    uname.pack()
    password = Entry(frame, font=("arial", 20, "bold"), bd=5,show="●")
    password.pack()
    Sb = Button(frame,text="Login",command=interface,fg=fg,font=("arial",10,"bold"),width=10,bg=bg)
    Sb.pack()
    def cc(r):
        Sb.config(fg="green")
    def ccs(e):
        Sb.config(fg=fg)
    Sb.bind("<Enter>",cc)
    Sb.bind("<Leave>", ccs)
    def shob(c):
        bv = uname.get()
        cbv = password.get()
        if len(bv) > 0 and len(cbv) > 0:
            Sb.invoke()
        else:
            def shobs(n):
                b = uname.get()
                if len(b) == 0:
                    enteru = Label(frame,text="Enter The username!",font=("arial",10,"bold"),fg="red")
                    enteru.pack()
                    enteru.after(650,lambda : enteru.destroy())
                    uname.focus_set()
                else:
                    interface()
            password.focus_set()
            password.bind("<Return>", shobs)
            password.bind("<Up>", shobss)
    uname.bind("<Return>",shob)
    def nope(b):
        Sb.invoke()
    password.bind("<Return>",nope)
    def shobsss(v):
        password.focus_set()
    uname.bind("<Down>", shobsss)
    def shobss(e):
        uname.focus_set()
    password.bind("<Up>", shobss)
    w = 1000
    h = 600
    screen_w = windows.winfo_screenwidth()
    screen_h = windows.winfo_screenheight()
    x = (screen_w/2) - (w/2)
    y = (screen_h/2) - (h/2)
    x = x - 75
    y = y - 25
    windows.geometry(f"{w}x{h}+{int(x)}+{int(y)}")
    def sendm():
        def dd():
            foundc = 0
            a = e1o.get()
            for i in Str:
                if i[5] == a:
                    try:
                        Label(otpf, text="----------------", font=("arial", 12, "bold"), fg="white", bg="white").grid(row=3, column=0)
                        f = random.randint(1111, 9999)
                        sender = Mail_Sender
                        foundc = 1
                        receiver = i[9]
                        idc = i[0]
                        pin = i[1]
                        accnoh = i[4]
                        password = Mail_Password
                        subject = "Otp for your account recovery!"
                        body = "DBS Bank\nYour otp is: {}\nDo not share with anyone".format(str(f))
                        message = f"""From: {sender}To: {receiver}\nSubject: {subject}\n\n{body}"""
                        server = smtplib.SMTP("smtp.gmail.com", 587)
                        server.starttls()
                        server.login(sender, password)
                        server.sendmail(sender, receiver, message)
                        server.close()
                    except socket.gaierror:
                        tkinter.messagebox.showerror("Error", "Something went wrong\nPlease Try again later")
                        windows.destroy()
                        welcome()
                    except smtplib.SMTPRecipientsRefused:
                        tkinter.messagebox.showerror("Error", "Please Check your mail ID")
                        windows.destroy()
                        welcome()
                    else:
                        e1o.config(state=DISABLED)
                        sub.config(state=DISABLED)
                        n = Label(otpf,text="Otp Sent to your registered Gmail account!",fg="green",font=("arial",22,"bold"))
                        n.grid(row=4,column=0)
                        fc = Entry(otpf, font=("arial", 22, "bold"), bd=5)
                        fc.grid(row=5,column=0)
                        def check():
                            def verify():
                                global Str
                                newps = fcd.get()
                                if len(newps) == 0:
                                    tkinter.messagebox.showerror("Invalid","Enter a Valid Password!")
                                else:
                                    for newp in Str:
                                        if newp[5] == a:
                                            subjects = "Bankalerts!"
                                            account_number = newp[4]
                                            dc = "UPDATE details SET pin = '{}' WHERE accno = '{}'".format(newps,account_number)
                                            myc.execute(dc)
                                            db.commit()
                                            myc.execute("SELECT * FROM details")
                                            Str = myc.fetchall()
                                            string = strftime('%X, %d - %b - %y')
                                            body = "DBS Bank\n-------------------\nPassword changed for your Account Number: {}\nAt: {}\nIf The Password was not changed by you, please contact The bank\nThank you\nRegards\nDBS bank".format(accnoh,string)
                                            message = f"""From: {sender}To: {receiver}\nSubject: {subjects}\n\n{body}"""
                                            server = smtplib.SMTP("smtp.gmail.com", 587)
                                            server.starttls()
                                            server.login(sender, password)
                                            server.sendmail(sender, receiver, message)
                                            server.close()
                                            tkinter.messagebox.showinfo("Success","Your Password Has been Changed Successfully")
                                            windows.destroy()
                                            welcome()
                            if fc.get() == str(f):
                                fc.config(state=DISABLED)
                                us.config(state=DISABLED)
                                tkinter.messagebox.showinfo("Verified!","Your account Has been Verified")
                                Label(otpf,text="Enter Your New Password!",fg=fg,bg=bg,font=("arial",15,"bold")).grid(row=6,column=0)
                                fcd = Entry(otpf, font=("arial", 22, "bold"), bd=5)
                                fcd.grid(row=7,column=0)
                                cvc = Button(otpf,text="Submit",font=("arial",10,"bold"),fg=fg,bg=bg,command=verify)
                                cvc.grid(row=8,column=0)
                            else:
                                tkinter.messagebox.showerror("Invalid","Invalid Otp! Exit and Try again")
                        us = Button(otpf,text="Submit",font=("arial",10,"bold"),command=check)
                        us.grid(row=6,column=0)
            if foundc == 0:
                tkinter.messagebox.showerror("Invalid", "Invalid Mobile Number")
        frame.destroy()
        otpf = Frame(windows,width=1000, height=650, background="white")
        otpf.pack()
        Label(otpf,text="Enter your Registered Mobile Number:",font=("arial",22,"bold"),fg=fg,bg=bg).grid(row=0,column=0)
        e1o = Entry(otpf,font=("arial",20,"bold"),bd=5)
        e1o.grid(row=1,column=0)
        sub = Button(otpf,text="Submit",command=dd,font=("arial",10,"bold"))
        sub.grid(row=2,column=0)
        def ddm():
            windows.destroy()
            welcome()
        Button(otpf, text="Exit", command=ddm, font=("arial", 10, "bold")).grid(row=15, column=0)
    Button(frame,text="Forget password/ Id ?",command=sendm,fg=fg,bg=bg,font=("arial",10,"bold")).place(x=50,y=420)
    def SUREs():
        if tkinter.messagebox.askyesno("Are you Sure", "Are you Sure\nDo you Want To Exit?"):
            exit(0)
    windows.protocol("WM_DELETE_WINDOW", SUREs)
    windows.mainloop()
welcome()
db.close()

