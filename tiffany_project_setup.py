"""
Module: Tiffany_project_setup

Purpose: Provide functions to script project folders (and domonstrate basic Python coding skills).

Description: This module provides functions for creating a series of project folders.

Author: Tiffany Hildebrand


"""

#####################################
# Import Modules at the Top
#####################################

# Import moduldes from standand library
# TODO: Import additional modules as needed
import pathlib
import time

from click import Argument

# Import local modules
# TODO: Change this to import your module and uncomment
import tjh2_utils 

#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    # Ensure this loop is indented correctly
    for year in range(start_year, end_year + 1):  # Correct scope
        year_folder = data_path.joinpath(str(year))
        year_folder.mkdir(exist_ok=True)
        print(f"Created folder: {year_folder}")


  
#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    '''

    
    Arguments:
    folder_list -- A list of folder names to create.
    to_lowercase -- If True, convert folder names to lowercase.
    remove_spaces -- If True, replace spaces with underscores.
   
    Returns:
    None
    '''

    for folder_name in folder_list:
        if to_lowercase:
            folder_name = folder_name.lower()               
        if remove_spaces:
            folder_name = folder_name.replace(" ", "_")     
                
        folder_name = data_path.joinpath(folder_name)       # Create a path object for the folder
        folder_name.mkdir(parents=True, exist_ok=True)      # Create the folder if it doesn't exist
        print(f"Created folder: {folder_name}")

    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_from_list with folder_list={folder_list}, to_lowercase={to_lowercase}, remove_spaces={remove_spaces}")

     
#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
 '''
 Arguments:
    folder_list -- A list of folder names to create.
    prefix -- A prefix added to each folder name. '''
 
 for folder_name in folder_list:
    folder_name = f"{project_path}/{prefix}- {name.lower()}"
    pathlib.Path(folder_name.replace(" ","_")).mkdir(parents=True, exist_ok=True)
      
    print(f"Created folder: {folder_name} from list '{folder_list}'")
            

    # Log the function call and its arguments using an f-string
    print(f" Created folder:{folder_name} from list '{folder_list}'")

#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int, max_folders: int) -> None:
    '''Arguments: 
       duration_seconds-- The time in seconds to wait before creating the next folder.
       max_folders -- maxium number of folders'''
    for i in range(max_folders + 1):
        folder_name = f"folder{i+1}"
        folder_path = data_path.joinpath(folder_name)
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")
        time.sleep(duration_seconds)


  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    # TODO: Change this to use your module function and uncomment
    # print(f"Byline: {case_utils.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # TODO: Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    # Uncomment this line after you've added your custom logic
    # create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

#TODO: Run this as a script to test that all functions work as intended.
