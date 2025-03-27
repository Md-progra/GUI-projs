import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Stickman ")

# Create a canvas
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Draw the stickman body
canvas.create_oval(150, 50, 250, 150, fill="green")  # Head
canvas.create_line(200, 150, 200, 300, fill="black", width=7)  # Body
canvas.create_line(200, 200, 150, 250, fill="black", width=3)  # Left arm
canvas.create_line(200, 200, 250, 250, fill="black", width=3)  # Right arm
canvas.create_line(200, 300, 150, 350, fill="black", width=3)  # Left leg
canvas.create_line(200, 300, 250, 350, fill="black", width=3)  # Right leg

# Run the Tkinter event loop
root.mainloop()
