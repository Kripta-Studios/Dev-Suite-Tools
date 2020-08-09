if ping -q -c 1 -W 1 google.com >/dev/null; then
  echo "The network is up and ready to update. . ."

  cd ../../
  sudo rm -rf Dev-Suite-Tools/
  sudo rm /usr/bin/installAll.py
  sudo rm /usr/bin/lonePrograms.py
  sudo rm /usr/bin/installBasics.py
  sudo rm /usr/bin/devsuite
  git clone https://github.com/Kripta-Studios/Dev-Suite-Tools.git
  sudo chmod a+x Dev-Suite-Tools/scripts/install.sh && sudo chmod a+x Dev-Suite-Tools/scripts/update.sh && sudo chmod a+x Dev-Suite-Tools/scripts/uninst000.sh
  cd Dev-Suite-Tools/scripts/
  sudo ./install.sh
  echo Dev-Suite-Tools upgrade succesfully.

else
  echo "The network is down unable to update . . ."
fi



