#MainPage

import tkinter as tk
import Client_login as cl

sock=cl.sock

class MainPage(tk.Frame):

    def __init__(self, master=None,userinfo):
        tk.Frame.__init__(self, master=master)
        self.pack()
        self.createwidgets()

    def createwidgets(self):
        self.upLabel = tk.Label(self, text='登录教务系统', font='微软雅黑').grid(row=0, column=1, stick=tk.W, pady=5)