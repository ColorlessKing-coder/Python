"""
text = "Aslankral"

# İkişer ikişer karakterleri yazdırmak için for döngüsü
for i in range(0, len(text), 2):
    print(text[i:i+2])
"""

import random
from rich import print
import argparse





def ParserIPCreate():
    parser = argparse.ArgumentParser(description="This is Mac Createin App")
    parser.add_argument_group('Section Of IPv4 Creator')
    parser.add_argument('--type',help='What Would You Want To Do  ',dest='type',choices=['IPv4','IPv6','EUI'],required=True)
    parser.add_argument('-v','--version',action='version',help='Will Show You Version Of App' ,version='0x00',dest='version')
    parser.add_argument('-c','--count',help='How Many Time Do You Wana repaid it',dest='count',type=int,default=1)
    parser.add_argument('--class-ipv4',dest='_class_ipv4',help='Chose The Ip Class',choices=['A','B','C'],default=None)
    parser.add_argument('--class-ipv6',help='Will Create A Global Unicast Address',dest='_class_ipv6',choices=['GUA','LLA','SLA','ULA'])
    parser.add_argument('-m','--mac_address',help='Please Enter Your Mac Address',dest='mac_address')
    args = parser.parse_args()
    return args





def CreateIpv4Class_A(count:int):
    ip_list = []
    try:
        for _ in range(count):
            octet1 = random.randint(1,127)
            octet2 = random.randint(1,255)
            octet3 = random.randint(1,255)
            octet4 = random.randint(1,255)

            Ip_Address = f'{octet1}.{octet2}.{octet3}.{octet4}'
            ip_list.append(Ip_Address)
    except Exception as e:
        print('Error : ', e)

    return ip_list   
def CreateIpv4Class_B(count:int):
    ip_list = []
    try:
        for _ in range(count):
            octet1 = random.randint(128,191)
            octet2 = random.randint(1,255)
            octet3 = random.randint(1,255)
            octet4 = random.randint(1,255)

            Ip_Address = f'{octet1}.{octet2}.{octet3}.{octet4}'
            ip_list.append(Ip_Address)
    except Exception as e:
        print('Error : ', e)
    
    return ip_list
def CreateIpv4Class_C(count:int):
    ip_list = []
    try:
        for _ in range(count):
            octet1 = random.randint(192,223)
            octet2 = random.randint(1,255)
            octet3 = random.randint(1,255)
            octet4 = random.randint(1,255)

            Ip_Address = f'{octet1}.{octet2}.{octet3}.{octet4}'
            ip_list.append(Ip_Address)
    except Exception as e:
        print('Error : ',e)
    
    return ip_list





def EUI_64(mac: str) -> str:
    # FE80: kısmı sabit, bağlantı yerel adresi (link-local address)
    firstSixteenBits = 'FE80'
    
    # MAC adresini ':' işaretine göre böl ve birleştir
    mac_address = mac.replace(":", "")
    
    # İlk 3 byte ve son 3 byte ayrılıyor
    First24Bits = mac_address[:6]
    Last24Bits = mac_address[6:]
    
    # İlk baytı binary olarak alıyoruz
    first_byte = int(First24Bits[:2], 16)
    
    # 7. bitin ters çevrilmesi (örneğin global/yerel biti)
    # Binary olarak ilk baytı al ve 7. biti ters çevir
    first_byte ^= 0x02
    
    # İlk byte'ı güncellenmiş haliyle string olarak formatlıyoruz
    updated_first_byte = f"{first_byte:02x}"
    
    # EUI-64 formatına dönüştürme işlemi
    # FE80::[UpdatedFirstByte][Remaining First24Bits]FF:FE[Last24Bits]
    eui_64_address = f"{firstSixteenBits}::{updated_first_byte}{First24Bits[2:4]}:{First24Bits[4:]}FF:FE{Last24Bits[:2]}:{Last24Bits[2:]}"
    
    return eui_64_address


def CreateIpv4(count:int) -> list:
    ip_list = []
    try:
        for _ in range(0,count,1):
            Creating_ip = [str(random.randint(1,254)) for _ in range(4)]
            dotted_ip = '.'.join(Creating_ip)
            ip_list.append(dotted_ip)
    except Exception as e:
        print('Error : ',e)

    return ip_list
    
def CreateIpv6(count:int) -> list:
    ip_list = []
    try:
        for _ in range(0,count ,1):
            SixtennBits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            creating_ip = [ ''.join(random.choices(SixtennBits, k=4)) for _ in range(8)]
            #ip = [x.lstrip('0') if x.startswith('0') else x for x in ip]
            double_dotted =  ':'.join(creating_ip)
            ip_list.append(double_dotted)
    except Exception as e:
        print('Error : ',e )
    
    return ip_list
    
def CreateIpv6GlobalSiteLocalAddress(count:int) -> list:
    ip_list = []
    try:
        # 112 bit için kullanılan karakterler
        for x in range(count):
            FirstSixteenBits = 'FECO'
            NinetysixBits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            LastSixteenBits = ['0', '1', '2', '3', 'A', 'B', 'C', 'D', 'E', 'F']
            creating_ip_loop_seven_times = [ ''.join(random.choices(NinetysixBits, k=4)) for _ in range(6)]
            creating_ip_loop_one_times = ''.join(random.choices(LastSixteenBits, k=4))
        
        # IPv6 adresi oluşturuluyor
            Bits128 = f'{FirstSixteenBits}:' + ':'.join(creating_ip_loop_seven_times) + f':{creating_ip_loop_one_times}'
            ip_list.append(Bits128)
    except Exception as e:
        print('Error :', e)
    
    return ip_list

def CreateIpv6GlobalUnicastAddress(count:int) -> list:
    ip_list = []
    try:
        # 112 bit için kullanılan karakterler
        for x in range(count):
            FirstSixteenBits = '2001'
            NinetysixBits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            LastSixteenBits = ['0', '1', '2', '3', 'A', 'B', 'C', 'D', 'E', 'F']
            creating_ip_loop_seven_times = [ ''.join(random.choices(NinetysixBits, k=4)) for _ in range(6)]
            creating_ip_loop_one_times = ''.join(random.choices(LastSixteenBits, k=4))
        
        # IPv6 adresi oluşturuluyor
            Bits128 = f'{FirstSixteenBits}:' + ':'.join(creating_ip_loop_seven_times) + f':{creating_ip_loop_one_times}'
            ip_list.append(Bits128)
    except Exception as e:
        print('Error :', e)
    
    return ip_list

def CreateIpv6LinkLocalAddress(count:int) -> list:
    ip_list = []
    try:
        for x in range(count):
            FirstSixteenBits = 'FE80'
            OtherBits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            creating_ip = [ ''.join(random.choices(OtherBits, k=4)) for _ in range(7)]
            double_dotted =  f'{FirstSixteenBits}:' + ':'.join(creating_ip)
            ip_list.append(double_dotted)
    except Exception as e:
        print('Error : ',e )
    
    return ip_list

def CreateIpv6GlobalUniqueLocalAddress(count:int) -> list:
    ip_list = []
    try:
        # 112 bit için kullanılan karakterler
        for x in range(count):
            FirstSixteenBits = 'FECO'
            NinetysixBits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

            LastSixteenBitsFirstNibble = ['0', '1', '2', '3', 'A', 'B', 'C', 'D', 'E', 'F']
            LastSixteenBitsSecondNibble = ['0', '1', '2', '3', 'A', 'B', 'C', 'D']
            LastSixteenBitsThirdNibble = ['0', '1', '2', '3', 'A', 'B', 'C', 'D', 'E', 'F']
            LastSixteenBitsForthNibble = ['0', '1', '2', '3', 'A', 'B', 'C', 'D', 'E', 'F']

            creating_ip_loop_seven_times = [ ''.join(random.choices(NinetysixBits, k=4)) for _ in range(6)]
            creating_ip_loop_one_times_firstNibble = ''.join(random.choices(LastSixteenBitsFirstNibble, k=1))
            creating_ip_loop_one_times_SecondNibble = ''.join(random.choices(LastSixteenBitsSecondNibble, k=1))
            creating_ip_loop_one_times_ThirdNibble = ''.join(random.choices(LastSixteenBitsThirdNibble, k=1))
            creating_ip_loop_one_times_ForthNibble = ''.join(random.choices(LastSixteenBitsForthNibble, k=1))
        
        # IPv6 adresi oluşturuluyor
            Bits128 = f'{FirstSixteenBits}:' + ':'.join(creating_ip_loop_seven_times) + f':{creating_ip_loop_one_times_firstNibble}{creating_ip_loop_one_times_SecondNibble}{creating_ip_loop_one_times_ThirdNibble}{creating_ip_loop_one_times_ForthNibble}'
            ip_list.append(Bits128)
    except Exception as e:
        print('Error :', e)
    
    return ip_list

"""
def CreateIpv6Type2():
    create_ip = [random.randint(0x00, 0xff) for _ in range(8)]
    designed_ip = [f'{x:04x}' for x in create_ip]
    control_ip = [x.lstrip('0') or '0' for x in designed_ip]
    return ':'.join(control_ip)
"""



if __name__ == '__main__':
    args = ParserIPCreate()
    try:
        if args.type == "IPv4":
            if args._class_ipv4 == "A":
                ip = CreateIpv4Class_A(args.count)
                for x in ip:
                    print(x)
            elif args._class_ipv4 == "B":
                ip = CreateIpv4Class_B(args.count)
                for x in ip:
                    print(x)
            elif args._class_ipv4 == "C": 
                ip = CreateIpv4Class_C(args.count)
                for x in ip:
                    print(x)
            else:
                ip = CreateIpv4(args.count)
                for x in ip:
                    print(x)
        
        if args.type == "IPv6":
            if args._class_ipv6 == 'GUA':
                ip = CreateIpv6GlobalUnicastAddress(args.count)
                for x in ip:
                    print(x)

            elif args._class_ipv6 == 'LLA':
                ip = CreateIpv6LinkLocalAddress(args.count)
                for x in ip:
                    print(x)

            elif args._class_ipv6 == 'SLA':
                ip = CreateIpv6GlobalSiteLocalAddress(args.count)
                for x in ip:
                    print(x)
            
            elif args._class_ipv6 == 'ULA':
                ip = CreateIpv6GlobalUniqueLocalAddress(args.count)
                for x in ip:
                    print(x)


            else:
                ip = CreateIpv6(args.count)
                for x in ip:
                    print(x)

        if args.type == 'EUI':
            print(EUI_64(args.mac_address))
                    
        

    except Exception as e:
        print('Error :' ,e)   
   