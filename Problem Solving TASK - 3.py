Guvi Geeks Network Pvt Lid
--------------------------
Problem Solving TASK - 3
--------------------------

1.) You have been given a Python List [10, 501, 22, 37, 100, 999, 87, 351] your task is to
create two List one which have all the Even Numbers and another List which will have all
the ODD numbers in it ?

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Lists to store even and odd numbers
even_numbers = []
odd_numbers = []

# Loop through each number in the list
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)  # Add to even_numbers list
    else:
        odd_numbers.append(number)   # Add to odd_numbers list

# Print the results
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)


OUTPUT:
-------

= RESTART: C:/Users/vasan/OneDrive/Desktop/Python Prgrams Guvi Tasks/Problem Solving TASK - 3.py
Even Numbers: [10, 22, 100]
Odd Numbers: [501, 37, 999, 87, 351]

-------------------------------------------------------------------------------------------------------------------

2.) Given a Python List [10, 501, 22, 37, 100, 999, 87, 351] your task is to Count all the
Prime Numbers and create a new Python List which will contain all the Prime Numbers
in it ?

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# List comprehension to create a new list of prime numbers
prime_numbers = [number for number in numbers if is_prime(number)]

# Count of prime numbers
count_of_primes = len(prime_numbers)

# Print the results
print("Count of prime numbers:", count_of_primes)
print("List of prime numbers:", prime_numbers)

OUTPUT:
--------

= RESTART: C:/Users/vasan/OneDrive/Desktop/Python Prgrams Guvi Tasks/Problem Solving TASK - 3.py
Count of prime numbers: 1
List of prime numbers: [37]


-------------------------------------------------------------------------------------------------------------------
3.) Given a Python List [10, 501, 22, 37, 100, 999, 87, 351] Find out how many numbers are
there in the given Python List which are Happy Numbers ?

# Define a function to check if a number is Happy
def is_happy(number):
  # Create a set to store visited numbers
  seen = set()
  
  # Loop until the number becomes 1 (Happy) or we've seen it before (not Happy)
  while number != 1 and number not in seen:
    # Add the current number to the set of visited numbers
    seen.add(number)
    
    # Initialize a variable to store the sum of squares of digits
    sum_of_squares = 0
    
    # Iterate over each digit in the number
    for digit in str(number):
      # Add the square of the digit to the sum
      sum_of_squares += int(digit) ** 2
      
    # Update the number to the sum of squares
    number = sum_of_squares
    
  # Return True if the number is Happy (reaches 1), False otherwise
  return number == 1

# Create a list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Create a list to store Happy Numbers
happy_numbers = []

# Iterate over the numbers and check if they're Happy
for num in numbers:
  # Check if the number is Happy using the is_happy function
  if is_happy(num):
    # Add the Happy Number to the list
    happy_numbers.append(num)

# Print the Happy Numbers and their count
print("Happy Numbers: ", happy_numbers)
print("Count of Happy Numbers: ", len(happy_numbers))

OUTPUT:
-------
= RESTART: C:\Users\vasan\OneDrive\Desktop\Python Prgrams Guvi Tasks\Problem Solving TASK - 3.py
Happy Numbers:  [10, 100]
Count of Happy Numbers:  2

-------------------------------------------------------------------------------------------------------------------
4.) Write a python program to find the sum of the first and last digit of an integer ?

def sum_of_first_and_last_digit(number):
    # Convert number to positive in case it's negative
    number = abs(number)
    
    # Convert number to string to easily access digits
    number_str = str(number)
    
    # Extract the first and last digits
    first_digit = int(number_str[0])
    last_digit = int(number_str[-1])
    
    # Calculate the sum of the first and last digit
    sum_digits = first_digit + last_digit
    
    return sum_digits

num = 8754561
result = sum_of_first_and_last_digit(num)

print(f"The sum of the first and last digit of {num} is: {result}")

OUTPUT:
-------
= RESTART: C:\Users\vasan\OneDrive\Desktop\Python Prgrams Guvi Tasks\Problem Solving TASK - 3.py
The sum of the first and last digit of 8754561 is: 9
-------------------------------------------------------------------------------------------------------------------

5.) You have been given a list of N integers which represents the number of
Mangoes in a bag. Each bag has a variable number of Mangoes. There are M
students in a Guvi class, your task is to distribute the Mangoes in such a way that
each student gets one Bag. The difference between the number of Mangoes in a
bag with maximum Mangoes and Bag with minimum Mangoes given to the
student is minimum ?

def distribute_mangoes(mangoes, students):
  # Sort the list of mangoes in ascending order
  mangoes.sort()
  
  # Initialize the minimum difference
  min_diff = float('inf')
  
  # Iterate over the list to find the minimum difference
  for i in range(len(mangoes) - students + 1):
    diff = mangoes[i + students - 1] - mangoes[i]
    min_diff = min(min_diff, diff)
  
  return min_diff

# Test the function
mangoes = [10, 20, 30, 40, 50]
students = 3
result = distribute_mangoes(mangoes, students)
print("Minimum difference:", result)

OUTPUT:
-------

PS C:\Users\vasan> & C:/Users/vasan/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/vasan/OneDrive/Desktop/Python Prgrams Guvi Tasks/Problem Solving TASK - 3.py"
Minimum difference: 20
PS C:\Users\vasan> 

-------------------------------------------------------------------------------------------------------------------
6.) You have been given three lists. Your task is to find the duplicates in the three
lists. Write a python program for the same. You can use your own python lists ?

# Define the three lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [4, 5, 9, 10, 11]

# Convert the lists to sets
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

# Find the duplicates using set intersection
duplicates = set1 & set2 & set3

# Print the duplicates
print("Duplicates:", duplicates)

OUTPUT:
--------

PS C:\Users\vasan> & C:/Users/vasan/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/vasan/OneDrive/Desktop/Python Prgrams Guvi Tasks/Problem Solving TASK - 3.py"
Duplicates: {4, 5}
PS C:\Users\vasan> 
-------------------------------------------------------------------------------------------------------------------

7.) Write a python program to find the first non - repeating elements in a given list of
integers ?

def first_non_repeating_element(lst):
  # Create a dictionary to store the count of each element
  count_dict = {}
  for num in lst:
    if num in count_dict:
      count_dict[num] += 1
    else:
      count_dict[num] = 1
  
  # Find the first element with a count of 1
  for num in lst:
    if count_dict[num] == 1:
      return num
  
  # If no non-repeating element is found, return None
  return None

# Test the function
lst = [1, 2, 2, 3, 3, 3, 4, 5, 5]
result = first_non_repeating_element(lst)
print("First non-repeating element:", result)

OUTPUT:
--------

PS C:\Users\vasan> & C:/Users/vasan/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/vasan/OneDrive/Desktop/Python Prgrams Guvi Tasks/Problem Solving TASK - 3.py"
First non-repeating element: 1
PS C:\Users\vasan> 

-------------------------------------------------------------------------------------------------------------------
8.) Write a python program to find the minimum element in a rated and sorted list ?

def find_min(sorted_list):
  # Return the first element of the sorted list
  return sorted_list[0]

# Test the function
sorted_list = [1, 2, 3, 4, 5]
min_element = find_min(sorted_list)
print("Minimum element:", min_element)

OUTPUT:
--------
PS C:\Users\vasan> & C:/Users/vasan/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/vasan/OneDrive/Desktop/Python Prgrams Guvi Tasks/Problem Solving TASK - 3.py"
Minimum element: 1
PS C:\Users\vasan>

-------------------------------------------------------------------------------------------------------------------
9.) You have been given a Python list [10,20,30,9] and a value of 59. Write a python
program to find the triplet in the list whose sum is equal to the given value ?

def find_triplet(lst, target_sum):
  for i in range(len(lst)):
    for j in range(i+1, len(lst)):
      for k in range(j+1, len(lst)):
        if lst[i] + lst[j] + lst[k] == target_sum:
          return [lst[i], lst[j], lst[k]]
  return None

# Test the function
lst = [10, 20, 30, 9]
target_sum = 59
triplet = find_triplet(lst, target_sum)
print("Triplet:", triplet)

OUTPUT:
--------
PS C:\Users\vasan> & C:/Users/vasan/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/vasan/OneDrive/Desktop/Python Prgrams Guvi Tasks/Problem Solving TASK - 3.py"
Triplet: [20, 30, 9]
PS C:\Users\vasan> 
-------------------------------------------------------------------------------------------------------------------
10.) Given a list [4,2,-3,1,6] Write a python program to find if there is a sub-list with
sum equal to Zero ?

def find_zero_sum_sublist(lst):
  for i in range(len(lst)):
    for j in range(i, len(lst)):
      sublist = lst[i:j+1]
      if sum(sublist) == 0:
        return sublist
  return None

# Test the function
lst = [4, 2, -3, 1, 6]
result = find_zero_sum_sublist(lst)
print("Sub-list with sum equal to zero:", result)

OUTPUT:
------
PS C:\Users\vasan> & C:/Users/vasan/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/vasan/OneDrive/Desktop/Python Prgrams Guvi Tasks/Problem Solving TASK - 3.py"
Sub-list with sum equal to zero: [2, -3, 1]
PS C:\Users\vasan> 
