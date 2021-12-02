from robot import Robot

class Car(Robot):
    def __init__(self, behavior_matches):
        super().__init__(behavior_matches)
        # Initialize the motors connected to the back wheels.
        self.left_wheel_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
        self.right_wheel_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)

        # Initialize the motor connected to the front wheels.
        # Worm gear moves 1 tooth per rotation. It is interfaced to a 24-tooth
        # gear. The 24-tooth gear is connected to parallel 12-tooth gears via
        # an axle. The 12-tooth gears interface with 36-tooth gears.
        # self.front_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE,
        #                         gears=[[1, 24], [12, 36]])

    def step_0_node_0_action(self):
        if self.behavior_matches:
            self.drive_forward()
            pass
        else:
            pass

    def drive_forward(self, distance):
        pass 


if __name__ == "__main__":
    c = Car()
    c.drive_forward(40)