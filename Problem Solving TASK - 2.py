Guvi Geeks Network Pvt Ltd
Problem Solving TASK - 2

1.Write a Python program to calculate the total number of Vowels and Count of each individual vowel A,E,I,O,U in the string
 "Guvi Geeks Network Private Limited"?

# Define a string
string = "Guvi Geeks Network Private Limited"

# Initialize counters for each vowel
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

# Initialize a total vowel counter
total_vowels = 0

# Loop through each character in the string
for char in string:
  # Convert the character to lowercase
  char = char.lower()
  
  # Check if the character is a vowel
  if char == 'a':
    a_count += 1
    total_vowels += 1
  elif char == 'e':
    e_count += 1
    total_vowels += 1
  elif char == 'i':
    i_count += 1
    total_vowels += 1
  elif char == 'o':
    o_count += 1
    total_vowels += 1
  elif char == 'u':
    u_count += 1
    total_vowels += 1

# Print the results
print("Total vowels:", total_vowels)
print("A:", a_count)
print("E:", e_count)
print("I:", i_count)
print("O:", o_count)
print("U:", u_count)

Output
-------
PS C:\Users\vasan> & C:/Users/vasan/AppData/Local/Programs/Python/Python312/python.exe 
"c:/Users/vasan/OneDrive/Desktop/Python Prgrams Guvi Tasks/FInding Vowels in the given string.py"
Total vowels: 12
A: 1
E: 5
I: 4
O: 1
U: 1
PS C:\Users\vasan>


==================================================================
2) Create a Pyramid of Numbers from 1 to 20 using For loop?

num = 1
for i in range(1, 21):
    for j in range(i):
        if num > 20:
            break
        print(num, end=' ')
        num += 1
    if num > 20:
        break
    print()


Output 
------

PS C:\Users\vasan> & C:/Users/vasan/AppData/Local/Programs/Python/Python312/python.exe 
"c:/Users/vasan/OneDrive/Desktop/Python Prgrams Guvi Tasks/Python Programs.py"
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20
PS C:\Users\vasan>
==================================================================
3) Write a program that takes a string and returns a new string with all the vowels removed.
  
def remove_vowels(string):
 # Define the vowels
    vowels = "aeiouAEIOU"
    # Loop through each character in the input new_string
    new_string = ""
    for char in string:
    # If the character is not a vowel, add it to the new_string
        if char not in vowels:
            new_string += char
    return new_string

# Test the function
string = "Guvi Geeks Network Private Limited"
new_string = remove_vowels(string)
print(new_string)

output:
-------
PS C:\Users\vasan> & C:/Users/vasan/AppData/Local/Programs/Python/Python312/python.exe 
"c:/Users/vasan/OneDrive/Desktop/Python Prgrams Guvi Tasks/Python Programs.py"
Gv Gks Ntwrk Prvt Lmtd
PS C:\Users\vasan>

==================================================================
4) Write a program that takes a string and returns the number of unique characters in it.

def count_unique_chars(string):
    unique_chars = set(string)  # Convert string to set to remove duplicates
    return len(unique_chars)  # Return the number of unique characters

# Test the function
string = "Guvi Geeks Network Private Limited"
num_unique_chars = count_unique_chars(string)
print(num_unique_chars)

Output
-----
PS C:\Users\vasan> & C:/Users/vasan/AppData/Local/Programs/Python/Python312/python.exe 
"c:/Users/vasan/OneDrive/Desktop/Python Prgrams Guvi Tasks/Python Programs.py"
18
PS C:\Users\vasan> 

=========================================================================
5) Write a program that takes a string and returns True if it is a palindrome, False otherwise.

def is_palindrome(string):
    # Remove spaces from the string
    string = string.replace(" ", "")
    
    # Convert the string to lowercase
    string = string.lower()
    
    # Initialize two pointers, one at the start and one at the end of the string
    left = 0
    right = len(string) - 1
    
    # Compare characters from the start and end, moving towards the center
    while left < right:
        if string[left] != string[right]:
            return False  # Not a palindrome
        left += 1
        right -= 1
    
    return True  # Palindrome
    

Output
-----
PS C:\Users\vasan> & C:/Users/vasan/AppData/Local/Programs/Python/Python312/python.exe 
"c:/Users/vasan/OneDrive/Desktop/Python Prgrams Guvi Tasks/Python Programs.py"
False
PS C:\Users\vasan> 

------------------------------------------------------------
def is_palindrome(s):
    # Remove spaces and punctuation
    s = ''.join(filter(str.isalnum, s)).lower()
    # Check if the string equals its reverse
    return s == s[::-1]

# Example usage:
input_string = "A man, a plan, a canal, Panama!"
print(f"Input string: '{input_string}'")
print(f"Is palindrome? {is_palindrome(input_string)}")

Output
-------

PS C:\Users\vasan> & C:/Users/vasan/AppData/Local/Programs/Python/Python312/python.exe 
"c:/Users/vasan/OneDrive/Desktop/Python Prgrams Guvi Tasks/Python Programs.py"
Input string: 'A man, a plan, a canal, Panama!'
Is palindrome? True
PS C:\Users\vasan> 

=========================================================================
6)Write a program that takes two strings and returns the longest common substring between them.

def longest_common_substring(s1, s2):
    m = len(s1)
    n = len(s2)
    result = ""
    length = 0
    
    for i in range(m):
        for j in range(n):
            k = 0
            while i+k < m and j+k < n and s1[i+k] == s2[j+k]:
                k += 1
            if k > length:
                length = k
                result = s1[i:i+k]
    return result

# Test the function
s1 = "ABCDEF"
s2 = "ZBCDFG"
print(longest_common_substring(s1, s2))  # Output: BCD

Output
--------

PS C:\Users\vasan> & C:/Users/vasan/AppData/Local/Programs/Python/Python312/python.exe 
"c:/Users/vasan/OneDrive/Desktop/Python Prgrams Guvi Tasks/Python Programs.py"
BCD
PS C:\Users\vasan> 

==================================================================
7) Write a program that takes a string and returns the most frequent character in it.

def most_frequent_character(s):
    # Initialize variables to track the most frequent character and its count
    max_char = ''
    max_count = 0
    
    # Count occurrences of each character in the string
    for char in s:
        count = s.count(char)
        if count > max_count:
            max_count = count
            max_char = char
    
    return max_char

# Example usage:
input_string = "Guvi Geeks Network Private Limited"
print(f"Input string: '{input_string}'")
print(f"Most frequent character: '{most_frequent_character(input_string)}'")

Output:
------
PS C:\Users\vasan> & C:/Users/vasan/AppData/Local/Programs/Python/Python312/python.exe 
"c:/Users/vasan/OneDrive/Desktop/Python Prgrams Guvi Tasks/Python Programs.py"
Input string: 'Guvi Geeks Network Private Limited'
Most frequent character: 'e'
PS C:\Users\vasan> 

====================================================================
8) Write a program that takes a string and returns True if it is an anagram of another string, False otherwise.

def is_anagram(s1, s2):
    # Remove spaces and convert both strings to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    # Check if the lengths of the strings are equal
    if len(s1) != len(s2):
        return False
    
    # Sort both strings and compare
    return sorted(s1) == sorted(s2)

# Example usage:
string1 = "listen"
string2 = "silent"
print(f"String 1: '{string1}'")
print(f"String 2: '{string2}'")
print(f"Are they anagrams? {is_anagram(string1, string2)}")

Output:
------
PS C:\Users\vasan> & C:/Users/vasan/AppData/Local/Programs/Python/Python312/python.exe 
"c:/Users/vasan/OneDrive/Desktop/Python Prgrams Guvi Tasks/Python Programs.py"
String 1: 'listen'
String 2: 'silent'
Are they anagrams? True
PS C:\Users\vasan> 


==========================================================================
9) Write a program that takes a string and returns the number of words in it.

def count_words(s):
    # Split the string by whitespace to get a list of words
    words = s.split()
    # Return the number of words in the list
    return len(words)

# Example usage:
input_string = "Guvi Geeks Network Private Limited"
print(f"Input string: '{input_string}'")
print(f"Number of words: {count_words(input_string)}")

Output
------
PS C:\Users\vasan> & C:/Users/vasan/AppData/Local/Programs/Python/Python312/python.exe 
"c:/Users/vasan/OneDrive/Desktop/Python Prgrams Guvi Tasks/Python Programs.py"
Input string: 'Guvi Geeks Network Private Limited'
Number of words: 5
PS C:\Users\vasan> 
==================================================================================