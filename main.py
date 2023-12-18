from econfunctions import *
import numpy as np

# Get user input for the function call
while True:
    try:
        user_input = input("Enter String(Ctrl+C ) To Break use help() for introduction: ")
        # Use eval to execute the user input
        result = eval(user_input)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)
