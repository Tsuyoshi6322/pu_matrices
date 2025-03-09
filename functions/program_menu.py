from classes.matrix_dimensions import *
from functions.calculations_matrices import *
from functions.calculations_two_matrices import *
from functions.user_input import get_valid_input


# Task menu
def display_menu():
    while True:
        print("""
        =====================================================================
                                     Task menu                              
        =====================================================================
            [1]  Sum of two matrices
            [2]  Substraction of two matrices
            [3]  Multiplication product of two matrices
            [4]  Transposition of a single matrix
            [5]  Zeroing the elements on the main diagonal of the matrix
            [6]  Product of the inverses of the non-zero elements of a matrix
            [7]  Arithmetic mean of all values in the matrix
            [8]  Geometric mean of all values in the matrix
            [9]  Frequency of occurence (a table) of each value in the matrix
            [10] LU decomposition using Doolittle's method
        =====================================================================\n""")

        choice = get_valid_input("Provide a task number (1-10): ")

        if 1 <= choice <= 10:
            print(f"Chosen task: {choice}")
            return choice
        else:
            print("There is no such task")
            print("Try again")


# Task execution
def task_choice(choice, matrix_one, matrix_two, dimensions_two):
    match choice:
        case 1:  sum_of_matrices(matrix_one,matrix_two)
        case 2:  subtraction_of_matrices(matrix_one,matrix_two)
        case 3:  multiplication_product(matrix_one,matrix_two)
        case 4:  transposition(matrix_one)
        case 5:  zeroing_diagonal(matrix_one)
        case 6:  product_of_inverses(matrix_one)
        case 7:  arithmetic_mean(matrix_one)
        case 8:  geometric_mean(matrix_one)
        case 9:  frequency_of_occurence(matrix_one)
        case 10: decomposition_LU(dimensions_two, matrix_one)
        case _:  print("There is no such task - error task_choice()")