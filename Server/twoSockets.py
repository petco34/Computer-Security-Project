#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket


# In[3]:


import socket
debug = False
def makeSocket(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen()
    connect, address = s.accept()
    print("Connected with: ", address)
    return s, connect, address

def userNamePassword(socket):
    socket.send(b"Enter username: ")
    username = socket.recv(1024)
    if debug == True:
        print("Receiving username", username)
    socket.send(b"Username Receuved. Please enter Password")
    password = socket.recv(1024)
    return username, password
    
host = "127.0.0.1"
port = 12347
active_users = []
sock1, connect1, address1 = makeSocket(host,port)
#sock2, connect2, address2 = makeSocket(host,port+1)

username, password = userNamePassword(connect1)

while True:
    incoming = connect1.recv(1028)
    incoming = incoming.decode('utf-8')
    print(incoming)
    if incoming == "disaster":
        sock1.close()
        connect1.close()
        break

print(username, password)
    


# In[3]:





# In[ ]:




