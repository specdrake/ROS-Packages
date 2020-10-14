# ROS-Packages
A repo to store ROS packages

#### learning_tf
Usage : ``roslaunch learning_tf py_start_demo.launch`` 

#### model
Usage : ``roslaunch model gazebo.launch`` followed by ``roslaunch model display.launch`` and finally ``roslaunch model gmapping.launch``

#### alvar_webcam
Usage : 

1) Put head_camera.yaml at ```~/.ros/camera_info/head_camera.yaml```
2) roslaunch alvar_webcam usb_cam_ar_track.launch
