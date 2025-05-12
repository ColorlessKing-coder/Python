from rich import print
import subprocess
import argparse

def ParseArg():
    # Argument parser oluşturuluyor
    parser = argparse.ArgumentParser(description='Mac Changer', add_help=True)
    parser.add_argument('-v', '--version', action='version', version='MacChanger.py 1.0')
    parser.add_argument('-i', '--interface', dest='interface', help='This Is Your Ethernet Device')
    parser.add_argument('-m', '--mac_address', dest='mac_address', default='08:00:27:87:46:68', help='Give A Mac Address')
    args = parser.parse_args()

    #interface = args.interface
    #mac_address = args.mac_address
    return args   
args = ParseArg()

def ChageMacAddress(interfacedif , mac_addressdif):
    try:
        subprocess.call(["ip", "link", "set", "dev", interfacedif, "down"])
        subprocess.call(["ip", "link", "set", "dev", interfacedif, "address", mac_addressdif])
        subprocess.call(["ip", "link", "set", "dev", interfacedif, "up"])
        print('[bold green]Mac Adresi Değişti[/bold green]')
    except Exception as e:
        print(f'[bold red]Bir hata oluştu: {e}[/bold red]')

ChageMacAddress(args.interface , args.mac_address)

