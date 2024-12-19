import tkinter as tk
from tkinter import messagebox
from tkinter import DISABLED, NORMAL, CENTER
from random import randint
import logsignbysam as logsignx
import algobysam as algox

x_close = False

def mainscreen():
    main.withdraw()
    a = tk.Toplevel()
    a.title("Civilisation Simulation")

    def di_contingency():
        frame.destroy()
        a.destroy()
        global x_close
        x_close = True
        if x_close == True:
            mainchange()
            main.deiconify()
    
    a.protocol("WM_DELETE_WINDOW",di_contingency)
    a.geometry("500x500")
    frame = tk.Frame(a)
    frame.pack(fill="both", expand=True)

    global var_act, var1_act, var2_act,var3_act,var4_act,var5_act
    var = tk.IntVar()
    var_act = True
    var1 = tk.IntVar()
    var1_act = True
    var2 = tk.IntVar()
    var2_act = True
    var3 = tk.IntVar()
    var3_act = True
    var4 = tk.IntVar()
    var4_act = True
    var5 = tk.IntVar()
    var5_act = True

    tk.Label(frame, text="\nCIVILISATION SIMULATOR").place(relx = 0.5, rely = 0, anchor = CENTER)
    tk.Label(frame, text="Slide the variables to create scenario").place(relx = 0.5, rely = 0.1, anchor = CENTER)
    def varinfo():
        with open("varinfo.txt","r") as f:
            varinfotext = f.read()
        messagebox.showinfo("Know your varibale!",varinfotext)
    tk.Button(frame, text = "Know your variables", command = varinfo).place(relx = 0.5, rely = 0.2, anchor = CENTER)

    def dis():
        global var_act, var1_act, var2_act,var3_act,var4_act,var5_act
        if var.get() == 1:
            harm.config(state = DISABLED)
            var_act = False
        elif var.get() == 0:
            harm.config(state = NORMAL)
            var_act = True
        if var1.get() == 1:
            cult.config(state = DISABLED)
            var1_act = False
        elif var1.get() == 0:
            cult.config(state = NORMAL)
            var1_act = True
        if var2.get() == 1:
            inno.config(state = DISABLED)
            var2_act = False
        elif var2.get() == 0:
            inno.config(state = NORMAL)
            var2_act = True
        if var3.get() == 1:
            mil.config(state = DISABLED)
            var3_act = False
        elif var3.get() == 0:
            mil.config(state = NORMAL)
            var3_act = True
        if var4.get() == 1:
            gov.config(state = DISABLED)
            var4_act = False
        elif var4.get() == 0:
            gov.config(state = NORMAL)
            var4_act = True
        if var5.get() == 1:
            eco.config(state = DISABLED)
            var5_act = False
        elif var5.get() == 0:
            eco.config(state = NORMAL)
            var5_act = True

    harm = tk.Scale(frame, from_=0, to=100, orient="horizontal", label="Hamrony")
    cult = tk.Scale(frame, from_=0, to=100, orient="horizontal", label="Culture")
    inno = tk.Scale(frame, from_=0, to=100, orient="horizontal", label="Innovation")
    mil = tk.Scale(frame, from_=0, to=100, orient="horizontal", label="Military")
    gov = tk.Scale(frame, from_=0, to=100, orient="horizontal", label="Government")
    eco = tk.Scale(frame, from_=0, to=100, orient="horizontal", label="Economics")

    r1 = tk.Checkbutton(frame, text="Randomize Harmony", variable = var, command = dis)
    r2 = tk.Checkbutton(frame, text="Randomize Culture", variable = var1, command = dis)
    r3 = tk.Checkbutton(frame, text="Randomize Innovation", variable = var2, command = dis)
    r4 = tk.Checkbutton(frame, text="Randomize Military", variable = var3, command = dis)
    r5 = tk.Checkbutton(frame, text="Randomize Government", variable = var4, command = dis)
    r6 = tk.Checkbutton(frame, text="Randomize Economics", variable = var5, command = dis)

    harm.place(relx = 0.2, rely = 0.3, anchor = CENTER)
    r1.place(relx = 0.2, rely = 0.4, anchor = CENTER)

    cult.place(relx = 0.2, rely = 0.6, anchor = CENTER)
    r2.place(relx = 0.2, rely = 0.7, anchor = CENTER)

    inno.place(relx = 0.5, rely = 0.3, anchor = CENTER)
    r3.place(relx = 0.5, rely = 0.4, anchor = CENTER)

    mil.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    r4.place(relx = 0.5, rely = 0.7, anchor = CENTER)

    gov.place(relx = 0.8, rely = 0.3, anchor = CENTER)
    r5.place(relx = 0.8, rely = 0.4, anchor = CENTER)

    eco.place(relx = 0.8, rely = 0.6, anchor = CENTER)
    r6.place(relx = 0.8, rely = 0.7, anchor = CENTER)
    
    def deiconify():
        frame.destroy()
        a.destroy()
        mainchange()
        main.deiconify()
    
    def print_var():
        if var_act == True:
            harmony = harm.get()
        else:
            harmony = randint(0,100)
        if var1_act == True:
            culture = cult.get()
        else:
            culture = randint(0,100)
        if var2_act == True:
            innovation = inno.get()
        else:
            innovation = randint(0,100)
        if var3_act == True:
            military = mil.get()
        else:
            military = randint(0,100)
        if var4_act == True:
            govern = gov.get()
        else:
            govern = randint(0,100)
        if var5_act == True:
            economics = eco.get()
        else:
            economics = randint(0,100)
        messagebox.showinfo("Result", algox.civscorex(harmony,culture,innovation,military,govern,economics))
        

    rad1 = tk.Button(frame, text = "Show Result", command = print_var).place(relx = 0.4, rely = 0.9, anchor = CENTER)
    rad2 = tk.Button(frame, text = "Close", command = deiconify).place(relx = 0.6, rely = 0.9, anchor = CENTER)


main = tk.Tk()
main.title("History Simulation - Account Login")
main.geometry("400x400")

def mainchange():
    for widget in main.winfo_children():
        widget.destroy()
    main.title("History Simulation")
    main.geometry("300x300")
    l1 = tk.Label(main, text=f"Welcome, History Nerd!")
    l1.place(relx = 0.5, rely = 0.3, anchor = CENTER)
    b2 = tk.Button(main, text="Play again!", command = mainscreen)
    b2.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    b1 = tk.Button(main, text="Exit", command = main.destroy)
    b1.place(relx = 0.5, rely = 0.6, anchor = CENTER)

def sign():
    main.withdraw()
    a = tk.Toplevel()
    a.title("Sign in")

    def di_contingency():
        frame.destroy()
        a.destroy()
        global x_close
        x_close = True
        if x_close == True:
            main.deiconify()
    
    a.protocol("WM_DELETE_WINDOW",di_contingency)
    a.geometry("230x360")
    
    signchecker = False
    vars_list = []
    entry = {}

    tk.Label(a,text="Sign-up\n").pack()
    
    if bool(logsignx.online) == True:
        for i in ["Username", "Password", "Email"]:
            frame = tk.Frame(a)
            frame.pack()
            tk.Label(frame,text=i).pack()
            var = tk.IntVar(value=0)
            vars_list.append(var)
            entry[i] = tk.StringVar()
            if i == "Password":
                entry_show = "*"
            else:
                entry_show = ""
            tk.Entry(frame, show=entry_show, textvariable = entry[i]).pack()
            tk.Label(frame,text="\n").pack()

        warn = tk.Label(a,text="")
        warn.pack()
        
        def signbutx():
            logsignobj = logsignx.signin()
            nonlocal signchecker
            signchecker = logsignobj.sign(entry["Username"].get(), entry["Password"].get(), entry["Email"].get())
            if signchecker == True:
                signbut.config(state = DISABLED)
                warn.config(text = "Sign In Successful", fg="green")
                radx.config(text = "Continue")
            elif signchecker == False:
                warn.config(text = "Email already in use", fg="red")
            else:
                warn.config(text = "Avoid: Empty field/Wrong format", fg="red")
        def deiconify():
            frame.destroy()
            a.destroy()
            if signchecker == True:
                mainscreen()
            else:
                main.deiconify()
        radx = tk.Button(a, text = "Back", command = deiconify)
        radx.place(relx = 0.2, rely = 0.9, anchor = CENTER)
        signbut = tk.Button(a, text = "Signin", command = signbutx)
        signbut.place(relx = 0.8, rely = 0.9, anchor = CENTER)
    


def log():
    main.withdraw()
    a = tk.Toplevel()
    a.title("Login")

    def di_contingency():
        frame.destroy()
        a.destroy()
        global x_close
        x_close = True
        if x_close == True:
            main.deiconify()
    
    a.protocol("WM_DELETE_WINDOW",di_contingency)
    a.geometry("230x330")
    
    logchecker = False
    vars_list = []
    entry = {}

    tk.Label(a,text="Login\n").pack()

    if bool(logsignx.online) == True:
        for i in ["Username", "Password", "Email"]:
            frame = tk.Frame(a)
            frame.pack()
            tk.Label(frame,text=i).pack()
            var = tk.IntVar(value=0)
            vars_list.append(var)
            entry[i] = tk.StringVar()
            if i == "Password":
                entry_show = "*"
            else:
                entry_show = ""
            tk.Entry(frame, show=entry_show, textvariable = entry[i]).pack()
            tk.Label(frame,text="\n").pack()

        warn = tk.Label(a,text="")
        warn.pack()
        
        def logbutx():
            logsignobj = logsignx.login()
            nonlocal logchecker
            logchecker = logsignobj.log(entry["Username"].get(), entry["Password"].get(), entry["Email"].get())
            if logchecker == True:
                logbut.config(state = DISABLED)
                warn.config(text = "Login Successful", fg="green")
                radx.config(text = "Continue")
            elif logchecker == False:
                warn.config(text = "User not found", fg="red")
            else:
                warn.config(text = "Avoid: Empty field/Wrong format", fg="red")
        def deiconify():
            frame.destroy()
            a.destroy()
            if logchecker == True:
                mainscreen()
            else:
                main.deiconify()
        radx = tk.Button(a, text = "Back", command = deiconify)
        radx.place(relx = 0.2, rely = 0.9, anchor = CENTER)
        logbut = tk.Button(a, text = "Login", command = logbutx)
        logbut.place(relx = 0.8, rely = 0.9, anchor = CENTER)

tk.Label(main, text = "Welcome to the Civilisation simulator!\nPlease signup/Login to continue!").place(relx = 0.5, rely = 0.2, anchor = CENTER)
b1 = tk.Button(main, text= "Signup", command = sign)
b1.place(relx = 0.5, rely = 0.4, anchor = CENTER)
b2 = tk.Button(main, text= "Login", command = log)
b2.place(relx = 0.5, rely = 0.6, anchor = CENTER)

main.mainloop()
