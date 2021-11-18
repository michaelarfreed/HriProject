

class Story:
    
    def __init__(self):
        self.step = 0
        self.node = 0
        pass
        
    # utility functions
    def move_to_next_step(self, input):
        pass

    def set_next_node(self, sensor_input):
        if self.step == 0:  # at (step=0, node=0)
            self.node = 0   #   go to (step=1, node=0)
            self.step = 1
        elif self.step == 1:        # at (step=1, node=0)
            self.step = 2
            if sensor_input == 0:   #   input == no button press
                self.node = 0       #     go to (step=2, node=0)
            elif sensor_input == 1: #   input == button press
                self.node = 1       #     go to (step=2, node=1)
        elif self.step == 2:
            self.step = 3
            if self.node == 0:          # at (step=2, node=0)
                if sensor_input == 0:   #   input == no button press
                    self.node = 0       #     go to (step=3, node=0)
                if sensor_input == 1:   #   input == button press
                    self.node = 1       #     go to (step=3, node=1)
            elif self.node == 1:        # at (step=2, node=1)
                if sensor_input == 0:   #   input == no button press
                    self.node = 2       #     go to (step=3, node=2)
                if sensor_input == 1:   #   input == button press
                    self.node = 3       #     go to (step=3, node=3)

    def get_current_step(self):
        if self.step == 0:
            if self.node == 0:
                return step_0_node_0()
        if self.step == 1:
            if self.node == 0:
                return step_1_node_0()
        if self.step == 2:
            if self.node == 0:
                return step_2_node_0()
            if self.node == 1:
                return step_2_node_1()
        if self.step == 3:
            if self.node == 0:
                return step_3_node_0()
            if self.node == 1:
                return step_3_node_1()
            if self.node == 2:
                return step_3_node_2()
            if self.node == 3:
                return step_3_node_3()
    

    # Step 0
    def step_0_node_0(self):
        return "Welcome! Here are some instructions!"

    def step_1_node_0(self):
        return "This is the first step! To move to the left, press the button. To move to the right, do not press the button."

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

    