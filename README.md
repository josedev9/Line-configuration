# Line configuration project

Creation of the config_nvdsanalytics.txt file for the line creation in the Deepstream SDK

## Description

This python scripts provide the oportunity to save a camera frame, draw the required line points definition for deepstream and update the destination file in the Nvidia Jetson.

## Getting Started

### Dependencies

* Prior to running the main.py script it is recommended to create a virtual environment based on the requirements.txt file added in the project.
 ```
$ sudo apt-get install python3-pip
$ python -m pip install virtualenvwrapper
```
* Create a virtual environment using the requirements.txt file added in this repository
```
$ virtualenv -r /path/to/repository/folder/requirements.txt name_of_venv
```

### Installing
```
git clone https://www.github.com/josedev9/Line-configuration.git
```


### Executing program

* How to run the program
* Capture a frame with the camera
```
$ python3 .\main.py -s name_of_frame_to_save
```
* Select the 2 direction points of the line and the 2 required points for the line definition, once the GUI has been opened.
* Click to select each of the points, a circle and then a line will apear on the screen, to restart press the r key.
* Once done press q to exit the app and to save the coordinates in the appropriate file.

## Help

Any advise for common problems or issues.
```
$ python3 .\main.py --help
```
