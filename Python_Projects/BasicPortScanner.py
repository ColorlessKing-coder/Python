
import socket

def PortScanner(ip_address:str,port:int):
    Client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    Client.settimeout(1) # Bağlantı Zaman Aşımı Süreisi

    try:
        Control = Client.connect((ip_address,port))
        print("Open Port :" , port )
    
    except (socket.timeout, socket.error):
        print("Closed Port Or No Response Port" , port)

    finally:     
        Client.close()
   
    
for x in range(65535):
    PortScanner("192.168.1.1",x)