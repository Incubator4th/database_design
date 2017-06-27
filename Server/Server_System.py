import pymysql
import socket
import threading
from time import sleep

address = ('127.0.0.1', 20176)

def checkuser(username,password):
    conn = pymysql.connect()
    cursor = conn.cursor()
    cursor.execute('''select * from 111 WHERE username == %d AND password == %d''' % (int(username),int(password)))
    return cursor.fetchall()


def tcplink(sock,addr):
    while True:
        datalist = sock.recv(1024).split(" ")
        datalist = datalist.decode()
        sleep(1)
        if len(datalist) == 3:
            if datalist[0] == 'U&P' and checkuser(datalist[1],datalist[2]):
                break#登陆成功
            sock.send(b'Login success')
    sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(address=address)
    s.listen(10)
    while True:
        sock,addr = s.accept()
        t = threading.Thread(target=)