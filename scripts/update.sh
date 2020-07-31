cd ../../
sudo rm -rf Dev-Suite-Tools/
sudo rm /usr/bin/installAll.py
sudo rm /usr/bin/lonePrograms.py
sudo rm /usr/bin/installBasics.py
sudo rm /usr/bin/devsuite
git clone https://github.com/Kripta-Studios/Dev-Suite-Tools.git
sudo chmod a+x Dev-Suite-Tools/scripts/install.sh
cd Dev-Suite-Tools/scripts/
sudo ./install.sh
echo Dev-Suite-Tools upgrade succesfully.
