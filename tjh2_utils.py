"""
Module: utils_tjh2

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

I like dogs, and have had several over the years of various ages and breed types. 
I just used something I know about for this project.  

Author: Tiffany Hildebrand

TODO: Change the module name in this opening docstring
TODO: Change the author in this opening docstring
"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

#####################################
# Declare Global Variables
#####################################

import statistics  # provides mean(), stdev() and more....

# declare a boolean variable (has a value True or False)
# TODO: Add another or replace this with your own boolean variable
Has_pet_dog: bool = True

# declare an integer variable 
# TODO: Add or replace this with your own integer variable
Age_of_dog: int = 17

# declare a floating point variable
# TODO: Add or replace this with your own floating point variable
average_dog_age: float = 10

# declare a list of strings
# TODO: Add or replace this with your own list  
dog_Breeds: list = ["Min Pin", "Pit", "Akita"]

# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your own numeric list  
dog_age_all_breed: list = [17,3,7,14,10,8]

# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your own numeric list - completed
min_age: float = min(dog_age_all_breed)  
max_age: float = max(dog_age_all_breed)  
mean_age: float = statistics.mean(dog_age_all_breed)  
stdev_age: float = statistics.stdev(dog_age_all_breed)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information - done 
# TODO: Modify the variables in the byline to use your variable names
byline: str = f""" 
---------------------------------------------------------
Stellar Analytics: Delivering Professional Insights
---------------------------------------------------------
Has Pet Dog:  {Has_pet_dog}
Age of Dog:         {Age_of_dog}
Dog Breed:             {dog_Breeds}
Breed age: {dog_age_all_breed}
Minimum Dog Age: {min_age}
Maximum Dog Age: {max_age}
Mean Dog Age: {mean_age:.2f}
Standard Deviation of Dog Age: {stdev_age:.2f}
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.
