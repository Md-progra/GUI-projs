
def callback(letter):
    text = f"Button {letter} clicked"
    label.config(text=text)
    # Use the text-to-speech engine to say the text
    engine.say(text)
    engine.runAndWait()

root = Tk()

label = Label()
label.grid(row=1, column=0, columnspan=26)

buttons = [0] * 26
for i in range(26):
    buttons[i] = Button(text=alphabet[i], command=lambda letter=alphabet[i]: callback(letter))
    buttons[i].grid(row=0, column=i)

mainloop()
