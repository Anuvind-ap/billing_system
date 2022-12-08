import csv
import tkinter as tk
from tkinter.ttk import Combobox
root = tk.Tk()
root.title("BILLING SYSTEM")

menu = ("pizza", "burger", "pasta", "noodles")

# width x height
root.geometry("500x500")

sbillno = tk.StringVar(root)
squa = tk.IntVar(root)
scos = tk.IntVar(root)
samt = tk.IntVar(root)


y = sbillno.get()
x = y + ".csv"
f = open(x, "a")
rec = csv.writer(f, delimiter="|")
rec.writerow(['ITEM', 'COST', "QUANTITY", "AMOUNT"])


def nxtent():
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


Lbillno = tk.Label(root, text="BILL INVOICE :")
Lbillno.grid(row=1, column=1)
Ebillno = tk.Entry(root, textvariable=sbillno)
Ebillno.grid(row=1, column=2)

Litem = tk.Label(root, text="ITEM :")
Litem.grid(row=2, column=1)
Citem = Combobox(root, values=menu)
Citem.grid(row=2, column=2)
Citem.current()
Citem.bind('<<ComboboxSelected>>', setcost)

Lcost = tk.Label(root, text="COST :")
Lcost.grid(row=3, column=1)
Ecost = tk.Entry(root, textvariable=scos)
Ecost.grid(row=3, column=2)

Lqua = tk.Label(root, text="QUANTITY :")
Lqua.grid(row=4, column=1)
Equa = tk.Entry(root, textvariable=squa)
Equa.grid(row=4, column=2)
Equa.bind("<Enter>", setamt)

Lamt = tk.Label(root, text="AMOUNT :")
Lamt.grid(row=5, column=1)
Eamt = tk.Entry(root, textvariable=samt)
Eamt.grid(row=5, column=2)

Lcost = tk.Button(root, text="NEXT\nENTRY", command=nxtent)
Lcost.grid(row=6, column=1)


root.mainloop()
