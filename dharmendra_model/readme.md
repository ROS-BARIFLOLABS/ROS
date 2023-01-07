# The different bfl files explains the different types of upgradation and minimizing the errors we had gone through.

**bfl_1** is the initial designed vehicle in gazebo.

**bfl_3** DEALS WITH THE TWO-WHEELED ROBOT+CASTOR WHEEL. THE GAZEBO FILES ARE DISTINGUISHED IN 3 FILE's I.E. .materials, .physics,.plugins (WHICH USES DIFFERENTIAL DRIVE PLUGIN ). These files are similar to .gazebo file but for understanding purpose we have separated it.

Initially we were unable to get color of the vehicle. So after some changes in  we have created a new file **bfl_5**(**four wheeled + lidar on TOP)** this  shows the color of vehicle. We also trying to see the lidar data in rviz but couldn't because lidar rays were around the lidar only which couldnt show the stationaried model.

**bfl_6_update(2 WHEELED +LIDAR)** is the solution for the above problem addition to color of the vehicle.

Now we need a 3D view of the object present in front of vehicle or the lidar detectd object. We can use openni_kinect camera to see the object in 3D view.

**bfl_8, bfl_9, bfl_10** deals with the axis rotation of camera object to project the camera view combined with lidar view.

**bfl_12** is the solution where the camera and lidar projection is coincide. For addition we can do 2D mapping in rviz.

# Launch_files of bfl_14 model

$ roslaunch dharmendra_model bfl_14.launch

**The below screenshots are the resultant view of the commnads**

![Screenshot from 2023-01-07 14-42-51](https://user-images.githubusercontent.com/121598999/211143219-6d07f6da-5ecc-4b32-a730-62042fd4351f.png)

![Screenshot from 2023-01-07 14-42-42](https://user-images.githubusercontent.com/121598999/211143225-f435d087-d4cd-4129-ba3b-8fe275d6c286.png)

![Screenshot from 2023-01-07 14-41-56](https://user-images.githubusercontent.com/121598999/211143229-4e3acbb4-ea15-4cf2-9bb1-5877b0522c0e.png)

![Screenshot from 2023-01-07 14-42-30](https://user-images.githubusercontent.com/121598999/211143241-41fbd44f-b82b-4289-912e-219be6b93603.png)
