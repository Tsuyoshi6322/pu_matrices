# from functools import partial
# from collections import defaultdict
# from tabulate import tabulate
# import numpy as np
# import random

from functions.user_input import *
from functions.program_menu import *


# First matrix
dimensions_one, matrix_one = tworzenieMacierzy()


# Declaring user's choice of task
choice = display_menu()

# Depending on the choice, the second matrix is created
if choice < 4:
    dimensions_two, matrix_two = tworzenieMacierzy()

else:
    dimensions_two, matrix_two = []


# Task execution
task_choice(choice, matrix_one, matrix_two, dimensions_two)


# End of the program
print("""
        ===================================================
                        End of the program                    
        ===================================================""")