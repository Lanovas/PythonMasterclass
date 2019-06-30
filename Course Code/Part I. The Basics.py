# Basic Python Concepts
# Welcome
print("Hello World!")

# Mathematical Operations
456/0
# Notice the float and integer operations
200+300
500/100
500//100
6.0*3
6*3
2**3
# Nice trick to get the square root of a number
49**(1/2)

7/3
7%3
6%3
7%(5//2)

# Strings
"Hello World!"
"He's a good guy!"
'He\'s a good guy!'

"Hey" + " " + "world!"
"5" + "5"
5+5

"Hello!" + 5
"Hello!" + "5"
"James " * 3
"James " * "2"

# User Input
input("Please enter a value:")
# The newline character
print("Hello James, \nwelcome to the club!\nWe are glad to have you here!")

# Variables
a = 10
b = 20
print(a)
c = a + b
print(c)
d = "James"
# Delete the variable
del a

# Inplace operators
age = 39
age += 1
print(age)
age *= 2
print(age)
age -= 10
print(age)
age //= 2
print(age)

b = "Hello"
b += " World!"
print(b)

# Our first program
# Calculator
p = int(input("Enter the value for the principal value (p): "))
n = int(input("Enter the value for the number of years (n): "))
r = int(input("Enter the value for the interest rate (r): "))

# Simple Interest calculation
simple_interest = (p*n*r)/100

print("The value for the simple interest is: " + str(simple_interest))

# Control Statements
age = int(input("Please enter your age: "))

if age >= 18:
    print("Well done, you are an adult!")
else:
    print("I am sorry, but you are not an adult...")

# Grading student's marks
marks = int(input("Please enter the marks of the student: "))

if marks >= 90:
    print("The student's grade is A")
elif marks >= 70:
    print("The student's grade is B")
elif marks >= 50:
    print("The student's grade is C")
else:
    print("I am sorry, but the student failed the exams...")

# Introduction to lists
names = ["Ultron", "James", "Alan", "Harvey", "Tony"]
print(names)
print(names[0])
print(names[1])
print(names[-1])

numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[3])

empty_list = []
print(empty_list)

# Operations with lists
numbers[2] = 16
print(numbers)
numbers_new = [2, 2, 2, 2, 2]
print(numbers + numbers_new)
print(numbers * 2)

fruits = ["Apple", "Banana", "Mango", "Peach"]
print(fruits)
print("Apple" in fruits)
print("apple" in fruits)
print("Orange" in fruits)

# List functions
fruits.append("Orange")
print(fruits)
print(len(fruits))

fruits.insert(0, "Avocado")
print(fruits)

if "Mango" in fruits:
    print(fruits.index("Mango"))

numbers = list(range(10))
print(numbers)

numbers = list(range(1, 20, 2))
print(numbers)

# Code reuse - functions
def function_print():
    print("Hello James!")
    print("Ultron & Joker!")
    print("Boston Legal!")

function_print()

# For loop
for x in range(1, 11):
    print(x)
    print("James")

fruits = ["Banana", "Peach", "Orange", "Apple"]
for fruit in fruits:
    print(fruit)

# Boolean Logic
username = "admin"
password = "admin123"
# both conditions to be true
if username == "admin" and password == "admin123":
    print("Congrats, you are logged in!")
else:
    print("Sorry, try again...")

username = "user"
password = "admin123"
# one of the conditions to be true
if username == "admin" or password == "admin123":
    print("Congrats, you are logged in!")
else:
    print("Sorry, try again...")

# While loop
counter = 0
# while counter <= 10:
while (counter <= 10):
    print("Alan Shore!")
    print(counter)
    counter += 1

# Coding Challenge 2
fav_food = ["Bimbimbab", "Spatzle", "Cheese", "Steak", "Mousaka", "Corn Flakes"]
print(fav_food[2])

fav_food.append("Croisant")
print(fav_food)

fav_food.insert(3, "Tacos")
print(fav_food)

# Coding Challenge 3
for i in range(5):
    print("I am a programmer")

def square_values():
    for i in range(1, 10, 1):
        print(i*i)
square_values()

# Functions & Modules
def add_numbers(a,b):
    print(a+b)

add_numbers(a = 5, b = 5)
add_numbers(a=100, b=200)

def add(a,b):
    c = a + b
    return c

result = add(a=5, b=10)
print(result)

def add_numbers(a, b):
    return a + b

def square(c):
    return c * c

result = square(c = add_numbers(a = 2, b = 3))
print(result)

# Importing a module
import random

for x in range(5):
    result = random.randint(1,6)
    print(result)

# A Body Mass Index Calculator
def bmi(weight, height):
    bmi_value = round(number=(weight)/pow(height, 2), ndigits=2)
    return bmi_value

user_bmi = bmi(weight = float(input("Please enter the weight in kg: ")),
               height = float(input("Please enter the height in meters: ")))
print(user_bmi)