

class Story:
    
    def __init__(self):
        self.step = 0
        self.node = 0
        self.done = False
        pass
        
    # utility functions
    def set_next_node(self, sensor_input):
        if self.step == 0:         # at (step=0, node=0)
            if sensor_input == -1: #   no button press
                self.node = 1      #     go to (step=0, node=1) / wait for button press 
            else:                  #   yes button press
                self.node = 0      #     go to (step=1, node=0)
                self.step = 1
        elif self.step == 1:        # at (step=1, node=0)
            if sensor_input != -1:  #   recieved input
                self.step = 2       #     move to next step = 2
            if sensor_input == 0:   #   left button press
                self.node = 0       #     go to (step=2, node=0)
            elif sensor_input == 1: #   right button press
                self.node = 1       #     go to (step=2, node=1)
        elif self.step == 2:
            if sensor_input != -1:      # recieved input
                self.step = 3           #   move to next step =3
            if self.node == 0:          # at (step=2, node=0)
                if sensor_input == 0:   #   input == left button press
                    self.node = 0       #     go to (step=3, node=0)
                if sensor_input == 1:   #   input == right button press
                    self.node = 1       #     go to (step=3, node=1)
            elif self.node == 1:        # at (step=2, node=1)
                if sensor_input == 0:   #   input == left button press
                    self.node = 2       #     go to (step=3, node=2)
                if sensor_input == 1:   #   input == right button press
                    self.node = 3       #     go to (step=3, node=3)
        elif self.step == 3:
            if sensor_input != -1:      # recieved input
                self.step = 4           #   move to next step = 4
            if self.node == 0:          # at (step=3, node=0)
                if sensor_input == 0:   #   input == left button press
                    self.node = 0       #     go to (step=4, node=0)
                if sensor_input == 1:   #   input == right button press
                    self.node = 1       #     go to (step=4, node=1)
            if self.node == 1:          # at (step=3, node=1)
                if sensor_input == 0:   #   input == left button press
                    self.node = 0       #     go to (step=4, node=0)
                if sensor_input == 1:   #   input == right button press
                    self.node = 1       #     go to (step=4, node=1)
            if self.node == 2:          # at (step=3, node=2)
                if sensor_input == 0:   #   input == left button press
                    self.node = 1       #     go to (step=4, node=1)
                if sensor_input == 1:   #   input == right button press
                    self.node = 0       #     go to (step=4, node=0)
            if self.node == 3:          # at (step=3, node=3)
                if sensor_input == 0:   #   input == left button press
                    self.node = 1       #     go to (step=4, node=1)
                if sensor_input == 1:   #   input == right button press
                    self.node = 0       #     go to (step=4, node=0)

    def get_current_step(self):
        return self.step

    def get_current_node_text(self):
        if self.step == 0:
            if self.node == 0:
                return self.step_0_node_0()
        if self.step == 1:
            if self.node == 0:
                return self.step_1_node_0()
        if self.step == 2:
            if self.node == 0:
                return self.step_2_node_0()
            if self.node == 1:
                return self.step_2_node_1()
        if self.step == 3:
            if self.node == 0:
                return self.step_3_node_0()
            if self.node == 1:
                return self.step_3_node_1()
            if self.node == 2:
                return self.step_3_node_2()
            if self.node == 3:
                return self.step_3_node_3()
        if self.step == 4:
            if self.node == 0:
                return self.step_4_node_0()
            if self.node == 1:
                return self.step_4_node_1()

    def get_current_node_action_function_name(self):
        return "step_" + str(self.step) + "_node_" + str(self.node) + "_action"

    def is_current_step_end(self):
        if self.step == 4:
            return True
        else:
            return False

    # Step 0
    def step_0_node_0(self):
        return "Welcome! Here are some instructions!"

    def step_0_node_1(self):
        return "You're still stuck at welcome! Press the button!"

    # Step 1
    def step_1_node_0(self):
        return "This is the first step! To move to the left, press the button. To move to the right, do not press the button."

    # Step 2
    def step_2_node_0(self):
        return "This is the left branch of the second step! To move to the left, press the button. To move to the right, do not press the button"

    def step_2_node_1(self):
        return "This is the right branch of the second step! To move to the left, press the button. To move to the right, do not press the button"

    def step_3_node_0(self):
        return "This is branch 0 of the third step! To move to the left, press the button. To move to the right, do not press the button"

    def step_3_node_1(self):
        return "This is branch 1 of the third step! To move to the left, press the button. To move to the right, do not press the button"

    def step_3_node_2(self):
        return "This is branch 2 of the third step! To move to the left, press the button. To move to the right, do not press the button"

    def step_3_node_3(self):
        return "This is branch 3 of the third step! To move to the left, press the button. To move to the right, do not press the button"

    def step_4_node_0(self):
        return "This is a terminal branch! You win."

    def step_4_node_1(self):
        return "This is a terminal branch! You lose."