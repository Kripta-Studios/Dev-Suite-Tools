#! /usr/bin/python3


def installBasics():
    import time, colorama, os, sys

    print(colorama.Fore.CYAN +"The following programs are going to install:\n" + colorama.Fore.GREEN + " · VIM: Vim is an improved version of the Vi text editor, present on all UNIX systems.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.RED +" · GVIM: It is an open source program released under the GNU license. It is a graphic version of the Vim text editor.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.GREEN +" · VSCode: Visual Studio Code is a source code editor developed by Microsoft for Windows, Linux and macOS.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.MAGENTA +" · Code::Blocks: Code :: Blocks is an open source integrated development environment, supporting multiple compilers, including GCC, Clang, and Visual C ++.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.BLUE +" · GCC + G++: The GNU Compiler Collection is a set of compilers created by the GNU project.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.WHITE +" · Micro Text Editor: micro a modern and intuitive terminal-based text editor")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.CYAN +" · Tor Web Browser: Tor is a project whose main objective is the development of a distributed low-latency communications network superimposed on the internet.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.RED +" · Chrome Web Browser: Google Chrome is a closed source web browser developed by Google, although derived from open source projects.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.GREEN +" · GIMP: Gimp is a digital image editing program in the form of a bitmap, both drawings and photographs. It is a free and free program.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.MAGENTA +" · WINE: Wine is a reimplementation of the Win16 and Win32 application programming interface for Unix-based operating systems.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.BLUE +" · Blender: Blender is a multi-platform computer program, especially dedicated to modeling, lighting, rendering, animating, and creating 3D graphics.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.WHITE +" · Audacity: Audacity is a free cross-platform computer application, which can be used for audio recording and editing, distributed under the GPLv2 license.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.RED + " · Git: Git is a version control software designed by Linus Torvalds, thinking about the efficiency and reliability of application version maintenance.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.RED + " · Steam: Steam is a digital video game distribution platform developed by Valve Corporation.")
    input("PRESS ENTER TO CONTINUE...")

    os.system("clear")
    print(colorama.Fore.RED + "UPDATING REPOSITORIES AND PROGRAMS. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    print(colorama.Fore.BLUE +"UPDATE and UPGRADE succesfully finished.")
    time.sleep(1.5)
    input(colorama.Fore.WHITE + "IF are you SURE that you wanna continue press enter, else Ctrl^C. . ." )
    print(colorama.Fore.GREEN +"Installing VIM. . .")
    os.system("apt install vim -y")
    time.sleep(1.5)
    print(colorama.Fore.MAGENTA +"Installing GVIM. . .")
    os.system("apt install vim-gtk3 -y")
    time.sleep(1.5)
    print(colorama.Fore.WHITE +"Installing VSCode. . .")
    os.system("apt install software-properties-common apt-transport-https wget -y")
    os.system("wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -")
    os.system("add-apt-repository \"deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main\"")
    os.system("apt update -y")
    os.system("apt install code -y")
    time.sleep(1.5)
    print(colorama.Fore.CYAN+"Installing Code::Blocks. . .")
    os.system("apt install codeblocks -y")
    time.sleep(1.5)
    print(colorama.Fore.RED +"Installing GCC + G++. . .")
    os.system("apt install gcc -y && apt install g++ -y")
    time.sleep(1.5)
    print(colorama.Fore.BLUE +"Installing Micro Text Editor. . .")
    os.system("curl https://getmic.ro | bash")
    os.system("mv micro /usr/bin/")
    time.sleep(1.5)
    print(colorama.Fore.GREEN +"Installing Tor Web Browser. . .")
    os.system("add-apt-repository ppa:micahflee/ppa")
    os.system("apt update -y")
    os.system("apt install torbrowser-launcher -y")
    time.sleep(1.5)
    print(colorama.Fore.MAGENTA +"Installing Chrome Web Browser. . .")
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("apt install ./google-chrome-stable_current_amd64.deb -y")
    time.sleep(1.5)
    print(colorama.Fore.WHITE +"Installing GIMP. . .")
    os.system("add-apt-repository ppa:otto-kesselgulasch/gimp-edge")
    os.system("apt update -y && sudo apt install gimp gimp-gmic -y")
    time.sleep(1.5)
    print(colorama.Fore.CYAN +"Installing WINE. . .")
    os.system("apt install wine64 -y")
    time.sleep(1.5)
    print(colorama.Fore.RED +"Installing Blender. . .")
    os.system("apt install blender -y")
    time.sleep(1.5)
    print(colorama.Fore.BLUE +"Installing Audacity. . .")
    os.system("apt install audacity -y")
    time.sleep(1.5)
    print(colorama.Fore.GREEN +"Installing GIT. . .")
    os.system("apt install git -y")
    time.sleep(1.5)
    print(colorama.Fore.MAGENTA + "Installing Steam. . .")
    os.system("add-apt-repository multiverse")
    os.system("apt update -y && apt upgrade -y")
    os.system("apt install steam")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("apt update -y && apt upgrade -y")
    os.system("rm google-chrome-stable_current_amd64.deb")
    os.system("apt autoclean")
    os.system("apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED + colorama.Style.BRIGHT +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))
    
    infoFile = open("DownloadedPrograms.doc","w+")
    infoFile.write("The following programs are going to install:\n\nVIM: Vim is an improved version of the Vi text editor, present on all UNIX systems.\n\nGVIM: It is an open source program released under the GNU license. It is a graphic version of the Vim text editor.\n\nVSCode: Visual Studio Code is a source code editor developed by Microsoft for Windows, Linux and macOS.\n\nCode::Blocks: Code :: Blocks is an open source integrated development environment, supporting multiple compilers, including GCC, Clang, and Visual C ++.\n\nGCC + G++: The GNU Compiler Collection is a set of compilers created by the GNU project.\nMicro Text Editor: micro a modern and intuitive terminal-based text editor.\n\nTor Web Browser: Tor is a project whose main objective is the development of a distributed low-latency communications network superimposed on the internet.\n\nChrome Web Browser: Google Chrome is a closed source web browser developed by Google, although derived from open source projects.\n\nGIMP: Gimp is a digital image editing program in the form of a bitmap, both drawings and photographs. It is a free and free program.\n\nWINE: Wine is a reimplementation of the Win16 and Win32 application programming interface for Unix-based operating systems.\n\nBlender: Blender is a multi-platform computer program, especially dedicated to modeling, lighting, rendering, animating, and creating 3D graphics.\n\nAudacity: Audacity is a free cross-platform computer application, which can be used for audio recording and editing, distributed under the GPLv2 license.\n\nGit: Git is a version control software designed by Linus Torvalds, thinking about the efficiency and reliability of application version maintenance.\nSteam: Steam is a digital video game distribution platform developed by Valve Corporation.\n\nDeveloped by Kripta Studios 2020")
    sys.exit()



def installAll():
    import time, colorama, os, sys

    print(colorama.Fore.CYAN +"The following programs are going to install:\n" + colorama.Fore.GREEN + " · VIM: Vim is an improved version of the Vi text editor, present on all UNIX systems.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.RED +" · GVIM: It is an open source program released under the GNU license. It is a graphic version of the Vim text editor.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.GREEN +" · VSCode: Visual Studio Code is a source code editor developed by Microsoft for Windows, Linux and macOS.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.MAGENTA +" · Code::Blocks: Code :: Blocks is an open source integrated development environment, supporting multiple compilers, including GCC, Clang, and Visual C ++.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.BLUE +" · GCC + G++: The GNU Compiler Collection is a set of compilers created by the GNU project.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.WHITE +" · Micro Text Editor: micro a modern and intuitive terminal-based text editor")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.CYAN +" · Tor Web Browser: Tor is a project whose main objective is the development of a distributed low-latency communications network superimposed on the internet.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.RED +" · Chrome Web Browser: Google Chrome is a closed source web browser developed by Google, although derived from open source projects.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.GREEN +" · GIMP: Gimp is a digital image editing program in the form of a bitmap, both drawings and photographs. It is a free and free program.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.MAGENTA +" · WINE: Wine is a reimplementation of the Win16 and Win32 application programming interface for Unix-based operating systems.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.BLUE +" · Blender: Blender is a multi-platform computer program, especially dedicated to modeling, lighting, rendering, animating, and creating 3D graphics.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.WHITE +" · Audacity: Audacity is a free cross-platform computer application, which can be used for audio recording and editing, distributed under the GPLv2 license.")
    input("PRESS ENTER TO CONTINUE...")
    print(colorama.Fore.RED + " · Steam: Steam is a digital video game distribution platform developed by Valve Corporation.")
    input("PRESS ENTER TO CONTINUE...")

    os.system("clear")
    print(colorama.Fore.RED + "UPDATING REPOSITORIES AND PROGRAMS. . .")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    print(colorama.Fore.BLUE +"UPDATE and UPGRADE succesfully finished.")
    time.sleep(1.5)
    input(colorama.Fore.WHITE + "IF are you SURE that you wanna continue press enter, else Ctrl^C. . ." )
    print(colorama.Fore.GREEN +"Installing VIM. . .")
    os.system("apt install vim -y")
    time.sleep(1.5)
    print(colorama.Fore.MAGENTA +"Installing GVIM. . .")
    os.system("apt install vim-gtk3 -y")
    time.sleep(1.5)
    print(colorama.Fore.WHITE +"Installing VSCode. . .")
    os.system("apt install software-properties-common apt-transport-https wget -y")
    os.system("wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -")
    os.system("add-apt-repository \"deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main\"")
    os.system("apt update -y")
    os.system("apt install code -y")
    time.sleep(1.5)
    print(colorama.Fore.CYAN+"Installing Code::Blocks. . .")
    os.system("apt install codeblocks -y")
    time.sleep(1.5)
    print(colorama.Fore.RED +"Installing GCC + G++. . .")
    os.system("apt install gcc -y && apt install g++ -y")
    time.sleep(1.5)
    print(colorama.Fore.BLUE +"Installing Micro Text Editor. . .")
    os.system("curl https://getmic.ro | bash")
    os.system("mv micro /usr/bin/")
    time.sleep(1.5)
    print(colorama.Fore.GREEN +"Installing Tor Web Browser. . .")
    os.system("add-apt-repository ppa:micahflee/ppa")
    os.system("apt update -y")
    os.system("apt install torbrowser-launcher -y")
    time.sleep(1.5)
    print(colorama.Fore.MAGENTA +"Installing Chrome Web Browser. . .")
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("apt install ./google-chrome-stable_current_amd64.deb -y")
    time.sleep(1.5)
    print(colorama.Fore.WHITE +"Installing GIMP. . .")
    os.system("add-apt-repository ppa:otto-kesselgulasch/gimp-edge")
    os.system("apt update -y && sudo apt install gimp gimp-gmic -y")
    time.sleep(1.5)
    print(colorama.Fore.CYAN +"Installing WINE. . .")
    os.system("apt install wine64 -y")
    time.sleep(1.5)
    print(colorama.Fore.RED +"Installing Blender. . .")
    os.system("apt install blender -y")
    time.sleep(1.5)
    print(colorama.Fore.BLUE +"Installing Audacity. . .")
    os.system("apt install audacity -y")
    time.sleep(1.5)
    print(colorama.Fore.GREEN +"Installing GIT. . .")
    os.system("apt install git -y")
    time.sleep(1.5)
    print(colorama.Fore.MAGENTA + "Installing Steam. . .")
    os.system("add-apt-repository multiverse")
    os.system("apt update -y && apt upgrade -y")
    os.system("apt install steam")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("apt update -y && apt upgrade -y")
    os.system("rm google-chrome-stable_current_amd64.deb")
    os.system("apt autoclean")
    os.system("apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED + colorama.Style.BRIGHT +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))
    
    infoFile = open("DownloadedPrograms.doc","w+")
    infoFile.write("The following programs are going to install:\n\nVIM: Vim is an improved version of the Vi text editor, present on all UNIX systems.\n\nGVIM: It is an open source program released under the GNU license. It is a graphic version of the Vim text editor.\n\nVSCode: Visual Studio Code is a source code editor developed by Microsoft for Windows, Linux and macOS.\n\nCode::Blocks: Code :: Blocks is an open source integrated development environment, supporting multiple compilers, including GCC, Clang, and Visual C ++.\n\nGCC + G++: The GNU Compiler Collection is a set of compilers created by the GNU project.\nMicro Text Editor: micro a modern and intuitive terminal-based text editor.\n\nTor Web Browser: Tor is a project whose main objective is the development of a distributed low-latency communications network superimposed on the internet.\n\nChrome Web Browser: Google Chrome is a closed source web browser developed by Google, although derived from open source projects.\n\nGIMP: Gimp is a digital image editing program in the form of a bitmap, both drawings and photographs. It is a free and free program.\n\nWINE: Wine is a reimplementation of the Win16 and Win32 application programming interface for Unix-based operating systems.\n\nBlender: Blender is a multi-platform computer program, especially dedicated to modeling, lighting, rendering, animating, and creating 3D graphics.\n\nAudacity: Audacity is a free cross-platform computer application, which can be used for audio recording and editing, distributed under the GPLv2 license.\n\nGit: Git is a version control software designed by Linus Torvalds, thinking about the efficiency and reliability of application version maintenance.\nSteam: Steam is a digital video game distribution platform developed by Valve Corporation.\n\nDeveloped by Kripta Studios 2020")
    sys.exit()

def argvAll():
    try:
        import colorama, os, sys, time, random
        installAll()
    except:
        dependenciesInstaller()

def dependenciesInstaller():
    import os,sys

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

        main2()
    else:
        print("\n\n")
        sys.exit()


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
    os.system("apt install vim -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("apt update -y && apt upgrade -y")
    os.system("apt autoclean")
    os.system("apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))

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
    os.system("apt install vim-gtk3 -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("apt update -y && apt upgrade -y")
    os.system("apt autoclean")
    os.system("apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))


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
    os.system("apt install software-properties-common apt-transport-https wget -y")
    os.system("wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -")
    os.system("add-apt-repository \"deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main\"")
    os.system("apt update -y")
    os.system("apt install code -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("apt update -y && apt upgrade -y")
    os.system("apt autoclean")
    os.system("apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))


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
    os.system("apt install codeblocks -y")
    time.sleep(1.5)
    print(colorama.Fore.RED +"Installing GCC + G++. . .")
    os.system("apt install gcc -y && apt install g++ -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("apt update -y && apt upgrade -y")
    os.system("apt autoclean")
    os.system("apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))


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
    os.system("apt install gcc -y && apt install g++ -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("apt update -y && apt upgrade -y")
    os.system("apt autoclean")
    os.system("apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))


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
    os.system("mv micro /usr/bin/")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("apt update -y && apt upgrade -y")
    os.system("apt autoclean")
    os.system("apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))


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
    os.system("apt update -y")
    os.system("apt install torbrowser-launcher -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("apt update -y && apt upgrade -y")
    os.system("apt autoclean")
    os.system("apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))


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
    os.system("apt install ./google-chrome-stable_current_amd64.deb -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("rm google-chrome-stable_current_amd64.deb")
    os.system("apt update -y && apt upgrade -y")
    os.system("apt autoclean")
    os.system("apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))

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
    os.system("apt update -y && sudo apt install gimp gimp-gmic -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("apt update -y && apt upgrade -y")
    os.system("apt autoclean")
    os.system("apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))


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
    os.system("apt install wine64 -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("apt update -y && apt upgrade -y")
    os.system("apt autoclean")
    os.system("apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))


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
    os.system("apt install blender")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("apt update -y && apt upgrade -y")
    os.system("apt autoclean")
    os.system("apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))


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
    os.system("apt install audacity -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("apt update -y && apt upgrade -y")
    os.system("apt autoclean")
    os.system("apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))


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
    os.system("apt install git -y")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("apt update -y && apt upgrade -y")
    os.system("apt autoclean")
    os.system("apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

    os.system("clear")
    print("Installation finished. Comprobe all the programs, you have a list of the installed programs in this directory. If any program don't run or aren't install report it.")
    print(colorama.Fore.RED +"Kripta Studios made this program.")
    time.sleep(2)
    print(colorama.Fore.RESET +"Press enter to close this program. . .")
    str(input(''))

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
    os.system("apt update -y && apt upgrade -y")
    os.system("apt install steam")
    time.sleep(1.5)
    print("Finishing the installation. . .")
    os.system("apt update -y && apt upgrade -y")
    os.system("apt autoclean")
    os.system("apt autoremove")
    time.sleep(2)
    input("Press ENTER. . .")

def main():
    try:
        import os, sys, colorama, time, random

        install = sys.argv[1].lower() == "install"
        lenght = len(sys.argv) == 3

        if install and sys.argv[2].lower() == "all" and lenght:
            argvAll()

        elif install and sys.argv[2].lower() == "basics" and lenght:
            argvAll()

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

        elif install and sys.argv[2].lower() != "git" or sys.argv[2].lower() != "blender" or sys.argv[2].lower() != "wine" or sys.argv[2].lower() != "audacity" or sys.argv[2].lower() != "gimp" or sys.argv[2].lower() != "chrome" or sys.argv[2].lower() != "tor" or sys.argv[2].lower() != "micro" or sys.argv[2].lower() != "all" or sys.argv[2].lower() != "gccg++" or sys.argv[2].lower() != "codeblocks" or sys.argv[2].lower() != "vscode" or sys.argv[2].lower() != "gvim" or sys.argv[2].lower() != "vim" and lenght or sys.argv[2].lower() != "steam" and lenght:
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
            print("All the programs  |         devSuite install all")

    except:
        dependenciesInstaller()



def main2():
    import os, sys, colorama, time, random
    try:
        if sys.argv[1].lower() == "install":
            install = sys.argv[1].lower() == "install"
            lenght = len(sys.argv) == 3

            if install and sys.argv[2].lower() == "all" and lenght:
                installBasics()

            elif install and sys.argv[2].lower() == "basics" and lenght:
                installAll()

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

            elif install and sys.argv[2].lower() != "git" or sys.argv[2].lower() != "blender" or sys.argv[2].lower() != "wine" or sys.argv[2].lower() != "audacity" or sys.argv[2].lower() != "gimp" or sys.argv[2].lower() != "chrome" or sys.argv[2].lower() != "tor" or sys.argv[2].lower() != "micro" or sys.argv[2].lower() != "all" or sys.argv[2].lower() != "gccg++" or sys.argv[2].lower() != "codeblocks" or sys.argv[2].lower() != "vscode" or sys.argv[2].lower() != "gvim" or sys.argv[2].lower() != "vim" and lenght or sys.argv[2].lower() != "steam" and lenght:
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
                print("All the programs  |         devSuite install all")

    except:
        print("For now you must use this syntax: devSuite install <pkg>")

main()
