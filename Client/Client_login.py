import tkinter as tk
import socket
from . import MainPage

address = ('127.0.0.1', 20176)

class Client_login(tk.Frame):

    def __init__(self,master=None):

        tk.Frame.__init__(self,master=master)

        self.username = tk.StringVar(value='')
        self.password = tk.StringVar(value='')

        self.pack()
        self.createwidgets()

    def createwidgets(self):

        self.upLabel = tk.Label(self, text='登录教务系统',font='微软雅黑').grid(row=0, column=1,stick=tk.W,  pady=5)

        self.userLabel = tk.Label(self, text='Username:').grid(row=1, stick=tk.W, pady=5)
        self.userEntry = tk.Entry(self, textvariable=self.username).grid(row=1, column=1, stick=tk.E)
        self.passLabel = tk.Label(self, text='Password:').grid(row=2, stick=tk.W, pady=5)
        self.passEntry = tk.Entry(self, textvariable=self.password).grid(row=2, column=1, stick=tk.E)

        self.loginButton = tk.Button(self, text='Log in', command=None).grid(row=3, stick=tk.W, pady=5)
        self.exitButton = tk.Button(self, text='Exit', command=self.quit).grid(row=3, column=1, stick=tk.E)

    def login(self):
        username = self.username.get()
        password = self.password.get()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
        if username and password:
            loginpage.destory()
            MainPage.MainPage()




if __name__ == '__main__':
    root = tk.Tk()
    root.option_add("*Font", "Consolas")
    root.resizable(False, False)

    curWidth = root.winfo_screenwidth()  # get current width
    curHeight = root.winfo_screenheight()  # get current height
    scnWidth, scnHeight = (300, 160)  # get screen width and height
    # now generate configuration information
    tmpcnf = '%dx%d+%d+%d' % (scnWidth, scnHeight,(curWidth - scnWidth) / 2, (curHeight - scnHeight ) / 2)
    print(tmpcnf)
    print(curWidth)
    print(curHeight)
    root.geometry(tmpcnf)
    loginpage = Client_login().pack(expand=0)
    root.mainloop()