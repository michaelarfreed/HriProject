from robot import *

class Puppy(Robot):
    # These constants are used for positioning the legs.
    HALF_UP_ANGLE = 25
    STAND_UP_ANGLE = 65
    STRETCH_ANGLE = 125

    # These constants are for positioning the head.
    HEAD_UP_ANGLE = 0
    HEAD_DOWN_ANGLE = -40

    def __init__(self):
        super().__init__()

        # Initialize the motors connected to the back legs.
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


