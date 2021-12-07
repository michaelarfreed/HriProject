from robot import *

class Car(Robot):
    SOUND_MOTOR_START   = SoundFile.MOTOR_START
    SOUND_MOTOR_IDLE    = SoundFile.MOTOR_IDLE
    SOUND_MOTOR_STOP    = SoundFile.MOTOR_STOP
    SOUND_BEEP_BEEP     = SoundFile.HORN_1
    SOUND_LONG_BEEP     = SoundFile.HORN_2
    SOUND_BACKING_ALERT = SoundFile.BACKING_ALERT

    def __init__(self, behavior_matches):
        super().__init__(behavior_matches)
        # Initialize the motors connected to the back wheels.
        self.left_rear_wheel_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
        self.right_rear_wheel_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
        self.front_turning_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)

        self.touch_sensor = TouchSensor(Port.S1)


    def drive_forward(self, n_rotations=1):
        self.left_rear_wheel_motor.run_angle(200,360*n_rotations,wait=False)
        self.right_rear_wheel_motor.run_angle(200,360*n_rotations,wait=True)

    def drive_backward(self, n_rotations=1):
        self.left_rear_wheel_motor.run_angle(-200,360*n_rotations,wait=False)
        self.right_rear_wheel_motor.run_angle(-200,360*n_rotations,wait=True)

    def drive_in_place(self):
        self.left_rear_wheel_motor.run_angle(-200,360,wait=False)
        self.right_rear_wheel_motor.run_angle(200,360,wait=True)

    def turn_left(self):
        self.front_turning_motor.run_target(200,-50,wait=True)    

    def turn_right(self):
        self.front_turning_motor.run_target(200,50,wait=True)    

    def turn_to_center(self):
        self.front_turning_motor.run_target(200,0,wait=True)    


    def step_0_node_0_action(self): #start
        self.ev3.speaker.play_file(self.SOUND_BEEP_BEEP)
        self.ev3.speaker.play_file(self.SOUND_MOTOR_START)
        print("Step 0 Node 0 complete")

    def step_0_node_1_action(self):
        if self.behavior_matches:
            self.turn_left()
            self.turn_right()
            self.turn_left()
            self.turn_right()
            self.turn_to_center()
        else:
            pass
        print("Step 0 Node 1 complete")
        
    def step_1_node_0_action(self):
        if self.behavior_matches:
            self.turn_left()
            self.turn_right()
            self.turn_left()
            self.turn_right()
            self.turn_to_center()
        else:
            pass
        print("Step 1 Node 0 complete")

    def step_2_node_0_action(self): #vents
        if self.behavior_matches:
            self.turn_left()
            self.ev3.speaker.say("This way?")
            self.turn_right()
            self.ev3.speaker.say("Or this way?")
            self.turn_to_center()
        else: 
            pass
        print("Step 2 Node 0 complete")
    def step_2_node_1_action(self): #helecopter
        if self.behavior_matches:
            self.drive_forward()
            self.ev3.speaker.say("Uh oh")
            self.drive_backward()
        else:
            pass
        print("Step 2 Node 1 complete")
    def step_3_node_0_action(self):
        if self.behavior_matches:
            self.ev3.speaker.play_file(self.SOUND_BACKING_ALERT)
            self.drive_backward()
        else:
            pass        
        print("Step 3 Node 0 complete")
    def step_3_node_1_action(self):
        if self.behavior_matches:
            self.turn_left()
            self.drive_forward()
            self.turn_right()
            self.drive_forward()
            self.turn_to_center()
        else:
            pass    
        print("Step 3 Node 1 complete")
    def step_3_node_2_action(self):
        if self.behavior_matches:
            self.turn_left()
            self.drive_backward()
            self.turn_right()
            self.drive_backward()  
            self.turn_to_center()       
        else:
            pass    
        print("Step 3 Node 2 complete")
    def step_3_node_3_action(self):
        return self.step_3_node_0_action()

    def step_4_node_0_action(self):
        if self.behavior_matches:
            self.drive_in_place()
        else:
            pass    
        print("Step 4 Node 0 complete")
    def step_4_node_1_action(self):
        if self.behavior_matches:
            self.turn_to_center()
            self.drive_backward()
            self.drive_forward() 
        else:
            pass  
        print("Step 4 Node 1 complete")  
    def step_4_node_2_action(self):
        if self.behavior_matches:
            self.turn_right()
            self.drive_forward()
            self.drive_backward()
            self.turn_to_center()
        else:
            pass    
        print("Step 4 Node 2 complete")
    def step_4_node_3_action(self):
        if self.behavior_matches:
            self.turn_to_center()
            self.drive_forward()
            self.ev3.speaker.play_file(self.SOUND_BEEP_BEEP)
            self.drive_backward()
        else:
            pass 
        print("Step 4 Node 3 complete")  

    def step_5_node_0_action(self):
        if self.behavior_matches:
            self.drive_backward()
            self.ev3.speaker.play_file(self.SOUND_BEEP_BEEP)
            self.drive_forward()

        else:
            pass   
        print("Step 5 Node 0 complete") 
    def step_5_node_1_action(self):
        if self.behavior_matches:
            self.turn_right()
            self.turn_left()
            self.turn_to_center()
        else:
            pass   
        print("Step 5 Node 1 complete")
    def step_5_node_2_action(self):
        if self.behavior_matches:
            self.turn_left()
            self.turn_right()
            self.turn_to_center()
        else:
            pass    
        print("Step 5 Node 2 complete")
    def step_5_node_3_action(self):
        if self.behavior_matches:
            self.move_forward()
            self.move_backward()
        else:
            pass 
        print("Step 5 Node 3 complete")   
    def step_6_node_0_action(self):
        if self.behavior_matches:
            self.drive_forward(0.5)
            self.drive_backward(0.5)
            self.drive_forward(0.5)
            self.drive_backward(0.5)
        else:
            pass 
        print("Step 6 Node 0 complete")   
    def step_6_node_1_action(self):
        if self.behavior_matches:
            self.drive_backward(0.5)
            self.ev3.speaker.play_file(self.SOUND_LONG_BEEP)
            self.drive_forward(0.5)
        else:
            pass    
        print("Step 6 Node 1 complete")
    def step_6_node_2_action(self):
        if self.behavior_matches:
            self.ev3.speaker.play_file(self.SOUND_MOTOR_IDLE)
            self.drive_in_place()
        else:
            pass
        print("Step 6 Node 2 complete")    
    def step_6_node_3_action(self):
        if self.behavior_matches: #eating
            self.ev3.speaker.play_file(self.SOUND_MOTOR_IDLE)
            self.drive_in_place()
        else:
            pass   
        print("Step 6 Node 3 complete") 
    def step_7_node_0_action(self):
        if self.behavior_matches: #tantrum
            self.ev3.speaker.play_file(self.SOUND_LONG_BEEP)
            self.turn_left()
            self.turn_right()
            self.turn_to_center()
            self.drive_backward()
            self.drive_forward()
            self.ev3.speaker.play_file(self.SOUND_MOTOR_STOP)
        else:
            pass  
        print("Step 7 Node 0 complete")  
    def step_7_node_1_action(self):
        if self.behavior_matches:
            self.ev3.speaker.play_file(self.SOUND_LONG_BEEP)
            self.turn_left()
            self.turn_right()
            self.turn_to_center()
            self.drive_backward()
            self.drive_forward()
            self.ev3.speaker.play_file(self.SOUND_MOTOR_STOP)
        else:
            pass  
        print("Step 7 Node 1 complete")  
    def step_7_node_2_action(self):
        if self.behavior_matches:
            self.ev3.speaker.play_file(self.SOUND_LONG_BEEP)
            self.turn_left()
            self.turn_right()
            self.turn_to_center()
            self.drive_backward()
            self.drive_forward()
            self.ev3.speaker.play_file(self.SOUND_MOTOR_STOP)
        else:
            pass    
        print("Step 7 Node 2 complete")
    def step_7_node_3_action(self):
        if self.behavior_matches:
            self.ev3.speaker.play_file(self.SOUND_BEEP_BEEP)
            self.turn_left()
            self.turn_right()
            self.turn_to_center()
            self.drive_backward()
            self.drive_forward()
            self.ev3.speaker.play_file(self.SOUND_MOTOR_STOP)
        else:
            pass  
        print("Step 7 Node 3 complete")  
   
