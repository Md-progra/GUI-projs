from tkinter import *
import pyttsx3
import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

engine = pyttsx3.init()

def announce_letter():
    global target_letter
    target_letter = random.choice(alphabet)
    global name
    name = input("Enter your name: ")
    begin = f"Welcome {name}!"
    engine.say(begin)
    announcement = f"Click the letter {target_letter}"
    label.config(text=announcement)
    engine.say(announcement)
    engine.runAndWait()


def callback(letter):
    if letter == target_letter:
        message = f"Correct {name}! You clicked {letter}."
        engine.say(message)
        label.config(text=message)
    else:
        message = f"Wrong! {name} You clicked {letter}. Try again."
        engine.say(message)
        label.config(text=message)
    engine.runAndWait()


root = Tk()


label = Label()
label.grid(row=1, column=0, columnspan=26)


buttons = [0] * 26
for i in range(26):
    buttons[i] = Button(text=alphabet[i], command=lambda letter=alphabet[i]: callback(letter))
    buttons[i].grid(row=0, column=i)

# Randomly announce a letter when the program starts
announce_letter()

mainloop()
