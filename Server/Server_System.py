import pymysql
import pymssql
import socket
import threading
from time import sleep

address = ('127.0.0.1', 20176)
usermode = {1: 'Wangcz_Students',
            2: 'Wangcz_Teachers',
            3: 'Wangcz_Admin'
            }

def checkuser(username, password, cursor, user_db):

    cursor.execute('''select * from %s WHERE username = %d AND password = %d''' % (user_db, int(username), int(password)))
    return cursor.fetchall()


def tcplink(sock, addr):
    conn = pymysql.connect()
    cursor = conn.cursor()
    while True:
        bytedata = sock.recv(1024)
        data = eval(bytedata.decode())
        sleep(1)
        if data:
            if 'username' and 'password' and 'login_mode' in data.keys():
                if checkuser(data['username'],data['password'],cursor=cursor, user_db=usermode[data[login_mode]]):
                    sock.send(b'Login success')#登陆成功
                else:
                    sock.send(b'Error')#发送错误消息
        else:
            break

    sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(address)
    s.listen(10)
    while True:
        sock,addr = s.accept()
        t = threading.Thread(target=tcplink,args=(sock,addr))