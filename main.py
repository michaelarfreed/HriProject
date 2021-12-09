#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from car import Car
from gyroboy import GyroBoy
from puppy import Puppy
from script import Story 

import time

class Experiment:
    def __init__(self, form=0, behavior=True):
        self.form_factor = form  # 0 = puppy, 1 = gyroboy, 2 = car
        self.behavior_matches = behavior # boolean, i.e. True = puppy form + puppy behaviors, False = puppy form + boy/car behaviors
        self.story = Story()
        
        self.robot = self.get_robot()
        self.prev_touched = 0

        self.input_list = []
        self.input_time_stamps_list = []
        self.start_time=time.time()


    def get_robot(self):
        if self.form_factor == 0:
            return Puppy(self.behavior_matches)
        if self.form_factor == 1:
            return GyroBoy(self.behavior_matches)
        if self.form_factor == 2:
            return Car(self.behavior_matches)

    def get_robot_string(self):
        if self.form_factor == 0:
            return "puppy"
        if self.form_factor == 1:
            return "gyroboy"
        if self.form_factor == 2:
            return "car"

    def run(self):

        while not self.story.is_current_step_end():
            # get the text for current step
            text = self.story.get_current_node_text(self.form_factor)
            self.robot.ev3.speaker.say(str(text))

            # user input
            sensor_start_time = time.time()             # get time when prompt user for input
            sensor_input = self.wait_for_sensor_input() # wait for actual input
            self.input_list.append(sensor_input)        # get time when user gives input

            self.input_time_stamps_list.append((sensor_start_time,time.time()))  # record the amount of time user spends on a step

            if sensor_input != -1:
                # do the action            
                function_name = self.story.get_current_node_action_function_name()
                # print(function_name)
                method = getattr(self.robot, function_name)
                method()
                
                # move to the next step
                self.story.set_next_node(sensor_input)

        return True

    def wait_for_sensor_input(self, max_time=5):
        """
        wait max_time seconds for button to be pressed
        once the button is pressed, continue waiting 

        Args:
            max_time (int, optional): maximum amount of time (in seconds) to wait for button press. Defaults to None. 
                                      If None, robot will wait forever for button press

        Returns:
            boolean: if button was pressed, returns True. else, returns False
        """
        # wait the maximum amount of time for button press
        tic = time.perf_counter()
        toc = time.perf_counter()
        while toc-tic < max_time:
            toc = time.perf_counter()
            if self.robot.touch_sensor.pressed():
                print("touch sensor pressed")
                return 0
            if Button.CENTER in self.robot.ev3.buttons.pressed():
                print("center button pressed")
                return 1
            # if Button.LEFT in self.robot.ev3.buttons.pressed():
            #     return 0
            # if Button.RIGHT in self.robot.ev3.buttons.pressed():
            #     return 1
        # return 0
        return -1

    def write_sensor_input_to_file(self):
        file_name = str(time.time()) + ".log"
        try:
            with open(file_name,'w') as file:
                # write start_time
                file.write('start_time:'+str(self.start_time)+'\n')

                # write end_time
                file.write('end_time:'+str(time.time())+'\n')

                # write input_timestamp_list
                file.write('input_times:')
                comma_prefix = False
                for item in self.input_time_stamps_list:
                    if comma_prefix:
                        file.write(',')
                    file.write('('+str(item[0])+','+str(item[1])+')')
                    comma_prefix=True
                file.write('\n')
                
                # write input_list
                file.write('input_list:')
                comma_prefix = False
                for item in self.input_list:
                    if comma_prefix:
                        file.write(',')
                    file.write(str(item))
                    comma_prefix=True
                file.write('\n')

        except Exception as e:
            print('file write failed')
            print(e)


if __name__ == '__main__':
    experiment = Experiment(form=2, behavior=False)
    # gyroboy = GyroBoy(True)
    # gyroboy.ev3.screen.load_image(ImageFile.NEUTRAL)
    finished = experiment.run()
    experiment.write_sensor_input_to_file()
    # story = Story()
    # print(story.get_current_step())

# test code to run through all the actions
#if __name__ == '__main__':
  #  gyroboy = GyroBoy(True)
    # gyroboy.step_0_node_0_action()
    # gyroboy.step_0_node_1_action()
    # gyroboy.step_1_node_0_action()
    # gyroboy.step_2_node_0_action()
    # gyroboy.step_2_node_1_action()
    # gyroboy.step_3_node_0_action()
    # gyroboy.step_3_node_1_action()
    # gyroboy.step_3_node_2_action()
    # gyroboy.step_4_node_0_action()
    # gyroboy.step_4_node_1_action()
    # gyroboy.step_4_node_2_action()
    # gyroboy.step_4_node_3_action()
    # gyroboy.step_5_node_0_action()
    # gyroboy.step_5_node_1_action()
    # gyroboy.step_5_node_2_action()
    # gyroboy.step_5_node_3_action()
    # gyroboy.step_6_node_0_action()
    # gyroboy.step_6_node_1_action()
    # gyroboy.step_6_node_2_action()
    # gyroboy.step_6_node_3_action()
    # gyroboy.step_7_node_0_action()
    # gyroboy.step_7_node_1_action()
    # gyroboy.step_7_node_2_action()





