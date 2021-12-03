from robot import *

class GyroBoy(Robot):
    def __init__(self, behavior_matches):
        super().__init__(behavior_matches)

        ##MOTORS
        # Initialize a motor at port C, for both arms
        arm_motor = Motor(Port.C)
        # Initialize right wheel motor
        rightwheel_motor = Motor(Port.A)
        # Initialize left wheel motor 
        leftwheel_motor = Motor(Port.D)
        bothwheels = DriveBase(leftwheel_motor, rightwheel_motor, 5.5,10.25) # left motor right motor, wheel diameter, distance between wheels
        
        #SENSORS
        obstacle_sensor = UltrasonicSensor(Port.S4)
        GoButton = TouchSensor(Port.S3)

    def step_0_node_0_action(self):
        self.ev3.screen.load_image(ImageFile.AWAKE)
        print("Step 0 Node 0 complete")

    def step_1_node_0_action(self):
        self.ev3.screen.load_image(ImageFile.LOVE)
        print("Step 1 Node 0 complete")
    def step_1_node_0_action(self):
        