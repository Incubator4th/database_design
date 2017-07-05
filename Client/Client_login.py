import tkinter as tk
import socket
import MainPage

address = ('127.0.0.1', 20176)

global login_mode

class Client_login(tk.Frame):

    def __init__(self,master=None):
        tk.Frame.__init__(self,master=master)

        self.username = tk.StringVar(value='')
        self.password = tk.StringVar(value='')
        self.radVar = tk.IntVar()

        self.pack()
        self.createwidgets()

    def createwidgets(self):

        self.upLabel = tk.Label(self, text='登录教务系统', font='微软雅黑').grid(row=0, column=1,stick=tk.W,  pady=5)

        self.rad1 = tk.Radiobutton(text='学生', font='微软雅黑', variable=self.radVar, value=1,command=self.radcall).pack(side=tk.LEFT, padx=15)
        self.rad2 = tk.Radiobutton(text='教师', font='微软雅黑', variable=self.radVar, value=2, command=self.radcall).pack(side=tk.LEFT, padx=15)
        self.rad3 = tk.Radiobutton(text='管理员', font='微软雅黑', variable=self.radVar, value=3, command=self.radcall).pack(side=tk.LEFT, padx=15)

        self.userLabel = tk.Label(self, text='Username:').grid(row=1, stick=tk.W, pady=5)
        self.userEntry = tk.Entry(self, textvariable=self.username).grid(row=1, column=1, stick=tk.E)
        self.passLabel = tk.Label(self, text='Password:').grid(row=2, stick=tk.W, pady=5)
        self.passEntry = tk.Entry(self, textvariable=self.password).grid(row=2, column=1, stick=tk.E)

        self.loginButton = tk.Button(self, text='Log in', command=self.login).grid(row=3, stick=tk.W, pady=5)
        self.exitButton = tk.Button(self, text='Exit', command=self.quit).grid(row=3, column=1, stick=tk.E)

    def login(self):
        username = self.username.get()
        password = self.password.get()
        data = {
            'username': username,
            'password': password,
            'login_mode': login_mode
        }
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(address)
        bytedata = repr(data).encode()
        sock.send(bytedata)
        logininfo = sock.recv(1024)
        logininfo = logininfo.decode()
        if 'success' in logininfo:
            userinfo = sock.recv(1024)
            userinfo = repr(userinfo.decode())
            self.destory()
            m = MainPage.MainPage(userinfo=userinfo)
            m.mainloop()
        elif 'Error' in logininfo:
            pass#账号或密码错误
        else:
            pass#连接错误

    def radcall(self):
        login_mode = self.radVar.get()



if __name__ == '__main__':
    root = tk.Tk()
    root.option_add("*Font", "Consolas")
    root.resizable(False, False)
    curWidth = root.winfo_screenwidth()  # get current width
    curHeight = root.winfo_screenheight()  # get current height
    scnWidth, scnHeight = (300, 200)  # get screen width and height
    tmpcnf = '%dx%d+%d+%d' % (scnWidth, scnHeight, (curWidth - scnWidth) / 2, (curHeight - scnHeight ) / 2)
    print(tmpcnf)
    print(curWidth)
    print(curHeight)
    root.geometry(tmpcnf)
    loginpage = Client_login()
    loginpage.pack(expand=0)
    root.mainloop()
