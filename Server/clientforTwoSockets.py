#!/usr/bin/env python
# coding: utf-8

# In[2]:


import socket
host = "127.0.0.1" #server's hostname or ip address
port = 12347

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect ((host,port))
    counter = 0
    s.recv(1024)
    s.send(b'User Name')
    s.recv(1024)
    s.send(b'Password')
    while True:
        put = input("You have Successfully logged in")
        if put == "disaster":
            put = bytes(put, encoding='utf-8')
            s.send(put)
            s.close()
            break
        put = bytes(put, encoding='utf-8')
        s.send(put)
        
        #s.recv(1024)
        
        


# In[ ]:





# In[ ]:




