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
       # self.obstacle_sensor = UltrasonicSensor(Port.S4)
        self.touch_sensor = TouchSensor(Port.S3)

    def turn_left(self):
        self.bothwheels.turn(45)
        self.bothwheels.turn(-45)

    def turn_right(self): 
        self.bothwheels.turn(-45)
        self.bothwheels.turn(45)

        

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
        if self.behavior_matches:
            self.ev3.screen.load_image(ImageFile.LOVE)
            self.arm_motor.run_angle(200, self.rightup)
            self.arm_motor.run_angle(200, -self.rightup)
            self.ev3.speaker.say("Thank you!")
            self.ev3.screen.load_image(ImageFile.NEUTRAL)
        else:
            self.ev3.speaker.play_file(self.SOUND_BEEP_BEEP)
            self.ev3.speaker.play_file(self.SOUND_MOTOR_START)
        print("Step 0 Node 0 complete")

    def step_1_node_0_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(200,self.wiggle)
            self.arm_motor.run_angle(200,-self.wiggle)
        else:
            self.turn_left()
            self.turn_right()
            self.turn_left()
            self.turn_right()
            self.turn_to_center()

        print("Step 1 Node 0 complete")
    def step_2_node_0_action(self): #vents
        if self.behavior_matches:
            self.bothwheels.turn(-45)
            self.ev3.speaker.say("This way?")
            self.bothwheels.turn(90)
            self.ev3.speaker.say("Or this way?")
            self.bothwheels.turn(-45)
        else: 
            self.bothwheels.turn(-45)
            self.ev3.speaker.play_file(SoundFile.HORN_1)
            self.bothwheels.turn(90)
            self.ev3.speaker.play_file(SoundFile.HORN_1)
            self.bothwheels.turn(-45)
        print("Step 2 Node 0 complete")

    def step_2_node_1_action(self): #helecopter
        if self.behavior_matches:
            self.ev3.screen.load_image(ImageFile.BOTTOM_LEFT)
            self.bothwheels.turn(60)
            self.ev3.speaker.say("Uh oh")
            self.bothwheels.turn(-60)
        else:
            self.ev3.screen.load_image(ImageFile.LEFT)
            self.bothwheels.turn(60)
            self.ev3.speaker.play_file(SoundFile.DOG_BARK_1)
            self.bothwheels.turn(-60)
        print("Step 2 Node 1 complete")

    def step_3_node_0_action(self):
        if self.behavior_matches:
            self.ev3.screen.load_image(ImageFile.DOWN)
            self.slowturn(.5, 360) 

        else:
            self.ev3.screen.load_image(ImageFile.BACKWARD)
            self.slowturn(.5, 360)        
        print("Step 3 Node 0 complete")

    def step_3_node_1_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(200, -self.rightup)
            self.arm_motor.run_angle(100, self.rightup)
        else:
            self.bothwheels.straight(10)
            self.bothwheels.turn(45)
            self.bothwheels.turn(-90)
            self.bothwheels.turn(45)
            self.bothwheels.straight(-10)

        print("Step 3 Node 1 complete")
    def step_3_node_2_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(200, self.rightup)
            self.arm_motor.run_angle(100, -self.rightup)           
        else:
            self.bothwheels.straight(10)
            self.bothwheels.turn(45)
            self.bothwheels.turn(-90)
            self.bothwheels.turn(45)
            self.bothwheels.straight(-10)    
        print("Step 3 Node 2 complete")
    def step_4_node_0_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(200, -2*self.wiggle)
            self.arm_motor.run_angle(200, 2*self.wiggle)
        else:
            self.ev3.screen.load_image(ImageFile.BACKWARD)
            self.ev3.screen.load_image(ImageFile.FORWARD)    
            self.bothwheels.straight(10)
            self.bothwheels.straignt(-10)
            self.bothwheels.turn(-15)
            self.bothwheels.turn(15)
            self.bothwheels.turn(-15)
            self.bothwheels.turn(15)
            self.bothwheels.turn(-15)
            self.bothwheels.turn(15)
        print("Step 4 Node 0 complete")

    def step_4_node_1_action(self):
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
            self.ev3.screen.load_image(ImageFile.BACKWARD)
            self.ev3.screen.load_image(ImageFile.FORWARD)    
            self.bothwheels.straight(10)
            self.bothwheels.straignt(-10)
            self.bothwheels.turn(-15)
            self.bothwheels.turn(15)
            self.bothwheels.turn(-15)
            self.bothwheels.turn(15)
            self.bothwheels.turn(-15)
            self.bothwheels.turn(15)

        print("Step 4 Node 1 complete")  
    def step_4_node_2_action(self):
        if self.behavior_matches:
            self.bothwheels.turn(90)
            self.arm_motor.run_angle(200,self.wiggle)
            self.arm_motor.run_angle(200,-2*self.wiggle)
            self.arm_motor.run_angle(200,self.wiggle)
            self.bothwheels.turn(-90)
        else:
            self.ev3.screen.load_image(ImageFile.BACKWARD)
            self.ev3.screen.load_image(ImageFile.FORWARD)    
            self.bothwheels.straight(10)
            self.bothwheels.straignt(-10)
            self.bothwheels.turn(-15)
            self.bothwheels.turn(15)
            self.bothwheels.turn(-15)
            self.bothwheels.turn(15)
            self.bothwheels.turn(-15)
            self.bothwheels.turn(15) 

        print("Step 4 Node 2 complete")
    def step_4_node_3_action(self):
        if self.behavior_matches:
            self.bothwheels.turn(90)
            self.arm_motor.run_angle(200,self.wiggle)
            self.arm_motor.run_angle(200,-2*self.wiggle)
            self.arm_motor.run_angle(200,self.wiggle)
            self.bothwheels.turn(-90)
        else:
            self.ev3.screen.load_image(ImageFile.BACKWARD)
            self.ev3.screen.load_image(ImageFile.FORWARD)    
            self.bothwheels.straight(10)
            self.bothwheels.straignt(-10)
            self.bothwheels.turn(-15)
            self.bothwheels.turn(15)
            self.bothwheels.turn(-15)
            self.bothwheels.turn(15)
            self.bothwheels.turn(-15)
            self.bothwheels.turn(15) 
        print("Step 4 Node 3 complete")  
    def step_5_node_0_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(100,self.rightup)
            self.ev3.speaker.say("I love to arm wrestle!")
            self.arm_motor.run_angle(250, -self.rightup)

        else:
            self.bothwheels.turn(20)
            self.ev3.speaker.play_file(SoundFile.DOG_BARK_1)
            self.bothwheels.turn(-20)
        print("Step 5 Node 0 complete") 

    def step_5_node_1_action(self):
        if self.behavior_matches:
            self.bothwheels.turn(-90)
            self.bothwheels.turn(180)
            self.bothwheels.turn(-90)
        else:
            self.bothwheels.turn(20)
            self.ev3.speaker.play_file(SoundFile.DOG_BARK_1)
            self.bothwheels.turn(-20)  
        print("Step 5 Node 1 complete")
    def step_5_node_2_action(self):
        if self.behavior_matches:
            self.bothwheels.turn(-90)
            self.bothwheels.turn(180)
            self.bothwheels.turn(-90) 
        else:
            self.bothwheels.turn(20)
            self.ev3.speaker.play_file(SoundFile.DOG_BARK_1)
            self.bothwheels.turn(-20)    
        print("Step 5 Node 2 complete")
    def step_5_node_3_action(self):
        if self.behavior_matches:
            self.bothwheels.straight(10)
            self.arm_motor.run_angle(100, self.leftup) 
            self.arm_motor.run_angle(200,-self.leftup)
        else:
            self.bothwheels.turn(20)
            self.ev3.speaker.play_file(SoundFile.DOG_BARK_1)
            self.bothwheels.turn(-20) 
        print("Step 5 Node 3 complete")   
    def step_6_node_0_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(50,self.rightup)
            self.arm_motor.run_angle(50,-self.rightup)
        else:
            self.bothwheels.straight(10)
            self.bothwheels.straight(-10)
            self.bothwheels.straight(10)
            self.bothwheels.straight(-10)

        print("Step 6 Node 0 complete")   
    def step_6_node_1_action(self):
        if self.behavior_matches:
            self.bothwheels.straight(-10)
            self.arm_motor.run_angle(100,-self.wiggle)
            self.arm_motor.run_angle(100, self.wiggle)
        else:
            self.bothwheels.straight(10)
            self.bothwheels.straight(-10)
            self.bothwheels.straight(10)
            self.bothwheels.straight(-10)    
        print("Step 6 Node 1 complete")
    def step_6_node_2_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(50,self.rightup)
            self.arm_motor.run_angle(50,-2*self.rightup)
            self.arm_motor.run_angle(50,2*self.rightup)
            self.arm_motor.run_angle(50,-2*self.rightup)
            self.arm_motor.run_angle(50,self.rightup)
        else:
            self.bothwheels.straight(10)
            self.bothwheels.straight(-10)
            self.bothwheels.straight(10)
            self.bothwheels.straight(-10)
        print("Step 6 Node 2 complete")    
    def step_6_node_3_action(self):
        if self.behavior_matches: #eating
            self.arm_motor.run_angle(250,self.rightup)
            self.arm_motor.run_angle(250,-2*self.rightup)
            self.arm_motor.run_angle(250,2*self.rightup)
            self.arm_motor.run_angle(250,-2*self.rightup)
            self.arm_motor.run_angle(250,self.rightup)  
        else:
            self.bothwheels.straight(10)
            self.bothwheels.straight(-10)
            self.bothwheels.straight(10)
            self.bothwheels.straight(-10)   
        print("Step 6 Node 3 complete") 

    def step_7_node_0_action(self):
        if self.behavior_matches: #tantrum
            self.bothwheels.straight(-10)
            self.arm_motor.run_angle(200,self.wiggle)
            self.arm_motor.run_angle(200,-2*self.wiggle)
            self.arm_motor.run_angle(200,2*self.wiggle)
            self.arm_motor.run_angle(200,-2*self.wiggle)
            self.arm_motor.run_angle(200,self.wiggle)
            self.ev3.speaker.say("Sorry")
        else:
            self.ev3.speaker.play_file(self.DOG_WHINE)
            self.bothwheels.straight(10)
            self.bothwheels.straight(-10)
            self.bothwheels.turn(-20)
            self.bothwheels.turn(20)
            self.bothwheels.straight(10)
            self.bothwheels.straight(-10) 
            self.ev3.speaker.play_file(self.SOUND_MOTOR_STOP)  
        print("Step 7 Node 0 complete")  
    def step_7_node_1_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(200,self.rightup)
            self.ev3.speaker.say("Fantastic!")
        else:
            self.ev3.speaker.play_file(self.SOUND_BEEP_BEEP)
            self.bothwheels.straight(10)
            self.ev3.speaker.play_file(self.DOG_BARK_1)    
        print("Step 7 Node 1 complete")  
    def step_7_node_2_action(self):
        if self.behavior_matches:
            self.arm_motor.run_angle(200,self.rightup)
            self.ev3.speaker.say("Fantastic!")
            
        else:
            self.ev3.speaker.play_file(self.SOUND_BEEP_BEEP)
            self.bothwheels.straight(10)
            self.ev3.speaker.play_file(self.DOG_BARK_1)      
        print("Step 7 Node 2 complete")
    def step_7_node_3_action(self):
        if self.behavior_matches:
            self.bothwheels.straight(-10)
            self.arm_motor.run_angle(200,self.wiggle)
            self.arm_motor.run_angle(200,-2*self.wiggle)
            self.arm_motor.run_angle(200,2*self.wiggle)
            self.arm_motor.run_angle(200,-2*self.wiggle)
            self.arm_motor.run_angle(200,self.wiggle)
            self.ev3.speaker.play_file(SORRY.wav)
        else:
            self.ev3.speaker.play_file(self.DOG_WHINE)
            self.bothwheels.straight(10)
            self.bothwheels.straight(-10)
            self.bothwheels.turn(-20)
            self.bothwheels.turn(20)
            self.bothwheels.straight(10)
            self.bothwheels.straight(-10) 
            self.ev3.speaker.play_file(self.SOUND_MOTOR_STOP)    
        print("Step 7 Node 3 complete")  
   

