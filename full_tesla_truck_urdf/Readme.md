# Steps to create a urdf file from solidwoks

 1) http://wiki.ros.org/sw_urdf_exporter This link will help you  to download the sw2urdf .exe for different versions of solidworks.

 2) After downloading the .exe file. Go to options > Add-Ins > In the end the sw2urdf file is their not. If not restart the solidworks and check once again.

 3) Follow our video for further process.   

 After creating the file create .gazebo and launch file 
 bfl_14 in dharmendra_model is same of full_tesla_truck_urdf
 
**The below command is used to open the model which is extracted from solidworks.**

$roslaunch full_tesla_truck_urdf gazebo.launch

![Screenshot from 2023-01-07 14-48-58](https://user-images.githubusercontent.com/121598999/211143400-58e494a9-63e6-4b1f-b782-5cc43ad06f1e.png)
