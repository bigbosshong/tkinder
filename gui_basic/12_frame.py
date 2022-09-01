from tkinter import *
from tkinter.ttk import Labelframe

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") #가로 #세로

Label(root, text='메뉴를 선택해주세요').pack(side='top')
Button(root, text='주문하기').pack(side='bottom')

# 메뉴 프레임
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side='left', fill='both', expand=True)

Button(frame_burger, text='햄버거').pack()
Button(frame_burger, text='치즈햄버거').pack()
Button(frame_burger, text='치킨햄버거').pack()

# 음료 프레임
frame_drink = Labelframe(root, text='음료')
frame_drink.pack(side='right', fill='both', expand=True)

Button(frame_drink, text='콜라').pack()
Button(frame_drink, text='사이다').pack()

root.mainloop()