import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import os
import pygubu
import PIL

class App():
    def __init__(self,master):
        #master für die app festlegen
        self.master = master
        #builder erstellen
        self.builder = builder = pygubu.Builder()
        #ui quelle laden
        builder.add_from_file('gui.ui')
        #Ein widget erstellen, der master wird als parent benutzt
        self.mainwindow = builder.get_object('mainwindow', self.master)
        #andere Objekte vom Pygubu builder holen
        self.answer = builder.get_object('answer',  self.master)

        #callbacks
        builder.connect_callbacks(self)

    def submit_button_click(self):
        self.request = self.builder.tkvariables['request'].get()
        if self.request == 'Hello There!':
            self.img = tk.PhotoImage(file = 'kenobi.gif')
            self.answer.configure(image = self.img)
            self.answer.image = self.img
        else:
            messagebox.showinfo('Error','Only a Sith deals in absolutes!')

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    #main loop der tk app ausführen
    root.mainloop()

