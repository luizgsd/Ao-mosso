from tkinter import *
from tkinter import ttk
import timeChecker as tc

window = Tk()
window.title('Ao mosso')
window.geometry("300x250")

setLabel = ttk.Label(text="Será que ja ta podendo ao mossar?")
setLabel.place(relx=0.5, rely=0.4, anchor=CENTER)


def changeLabel():
    if tc.checkLunchtime() == True:
        setLabel.config(text="Já ta podendo ao mossar :D")
    else:
        setLabel.config(text="Não ta podendo ao mossar :(")


setButton = ttk.Button(text="Checar o horário", command=changeLabel)
setButton.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()