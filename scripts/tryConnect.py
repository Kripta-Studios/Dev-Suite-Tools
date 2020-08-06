from isConnect import *

def tryConnect():
    import os, sys, colorama, time

    xstatus = net_is_up()

    if xstatus != 0:
        print("\nYou don't have internet connection. . .")
        time.sleep(3)
        os.system("clear")
        print("You wanna leave or try to reconnect to the internet [L/R]: ", end='')
        whatSayGuy = str(input())

        if whatSayGuy == 'R' or whatSayGuy == 'r':
            print(colorama.Fore.RESET + '', end='')
            os.system("sudo iw dev")
            selInterface = str(input("Type the name of the interface (ex. wlan0): "))
            time.sleep(2)
            os.system(f"sudo ip link set {selInterface} up")
            os.system("echo \"blacklist hp_wmi\" | sudo tee /etc/modprobe.d/hp.conf")
            os.system("sudo rfkill unblock all")
            os.system(f"sudo ip link set {selInterface} up")
            os.system(f"sudo iw {selInterface} link")
            os.system(f"sudo iw {selInterface} scan")
            selSSID = str(input("Insert the SSID of the network you wanna connect (ex. MyCompany_0831): "))

            selPasswd = str(input(f"Insert the password of the network {selSSID}: "))
            os.system(f"nmcli r wifi on")
            os.system(f"nmcli dev wifi connect {selSSID} password {selPasswd}")

            time.sleep(5)
            xstatus = net_is_up()
            if xstatus:
                print("ERORR: Can't able to connect to network, maybe you type bad the interface or the SSID or the password. . .")
                time.sleep(2)
                os.system("clear")
                print("Enable to do the installation: ERROR: Connection error")
                print(colorama.Fore.RED + colorama.Style.BRIGHT +"Kripta Studios made this program.")
                time.sleep(2)
                print(colorama.Fore.RESET +"Press enter to close this program. . .")
                str(input(''))
                sys.exit()
                sys.exit()
            else:
                pass

        elif whatSayGuy == 'L' or whatSayGuy == 'l':
            os.system("clear")
            print("Enable to do the installation: ERROR: Connection error")
            print(colorama.Fore.RED + colorama.Style.BRIGHT +"Kripta Studios made this program.")
            time.sleep(2)
            print(colorama.Fore.RESET +"Press enter to close this program. . .")
            str(input(''))
            sys.exit()

    elif xstatus == 0:
        print(colorama.Fore.MAGENTA + "\nCONNECTION OK\n\n")
        time.sleep(2)
