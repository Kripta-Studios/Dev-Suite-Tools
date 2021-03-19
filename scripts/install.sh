sudo chmod a+x devSuite.py && sudo chmod a+x update.sh && sudo chmod a+x uninst000.sh
sudo cp devSuite.py devsuite
sudo mv devsuite /usr/bin/
sudo cp installAll.py /usr/bin/ && sudo cp installBasics.py /usr/bin/ && sudo cp lonePrograms.py /usr/bin/ && sudo cp tryConnect.py /usr/bin/ && sudo cp isConnect.py /usr/bin/
echo To executeuse devsuite install <pkg>
