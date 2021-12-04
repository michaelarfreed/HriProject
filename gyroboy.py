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

    def step_0_node_0_action(self): #start
        self.ev3.screen.load_image(ImageFile.AWAKE)
        self.ev3.arm_motor.run_angle(200, 50,then=Stop.HOLD, wait=False)
        print("Step 0 Node 0 complete")

    def step_0_node_1_action(self):
        self.ev3.screen.load_image(ImageFile.LOVE)
        if self.behavior_matches:
            self.ev3.arm_motor.run_angle(200, -50,then=Stop.HOLD, wait=False)
            self.ev3.speaker.say("Thank you!")
            self.load_image(ImageFile.Neutral)
        else:
            pass
        print("Step 0 Node 1 complete")
    def step_1_node_0_action(self):
        if self.behavior_matches:
            self.ev3.arm_motor.run_angle(200,100)
            self.ev3.arm_motor.run_angle(200,-100)
        else:
            pass
    def step_2_node_1_action(self): #vents
        if self.behavior_matches:
            self.ev3.bothwheels.turn(-45)
            self.ev3.speaker.say("This way?")
            self.ev3.bothwheels.turn(90)
            self.ev3.speaker.say("Or this way?")
            self.ev3.bothwheels.turn(-45)
        else: 
    def step_2_node_2_action(self): #helecopter
        if self.behavior_matches:
            self.ev3.screen.load_image(ImageFile.LEFT)
            self.ev3.bothwheels.turn(60)
            self.ev3.speaker.say("Uh oh")
            self.ev3.bothwheels.turn(-60)
        else:
            pass
            
     def step_3_node_1_action(self):
        if self.behavior_matches:
            
        else:
            pass        