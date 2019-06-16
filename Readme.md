# Autonomous Indoor Navigation Robot using Raspberry Pi.

## Hardware and Software Components required:
- ### Hardware Requirements
	- #### Raspberry Pi 3.
	- #### Gyroscope and accelerometer sensor.
	- #### Motor driver (L293D). 
	- #### Wheels and chassis.
	- #### Ultrasonic sensors (HC-SR04).
	- #### Motors for wheels.
	- #### Breadboard and jumper cables.
- ### Software Requirements
	- #### Raspbian Jessi OS.
	- #### Python.
	
## Steps to build the robot : 
1. Install Raspbian Jessi Operating System and configure the settings to the Raspberry Pi.
2. Set up the motor driver(L293D) and the motors for the wheels.
3. Connect them via breadboard to the Raspberry Pi, as per the GPIO pins.
4. Connect the ultrasonic sensors to the Raspberry Pi.
5. Connect the lead acid battery (power supply 12V) via a common ground to the Raspberry Pi.
6. Connect a 5V (2A) power supply to the Raspberry Pi.
7. Program the wheels according to their GPIO pins to move forward, backward, left and right.
8. Program the ultrasonic sensor to do obstacle avoidance by setting a condition to stop at encountering an obstacle at a particular distance.
9. Program the accelerometer and gyroscope to obtain the speed and direction from them.
10. Have the accelerometer and gyroscope data for orientation of the robot and to improve the accuracy.
11. Set up a database to store the values from accelerometer and gyroscope.
12. Set up a keyboard control code to allow manual control of the robot and to populate a data file.
13. The data file will have the direction and time of motion of the robot. (It is the output of the keyboard controls code)
14. Import the data file to another python code which for the motion of the robot in all directions automatically
15. In the python code for automatic run, compare the values from the data file to check for the direction and time for running the robot.
16. Once the program reads and understands the data from the data, it will then allow the robot to run automatically in the path the robot has already taken manually via the keyboard controls.
17. Use data from accelerometer and gyroscope to improve the accuracy, by making use of a filter (Kalman).
18. Regulate the voltage to keep the speed constant with time.
19. Now, run the robot in the desired path using the keyboard controls and obtain the data in the data  file.
20. Then run the code for automatic run of robot and the robot will take the path which was already taken.

