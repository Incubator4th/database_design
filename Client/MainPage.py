#MainPage
import socket
import tkinter as tk
import tkinter.ttk as ttk
import Client_login as cl

address = ('127.0.0.1', 20176)
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect(address)

default_info = {
    '姓名': None,
    '学号': None,
    '班级': None,
    '性别': 'Unknown',

}


class MainPage(tk.Frame):

    def __init__(self, userinfo=default_info, master=None):
        tk.Frame.__init__(self, master=master)
        self.master.title('Form1')
        self.master.geometry('389x339')
        self.pack()
        self.createwidgets()

    def createwidgets(self):
        self.upLabel = tk.Label(self, text='欢迎登录教务系统', font='微软雅黑').grid(row=0, column=1, stick=tk.W)

        self.top = self.winfo_toplevel()
        self.scrollBar = tk.Scrollbar(self)
        self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree_1 = ttk.Treeview(self)

        self.style = ttk.Style()

        self.TabStrip1 = ttk.Notebook(self.top)
        self.TabStrip1.place(relx=0.062, rely=0.071, relwidth=0.887, relheight=0.876)

        self.TabStrip1__Tab1 = tk.Frame(self.TabStrip1)
        self.TabStrip1__Tab1Lbl = tk.Label(self.TabStrip1__Tab1, text='Please add widgets in code.')
        self.TabStrip1__Tab1Lbl.place(relx=0.1, rely=0.5)
        self.TabStrip1.add(self.TabStrip1__Tab1, text='我的信息')

        self.TabStrip1__Tab2 = tk.Frame(self.TabStrip1)
        self.TabStrip1__Tab2Lbl = tk.Label(self.TabStrip1__Tab2, text='Please add widgets in code.')
        self.TabStrip1__Tab2Lbl.place(relx=0.1, rely=0.5)
        self.TabStrip1.add(self.TabStrip1__Tab2, text='我的选课')

        self.TabStrip1__Tab3 = tk.Frame(self.TabStrip1)
        self.TabStrip1__Tab3Lbl = tk.Label(self.TabStrip1__Tab3, text='Please add widgets in code.')
        self.TabStrip1__Tab3Lbl.place(relx=0.1, rely=0.5)
        self.TabStrip1.add(self.TabStrip1__Tab3, text='查看成绩')


if __name__ == '__main__':
    root = tk.Tk()
    root.option_add("*Font", "Consolas")
    root.resizable(False, False)
    mainpage = MainPage()
    mainpage.pack(expand=0)
    root.mainloop()
