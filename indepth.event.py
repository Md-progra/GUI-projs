import tkinter as tk


def draw_stickman(canvas, x, y):
    # Draw head
    canvas.create_oval(x - 20, y - 60, x + 20, y - 20, fill="black")
    # Draw body
    canvas.create_line(x, y - 20, x, y + 40, width=3)
    # Draw arms
    canvas.create_line(x, y, x - 30, y - 30, width=3)
    canvas.create_line(x, y, x + 30, y - 30, width=3)
    # Draw legs
    canvas.create_line(x, y + 40, x - 20, y + 70, width=3)
    canvas.create_line(x, y + 40, x + 20, y + 70, width=3)


def left_click(event):
    x, y = event.x, event.y
    print(f"Coordinates: ({x}, {y})")
    draw_stickman(canvas, x, y)


def right_click(event):
    x, y = event.x, event.y
    canvas.create_rectangle(x - 25, y - 25, x + 25, y + 25, fill="blue", outline="black")

def scroll_click(event):
    x,y = event.x,event.y
    canvas.create_rectangle(x-20,y-20,x +20, y+20, fill = "green",outline = "orange")


# Main application window
root = tk.Tk()
root.title("Mouse Event ")

canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Bind left-click and right-click events
canvas.bind("<Button-1>", left_click)  # Left mouse button
canvas.bind("<Button-3>", right_click)
canvas.bind("<Button-2>",scroll_click)

root.mainloop()
