
from rich import pretty

def EUI_64() -> None:
    firstSixteenBits = 'FE80'
    mac_address = "509A:4CB5:1511"
    First24Bits = []
    Last24Bits = []
    

    for value in mac_address[0:7]:   
        First24Bits.append(value)
    #print(''.join(First24Bits))
    
    for value in mac_address[7:]:
        Last24Bits.append(value)
    
    First24Bits = ''.join(First24Bits)
    Last24Bits = ''.join(Last24Bits)
    return ''.join(f'{firstSixteenBits}::') + ''.join(f'{First24Bits}FF:') + ''.join(f'FE{Last24Bits}')
   
    
print(EUI_64())
    


def EUI_64() -> str:
    firstSixteenBits = 'FE80'
    mac_address = "509A:4CB5:1511"

    # MAC adresini ':' işaretine göre böl ve birleştir
    mac_address = mac_address.replace(":", "")
    
    # İlk 3 byte ve son 3 byte ayrılıyor
    First24Bits = mac_address[:6]
    Last24Bits = mac_address[6:]
    
    # EUI-64 formatına dönüştürme işlemi
    # FE80::[First24Bits]FF:FE[Last24Bits]
    eui_64_address = f"{firstSixteenBits}::{First24Bits[:2]}{First24Bits[2:4]}:{First24Bits[4:]}FF:FE{Last24Bits[:2]}:{Last24Bits[2:]}"
    
    return eui_64_address


print(EUI_64())

    