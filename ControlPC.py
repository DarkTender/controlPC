#This is python program with you have more options starting and remoting PC
#1.neofetch - this tool has you will show you hardware info and system info, CPU,....
#2.scan network with Netdiscover in range 192.168.1.1/192.168.1.255 this configuration can be changed
#3.This settings is information for you in  NetworkManager
#4.Change MAC for changing your mac address 
#5.This settings is information for you in  Bluetooth
#6.Classic settings for any hackers Update and Upgrade system on Kali/Parrot
#7.Install phpsploit on your PC
#8.Install airgeddon for hacking Wifi with more combination
#9.Restart PC command= reboot




import os
import sys
import datetime
import webbrowser

os.system("clear")

if not os.geteuid() == 0:
    sys.exit("""\033[1;91m\n[!] This program must be run as root!!. \n\033[1;m""")

def start():
    lists = """
[1]Neofetch (scan pc software...) 
[2]Scan network (range --192.168.1.1-192.168.1.255)
[3]Start/Stop/Restart/Status NetworkManager
[4]Change MAC
[5]Start/Stop/Restart/Status Bluetooth
[6]Update and Upgrade system
[7]Install PhpSploit
[8]Install Airgeddon
[9]Restart PC
[10]Exit
"""
    print(lists)
    menu = input("What number?: ")
    while True:
        
        if menu == "1":
            os.system("clear")
            print("click Ctrl+C for end neofetch")
            os.system("apt install neofetch -y | neofetch --de_version on --cpu_speed on --cpu_temp C ")
            start()
        
        elif menu == "2":
            print("Click Ctrl+C for end Scan network")
            os.system("netdiscover -r 192.168.1.1/24")
            os.system("clear")
            start()
       
        elif menu == "3":
            network = input("[1]Start [2]Stop [3]Restart [4]Status [5]Back NetworkManager: ")
            
            if network == "1":
                os.system("service NetworkManager start")
                start()    
            elif network == "2":
                os.system("service NetworkManager stop")
                start()
            elif network == "3":
                os.system("service NetworkManager restart")
                start()
            elif network == "4":
                os.system("service NetworkManager status")
                start()
            elif network == "5":
                start()

        elif menu == "4":
                os.system("service NetworkManager stop && macchanger -a wlan0 && service NetworkManager start ")
                os.system("clear")
                start()
                        
        elif menu == "5":
            
            def bluetooth():
                bluetooth = input("[1]Start [2]Stop [3]Restart [4]Status [5]Back Bluetooth: ")
                if bluetooth == "1":
                    os.system("service bluetooth start")
                    start()
                elif bluetooth == "2":
                    os.system("service bluetooth stop")
                    start()
                elif bluetooth == "3":
                    os.system("service bluetooth restart")
                    start()
                elif bluetooth == "4":
                    os.system("service bluetooth status")
                    start()
                elif bluetooth == "5":
                    start()            
            bluetooth()
        
        elif menu == "6":
            operating_system = input("""[1]Parrot
[2]Kali
Which one you have?: """)
            if operating_system == "1":
                os.system("parrot-upgrade")
                os.system("clear")
                start()
        
            elif operating_system == "2":
                os.system("apt update && apt upgrade -y")                
                os.system("clear")
                start()
        
        elif menu == "7":
            os.system("git clone https://github.com/nil0x42/phpsploit")
            os.system("clear")
            start()
        
        elif menu == "8":
            os.system("apt install airgeddon -y ")
            start()
        
        elif menu == "9":
            os.system("reboot")

        elif menu == "10":
            exit()       
       
        else:
            start()
start()