from tkinter import *
from tkinter import ttk
import timeChecker as tc
from PIL import ImageTk, Image

window = Tk()
window.title('Ao mosso')
window.geometry("540x360")
window.resizable(False, False)

background = ImageTk.PhotoImage(Image.open("img/background.jpg"))
backgroundLabel = ttk.Label(image=background)
backgroundLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

setLabel = ttk.Label(text="Será que ja ta podendo ao mossar?")
setLabel.place(relx=0.3, rely=0.4, anchor=CENTER)


def changeLabel():
    if tc.checkLunchtime() == True:
        setLabel.config(text="Já ta podendo ao mossar :D")
    else:
        setLabel.config(text="Não ta podendo ao mossar :(")


setButton = ttk.Button(text="Checar o horário", command=changeLabel)
setButton.place(relx=0.3, rely=0.5, anchor=CENTER)

window.mainloop()
