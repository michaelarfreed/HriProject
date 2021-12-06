from robot import *

class Puppy(Robot):

    def __init__(self, behavior_matches):
        super().__init__(behavior_matches)

        # Initialize the motors connected to the back legs.
        NEUTRAL_EYES = Image(ImageFile.NEUTRAL)
        TIRED_EYES = Image(ImageFile.TIRED_MIDDLE)
        TIRED_LEFT_EYES = Image(ImageFile.TIRED_LEFT)
        TIRED_RIGHT_EYES = Image(ImageFile.TIRED_RIGHT)
        SLEEPING_EYES = Image(ImageFile.SLEEPING)
        HURT_EYES = Image(ImageFile.HURT)
        ANGRY_EYES = Image(ImageFile.ANGRY)
        HEART_EYES = Image(ImageFile.LOVE)
        SQUINTY_EYES = Image(ImageFile.TEAR)
        self.left_leg_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
        self.right_leg_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)

        # Initialize the motor connected to the head.
        # Worm gear moves 1 tooth per rotation. It is interfaced to a 24-tooth
        # gear. The 24-tooth gear is connected to parallel 12-tooth gears via
        # an axle. The 12-tooth gears interface with 36-tooth gears.
        self.head_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE,
                                gears=[[1, 24], [12, 36]])

        # Initialize the touch sensor. It is used to detect when someone pets
        # the puppy.
        self.touch_sensor = TouchSensor(Port.S1)

    def walk_in_place(puppy, speed=100):
        puppy.right_leg_motor.run_angle(speed, 40, wait=False)
        puppy.left_leg_motor.run_angle(speed, -40, wait=True)
        puppy.right_leg_motor.run_angle(speed, -40, wait=False)
        puppy.left_leg_motor.run_angle(speed, 40, wait=True)
        puppy.right_leg_motor.run_angle(speed, -40, wait=False)
        puppy.left_leg_motor.run_angle(speed, 40, wait=True)
        puppy.right_leg_motor.run_angle(speed, 40, wait=False)
        puppy.left_leg_motor.run_angle(speed, -40, wait=True)

    def sit(left_leg_motor, right_leg_motor):
        left_leg_motor.run(-1000)
        right_leg_motor.run(-1000)
        wait(2000)
        left_leg_motor.stop()
        right_leg_motor.stop()

    def hop(left_leg_motor, right_leg_motor):
        left_leg_motor.run(500)
        right_leg_motor.run(500)
        wait(275)
        left_leg_motor.hold()
        right_leg_motor.hold()
        wait(275)
        left_leg_motor.run(-50)
        right_leg_motor.run(-50)
        wait(275)
        left_leg_motor.stop()
        right_leg_motor.stop()

    def step_0_node_0_action(self): 
        ev3.screen.load_image(NEUTRAL_EYES)

    def step_0_node_1_action(self):
        if self.behavior_matches:
            head_motor.run(1000)
            wait(1000)
            self.ev3.speaker.say("uh oh")
            head_motor.run(-1000)
            wait(1000)
        else:
            pass
  
    def step_1_node_0_action(self):
        if self.behavior_matches:
            walk_in_place(self, 100)
        else:
            pass
    
    def step_2_node_1_action(self): #vents
        if self.behavior_matches:
            head_motor.run(1000)
            wait(10)
            self.ev3.speaker.say("uh oh")
            head_motor.run(-1000)
            wait(10)
            head_motor.stop()
        else: 
            pass
    
    def step_2_node_2_action(self): #helicopter
        if self.behavior_matches:
            self.ev3.light.on(Color.GREEN)
            self.ev3.speaker.say("this way")
            self.ev3.light.on(Color.ORANGE)
            self.ev3.speaker.say("or that way")
        else:
            pass
            
    def step_3_node_1_action(self):
        if self.behavior_matches:
            sit(left_leg_motor, right_leg_motor)
        else:
            pass        
    
    def step_3_node_2_action(self):
        if self.behavior_matches:
            ev3.screen.load_image(TIRED_LEFT_EYES)
            ev3.screen.load_image(TIRED_RIGHT_EYES)
        else:
            pass    
    
    def step_3_node_3_action(self):
        if self.behavior_matches:
            ev3.screen.load_image(SQUINTY_EYES)   
            ev3.screen.load_image(HURT_EYES)   
            head_motor.run(10)
            wait(5)
            head_motor.stop()
        else:
            pass    

    def step_4_node_1_action(self):
        if self.behavior_matches:
            hop(left_leg_motor, right_leg_motor)
        else:
            pass    
   
    def step_4_node_2_action(self):
        if self.behavior_matches:
            #TODO 
        else:
            pass    
    def step_4_node_3_action(self):
        if self.behavior_matches:
            #TODO
        else:
            pass    
    def step_4_node_4_action(self):
        if self.behavior_matches:
            #TODO
        else:
            pass   
    def step_5_node_0_action(self):
        if self.behavior_matches:
            #TODO
        else:
            pass    
    def step_5_node_1_action(self):
        if self.behavior_matches:
            #TODO
        else:
            pass   
    def step_5_node_2_action(self):
        if self.behavior_matches:
            #TODO 
        else:
            pass    
    def step_5_node_3_action(self):
        if self.behavior_matches:
            #TODO
        else:
            pass    
    def step_6_node_0_action(self):
        if self.behavior_matches:
            #TODO
        else:
            pass    
    def step_6_node_1_action(self):
        if self.behavior_matches:
            #TODO
        else:
            pass    
    def step_6_node_2_action(self):
        if self.behavior_matches:
            #TODO
        else:
            pass    
    def step_6_node_3_action(self):
        if self.behavior_matches: 
            #TODO
        else:
            pass    
    def step_7_node_0_action(self):
        if self.behavior_matches:
            #TODO
        else:
            pass    
    def step_7_node_1_action(self):
        if self.behavior_matches:
            #TODO  
        else:
            pass    
    def step_7_node_2_action(self):
        if self.behavior_matches:
            #TODO
            
        else:
            pass    
    def step_7_node_3_action(self):
        if self.behavior_matches:
            #TODO
        else:
            pass 
