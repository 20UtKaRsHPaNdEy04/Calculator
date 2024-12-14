from tkinter import *

def click(event):
    global screenValue
    text = event.widget.cget("text")
    handle_input(text)
    
def keypress(event):
    global screenValue
    handle_input(event.char)

def handle_input(input_text):
    global screenValue
    if input_text in "0123456789+-*/.00":
        screenValue.set(screenValue.get() + input_text)
    elif input_text == "%":
        try:
            result = eval(screenValue.get()) / 100
            screenValue.set(str(result))
        except Exception:
            screenValue.set("Error")
    elif input_text == "=" or input_text == "\r":   # "\r" is the Enter Key
        try:
            result = eval(screenValue.get())
            screenValue.set(result)
        except Exception:
            screenValue.set("Error")
    elif input_text.lower() == "c":    # "\x08" is Backspace
        screenValue.set("")
    elif input_text == "\x08":  # Backspace key (remove last character)
        result = screenValue.get()
        screenValue.set(result[:-1])

# Creating the main window
root = Tk()
root.title("Calculator")
root.iconbitmap("E:/STUDY/Python/TKINTER MODULE/Calculator/calc.ico")
root.geometry("400x570")
root.config(background="#204051")
# root.resizable(False, False)


# creating the Screen to show calculations
screenValue = StringVar()
screen = Entry(root, textvar=screenValue, font="poppins 30 bold", justify=LEFT, bg="white", fg="black", highlightbackground="black",highlightcolor="white", highlightthickness=3, bd=1, insertbackground="black")
screen.pack(fill=BOTH, ipady=10, pady=10, )

# Button Layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "+"],
    ["%", "0", ".", "-"],
    ["C","00" ,"="]
]

# Creating Buttons using For loop
for row in buttons:
    button_row = Frame(root, background="#3B3B3B")
    button_row.pack(fill=BOTH, expand=True)
    for button_text in row:
        if button_text == "=":
            button = Button(button_row, text=button_text, font='poppins 18 bold', height=2, width=12, bd=5 ,background="#a17af6")
            button.pack(side=LEFT,fill=BOTH, expand=True,  padx=5, pady=5)
            button.bind("<Button-1>", click)
        else:
            button = Button(button_row, text=button_text, font='poppins 19 bold', height=2, width=5, background="#3B3B3B", foreground="white", highlightbackground="#204051",bd=5, highlightcolor="#204051")
            button.pack(side=LEFT,fill=BOTH, expand=True,  padx=5, pady=5)
            button.bind("<Button-1>", click)

# Bind keyboard keys to the application
root.bind("<Key>", keypress)

# Run the Tkinter main loop
root.mainloop()