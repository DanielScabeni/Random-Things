import random
from tkinter import *

class Dados(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.label = Label(master, font=("times", 100))
        botao = Button(master, text="Rolar os dados", command=self.rolar)
        botao.place(x=200, y=0)
    
    def rolar(self):
        simbolos =  ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
        self.label.config(text=f"{random.choice(simbolos)}{random.choice(simbolos)}{random.choice(simbolos)}")
        self.label.pack()

if __name__ == "__main__":
    root = Tk()
    root.title("clayton, Tole os DAdos")
    root.geometry("500x400")
    Dados(root)
    root.mainloop()



























































































































































































































































































































































































































































































































































