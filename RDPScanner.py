from subprocess import check_output as check 
from subprocess import CalledProcessError
from os import system,name
from time import sleep

def banner():
    system("clear")
    print("""
        _____  _____  _____   _____                                 
        |  __ \|  __ \|  __ \ / ____|                                
        | |__) | |  | | |__) | (___   ___ __ _ _ __  _ __   ___ _ __ 
        |  _  /| |  | |  ___/ \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
        | | \ \| |__| | |     ____) | (_| (_| | | | | | | |  __/ |   
        |_|  \_\_____/|_|    |_____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                                    
                                                            
                Author:  Batuhan Türkarslan
                GitHub : https://github.com/TURKZEN       
                                
    Example : 192.168.1.0

    """)
    
def rdpscan():
    ip = input("Network ID : ") 
    print("Tarama Başlıyor...")
    ip = ip.split(".") 

    firstOctet = int(ip[0])
    secondOctet = int(ip[1])
    thirdOctet = int(ip[2])
    fourthOctet = int(ip[3]) + 1

    for i in range(1,254):
        fourthOctet += 1
        ip = "{}.{}.{}.{}".format(firstOctet,secondOctet,thirdOctet,fourthOctet)
        try:
            output = check(["rdesktop",ip])
        except CalledProcessError:
            system("clear")
            print("{} ---> RDP YOK".format(ip))
        else:
            print("{} ---> RDP BULUNDU !!!!! ".format(ip))

            with open("RDPs.txt","a") as dosya:
                dosya.write(ip)
                dosya.write("\n")

            print("RDPs.txt dosyasına yazıldı !")
            print("Devam ediliyor...")
            sleep(3)

if __name__ == "__main__":
    if name == "nt":
        print("Windows desteklemiyor !")
    else:
        try:
            banner()
            rdpscan()
        except KeyboardInterrupt:
            print()
            print("Çıkış Yapıldı !")

        except EOFError:
            print()
            print("Çıkış Yapıldı !")