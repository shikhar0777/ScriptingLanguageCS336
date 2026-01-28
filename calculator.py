import tkinter as tk

def press(key):
    display.set(display.get() + str(key))

def calculate():
    try:
        display.set(str(eval(display.get())))
    except:
        display.set("Error")

def clear():
    display.set("")

def create_button(text, cmd, r, c):
    tk.Button(root, text=text, width=5, height=2, command=cmd).grid(row=r, column=c)

root = tk.Tk()
root.title("Calculator")

display = tk.StringVar()
tk.Entry(root, textvariable=display, font=("Arial", 18), justify="right").grid(row=0, column=0, columnspan=4)

keys = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3)
]

for k,r,c in keys:
    if k == "=":
        create_button(k, calculate, r, c)
    else:
        create_button(k, lambda x=k: press(x), r, c)

tk.Button(root, text="C", width=22, height=2, command=clear).grid(row=5, column=0, columnspan=4)

root.mainloop()
