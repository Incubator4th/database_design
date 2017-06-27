#MainPage

import tkinter as tk



class MainPage(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master=master)
        self.pack()
        self.createwidgets()

    def createwidgets(self):
        pass