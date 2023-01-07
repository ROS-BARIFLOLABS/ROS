# THIS  FILE IS USED TO CONVERT SDF FILES TO URDF FILES IN RESPECTIVE LOCATION. 
  **first change the version of sdf 1.7 to 1.5** 
 ![image](https://user-images.githubusercontent.com/121598999/211146458-287c0a12-d17e-4814-89e7-03fee86e6e50.png)


$ rosrun pysdf sdf2urdf.py  sdf_file_name   urdf_file_name

**example:** rosrun pysdf sdf2urdf.py model.sdf bfl_14.urdf.xacro
