Problem Solving TASK - 7
------------------------
1.) Write a Python program using Function to which will do the following :-
a.) The function will create a text file with the current timestamp.
b.) The file content should have the content of the current timestamp.

Python code:
------------
import datetime

def create_Curent_timestamp_file():
    # Get the current timestamp
    # strftime function in Python is used to format dates and times. It stands for "string format time" 
    #and is part of the datetime module. strftime allows you to convert a datetime object 
    #into a string that represents the date and time in a specified format.
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create a filename with the current timestamp
    filename = "Curent_timestamp_" + current_timestamp + ".txt"
    
    # Write the current timestamp into the file
    with open(filename, 'w') as file:
        file.write(current_timestamp)
    
    return filename

# Example usage
file_name = create_Curent_timestamp_file()
print("File created:", file_name)

------------------------------------------------------------------------------------------------------
2.) Write another Python function to read from a text file. The function will take the name of
the text file and display the content of the file into the console.

Python code:
------------

def read_file(filename):
    try:
        # Open the file and read the content
        with open(filename, 'r') as file:
            content = file.read()
            print("Content of", filename + ":")
            print(content)
    except FileNotFoundError:
        print("The file", filename, "does not exist.")

# Example usage
read_file(file_name)#calling a Function 

--------------------------------------------------------------------------------------------------------

Full Python code which will write and read the text file 
---------------------------------------------------------

import datetime

def create_Curent_timestamp_file():
    # Get the current timestamp
    # strftime function in Python is used to format dates and times. It stands for "string format time" 
    #and is part of the datetime module. strftime allows you to convert a datetime object 
    #into a string that represents the date and time in a specified format.
        
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create a filename with the current timestamp
    filename = "Curent_timestamp_" + current_timestamp + ".txt"
    
    # Write the current timestamp into the file
    with open(filename, 'w') as file:
        file.write(current_timestamp)
    
    return filename

def read_file(filename):
    try:
        # Open the file and read the content
        with open(filename, 'r') as file:
            content = file.read()
            print("Content of", filename + ":")
            print(content)
    except FileNotFoundError:
        print("The file", filename, "does not exist.")

# Example usage
file_name = create_Curent_timestamp_file()
print("File created:", file_name)


# Reading the created file
read_file(file_name)#calling a Function 
--------------------------------------------------------------------------------------------------------

OUTPUT:
-------

=============================== RESTART: C:/Users/vasan/Desktop/Python Prgrams Guvi Tasks/Creating new file with python.py ==============================
File created: Current_timestamp_2024-07-12_13-37-41.txt
Content of Current_timestamp_2024-07-12_13-37-41.txt:
2024-07-12_13-37-41