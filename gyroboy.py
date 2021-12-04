from robot import *

class GyroBoy(Robot):
    rightup = 90
    leftup = -120
    wiggle = 30
    def __init__(self, behavior_matches):
        super().__init__(behavior_matches)

        ##MOTORS
        # Initialize a motor at port C, for both arms
        self.arm_motor = Motor(Port.C)
        # Initialize right wheel motor
        self.rightwheel_motor = Motor(Port.A)
        # Initialize left wheel motor 
        self.leftwheel_motor = Motor(Port.D)
        self.bothwheels = DriveBase(self.leftwheel_motor, self.rightwheel_motor, 5.5,10.25) # left motor right motor, wheel diameter, distance between wheels
        
        #SENSORS
        self.obstacle_sensor = UltrasonicSensor(Port.S4)
        self.GoButton = TouchSensor(Port.S3)

    def slowturn(self, percentage, angle):
        # get current turn and move settings
        (straight_speed, straight_acceleration, turn_rate, turn_acceleration) = self.bothwheels.settings()
        # set turn rates to the slow percentage
        self.bothwheels.settings = (straight_speed, straight_acceleration, percentage*turn_rate, percentage*turn_acceleration)
        # make the slow turn
        self.bothwheels.turn(angle)
        # restore the standard settings
        self.bothwheels.settings = (straight_speed, straight_acceleration, turn_rate, turn_acceleration)

    def step_0_node_0_action(self): #start
        self.ev3.screen.load_image(ImageFile.NEUTRAL)
        self.arm_motor.run_angle(200, self.rightup)
        print("Step 0 Node 0 complete")

    def step_0_node_1_action(self):
        self.screen.load_image(ImageFile.LOVE)
        if self.behavior_matches:
            self.arm_motor.run_angle(200, -self.rightup)
            self.ev3.speaker.say("Thank you!")
            self.load_image(ImageFile.NEUTRAL)
        else:
            pass
        print("Step 0 Node 1 complete")
    def step_1_node_0_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(200,self.wiggle)
            self.arm_motor.run_angle(200,-self.wiggle)
        else:
            pass
    def step_2_node_1_action(self): #vents
        if self.behavior_matches:
            self.bothwheels.turn(-45)
            self.ev3.speaker.say("This way?")
            self.bothwheels.turn(90)
            self.ev3.speaker.say("Or this way?")
            self.bothwheels.turn(-45)
        else: 
            pass
    def step_2_node_2_action(self): #helecopter
        if self.behavior_matches:
            self.ev3.screen.load_image(ImageFile.LEFT)
            self.bothwheels.turn(60)
            self.ev3.speaker.say("Uh oh")
            self.bothwheels.turn(-60)
        else:
            pass
            
    def step_3_node_1_action(self):
        if self.behavior_matches:
            self.ev3.screen.load_image(ImageFile.DOWN)
            self.slowturn(self, .5, 360)  ##FLAG

        else:
            pass        
    def step_3_node_2_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(200, -self.rightup)
            self.arm_motor.run_angle(100, self.rightup)
        else:
            pass    
    def step_3_node_3_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(200, self.rightup)
            self.arm_motor.run_angle(100, -self.rightup)           
        else:
            pass    

    def step_4_node_1_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(200, -2*self.wiggle)
            self.arm_motor.run_angle(200, 2*self.wiggle)
        else:
            pass    
    def step_4_node_2_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(200, -self.wiggle)
            self.arm_motor.run_angle(200, self.wiggle)
            self.arm_motor.run_angle(200, -self.wiggle)
            self.arm_motor.run_angle(200, self.wiggle)
            self.arm_motor.run_angle(200, -self.wiggle)
            self.arm_motor.run_angle(200, self.wiggle)
            self.arm_motor.run_angle(200, -self.wiggle)
            self.arm_motor.run_angle(200, self.wiggle) 
    
        else:
            pass    
    def step_4_node_3_action(self):
        if self.behavior_matches:
            self.bothwheels(90)
            self.arm_motor.run_angle(200,self.wiggle)
            self.arm_motor.run_angle(200,-2*self.wiggle)
            self.arm_motor.run_angle(200,self.wiggle)
            self.bothwheels.turn(-90)
        else:
            pass    
    def step_4_node_4_action(self):
        if self.behavior_matches:
            self.bothwheels(90)
            self.arm_motor.run_angle(200,self.wiggle)
            self.arm_motor.run_angle(200,-2*self.wiggle)
            self.arm_motor.run_angle(200,self.wiggle)
            self.bothwheels.turn(-90)
        else:
            pass   
    def step_5_node_0_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(100,self.rightup)
            self.ev3.speaker.say("I love to arm wrestle!")
            self.arm_motor.run_angle(250, -self.rightup)

        else:
            pass    
    def step_5_node_1_action(self):
        if self.behavior_matches:
            self.bothwheels.turn(-90)
            self.bothwheels.turn(180)
            self.bothwheels.turn(-90)
        else:
            pass   
    def step_5_node_2_action(self):
        if self.behavior_matches:
            self.bothwheels.turn(-90)
            self.bothwheels.turn(180)
            self.bothwheels.turn(-90) 
        else:
            pass    
    def step_5_node_3_action(self):
        if self.behavior_matches:
            self.bothwheels.drive(100)
            self.arm_motor.run_angle(100, self.leftup) 
            self.arm_motor.run_angle(200,-self.leftup)
        else:
            pass    
    def step_6_node_0_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(50,self.rightup)
            self.arm_motor.run_angle(50,-self.rightup)
        else:
            pass    
    def step_6_node_1_action(self):
        if self.behavior_matches:
            self.bothwheels.drive(-10)
            self.arm_motor.run_angle(100,-self.wiggle)
            self.arm_motor.run_angle(100, self.wiggle)
        else:
            pass    
    def step_6_node_2_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(50,self.rightup)
            self.arm_motor.run_angle(50,-2*self.rightup)
            self.arm_motor.run_angle(50,2*self.rightup)
            self.arm_motor.run_angle(50,-2*self.rightup)
            self.arm_motor.run_angle(50,self.rightup)
        else:
            pass    
    def step_6_node_3_action(self):
        if self.behavior_matches: #eating
            self.arm_motor.run_angle(250,self.rightup)
            self.arm_motor.run_angle(250,-2*self.rightup)
            self.arm_motor.run_angle(250,2*self.rightup)
            self.arm_motor.run_angle(250,-2*self.rightup)
            self.arm_motor.run_angle(250,self.rightup)  
        else:
            pass    
    def step_7_node_0_action(self):
        if self.behavior_matches: #tantrum
            self.bothwheels.drive(-10)
            self.arm_motor.run_angle(200,self.wiggle)
            self.arm_motor.run_angle(200,-2*self.wiggle)
            self.arm_motor.run_angle(200,2*self.wiggle)
            self.arm_motor.run_angle(200,-2*self.wiggle)
            self.arm_motor.run_angle(200,self.wiggle)
            self.ev3.speaker.play_file(SORRY.wav)
        else:
            pass    
    def step_7_node_1_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(200,self.rightup)
            self.ev3.speaker.play_file(FANTASTIC.wav)    
        else:
            pass    
    def step_7_node_2_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(200,self.rightup)
            self.ev3.speaker.play_file(FANTASTIC.wav)
            
        else:
            pass    
    def step_7_node_3_action(self):
        if self.behavior_matches:
            self.bothwheels.drive(-10)
            self.arm_motor.run_angle(200,self.wiggle)
            self.arm_motor.run_angle(200,-2*self.wiggle)
            self.arm_motor.run_angle(200,2*self.wiggle)
            self.arm_motor.run_angle(200,-2*self.wiggle)
            self.arm_motor.run_angle(200,self.wiggle)
            self.ev3.speaker.play_file(SORRY.wav)
        else:
            pass    
   