from subprocess import check_output as check 
from subprocess import CalledProcessError
from os import system

print("""

  _____  _____  _____   _____                 
 |  __ \|  __ \|  __ \ / ____|                
 | |__) | |  | | |__) | (___   ___ __ _ _ __  
 |  _  /| |  | |  ___/ \___ \ / __/ _` | '_ \ 
 | | \ \| |__| | |     ____) | (_| (_| | | | |
 |_|  \_\_____/|_|    |_____/ \___\__,_|_| |_|
                                              
            Author:  Batuhan Türkarslan
            GitHub : https://github.com/TURKZEN       
                               
ÖRNEK KULLANIM : 192.168.1.0 ---> Şeklindeki Network ID ile çalışır

""")

ip = input("Network ID : ") 

ip = ip.split(".") 

birinciOktek = int(ip[0])
ikinciOktek = int(ip[1])
ucuncuOktek = int(ip[2])
dorduncuOktek = int(ip[3]) + 1

for i in range(1,254):
    dorduncuOktek += 1
    ipSon = "{}.{}.{}.{}".format(birinciOktek,ikinciOktek,ucuncuOktek,dorduncuOktek)
    try:
        output = check(["rdesktop",ipSon])
    except CalledProcessError:
        print("{} ---> RDP YOK".format(ipSon))
    else:
        print("{} ---> RDP BULUNDU !!!!! ".format(ipSon))
    
