#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import threading
import time

def tcplink(sock,addr):
	print 'accept connection from %s:%s...' %addr
	sock.send('welcome')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if data =='exit' or not data:
			break
		sock.send('Hell0, %s') %data
	sock.close()
	print ('connection closed')

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',9999))

s.listen(5)
print 'wating for connection'

while True:
	sock, addr = s.accept()
	t = threading.Thread(target=tcplink,args=(sock,addr))
	t.start()

