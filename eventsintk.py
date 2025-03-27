import tkinter as tk

root = tk.Tk()

num1_var = tk.IntVar()
num2_var = tk.IntVar()
# summation = tk.IntVar()

def receive():
    num1 = num1_var.get()
    num2 = num2_var.get()
    global summation
    print("Input 1 is " + str(num1))
    print("Input 2 is " + str(num2))
    summation = num1 + num2
    print(f"Their sum is {num1}+{num2} = {summation} ")
    num1_var.set(0)
    num2_var.set(0)


def move_focus(event):
    num2_entry.focus_set()


num1_label = tk.Label(root, text="num1")
num1_label.pack()

num1_entry = tk.Entry(root, textvariable=num1_var)
num1_entry.pack()
num1_entry.bind('<Return>', move_focus)

num2_label = tk.Label(root, text="num2")
num2_label.pack()

num2_entry = tk.Entry(root, textvariable=num2_var)
num2_entry.pack()

# summation_label = tk.Label(root, text = "summation")
# summation_label.pack()
# summation_entry = tk.Entry(root, textvariable=summation)
# summation_entry.pack()

submit_button = tk.Button(root, text="Ok", command=receive)
submit_button.pack()


root.mainloop()
