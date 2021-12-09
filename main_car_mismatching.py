#!/usr/bin/env pybricks-micropython
from main import *

if __name__ == '__main__':
    experiment = Experiment(form=2, behavior=False)
    finished = experiment.run()
    experiment.write_sensor_input_to_file()
