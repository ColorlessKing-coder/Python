"""
text = "Aslankral"

# İkişer ikişer karakterleri yazdırmak için for döngüsü
for i in range(0, len(text), 2):
    print(text[i:i+2])
"""

import random
from rich import print

def CreateIp():
    SixtennBits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    ip = [ ''.join(random.choices(SixtennBits, k=4)) for _ in range(8)]
    ip = [x.lstrip('0') if x.startswith('0') else x for x in ip]
   
    return ':'.join(ip)


print(CreateIp())





def generate_ipv6_address():
    create_ip = [random.randint(0x00, 0xff) for _ in range(8)]
    designed_ip = [f'{x:04x}' for x in create_ip]
    control_ip = [x.lstrip('0') or '0' for x in designed_ip]
    return ':'.join(control_ip)
ip = generate_ipv6_address()
print(ip)
