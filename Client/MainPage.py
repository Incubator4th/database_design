#MainPage
import socket
import tkinter as tk
import tkinter.ttk as ttk
import Client_login as cl

address = ('127.0.0.1', 20176)
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect(address)
trans_dict = {
    'id': '学号',
    'name': '姓名',
    'classes': '班级',
    'sex': '性别'
}

default_info = {
    '姓名': None,
    '学号': None,
    '班级': None,
    '性别': 'Unknown',

}
info_column=('id','name','sex','classes')





def find_db(sql):
    import pymssql
    conn = pymssql.connect(
        host='127.0.0.1',
        user='Administator',
        password='',
        database='Wangchengzhang04Mis',
        charset="utf8")
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    return result



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


        self.style = ttk.Style()

        self.TabStrip1 = ttk.Notebook(self.top)
        self.TabStrip1.place(relx=0.062, rely=0.071, relwidth=0.887, relheight=0.876)

        self.TabStrip1__Tab1 = tk.Frame(self.TabStrip1)

        self.subFrame = tk.Frame(self.TabStrip1__Tab1)
        self.subFrame.pack(side=tk.TOP)

        self.buttonwidth = 8

        self.insertButton = tk.Button(self.subFrame, text='插入数据', font='微软雅黑', width=self.buttonwidth, command=lambda : change_db(mode='insert'))
        self.insertButton.pack(anchor=tk.N, side=tk.LEFT, padx=10, pady=2)
        self.updateButton = tk.Button(self.subFrame, text='更新数据', font='微软雅黑', width=self.buttonwidth, command=lambda : change_db(mode='update'))
        self.updateButton.pack(anchor=tk.N, side=tk.LEFT, padx=10, pady=2)
        self.deleteButton = tk.Button(self.subFrame, text='删除数据', font='微软雅黑', width=self.buttonwidth, command=lambda : change_db(mode='delete'))
        self.deleteButton.pack(anchor=tk.N, side=tk.LEFT, padx=10, pady=2)

        self.scrollBar = tk.Scrollbar(self.TabStrip1__Tab1)
        self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y,expand=tk.YES)

        self.tree_1 = ttk.Treeview(self.TabStrip1__Tab1,
                                   columns=info_column,
                                   show='headings',
                                   yscrollcommand=self.scrollBar)

        for info in info_column:
            self.tree_1.column(info, width=80, anchor='center')
            self.tree_1.heading(info, text=trans_dict[info])

        self.tree_1.pack(side=tk.LEFT, fill=tk.Y)
        self.scrollBar.config(command=self.tree_1.yview)

        self.TabStrip1.add(self.TabStrip1__Tab1, text='我的信息')

        self.TabStrip1__Tab2 = tk.Frame(self.TabStrip1)
        self.TabStrip1__Tab2Lbl = tk.Label(self.TabStrip1__Tab2, text='Please add widgets in code.')
        self.TabStrip1__Tab2Lbl.place(relx=0.1, rely=0.5)
        self.TabStrip1.add(self.TabStrip1__Tab2, text='我的选课')

        self.TabStrip1__Tab3 = tk.Frame(self.TabStrip1)
        self.TabStrip1__Tab3Lbl = tk.Label(self.TabStrip1__Tab3, text='Please add widgets in code.')
        self.TabStrip1__Tab3Lbl.place(relx=0.1, rely=0.5)
        self.TabStrip1.add(self.TabStrip1__Tab3, text='插入数据')

        def change_db(self,mode):
            info = self.tree_1.get_children()
            data = {
                'mode': mode,
                'info': info
            }
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(address)
            bytedata = repr(data).encode()
            sock.send(bytedata)






if __name__ == '__main__':
    root = tk.Tk()
    root.option_add("*Font", "Consolas")
    root.resizable(False, False)
    mainpage = MainPage()
    mainpage.pack(expand=0)
    root.mainloop()
