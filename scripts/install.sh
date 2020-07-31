sudo chmod a+x devSuite.py && sudo chmod a+x update.sh && sudo chmod a+x uninst000.sh
sudo cp devSuite.py devsuite
sudo mv devsuite /usr/bin/
sudo cp installAll.py /usr/bin/ && sudo cp installBasics.py /usr/bin/ && sudo cp lonePrograms.py /usr/bin/
echo To execute use devsuite install <pkg>
