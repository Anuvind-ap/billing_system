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


def total():
    R = 0
    f.seek(0)
    row_read = csv.reader(f, delimiter="|")
    next(row_read)
    for row in row_read:
        R += int(row[3])
    stot.set(R)


def Exit():
    root.destroy()


def create_csv():
    if sbillno.get() != "":
        y = sbillno.get()
        x = y + ".csv"
        global f
        f = open(x, "a+")
        global rec
        rec = csv.writer(f, delimiter="|")
        rec.writerow(['ITEM', 'COST', "QUANTITY", "AMOUNT"])
        Bbillno["state"] = "disabled"
    else:
        pass


def nxtent():
    if Bbillno["state"] == "disabled":
        r = [Combobox.get(Citem), scos.get(), squa.get(), samt.get()]
        rec.writerow(r)
    squa.set(0)
    scos.set(0)
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


frame = tk.Frame(root, bg="powder blue", bd=5, relief='ridge')
frame.grid()

Ftitle = tk.Frame(frame, height=80, width=1036, bg="powder blue", bd=5, relief='ridge')
Ftitle.grid(row=0, column=0, columnspa=3)

Fdet = tk.Frame(frame, height=300, width=300, bg="powder blue", bd=5, relief='ridge')
Fdet.grid(row=1, column=0)

Fbill = tk.Frame(frame, height=300, width=300, bg="powder blue", bd=5, relief='ridge')
Fbill.grid(row=1, column=1)
Fbill1 = tk.Frame(Fbill, height=195, width=290, bg="powder blue", bd=5, relief='ridge')
Fbill1.grid(row=0, column=0)
Fbill2 = tk.Frame(Fbill, height=95, width=290, bg="powder blue", bd=5, relief='ridge')
Fbill2.grid(row=2, column=0)

Fdis = tk.Frame(frame, height=300, width=300, bg="powder blue", bd=5, relief='ridge')
Fdis.grid(row=1, column=2)

Lbillno = tk.Label(Fbill1, bg="powder blue", text="BILL INVOICE :")
Lbillno.grid(row=1, column=1)
Ebillno = tk.Entry(Fbill1, textvariable=sbillno)
Ebillno.grid(row=1, column=2)
Bbillno = tk.Button(Fbill1, text="confirm", padx=18, command=create_csv)
Bbillno.grid(row=1, column=3)

Litem = tk.Label(Fbill1, bg="powder blue", text="ITEM :")
Litem.grid(row=2, column=1)
Citem = Combobox(Fbill1, values=menu)
Citem.grid(row=2, column=2)
Citem.current()
Citem.bind('<<ComboboxSelected>>', setcost)

Lcost = tk.Label(Fbill1, bg="powder blue", text="COST :")
Lcost.grid(row=3, column=1)
Ecost = tk.Entry(Fbill1, textvariable=scos)
Ecost.grid(row=3, column=2)

Lqua = tk.Label(Fbill1, bg="powder blue", text="QUANTITY :")
Lqua.grid(row=4, column=1)
Equa = tk.Entry(Fbill1, textvariable=squa)
Equa.grid(row=4, column=2)
Equa.bind("<Enter>", setamt)

Lamt = tk.Label(Fbill1, bg="powder blue", text="AMOUNT :")
Lamt.grid(row=5, column=1)
Eamt = tk.Entry(Fbill1, textvariable=samt)
Eamt.grid(row=5, column=2)

Bnxtent = tk.Button(Fbill1, text="NEXT\nENTRY", command=nxtent, pady=40, padx=18)
Bnxtent.grid(row=2, column=3, rowspan=4)

Ltotal = tk.Label(Fbill2, text="Total :", bg="powder blue")
Ltotal.grid(row=0, column=0)
Etotal = tk.Entry(Fbill2, textvariable=stot)
Etotal.grid(row=0, column=1)

Bexit = tk.Button(Fbill2, text="Exit", command=Exit, pady=5, padx=5)
Bexit.grid(row=1, column=0)

Bshow = tk.Button(Fbill2, text="Generate bill", pady=5, padx=5, command=total)
Bshow.grid(row=1, column=1)

root.mainloop()
