## @@  Here are the lone programs to install @@ ##
############################################################################################################################################################################################################

def VIM():
    import time, colorama, os, sys

    print(colorama.Fore.GREEN + " · VIM: Vim is an improved version of the Vi text editor, present on all UNIX systems.")
    input("PRESS ENTER TO CONTINUE...")
    os.system("clear")
    print(colorama.Fore.RED + "UPDATING REPOSITORIES AND PROGRAMS. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    print(colorama.Fore.BLUE +"UPDATE and UPGRADE succesfully finished.")
    time.sleep(1.5)
    print(colorama.Fore.GREEN +"Installing VIM. . .")
    os.system("sudo apt install vim -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    os.system("sudo apt autoclean")
    os.system("sudo apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))

############################################################################################################################################################################################################

def GVIM():
    import time, colorama, os, sys

    print(colorama.Fore.RED +" · GVIM: It is an open source program released under the GNU license. It is a graphic version of the Vim text editor.")
    input("PRESS ENTER TO CONTINUE...")
    os.system("clear")
    print(colorama.Fore.RED + "UPDATING REPOSITORIES AND PROGRAMS. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    print(colorama.Fore.BLUE +"UPDATE and UPGRADE succesfully finished.")
    time.sleep(1.5)
    print(colorama.Fore.MAGENTA +"Installing GVIM. . .")
    os.system("sudo apt install vim-gtk3 -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    os.system("sudo apt autoclean")
    os.system("sudo apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))

############################################################################################################################################################################################################

def VSCODE():
    import time, colorama, os, sys

    print(colorama.Fore.GREEN +" · VSCode: Visual Studio Code is a source code editor developed by Microsoft for Windows, Linux and macOS.")
    input("PRESS ENTER TO CONTINUE...")
    os.system("clear")
    print(colorama.Fore.RED + "UPDATING REPOSITORIES AND PROGRAMS. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    print(colorama.Fore.BLUE +"UPDATE and UPGRADE succesfully finished.")
    time.sleep(1.5)
    print(colorama.Fore.WHITE +"Installing VSCode. . .")
    os.system("sudo apt install software-properties-common apt-transport-https wget -y")
    os.system("wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -")
    os.system("add-apt-repository \"deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main\"")
    os.system("sudo apt update -y")
    os.system("sudo apt install code -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    os.system("sudo apt autoclean")
    os.system("sudo apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))

############################################################################################################################################################################################################

def CODEBLOCKS():
    import time, colorama, os, sys

    print(colorama.Fore.MAGENTA +" · Code::Blocks: Code :: Blocks is an open source integrated development environment, supporting multiple compilers, including GCC, Clang, and Visual C ++.")
    input("PRESS ENTER TO CONTINUE...")
    os.system("clear")
    print(colorama.Fore.RED + "UPDATING REPOSITORIES AND PROGRAMS. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y") 
    print(colorama.Fore.BLUE +"UPDATE and UPGRADE succesfully finished.")
    time.sleep(1.5)
    print(colorama.Fore.CYAN+"Installing Code::Blocks. . .")
    os.system("sudo apt install codeblocks -y")
    time.sleep(1.5)
    print(colorama.Fore.RED +"Installing GCC + G++. . .")
    os.system("sudo apt install gcc -y && sudo apt install g++ -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    os.system("sudo apt autoclean")
    os.system("sudo apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))

############################################################################################################################################################################################################

def GCC():
    import time, colorama, os, sys

    print(colorama.Fore.BLUE +" · GCC + G++: The GNU Compiler Collection is a set of compilers created by the GNU project.")
    input("PRESS ENTER TO CONTINUE...")
    os.system("clear")
    print(colorama.Fore.RED + "UPDATING REPOSITORIES AND PROGRAMS. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    print(colorama.Fore.BLUE +"UPDATE and UPGRADE succesfully finished.")
    time.sleep(1.5)
    print(colorama.Fore.RED +"Installing GCC + G++. . .")
    os.system("sudo apt install gcc -y && sudo apt install g++ -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    os.system("sudo apt autoclean")
    os.system("sudo apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))

############################################################################################################################################################################################################

def MICRO():
    import time, colorama, os, sys

    print(colorama.Fore.WHITE +" · Micro Text Editor: micro a modern and intuitive terminal-based text editor")
    input("PRESS ENTER TO CONTINUE...")
    os.system("clear")
    print(colorama.Fore.RED + "UPDATING REPOSITORIES AND PROGRAMS. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    print(colorama.Fore.BLUE +"UPDATE and UPGRADE succesfully finished.")
    time.sleep(1.5)
    print(colorama.Fore.BLUE +"Installing Micro Text Editor. . .")
    os.system("curl https://getmic.ro | bash")
    os.system("sudo mv micro /usr/bin/")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    os.system("sudo apt autoclean")
    os.system("sudo apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))

############################################################################################################################################################################################################

def TOR():
    import time, colorama, os, sys

    print(colorama.Fore.CYAN +" · Tor Web Browser: Tor is a project whose main objective is the development of a distributed low-latency communications network superimposed on the internet.")
    input("PRESS ENTER TO CONTINUE...")
    os.system("clear")
    print(colorama.Fore.RED + "UPDATING REPOSITORIES AND PROGRAMS. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    print(colorama.Fore.BLUE +"UPDATE and UPGRADE succesfully finished.")
    time.sleep(1.5)
    print(colorama.Fore.GREEN +"Installing Tor Web Browser. . .")
    os.system("add-apt-repository ppa:micahflee/ppa")
    os.system("sudo apt update -y")
    os.system("sudo apt install torbrowser-launcher -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    os.system("sudo apt autoclean")
    os.system("sudo apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))

############################################################################################################################################################################################################

def GOOGLE():
    import time, colorama, os, sys
    
    print(colorama.Fore.RED +" · Chrome Web Browser: Google Chrome is a closed source web browser developed by Google, although derived from open source projects.")
    input("PRESS ENTER TO CONTINUE...")
    os.system("clear")
    print(colorama.Fore.RED + "UPDATING REPOSITORIES AND PROGRAMS. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    print(colorama.Fore.BLUE +"UPDATE and UPGRADE succesfully finished.")
    time.sleep(1.5)
    print(colorama.Fore.MAGENTA +"Installing Chrome Web Browser. . .")
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("sudo apt install ./google-chrome-stable_current_amd64.deb -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("sudo rm google-chrome-stable_current_amd64.deb")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    os.system("sudo apt autoclean")
    os.system("sudo apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))

############################################################################################################################################################################################################

def GIMP():
    import time, colorama, os, sys

    print(colorama.Fore.GREEN +" · GIMP: Gimp is a digital image editing program in the form of a bitmap, both drawings and photographs. It is a free and free program.")
    input("PRESS ENTER TO CONTINUE...")
    os.system("clear")
    print(colorama.Fore.RED + "UPDATING REPOSITORIES AND PROGRAMS. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    print(colorama.Fore.BLUE +"UPDATE and UPGRADE succesfully finished.")
    time.sleep(1.5)
    print(colorama.Fore.WHITE +"Installing GIMP. . .")
    os.system("add-apt-repository ppa:otto-kesselgulasch/gimp-edge")
    os.system("sudo apt update -y && sudo apt install gimp gimp-gmic -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    os.system("sudo apt autoclean")
    os.system("sudo apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))

############################################################################################################################################################################################################

def WINE():
    import time, colorama, os, sys

    print(colorama.Fore.MAGENTA +" · WINE: Wine is a reimplementation of the Win16 and Win32 application programming interface for Unix-based operating systems.")
    input("PRESS ENTER TO CONTINUE...")
    os.system("clear")
    print(colorama.Fore.RED + "UPDATING REPOSITORIES AND PROGRAMS. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    print(colorama.Fore.BLUE +"UPDATE and UPGRADE succesfully finished.")
    time.sleep(1.5)
    print(colorama.Fore.CYAN +"Installing WINE. . .")
    os.system("sudo apt install wine64 -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    os.system("sudo apt autoclean")
    os.system("sudo apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))

############################################################################################################################################################################################################

def BLENDER():
    import time, colorama, os, sys

    print(colorama.Fore.BLUE +" · Blender: Blender is a multi-platform computer program, especially dedicated to modeling, lighting, rendering, animating, and creating 3D graphics.")
    input("PRESS ENTER TO CONTINUE...")
    os.system("clear")
    print(colorama.Fore.RED + "UPDATING REPOSITORIES AND PROGRAMS. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    print(colorama.Fore.BLUE +"UPDATE and UPGRADE succesfully finished.")
    time.sleep(1.5)
    print(colorama.Fore.RED +"Installing Blender. . .")
    os.system("sudo apt install blender")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    os.system("sudo apt autoclean")
    os.system("sudo apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))

############################################################################################################################################################################################################

def AUDACITY():
    import time, colorama, os, sys
    
    print(colorama.Fore.WHITE +" · Audacity: Audacity is a free cross-platform computer application, which can be used for audio recording and editing, distributed under the GPLv2 license.")
    input("PRESS ENTER TO CONTINUE...")
    os.system("clear")
    print(colorama.Fore.RED + "UPDATING REPOSITORIES AND PROGRAMS. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    print(colorama.Fore.BLUE +"UPDATE and UPGRADE succesfully finished.")
    time.sleep(1.5)
    print(colorama.Fore.BLUE +"Installing Audacity. . .")
    os.system("sudo apt install audacity -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    os.system("sudo apt autoclean")
    os.system("sudo apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))

############################################################################################################################################################################################################

def GIT():
    import time, colorama, os, sys

    print(colorama.Fore.RED + " · Git: Git is a version control software designed by Linus Torvalds, thinking about the efficiency and reliability of application version maintenance.") 
    input("PRESS ENTER TO CONTINUE...")
    os.system("clear")
    print(colorama.Fore.RED + "UPDATING REPOSITORIES AND PROGRAMS. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    print(colorama.Fore.BLUE +"UPDATE and UPGRADE succesfully finished.")
    time.sleep(1.5)
    print(colorama.Fore.GREEN +"Installing GIT. . .")
    os.system("sudo apt install git -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    os.system("sudo apt autoclean")
    os.system("sudo apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))

############################################################################################################################################################################################################

def STEAM():
    import time, colorama, os, sys

    print(colorama.Fore.CYAN + " · Steam: Steam is a digital video game distribution platform developed by Valve Corporation.") 
    input("PRESS ENTER TO CONTINUE...")
    os.system("clear")
    print(colorama.Fore.GREEN + "UPDATING REPOSITORIES AND PROGRAMS. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    print(colorama.Fore.BLUE +"UPDATE and UPGRADE succesfully finished.")
    time.sleep(1.5)
    print(colorama.Fore.MAGENTA +"Installing STEAM. . .")
    os.system("add-apt-repository multiverse")
    os.system("sudo apt update -y && apt upgrade -y")
    os.system("sudo apt install steam -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    os.system("sudo apt autoclean")
    os.system("sudo apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

############################################################################################################################################################################################################

def VLC():
    import time, colorama, os, sys

    print(colorama.Fore.WHITE + " · VLC media player is a free and open source multimedia player and framework developed by the VideoLAN project.") 
    input("PRESS ENTER TO CONTINUE...")
    os.system("clear")
    print(colorama.Fore.RED + "UPDATING REPOSITORIES AND PROGRAMS. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    print(colorama.Fore.GREEN +"UPDATE and UPGRADE succesfully finished.")
    time.sleep(1.5)
    print(colorama.Fore.CYAN +"Installing VLC. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    os.system("sudo apt install vlc -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    os.system("sudo apt autoclean")
    os.system("sudo apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

############################################################################################################################################################################################################