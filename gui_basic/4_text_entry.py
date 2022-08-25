from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") #가로 #세로

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "Enter letters.")

e = Entry(root, width=30)
e.pack()
e.insert(0, "Enter only a line.")

def btncmd():
    print(txt.get("1.0", END))
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()