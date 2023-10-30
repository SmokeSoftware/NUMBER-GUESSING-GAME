import tkinter as yarrak
from tkinter import *
from tkinter import messagebox
import random

game = yarrak.Tk()

pc_sayisi = random.randint(1,100)

game.title("NUMBER GUESSİNG GAME")
game.minsize(400,200)
game.maxsize(400,200)

def SAYIMI_AL_K_ET():
    veri = int(gamer_input.get())

    if veri > 100:
        msg = Tk()
        msg.withdraw()
        messagebox.showwarning("WARNİNG!","PLEASE ENTER A NUMBER BETWEEN 1 TO 100")
        return 0

    if veri <= 0:
        msg = Tk()
        msg.withdraw()
        messagebox.showwarning("WARNİNG!","PLEASE ENTER A NUMBER BETWEEN 1 TO 100")
        return 0

    aradaki_fark = pc_sayisi - veri

    if aradaki_fark < 0:
        aradaki_fark *= -1

    if aradaki_fark == 0:
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON","YOU RİGHT :D")

    elif 1 <= aradaki_fark < 5:
        msg = Tk()
        msg.withdraw()
        messagebox.showerror("İMFORMATİON","SO CLOSE :()")

    elif 5 <= aradaki_fark <= 10:
        msg = Tk()
        msg.withdraw()
        messagebox.showerror("İMFORMATİON","CLOSE :|")

    else:
        msg = Tk()
        msg.withdraw()
        messagebox.showerror("İMFORMATİON","TOO FAR :(")


gamer_info = yarrak.Label(game,text = "ENTER\n NUMBER:",fg = "black",bg = "lime",font = "Arial 15")
gamer_info.place(width = 100,height = 100,x = 0,y = 0)

gamer_input = yarrak.Entry(game,fg = "lime",bg = "black",font = "Arial 50")
gamer_input.place(width = 300,height = 100,x = 100,y = 0)

gamer_okay_button = yarrak.Button(game,text = "CHECK",fg = "white",bg = "blue",font = "Arial 30",activebackground = "blue",activeforeground = "white",command = SAYIMI_AL_K_ET)
gamer_okay_button.place(width = 400,height = 100,x = 0, y = 100)

game.mainloop()

    
