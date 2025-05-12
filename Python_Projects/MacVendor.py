import requests
from time import sleep


def get_mac_vendor(mac_address: str) -> str:
    url = f"https://api.macvendors.com/{mac_address}"
    try:
        response = requests.get(url)
        sleep(1)
        response.raise_for_status()  # HTTP hataları varsa bir istisna oluşturur
        return response.text
    except requests.exceptions.RequestException:
        return "Error: Unknown Vendor"




get_mac_vendor()