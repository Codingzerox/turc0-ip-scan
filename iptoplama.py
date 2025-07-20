import requests
import time
from colorama import Fore, Style, init

init(autoreset=True)  # Renkleri her satırdan sonra sıfırlar

def banner():
    print(Fore.RED + r"""

@@@@@@@ @@@  @@@ @@@@@@@   @@@@@@@  @@@@@@   @@@@@@
  @!!   @@!  @@@ @@!  @@@ !@@      @@!  @@@ @@!  @@@
  @!!   @!@  !@! @!@!!@!  !@!      @!@  !@! @!@  !@!
  !!:   !!:  !!! !!: :!!  :!!      !!:  !!! !!:  !!!
   :     :.:: :   :   : :  :: :: :  : : ::   : :. :
                                                     """)
    print(Fore.RED + Style.BRIGHT + "[!] Coded by turc0\n")
    time.sleep(1)

def check():
    r = requests.get("https://ipinfo.io/")
    if r.status_code == 200:
        print("\n[+] Sunucu Çevrimiçi!\n")
    else:
        print("\n[!] Sunucu Çevrimdışı!\n")
        exit()

banner()

ip = input("Lütfen hedef ip giriniz: ")

check()

country = requests.get(f"https://ipinfo.io/{ip}/country/").text
city = requests.get(f"https://ipinfo.io/{ip}/city/").text
region = requests.get(f"https://ipinfo.io/{ip}/region/").text
postal = requests.get(f"https://ipinfo.io/{ip}/postal/").text
timezone = requests.get(f"https://ipinfo.io/{ip}/timezone/").text
orgination = requests.get(f"https://ipinfo.io/{ip}/org/").text
location = requests.get(f"https://ipinfo.io/{ip}/loc/").text

print("\n" + Fore.GREEN + "İp: " + ip)
print("Ülke: " + country.strip())
print("Şehir: " + city.strip())
print("Bölge: " + region.strip())
print("Posta Kodu: " + postal.strip())
print("Zaman Dilimi: " + timezone.strip())
print("Organizasyon: " + orgination.strip())
print("Lokasyon: " + location.strip())

