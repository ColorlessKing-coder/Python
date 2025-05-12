import scapy.all as scapy
import socket
from rich import print

def traceroute_simple(ip_address: str, max_hops: int = 30):
    print(f"Traceroute to {ip_address}")
    
    for ttl_value in range(1, max_hops + 1):
        # TTL değeriyle ICMP paketi oluştur ve gönder
        packet = scapy.IP(dst=ip_address, ttl=ttl_value) / scapy.ICMP()
        
        # Paketi gönder ve yanıtı bekle
        response = scapy.sr1(packet, timeout=2, verbose=0)
        
        if response is None:
            print(f"{ttl_value}\t*")
        elif response.type == 11:  # TTL exceeded (hops)
            print(f"{ttl_value}\t{response.src}")
        elif response.type == 0:  # Echo reply (destination reached)
            print(f"{ttl_value}\t{response.src} (Destination reached)")
            break
        else:
            print(f"{ttl_value}\tUnknown response")

traceroute_simple("8.8.8.8")


#Yol2
from scapy.layers.inet import traceroute

def run_traceroute(destination):
    result, _ = traceroute(destination, maxttl=20)
    result.show()

run_traceroute("8.8.8.8")


from scapy.all import *

# Traceroute fonksiyonu
def trace_route(ip_address):
    ans, unans = traceroute(ip_address, maxttl=30)
    ans.show()

# Hedef IP adresi için traceroute yapalım
ip_address = "192.168.1.1"
trace_route(ip_address)
