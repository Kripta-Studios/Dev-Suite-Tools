sudo chmod a+x devSuite.py
sudo cp devSuite.py devsuite
sudo mv devsuite /usr/bin/
sudo cp installAll.py /usr/bin/ && sudo cp installBasics.py /usr/bin/ && sudo cp lonePrograms.py /usr/bin/
echo To execute use devsuite install <pkg>
