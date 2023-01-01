import csv
import tkinter as tk
from tkinter.ttk import Combobox
root = tk.Tk()
root.title("BILLING SYSTEM")
root.config(background="powder blue")

menu = ("pizza", "burger", "pasta", "noodles")

# width x height
root.geometry("1020x370")
root.maxsize(1020, 370)

# ---------VARIABLES-------------
sbillno = tk.StringVar(root)
squa = tk.IntVar(root)
scos = tk.IntVar(root)
samt = tk.IntVar(root)
stot = tk.IntVar(root)
sname = tk.StringVar(root)
sno = tk.IntVar(root)
# --------------------------------

# ------BACKEND(FUNCTIONS)---------


def total():
    R = 0
    f.seek(0)
    row_read = csv.reader(f, delimiter="|")
    next(row_read)
    next(row_read)
    next(row_read)
    next(row_read)
    for row in row_read:
        R += int(row[3])
    stot.set(R)


def Exit():
    root.destroy()


def create_csv():
    if sbillno.get() != "" and sname.get() != "" and sno.get() != 0:
        y = sbillno.get()
        a = sname.get()
        b = sno.get()
        x = y + ".csv"
        global f
        f = open(x, "a+")
        global rec
        rec = csv.writer(f, delimiter="|")
        rec.writerow(["CUSTOMER NAME", a])
        rec.writerow(["CONTACT NO.", b])
        rec.writerow([])
        rec.writerow(['ITEM', 'COST', "QUANTITY", "AMOUNT"])
        Bbillno["state"] = "disabled"
    else:
        pass


def nxtent():
    if Bbillno["state"] == "disabled" and Citem.current() != -1:
        r = [Combobox.get(Citem), scos.get(), squa.get(), samt.get()]
        rec.writerow(r)
    Citem.delete(0, "end")
    scos.set(0)
    squa.set(0)
    samt.set(0)


def setamt(event):
    return samt.set(scos.get()*squa.get())


def setcost(event):
    if Citem.get() == "pizza":
        return scos.set("250")
    elif Citem.get() == "burger":
        return scos.set("100")
    elif Citem.get() == "pasta":
        return scos.set("150")
    elif Citem.get() == "noodles":
        return scos.set("220")
    else:
        pass


def receipt():
    if Bbillno["state"] == "disabled":
        textarea.delete(1.0, tk.END)
        textarea.insert(tk.END, "   THE URBAN CAFE   ")
        textarea.insert(tk.END, f"\nBILL NO. : {sbillno.get()}")
        textarea.insert(tk.END, f"\nCUSTOMER NAME : {sname.get()}")
        textarea.insert(tk.END, f"\nMOBILE NO. : {sno.get()}")
        textarea.insert(tk.END, "\n\nITEMS\tCOST\tQUANTITY\tAMOUNT")
        f.seek(0)
        read = csv.reader(f, delimiter="|")
        next(read)
        next(read)
        next(read)
        next(read)
        for i in read:
            textarea.insert(tk.END, f"\n{i[0]}\t{i[1]}\t{i[2]} \t{i[3]}")


# -------------------------------------------------------------------------------------------------------------

# ---------------------------------------------MAIN FRAME------------------------------------------------------
frame = tk.Frame(root, bg="powder blue", bd=5, relief='ridge')
frame.place(relx=0, rely=0, height=361, width=1013)
# -------------------------------------------------------------------------------------------------------------

# ----------------------------------------DEFINING FRAMES(GUI)-------------------------------------------------
Ftitle = tk.Frame(frame, bg="powder blue", bd=5, relief='ridge')
Ftitle.place(x=1, y=1, height=68, width=1000)

Fdet = tk.Frame(frame, bg="powder blue", bd=5, relief='ridge')
Fdet.place(x=1, y=71, height=45, width=1000)

Fbill = tk.Frame(frame, bg="powder blue", bd=5, relief='ridge')
Fbill.place(x=1, y=119, height=135, width=380)

Ftotal = tk.Frame(frame, bg="powder blue", bd=5, relief='ridge')
Ftotal.place(x=1, y=256, height=93, width=380)

Frec = tk.Frame(frame, bd=5, relief='ridge')
Frec.place(x=384, y=119, height=230, width=617)
# ------------------------------------------------------------------------------------------------------------

# ---------------------------------------------TITLE----------------------------------------------------------
Ltitle = tk.Label(Ftitle, text="THE URBAN CAFE", font=("Arial", 45, "bold"), bg="powder blue", fg="blue")
Ltitle.grid(row=0, column=0, columnspan=3, padx=300)
# ------------------------------------------------------------------------------------------------------------

# ---------------------------------------------ITEMS----------------------------------------------------------
Litem = tk.Label(Fbill, bg="powder blue", text="ITEM :")
Litem.grid(row=2, column=1)
Citem = Combobox(Fbill, values=menu)
Citem.grid(row=2, column=2)
Citem.current()
Citem.bind('<<ComboboxSelected>>', setcost)

Lcost = tk.Label(Fbill, bg="powder blue", text="COST :")
Lcost.grid(row=3, column=1)
Ecost = tk.Entry(Fbill, textvariable=scos)
Ecost.grid(row=3, column=2)

Lqua = tk.Label(Fbill, bg="powder blue", text="QUANTITY :")
Lqua.grid(row=4, column=1)
Equa = tk.Entry(Fbill, textvariable=squa)
Equa.grid(row=4, column=2)
Equa.bind("<Enter>", setamt)

Lamt = tk.Label(Fbill, bg="powder blue", text="AMOUNT :")
Lamt.grid(row=5, column=1)
Eamt = tk.Entry(Fbill, textvariable=samt)
Eamt.grid(row=5, column=2)

Bnxtent = tk.Button(Fbill, text="NEXT\nENTRY", command=nxtent, pady=40)
Bnxtent.grid(row=2, column=3, rowspan=4)

# -------------------------------------------------------------------------------------------------------------

# --------------------------------------TOTAL AMOUNT AND EXIT BUTTON-------------------------------------------
Ltotal = tk.Label(Ftotal, text="TOTAL\n(incl. tax):", bg="powder blue")
Ltotal.grid(row=0, column=0)
Etotal = tk.Entry(Ftotal, textvariable=stot)
Etotal.grid(row=0, column=1, pady=5)

Bexit = tk.Button(Ftotal, text="Exit", command=Exit, pady=5, padx=5)
Bexit.grid(row=1, column=0)

Bshow = tk.Button(Ftotal, text="Get Total", pady=5, padx=5, command=lambda: [total(), receipt()])
Bshow.grid(row=1, column=1)
# ----------------------------------------------------------------------------------------------------------

# ------------------------------------------CUSTOMER DETAILS------------------------------------------------
Lcname = tk.Label(Fdet, text="Customer Name :", bg="powder blue")
Lcname.grid(row=0, column=0)
Ecname = tk.Entry(Fdet, textvariable=sname)
Ecname.grid(row=0, column=1)

Lcno = tk.Label(Fdet, text="Contact No :", bg="powder blue")
Lcno.grid(row=0, column=3)
Ecno = tk.Entry(Fdet, textvariable=sno)
Ecno.grid(row=0, column=4)


Lbillno = tk.Label(Fdet, bg="powder blue", text="BILL INVOICE :")
Lbillno.grid(row=0, column=5)
Ebillno = tk.Entry(Fdet, textvariable=sbillno)
Ebillno.grid(row=0, column=6)
Bbillno = tk.Button(Fdet, text="confirm", padx=18, command=create_csv)
Bbillno.grid(row=0, column=7)
# ---------------------------------------------------------------------------------------------------------

# ----------------------------------------------RECEIPT----------------------------------------------------
Ldish = tk.Label(Frec, text="RECEIPT")
Ldish.pack(side="top")
scrol = tk.Scrollbar(Frec, orient="vertical")
scrol.pack(side="right", fill="y")
textarea = tk.Text(Frec, font="arial 15", yscrollcommand=scrol.set)
textarea.pack(fill="both")
scrol.config(command=textarea.yview)
# ----------------------------------------------------------------------------------------------------------

root.mainloop()
