import socket, threading, time

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('10.211.55.2',9999))
s.listen(5)
print 'Wainting for connection...'

def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if data=='exit' or not data:
            break
        sock.send('Hello, %s' % data)
    sock.close()
    print 'connection from %s:%s closed.' % addr

while True:
    sock, addr=s.accept()
    t=threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
