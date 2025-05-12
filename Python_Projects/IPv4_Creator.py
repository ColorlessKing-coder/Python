import random

#Yol1
octet1 = random.randint(0x00,0xff)
octet2 = random.randint(0x00,0xff)
octet3 = random.randint(0x00,0xff)
octet4 = random.randint(0x00,0xff)

Ip_Address = f'{octet1}.{octet2}.{octet3}.{octet4}'
print(Ip_Address)


#Yol2

def generate_random_ip():
    octets = [str(random.randint(1, 254)) for _ in range(4)]
    return '.'.join(octets)

ip_address = generate_random_ip()
print(ip_address)
