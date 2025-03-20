from tkinter import *

# Function to calculate the area
def calculate_area():
        num_width = eval(entry_width.get())
        num_length = eval(entry_length.get())
        area = num_width * num_length
        result_label.config(text=f"Area of rectangle: {area}")

root = Tk()


length_label = Label(root, text="Length:")
length_label.grid(row=0, column=0)

entry_length = Entry(root)
entry_length.grid(row=0, column=1)

width_label = Label(root, text="Width:")
width_label.grid(row=1, column=0)

entry_width = Entry(root)
entry_width.grid(row=1, column=1)

# Button to calculate area
calculate_button = Button(root, text="Calculate Area", command=calculate_area)
calculate_button.grid(row=2, column=0, columnspan=1)

# Label to display result
result_label = Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

# Run the main loop
root.mainloop()



