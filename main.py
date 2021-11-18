banner = r"""
 ███████╗██╗  ██╗███████╗██████╗            
 ██╔════╝██║  ██║██╔════╝██╔══██╗           
 ███████╗███████║█████╗  ██████╔╝           
 ╚════██║██╔══██║██╔══╝  ██╔══██╗           ___                      _____         __       
 ███████║██║  ██║███████╗██║  ██║          / _ \_______ __ ____ __  / __(_)__  ___/ /__ ____
 ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝         / ___/ __/ _ \\ \ / // / / _// / _ \/ _  / -_) __/
                                         /_/  /_/  \___/_\_\\_, / /_/ /_/_//_/\_,_/\__/_/   
 ██╗      ██████╗  ██████╗██╗  ██╗                        /___/                            
 ██║     ██╔═══██╗██╔════╝██║ ██╔╝
 ██║     ██║   ██║██║     █████╔╝ 
 ██║     ██║   ██║██║     ██╔═██╗ 
 ███████╗╚██████╔╝╚██████╗██║  ██╗
 ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
----------------------------------------------------
"""
import requests
from bs4 import BeautifulSoup
from time import sleep
import colorama
from colorama import Fore, Style
from requests.api import head

# RENK
colorama.init(autoreset=True)

# EKRAN TEMİZLE
import os
def temizle():
    os.system("cls")


# BANNER
def BANNER():
    print(Fore.RED + banner)

# TEMİZLE BANNER
def temizban():
    temizle()
    BANNER()


# PROXY ÇEKME
temizban()
print(Fore.BLUE+"\n [+] Proxyler Siteden Çekiliyor...")
def proxycek():
    global proxys
    site = "https://free-proxy-list.net"
    req = requests.get(site)
    soup = BeautifulSoup(req.content, "html.parser")  
    liste =  soup.find("tbody")
    proxys = []
    proxy = ""

    for satir in liste:
        sayi = 0
        for karak in satir:
            if sayi == 1:
                break
            else:
                proxy += str(karak.text) + ":"
                sayi+=1
        
            
        for karak in satir:
            try:
                kanal = int(karak.text)
                proxy += str(kanal)
                
            except:
                pass
            
        proxys.append(str(proxy))
        proxy = "" 
proxycek()
    
print(Fore.CYAN+ " - Çekilen Proxy Sayısı: "+ str(len(proxys)))   
print(Fore.BLUE+ "\n [+] Çekilen Proxyler Kontrol Ediliyor...\nSağlam olanlar dosya haline kaydedilecektir !\n\n")
    
    

# PROXY DENEME
saglam_proxys = []

for proxy in proxys:
    proxies = {
   'http': f'http://{proxy}',
   'https': f'http://{proxy}',
    }
    url = 'http://www.google.com'
    try:
        response = requests.get(url, proxies=proxies)
        
        if response.status_code == 200:
            saglam_proxys.append(proxy)
            print(Fore.GREEN+ "+ Başarılı  " + proxy )
                
        else:
            print(Fore.LIGHTRED_EX+ "- Başarısız  "+ proxy )
            
    except Exception as e:
        print(Fore.LIGHTRED_EX+ "- Başarısız  "+ proxy )
        
    with open("proxys.txt", "w", encoding="utf-8") as dosya:
        a = ""
        for i in saglam_proxys:
            a += i + "\n"
            
        dosya.write(a)
