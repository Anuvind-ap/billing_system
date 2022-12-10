import csv
import tkinter as tk
from tkinter.ttk import Combobox
root = tk.Tk()
root.title("BILLING SYSTEM")
root.config(background="powder blue")

menu = ("pizza", "burger", "pasta", "noodles")

# width x height
root.geometry("1100x800")

sbillno = tk.StringVar(root)
squa = tk.IntVar(root)
scos = tk.IntVar(root)
samt = tk.IntVar(root)
stot = tk.IntVar(root)
sname = tk.StringVar(root)
sno = tk.IntVar(root)

Citem_val = []
squa_val = []
scos_val = []
samt_val = []
prevclick = 0


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
    if Bbillno["state"] == "disabled":
        r = [Combobox.get(Citem), scos.get(), squa.get(), samt.get()]
        rec.writerow(r)
        Citem_val.append(Citem.current())
        scos_val.append(scos.get())
        squa_val.append(squa.get())
        samt_val.append(samt.get())
    Citem.delete(0, "end")
    scos.set(0)
    squa.set(0)
    samt.set(0)


def prevent():
    if Bbillno["state"] == "disabled":
        global prevclick
        prevclick += 1
        Citem.current(Citem_val[len(Citem_val)-prevclick])
        scos.set(scos_val[len(scos_val)-prevclick])
        squa.set(squa_val[len(squa_val)-prevclick])
        samt.set(samt_val[len(samt_val)-prevclick])


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


frame = tk.Frame(root, bg="powder blue", bd=5, relief='ridge')
frame.grid()

# ----------------------------------------DEFINING FRAMES(GUI)---------------------------------------------------
Ftitle = tk.Frame(frame, height=80, width=800, bg="powder blue", bd=5, relief='ridge')
Ftitle.grid(row=0, column=0, columnspa=3)


Fdet = tk.Frame(frame, height=80, width=800, bg="powder blue", bd=5, relief='ridge')
Fdet.grid(row=1, column=0, columnspa=3)

Fbill = tk.Frame(frame, height=300, width=380, bg="powder blue", bd=5, relief='ridge')
Fbill.grid(row=2, column=0)
Fbill.grid_propagate(False)

Ftotal = tk.Frame(frame, height=95, width=380, bg="powder blue", bd=5, relief='ridge')
Ftotal.grid(row=3, column=0)
Ftotal.grid_propagate(False)

Fmenu = tk.Frame(frame, height=300, width=300, bg="powder blue", bd=5, relief='ridge')
Fmenu.grid(row=2, column=1, rowspan=2)
# ---------------------------------------------------------------------------------------------------

# -----------------------------------------TITLE-----------------------------------------------------
Ltitle = tk.Label(Ftitle, text="Customer Billing Systems", font=("Arial", 30, "bold"), bg="powder blue", fg="blue")
Ltitle.grid(row=0, column=0, columnspa=3, padx=304)
# ---------------------------------------------------------------------------------------------------

# ----------------------------------------ADDING ITEMS---------------------------------------------------
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

Bprevent = tk.Button(Fbill, text="<", command=prevent, padx=10)
Bprevent.grid(row=6, column=1)
# -------------------------------------------------------------------------------------------------------

# -----------------------------------TOTAL AMOUNT AND EXIT BUTTON----------------------------------------
Ltotal = tk.Label(Ftotal, text="TOTAL\n(incl. tax):", bg="powder blue")
Ltotal.grid(row=0, column=0)
Etotal = tk.Entry(Ftotal, textvariable=stot)
Etotal.grid(row=0, column=1, pady=5)

Bexit = tk.Button(Ftotal, text="Exit", command=Exit, pady=5, padx=5)
Bexit.grid(row=1, column=0)

Bshow = tk.Button(Ftotal, text="Generate bill", pady=5, padx=5, command=total)
Bshow.grid(row=1, column=1)
# -----------------------------------------------------------------------------------------------------

# -----------------------------------CUSTOMER DETAILS--------------------------------------------------
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
# --------------------------------------------------------------------------------------------------

root.mainloop()