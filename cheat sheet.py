      #---IMPORTS---
# Import a package without an alias
import pandas 
# Import a package with an alias
import pandas 
# Import an object from a package
from pandas import DataFrame


      #--ARITHMETIC OPERATORS--
# Add two numbers with +
102 + 37 

# Subtract a number with -
102 - 37 

# Multiply two numbers with * 
4 * 6  

# Divide a number by another with /
22 / 7  

# Integer divide a number with //
22 // 7 

# Raise to the power with ** 
3 ** 4 
 
#Get the remainder after division with %
22 % 7  

      #--ASSIGNMENT OPERATORS--
a = 5 # Assign a value to a
x[0] = 1  # Change the value of an item in a list

      #--NUMERIC OPERATORS--
# Test for equality with ==
3 == 3

# Test for inequality with !=
3 != 3 

# Test greater than with >
3 > 1 

      #---LOGICAL OPERATORS---
# Logical NOT with ~
~( 2 == 2 )

# Logical AND with &
( 1 != 1 ) & ( 1 < 1 )

# Logical OR with |
( 1 >= 1 ) | ( 1 < 1 )

# Logical XOR with ^
( 1 != 1 ) ^ ( 1 < 1 )



      #---LISTS---
# Create a list
fruits = ["apple", "banana", "cherry"]

# Access an item by index (0-based)
first_fruit = fruits[0]  # "apple"

# Change an item by index
fruits[1] = "blueberry"  # fruits becomes ["apple", "blueberry", "cherry"]

# Add an item to the end of the list with append()
fruits.append("orange")  # fruits becomes ["apple", "blueberry", "cherry", "orange"]

# Remove an item from the list by value
fruits.remove("cherry")  # fruits becomes ["apple", "blueberry", "orange"]

# Remove an item by index with pop()
last_fruit = fruits.pop()  # removes "orange" and returns it, fruits becomes ["apple", "blueberry"]

# Get the length of a list
length = len(fruits)  # 2

# Iterate through a list
for fruit in fruits:
    print(fruit)

# Check if an item is in the list
if "apple" in fruits:
    print("Apple is in the list")
    
    
    
    
          #---DICTIONARIES---
# Create a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Access a value by key
name = person["name"]  # "Alice"

# Change a value by key
person["age"] = 26  # person becomes {"name": "Alice", "age": 26, "city": "New York"}

# Add a new key-value pair
person["email"] = "alice@example.com"  # person becomes {"name": "Alice", "age": 26, "city": "New York", "email": "alice@example.com"}

# Remove a key-value pair with pop()
email = person.pop("email")  # removes "email" and returns it, person becomes {"name": "Alice", "age": 26, "city": "New York"}

# Get all keys in a dictionary
keys = person.keys()  # dict_keys(['name', 'age', 'city'])

# Get all values in a dictionary
values = person.values()  # dict_values(['Alice', 26, 'New York'])

# Iterate through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# Check if a key is in the dictionary
if "name" in person:
    print("Name key is present")




   #---STRING OPERATIONS---
# Create a string
greeting = "Hello, World!"

# Access a character by index
first_char = greeting[0]  # "H"

# Slice a string
substring = greeting[0:5]  # "Hello"

# Convert to uppercase/lowercase
upper_case = greeting.upper()  # "HELLO, WORLD!"
lower_case = greeting.lower()  # "hello, world!"

# Replace a substring
new_greeting = greeting.replace("World", "Python")  # "Hello, Python!"

# Check if a substring is in a string
contains_hello = "Hello" in greeting  # True

# Split a string into a list of substrings
words = greeting.split(", ")  # ["Hello", "World!"]

# Join a list of strings into a single string
joined_string = " ".join(words)  # "Hello World!"

# Strip whitespace
trimmed_string = "  Hello  ".strip()  # "Hello"




   #---LOOPS---
# For loop
for i in range(5):
 print(i)  # Prints 0, 1, 2, 3, 4

# While loop
count = 0
while count < 5:
 print(count)
 count += 1  # Prints 0, 1, 2, 3, 4




   #---FUNCTIONS---
# Define a function
def greet(name):
 return f"Hello, {name}!"

# Call a function
message = greet("Alice")  # "Hello, Alice!"

# Function with default arguments
def greet(name="Guest"):
 return f"Hello, {name}!"



   #---CONDITIONALS---
# Basic if-else statement
x = 10
if x > 5:
 print("x is greater than 5")
else:
 print("x is 5 or less")

# if-elif-else statement
if x > 10:
 print("x is greater than 10")
elif x == 10:
 print("x is 10")
else:
 print("x is less than 10")
 
 
 
    #---EXCEPTION HANDLING---
# Handle exceptions with try-except
try:
 result = 10 / 0
except ZeroDivisionError:
 print("You can't divide by zero!")

# Use finally to ensure code runs
try:
 result = 10 / 2
finally:
 print("This will run no matter what.")



