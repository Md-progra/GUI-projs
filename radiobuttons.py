from tkinter import *

root = Tk()
root.title("tkkkk")



show_totals = IntVar()

Button1 = Checkbutton(root,text= "Show totals", variable = show_totals, onvalue = 1, offvalue = 0, height = 2, width = 10)
Button1.pack(side = "top",pady = 5)

v = StringVar(root, "1")
values = {"Red 1":"1","Green 2": "2","Blue 3":"3"}
for (text,value) in values.items():
    Radiobutton(root,text = text, variable = v,value =value).pack(side = "left", padx = 5)


mainloop()
