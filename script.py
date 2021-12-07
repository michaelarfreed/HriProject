

class Story:
    
    def __init__(self):
        self.step = 0
        self.node = 0
        self.done = False
        pass
        
    # utility functions
    def set_next_node(self, sensor_input):
        if self.step == 0:         # at (step=0, node=0)
            if self.node == 0: 
                if sensor_input == -1: #   no button press
                    self.node = 0      #     go to (step=0, node=) / repeat intro
                else:                  #   any button press
                    self.node = 1      #     go to (step=1, node=1)
            elif self.node == 1:
                self.step = 1        # move to next step = 1

        elif self.step == 1:        # at (step=1, node=0)
            if sensor_input != -1:  #   recieved input
                self.step = 2       #     move to next step = 2
            if sensor_input == 0:   #   touch sensor press
                self.node = 0       #     go to (step=2, node=0)
            elif sensor_input == 1: #   center button press
                self.node = 1       #     go to (step=2, node=1)
                
        elif self.step == 2:
            if sensor_input != -1:      # recieved input
                self.step = 3           #   move to next step =3
            if self.node == 0:          # at (step=2, node=0)
                if sensor_input == 0:   #   input == touch sensor press
                    self.node = 0       #     go to (step=3, node=0)
                elif sensor_input == 1:   #   input == center button press
                    self.node = 1       #     go to (step=3, node=1)
            elif self.node == 1:        # at (step=2, node=1)
                if sensor_input == 0:   #   input == touch sensor press
                    self.node = 1       #     go to (step=3, node=1)
                elif sensor_input == 1:   #   input == center button press
                    self.node = 2       #     go to (step=3, node=2)
        elif self.step == 3:
            if sensor_input != -1:      # recieved input
                self.step = 4           #   move to next step = 4
            elif self.node == 0:          # at (step=3, node=0)
                if sensor_input == 0:   #   input == touch sensor press
                    self.node = 0       #     go to (step=4, node=0)
                elif sensor_input == 1:   #   input == center button press
                    self.node = 1       #     go to (step=4, node=1)
            elif self.node == 1:          # at (step=3, node=1)
                if sensor_input == 0:   #   input == touch sensor press
                    self.node = 0       #     go to (step=4, node=0)
                elif sensor_input == 1:   #   input == center button press
                    self.node = 1       #     go to (step=4, node=1)
            elif self.node == 2:          # at (step=3, node=2)
                if sensor_input == 0:   #   input == touch sensor press
                    self.node = 2       #     go to (step=4, node=2)
                elif sensor_input == 1:   #   input == center button press
                    self.node = 3       #     go to (step=4, node=3)
        elif self.step == 4: 
            if sensor_input != -1:
                self.step = 5           # move to next step = 5
            if self.node == 0:          # step 4, node 0
                if sensor_input == 0:   # input = touch sensor
                    self.node = 1       # go to step 5, node 1
                elif sensor_input == 1:   # input = center button
                    self.node = 0       # go to step 5 node 0

            elif self.node == 1:          # step 4, node 1
                if sensor_input == 0:   # input = touch sensor
                    self.node = 0       # go to step 5, node 0
                elif sensor_input == 1:   # input = center button
                    self.node = 1       # go to step 5 node 1

            elif self.node == 2:          # at step 4 node 2
                if sensor_input == 0:   # input = touch sensor
                    self.node = 2       # go to step 5 node 2
                elif sensor_input == 1:   # input = center button
                    self.mode = 3       # go to step 5 node 3

            elif self.node == 3:          # at step 4 node 3
                if sensor_input == 0:   # input = touch sensor
                    self.node = 2      # go to step 5 node 2
                elif sensor_input == 1:   # input = center button
                    self.node = 3 
        elif self.step == 5:
            if sensor_input != -1:
                self.step = 6           # move to next step = 6          
            if self.node == 0:           # at step 5 node 0
                if sensor_input == 0:    # input = touch sensor
                    self.node = 0       # go to step 6 node 0
                elif sensor_input == 1:   # input = center button
                    self.node = 1       # go to step 6 node 1
            elif self.node == 1:          # at step 5 node 1
                if sensor_input == 0:    # input = touch sensor
                    self.node = 2       # go to step 6 node 2
                elif sensor_input == 1:   # input = center button
                    self.node = 3       # go to step 6 node 3

            elif self.node == 2:          # at step 5 node 2
                if sensor_input == 0:    # input = touch sensor
                    self.node = 2       # go to step 6 node 2
                elif sensor_input == 1:   # input = center button
                    self.node = 3       # go to step 6 node 3

            elif self.node == 3:          # at step 5 node 3
                if sensor_input == 0:    # input = touch sensor
                    self.node = 3       # go to step 6 node 3
                elif sensor_input == 1:   # input = center button
                    self.node = 2       # go to step 6 node 2

        elif self.step == 6:
            if sensor_input != -1:
                self.step = 7           # move to next step = 6          
            if self.node == 0:           # at step 6 node 0
                if sensor_input == 0:    # input = touch sensor
                    self.node = 0       # go to step 7 node 0
                elif sensor_input == 1:   # input = center button
                    self.node = 1       # go to step 7 node 1
            elif self.node == 1:          # at step 6 node 1
                if sensor_input == 0:    # input = touch sensor
                    self.node = 0       # go to step 7 node 0
                elif sensor_input == 1:   # input = center button
                    self.node = 1       # go to step 7 node 1
            elif self.node == 2:          # at step 6 node 2
                if sensor_input == 0:    # input = touch sensor
                    self.node = 1       # go to step 7 node 1
                elif sensor_input == 1:   # input = center button
                    self.node = 2       # go to step 7 node 2

            elif self.node == 3:          # at step 5 node 3
                if sensor_input == 0:    # input = touch sensor
                    self.node = 2       # go to step 7 node 2
                elif sensor_input == 1:   # input = center button
                    self.node = 3       # go to step 7 node 3

        elif self.step == 7:
            self.ev3.speaker.say("The game is over, thank you for playing with me!")



    def get_current_step(self):
        return self.step

    def get_current_node_text(self, robot_form_factor):
        if self.step == 0:
            if self.node == 0:
                return self.step_0_node_0(robot_form_factor)
        if self.step == 1:
            if self.node == 0:
                return self.step_1_node_0(robot_form_factor)
        if self.step == 2:
            if self.node == 0:
                return self.step_2_node_0(robot_form_factor)
            if self.node == 1:
                return self.step_2_node_1(robot_form_factor)
        if self.step == 3:
            if self.node == 0:
                return self.step_3_node_0(robot_form_factor)
            if self.node == 1:
                return self.step_3_node_1(robot_form_factor)
            if self.node == 2:
                return self.step_3_node_2(robot_form_factor)
            if self.node == 3:
                return self.step_3_node_3(robot_form_factor)
        if self.step == 4:
            if self.node == 0:
                return self.step_4_node_0(robot_form_factor)
            if self.node == 1:
                return self.step_4_node_1(robot_form_factor)
            if self.node == 2:
                return self.step_4_node_2(robot_form_factor)
            if self.node == 3:
                return self.step_4_node_3(robot_form_factor)
        if self.step == 5:
            if self.node == 0:
                return self.step_5_node_0(robot_form_factor)
            if self.node == 1:
                return self.step_5_node_1(robot_form_factor)
            if self.node == 2:
                return self.step_5_node_2(robot_form_factor)
            if self.node == 3:
                return self.step_5_node_3(robot_form_factor)
        if self.step == 6:
            if self.node == 0:
                return self.step_6_node_0(robot_form_factor)
            if self.node == 1:
                return self.step_6_node_1(robot_form_factor)
            if self.node == 2:
                return self.step_6_node_2(robot_form_factor)
            if self.node == 3:
                return self.step_6_node_3(robot_form_factor)
        if self.step == 7:
            if self.node == 0:
                return self.step_7_node_0(robot_form_factor)
            if self.node == 1:
                return self.step_7_node_1(robot_form_factor)
            if self.node == 2:
                return self.step_7_node_2(robot_form_factor)
            if self.node == 3:
                return self.step_7_node_3(robot_form_factor)

    def get_current_node_action_function_name(self):
        return "step_" + str(self.step) + "_node_" + str(self.node) + "_action"

    def is_current_step_end(self):
        if self.step == 4:
            return True
        else:
            return False

    def get_form_specific_action(self, form):
        if form == 0: # puppy
            return "pat my back. "
        if form == 1: # gyroboy
            return "hold my hand. "
        if form == 2: # car
            return "honk the horn. "    
        return "press the touch sensor. "

    # Step 0
    def step_0_node_0(self, form):
        instructions = (
            "Welcome! Today, we are going to tell a story together. "
            "At each step, I will give you two choices. "
            "For one choice, you will " +
            self.get_form_specific_action(form) +
            "For the second choice, you will push the button at the center of the keypad. "
            "If you would like to hear the instructions again, " +
            self.get_form_specific_action(form) +
            "If you understand, press the center button."
        )

        return instructions

    # Step 1
    def step_1_node_0(self, form):
        instructions = (
            "Great! I’m so excited, because I need some help delivering a top-secret letter to special agent double oh seven, "
            "but I can’t remember where to find them. "
            "We are in Halligan, but we can’t go out the front door. "
            "Should we call a helicopter from the roof, "
            "or should we sneak out through the vents? " +
            self.get_form_specific_action(form) +
            " to take the helicopter. "
            "Press the center button to take the vents."
        )

        return instructions

    # Step 2
    def step_2_node_0(self, form):
        instructions = (
            "The vents are dark, and we’re at a cross-roads. "
            "Which way should we check first? " +
            self.get_form_specific_action(form) +
            " to turn left. "
            "Press the center button to turn right."
        )

        return instructions

    def step_2_node_1(self, form):
        instructions = (
            "The helicopter is here and we are in the air! "
            "But, I think someone spotted us, because we are being followed. "
            "What should we do? " +
            self.get_form_specific_action(form) +
            " to take the helicopter. "
            "Press the center button to take the vents."
        )

        return instructions

    def step_3_node_0(self, form):
        instructions = (
            "Oh no, I think we’re lost! Do you want to turn around? " +
            self.get_form_specific_action() +
            " to turn around. "
            "Press the center button to keep going."
        )

        return instructions

    def step_3_node_1(self, form):
        instructions = (
            "You landed on top of Dunkin Donuts. "
            "Are you hungry? " +
            self.get_form_specific_action(form) +
            " stop for a snack. "
            "Press the center button to continue without stopping."
        )

        return instructions

    def step_3_node_2(self, form):
        instructions = (
            "They’re still on our tail! Quick, we need a distraction. "
            "Should we throw a banana peel or try on a silly disguise?" +
            self.get_form_specific_action() +
            " to throw the banana peel. "
            "Press the center button to put on a fake mustache."
        )

        return instructions

    def step_3_node_3(self, form):
        instructions = (
            "How weird, we ended up in a Dunkin Donuts. "
            "Are you hungry? " +
            self.get_form_specific_action(form) +
            " stop for a snack. "
            "Press the center button to continue without stopping."
        )

        return instructions

    def step_4_node_0(self, form):
        instructions = (
            "Yum! I love donuts. But I think I spot someone following us outside! "
            "What should we do as a distraction? " +
            self.get_form_specific_action(form) +
            " to sneak out the back door. "
            "Press the center button to challenge them to a race."
        )

        return instructions

    def step_4_node_1(self, form):
        instructions = (
            "Oh no, I think someone is following us, and they’ve spotted us. What should we do? " +
            self.get_form_specific_action(form) +
            " to challenge them to a race. "
            "Press the center button to hide under the table."
        )

        return instructions

    def step_4_node_2(self, form):
        instructions = (
            "Wow, they’re so clumsy. But that was the perfect distraction to give us time to get away! "
            "Now that we’re outside, where should we check? " +
            self.get_form_specific_action(form) +
            " to run out onto the street. "
            "Press the center button to call out for help."
        )

        return instructions

    def step_4_node_3(self, form):
        instructions = (
            "Wow, I can’t believe those other people don’t recognize us. "
            "Now that they’re distracted, where should we check? " +
            self.get_form_specific_action(form) +
            " to run out onto the street. "
            "Press the center button to call out for help."
        )

        return instructions

    def step_5_node_0(self, form):
        instructions = (
            "There is no other choice but to face the people following us. "
            "We can challenge them to a contest to see who they are and try to get information from them. "
            "Let’s challenge them to an arm wrestle. " +
            self.get_form_specific_action(form) +
            " to use your left arm. "
            "Press the center button to use your right arm."
        )

        return instructions

    def step_5_node_1(self,form):
        instructions = (
            "Let’s take our chances and sneak out through the back door! "
            "It looks like there’s no one there, so let's run down the street to lose them. "
            "What direction should we run towards? " +
            self.get_form_specific_action(form) +
            " to turn towards the river. "
            "Press the center button to turn towards the dining hall."
        )

        return instructions

    def step_5_node_2(self, form):
        instructions = (
            "Ok, we are out on the street. "
            "We could head for the river, or we could go into the dining hall. " +
            self.get_form_specific_action(form) +
            " to turn towards the river. "
            "Press the center button to duck into the dining hall."
        )

        return instructions

    def step_6_node_0(self, form):
        instructions = (
            "We best them with our strength, so they must tell us where the special agent is. "
            "They give us the answer. But do we trust them? "  +
            self.get_form_specific_action(form) +
            " if you trust them. "
            "Press the center button if you do not trust them."
        )

        return instructions

    def step_6_node_1(self, form):
        instructions = (
            "We cannot overcome the strength of our opponent. "
            "However, they give us some information anyways, "
            "and they tell us that the special agent is hiding on the bus next to the ferry. "
            "Should we trust them? "  +
            self.get_form_specific_action(form) +
            " if you trust them. "
            "Press the center button if you do not trust them."
        )

        return instructions
    
    def step_6_node_2(self, form):
        instructions = (
            "We run towards the river. "
            "The best way to get distance from our pursuer is to hop into a boat. "
            "We look over and see that there are two possible sources of transport in front of us. "
            "Which one should we choose? " +
            self.get_form_specific_action(form) +
            " to get in a row boat and enter the head of the charles. "
            "Press the center button to take the ferry that is leaving the dock."
        )

        return instructions

    def step_6_node_3(self, form):
        instructions = (
            "We run into the dining hall and hide among the crowd. "
            "Since we’re here, we may as well stop for a snack! What should we eat? " +
            self.get_form_specific_action(form) +
            " to have get an Italian sandwich from the deli. "
            "Press the center button to have a bowl of frosted mini wheats."
        )

        return instructions

    def step_7_node_0(self):
        instructions = (
            "We decided not to trust them, but they were telling the truth. "
            "We are sent on a wild goose chase across the country, and we are never able to deliver the letter."
        )

        return instructions

    def step_7_node_1(self):
        instructions = (
            "With the other people racing around us, our adrenaline kicks in, and we paddle extremely fast. "
            "We reach the other side of the river, and there is someone waiting there. "
            "You speak to them, and they tell you they are not the recipient of the letter! "
            "Unfortunately you are not in the right place, but this mysterious person can take over your mission and deliver the letter."
        )

        return instructions

    def step_7_node_2(self):
        intructions = (
            "With its powerful engines, the ferry is surely the way to go. "
            "We hop on, and it takes us to another port, at which point we run onto a bus. "
            "The bus travels for half an hour, and when it arrives at the final stop, secret agent 007 is there, waiting to receive the letter. "
            "Good job!"
        )
        
        return instructions 