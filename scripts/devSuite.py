#! /usr/bin/python3

from lonePrograms import *
from installBasics import *
from installAll import *
from isConnect import *
from tryConnect import * 

################################################################################################################################################################################################################################
### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ###
################################################################################################################################################################################################################################

counter = 0

################################################################################################################################################################################################################################
### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ###
################################################################################################################################################################################################################################


def argvAll():
    import colorama, os, sys, time, random
    installAll()
    
################################################################################################################################################################################################################################
### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ###
################################################################################################################################################################################################################################


def dependenciesInstaller():
    import os, sys

    if counter == 1:
        print("You don't have all the necesary dependencies to run this program. Do you wanna install it?[Y/N] ", end='')
        rect = str(input(''))

        if rect == '' or rect == 'S' or rect == 's' or rect == 'Y' or rect == 'y':
            print("Installing all necesary dependencies. . .")
            os.system("sudo pip3 install colorama") #&& sudo pip3 install random && sudo pip3 install time") 
            '''
            import colorama, time
            print(colorama.Fore.RED + "\nDone. Now start the installation of your suite. . .\n")
            time.sleep(2)
            install()'''

            main() #########~@@@~~@@~ AQUÍ ESTABA MAIN2()
        else:
            print("\n\n")
            sys.exit()


################################################################################################################################################################################################################################
### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ###
################################################################################################################################################################################################################################


def main():

    counter = 0


    try:
        import colorama
    except ImportError:
        # Que hacer si el módulo no se puede importar
        import os
        
        print("You don't have all the necesary dependencies to run this program. Do you wanna install it?[Y/N] ", end='')
        rect = str(input(''))
        
        if rect == '' or rect == 'S' or rect == 's' or rect == 'Y' or rect == 'y':
            print("Installing all necesary dependencies. . .")
            os.system("sudo pip3 install colorama") #&& sudo pip3 install random && sudo pip3 install time") 
                

    
    try:
        import os, sys, colorama, time, random

        install = sys.argv[1].lower() == "install"
        lenght = len(sys.argv) == 3

        if install and sys.argv[2].lower() == "all" and lenght:
            argvAll()

        elif install and sys.argv[2].lower() == "basics" and lenght:
            installBasics()

        elif install and sys.argv[2].lower() == "vim" and lenght:
            VIM()

        elif install and sys.argv[2].lower() == "gvim" and lenght:
            GVIM()

        elif install and sys.argv[2].lower() == "vscode" and lenght:
            VSCODE()

        elif install and sys.argv[2].lower() == "codeblocks" and lenght:
            CODEBLOCKS()
        
        elif install and sys.argv[2].lower() == "gccg++" and lenght:
            GCC()
        
        elif install and sys.argv[2].lower() == "micro" and lenght:
            MICRO()
        
        elif install and sys.argv[2].lower() == "tor" and lenght:
            TOR()
        
        elif install and sys.argv[2].lower() == "chrome" and lenght:
            GOOGLE()
        
        elif install and sys.argv[2].lower() == "gimp" and lenght:
            GIMP()

        elif install and sys.argv[2].lower() == "audacity" and lenght:
            AUDACITY()
        
        elif install and sys.argv[2].lower() == "wine" and lenght:
            WINE()
        
        elif install and sys.argv[2].lower() == "blender" and lenght:
            BLENDER()
        
        elif install and sys.argv[2].lower() == "git" and lenght:
            GIT()

        elif install and sys.argv[2].lower() == "steam" and lenght:
            STEAM()

        elif install and sys.argv[2].lower() == "vlc" and lenght:
            VLC()

        elif install and sys.argv[2].lower() != "git" or sys.argv[2].lower() != "blender" or sys.argv[2].lower() != "wine" or sys.argv[2].lower() != "audacity" or sys.argv[2].lower() != "gimp" or sys.argv[2].lower() != "chrome" or sys.argv[2].lower() != "tor" or sys.argv[2].lower() != "micro" or sys.argv[2].lower() != "all" or sys.argv[2].lower() != "gccg++" or sys.argv[2].lower() != "codeblocks" or sys.argv[2].lower() != "vscode" or sys.argv[2].lower() != "gvim" or sys.argv[2].lower() != "vim" and lenght or sys.argv[2].lower() != "steam" and lenght or sys.argv[2].lower() != "vlc":
            print("That program it's not now available. The programs availables now are:\n")
            print("VIM               |         devSuite install vim")
            print("GVIM              |         devSuite install gvim")
            print("VSCode            |         devSuite install vscode")
            print("Code::Blocks      |         devSuite install codeblocks")
            print("GCC and G++       |         devSuite install gccg++")
            print("Micro Text Editor |         devSuite install micro")
            print("TOR Web Browser   |         devSuite install tor")
            print("Google Chrome     |         devSuite install chrome")
            print("GIMP              |         devSuite install gimp")
            print("Audacity          |         devSuite install audacity")
            print("WINE              |         devSuite install wine")
            print("Blender           |         devSuite install blender")
            print("Git               |         devSuite install git")
            print("Steam             |         devSuite install steam")
            print("Vlc             |         devSuite install vlc")
            print("All the programs  |         devSuite install all")

    except:
        counter = 1
        dependenciesInstaller()

################################################################################################################################################################################################################################
### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ###
################################################################################################################################################################################################################################

'''
def main2():
    import os, sys, colorama, time, random

    try:
        if sys.argv[1].lower() == "install":
            install = sys.argv[1].lower() == "install"
            lenght = len(sys.argv) == 3

            if install and sys.argv[2].lower() == "all" and lenght:
                installAll()

            elif install and sys.argv[2].lower() == "basics" and lenght:
                installBasics()

            elif install and sys.argv[2].lower() == "vim" and lenght:
                VIM()

            elif install and sys.argv[2].lower() == "gvim" and lenght:
                GVIM()

            elif install and sys.argv[2].lower() == "vscode" and lenght:
                VSCODE()

            elif install and sys.argv[2].lower() == "codeblocks" and lenght:
                CODEBLOCKS()
            
            elif install and sys.argv[2].lower() == "gccg++" and lenght:
                GCC()
            
            elif install and sys.argv[2].lower() == "micro" and lenght:
                MICRO()
            
            elif install and sys.argv[2].lower() == "tor" and lenght:
                TOR()
            
            elif install and sys.argv[2].lower() == "chrome" and lenght:
                GOOGLE()
            
            elif install and sys.argv[2].lower() == "gimp" and lenght:
                GIMP()

            elif install and sys.argv[2].lower() == "audacity" and lenght:
                AUDACITY()
            
            elif install and sys.argv[2].lower() == "wine" and lenght:
                WINE()
            
            elif install and sys.argv[2].lower() == "blender" and lenght:
                BLENDER()
            
            elif install and sys.argv[2].lower() == "git" and lenght:
                GIT()

            elif install and sys.argv[2].lower() == "steam" and lenght:
                STEAM()
            
            elif install and sys.argv[2].lower() == "vlc" and lenght:
                VLC()

            elif install and sys.argv[2].lower() != "git" or sys.argv[2].lower() != "blender" or sys.argv[2].lower() != "wine" or sys.argv[2].lower() != "audacity" or sys.argv[2].lower() != "gimp" or sys.argv[2].lower() != "chrome" or sys.argv[2].lower() != "tor" or sys.argv[2].lower() != "micro" or sys.argv[2].lower() != "all" or sys.argv[2].lower() != "gccg++" or sys.argv[2].lower() != "codeblocks" or sys.argv[2].lower() != "vscode" or sys.argv[2].lower() != "gvim" or sys.argv[2].lower() != "vim" and lenght or sys.argv[2].lower() != "steam" and lenght or sys.argv[2].lower() != "vlc":
                print("That program it's not now available. The programs availables now are:")
                print("VIM               |         devSuite install vim")
                print("GVIM              |         devSuite install gvim")
                print("VSCode            |         devSuite install vscode")
                print("Code::Blocks      |         devSuite install codeblocks")
                print("GCC and G++       |         devSuite install gccg++")
                print("Micro Text Editor |         devSuite install micro")
                print("TOR Web Browser   |         devSuite install tor")
                print("Google Chrome     |         devSuite install chrome")
                print("GIMP              |         devSuite install gimp")
                print("Audacity          |         devSuite install audacity")
                print("WINE              |         devSuite install wine")
                print("Blender           |         devSuite install blender")
                print("Git               |         devSuite install git")
                print("Steam             |         devSuite install steam")
                print("Vlc             |         devSuite install vlc")
                print("All the programs  |         devSuite install all")

    except:
        print("For now you must use this syntax: devSuite install <pkg>")

'''
################################################################################################################################################################################################################################
### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ###
################################################################################################################################################################################################################################


main()
