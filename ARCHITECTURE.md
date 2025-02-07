## What is the problem?
Originally doodle effects need tremendous work for designer to draw.
Many software such as Adobe After Effect. Still this software suggest
half automatic(tracking) UI.
We will offer fully automatic software, also maintaining the idea of design.

#### Architecture Picture
![a](Image/Architecture/Architecture_Version1.0.png)

#### GUI/UI Expectation Picture
Expectation

![](Image/Architecture/GUI_Version1.3.png)

Current

![](Image/Result/GUI_Program3.PNG)

#### Development Expectation Picture
<div align="center">
    <img src="Image/Architecture/development_flow_version1.0.png" width="600">
</div>

<div align="center">
    <img src="Image/Architecture/Detectron2_Visualizer_Description.PNG" width="600">
</div>


##### Template GUI
* Video loading window
* Effect changing window
* Effect selecting window
* Video time selection window
* Video current play bar window
* Save/Change/Delete bar window

##### Functions
* Detection processing file
* Effect implementation file


##### Database (Future Work)

## GUI Language
[PtQy5](https://build-system.fman.io/pyqt5-tutorial):
[Tutorial](http://codetorial.net/pyqt5/basics/icon.html):
[What is pyqt](https://steemit.com/kr/@papasmf1/python-pyqt-gui-graphical-user-interface)  
[Pygtk VS Pyqt VS WxPython VS Tkinter](http://codingdojang.com/scode/257)

## Algorithm Language
Python, C++(Expected)

## Web Language
Django(if it is needed)

##References
[GUI],[DEV],[GIT]
* [[DEV] How to make webapp architecture](https://cs.lmu.edu/~ray/notes/webapps/)

* [[DEV] Useful diagram for understanding Python based architecture flow](https://www.researchgate.net/figure/ODM-Tools-Python-software-architecture_fig2_275673185)

* [[DEV] What is the differences between Back and Front Developer](https://moolgogiheart.tistory.com/16)

* [[GIT] Pull request](https://gmlwjd9405.github.io/2017/10/27/how-to-collaborate-on-GitHub-1.html)

* [Related Video(GUI, Python, OpenCV collaboration)](https://www.youtube.com/watch?v=6RCDWMEitDI)

* [[GUI] Automatic resize problem in PyQt5](https://www.youtube.com/watch?v=Y-8N1dPFsVE)

* [[GUI] Problem of automatic resizes in GUI](https://www.youtube.com/watch?v=FOIbK4bJKS8)

* How to import tensorflow-gpu in executable file

[Source 1](https://siran.tistory.com/69?category=846941)

[Source 2](https://www.youtube.com/watch?v=fLQg8dgB7cA)

* [GIT] What is the difference between branch and master

[git branch](https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%B8%8C%EB%9E%9C%EC%B9%98%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80)  
* [[GIT] How to handle the branch](https://trustyoo86.github.io/git/2017/11/28/git-remote-branch-create.html)

[git hotfix and branch](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)

* [[GUI] Useful example of GUI template](https://github.com/pyqt/examples)

Branch is made because of avoid interaction between other branch and master.

*[[GUI] merge, branch, master](https://backlog.com/git-tutorial/kr/stepup/stepup2_5.html)

[[GIT] How to organize the files with .gitignore.txt](https://blockchain-baam.tistory.com/3)

##Extra Information about Library setting
install tqdm -> conda install tqdm

intall detectron2 -> 
first install pytorch: 
Installed with conda altough I expect that I don't have cuda 10.1 I installed with cuda 10.1 version
conda install pytorch torchvision cudatoolkit=10.1 -c pytorch

second install fvcore: 
pip install git+https://github.com/facebookresearch/fvcore

install cython -> conda install cython

This also includes in installing pycocotools

This would work instead of description on detectron2
pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI

and then load the setup.py do the process of [python setup.py build develop]
