import random

def generate_random_mac():
    mac = [random.randint(0x00,0xff)for _ in range(6)]
    return ':'.join(f'{x:02x}' for x in mac)


mac = generate_random_mac()
print(str(mac))