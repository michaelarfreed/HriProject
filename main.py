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
            text = self.story.get_current_node_text()
            self.robot.ev3.speaker.say(text)

            # get the input from the user
            sensor_input = self.wait_for_sensor_input()

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
                return 0
            if Button.CENTER in self.robot.ev3.buttons.pressed():
                return 1
            # if Button.LEFT in self.robot.ev3.buttons.pressed():
            #     return 0
            # if Button.RIGHT in self.robot.ev3.buttons.pressed():
            #     return 1
        # return 0
        return -1

#if __name__ == '__main__':
 #   experiment = Experiment(form=0, behavior=True)
 #   finished = experiment.run()

if __name__ == '__main__':
    gyroboy = GyroBoy(True)
    gyroboy.step_0_node_0_action()
