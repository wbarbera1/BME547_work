print('This is the database module and python calls it {}'.format(__name__))
# special variables start w/ 2 underscores and describes the python environment

# first module run gets the name __main__, other modules get their own name

# place if __name__ == "__main__": at the beginning of modules

# palce direct commands at the beginning of your programs if you want them run when they are imported

# if 2 modules have functions with the same name, import the module and use "module.function" to specify in the code

# import blood_calculator as bc

from blood_calculator import check_cholesterol, accept_input

from analysis import check_HDL
#import blood_calculator import

HDL_val = 55
name_val = "HDL"
classification = check_cholesterol(name_val, HDL_val)
#classification = blood_calculator.check_cholesterol(name_val, HDL_val)

print('55 is {}'.format(classification))

#import numpy as np ---> good practice, use an alias
#import matplotlib.pyplot as plt

# from blood_calculator import * ---> imports all functions to be called
#       - problem when you have many lines of code and don't rememeber which
#           library the function gets called from (poor practice)