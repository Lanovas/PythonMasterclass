# Functional Programming
# Code written in functions for re-usability
# Pass one function as an argument to another
def add_ten(x):
    return x + 10

def twice(function, argument):
    return function(function(argument))

print(twice(add_ten, 10))

# Lambdas expressions
def square(x):
    return x**2

print(square(4))

result = (lambda x: x**2)(30)
print(result)

result = (lambda x: x**2)
print(result(30))

# Map
def add(x):
    return x+2
newlist = [1, 2, 20, 30, 60]
# it is like tha apply family of functions in R
result = list(map(add, newlist))
print(result)

newlist = [1, 2, 20, 30, 60]
# it is like tha apply family of functions in R
result = list(map(lambda x: x*2, newlist))
print(result)

# Filters
newlist = [10, 20, 30, 50, 60, 11, 13]
result = list(filter(lambda x: x % 2 == 0, newlist))
print(result)

# Generators - iterable lists or tuples
def function():
    counter = 0
    while counter < 5:
        yield counter
        counter += 1

for x in function():
    print(x)

# A useful example
def even_numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


print(list(even_numbers(21)))


# Coding Challenge 9
def student_discount(price):
    price = price - ( price * 0.10)
    return price


def additional_discount(newprice):
    newprice = newprice - (newprice * 0.05)
    return newprice


selling_price = 100
print(additional_discount(student_discount(selling_price)))

# Coding Challenge 10
result = (lambda x: x*(x+5)**2)(5)
print(result)

# Coding Challenge 11
item_prices = [10, 100, 200, 50]
discounted_prices = list(map(lambda x: x-(x*0.10), item_prices))
print(discounted_prices)


# Object - Oriented Programming (OOP)
# Define the class
class Students:

    # Define the attributes
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    # Define the methods
    def getdata(self):
        print("Accepting data")
        self.name = input("Please enter the name: ")
        self.contact = input("Please enter contact information: ")

    def putdata(self):
        print("The student's name is: {0}, with the following contact information: {1}".format(self.name,
                                                                                               self.contact))


students = Students("Blank", 0)
students.getdata()
students.putdata()


# Inheritance
class ScienceStudent(Students):

    def __init__(self, age):
        self.age = age

    def science(self):
        print("I am a science student")


Rob = ScienceStudent(20)
Rob.science()
Rob.getdata()
Rob.putdata()


# Recursion - calculating a factorial of any number
def factorial(x):
    if x == 1:
        return 1
    else:
        return x*(factorial(x-1))


result = factorial(6)
print(result)


# Sets - one more data structure
numbers = {1, 2, 3, 4, 5, 6}
print(numbers)
print(5 in numbers)
numbers.add(10)
print(numbers)
numbers.remove(3)
print(numbers)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
# union - all items of both sets, with no duplicate entries
print(set_a | set_b)
# intersection - common values in both sets
print(set_a & set_b)
# difference - removes all elements from the first that are common to the second
print(set_a - set_b)


# IterTools - a module for functional programming
from itertools import count
from itertools import accumulate, takewhile

for i in count(3):
    print(i)
    if i >= 20:
        break


numbers = list(accumulate(range(8)))
print(numbers)
print(list(takewhile(lambda x: x <= 6, numbers)))


# Operator OverLoading
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

point1 = Point(1, 4)
point2 = Point(2, 8)
print(point1 + point2)


# Data hiding - encapsulation
class Myclass:
    __hidden_variable = 0

    def add(self, increment):
        self.__hidden_variable += increment
        print(self.__hidden_variable)

object1 = Myclass()
object1.add(5)
object1.__hidden_variable

# Coding Challenge 12
class Computer:
    def __init__(self, ram, memory, processor):
        self.ram = ram
        self.memory = memory
        self.processor = processor

    def getspecs(self):
        print('Please enter the details')
        self.ram = input('Enter ram Size')
        self.memory = input('Enter memory size')
        self.processor = input('Enter processor')

    def displayspecs(self):
        print('Here are the specs of the computer')
        print(' Ram size is: ' + self.ram + ' Memory size is: ' + self.memory + ' processor is: ' + self.processor)


class Desktop(Computer):
    def __init__(self, casecolor):
        self.casecolor = casecolor

    def get_case_details(self):
        self.casecolor = input('Enter case color')

    def put_case_details(self):
        print('case color is: ' + self.casecolor)


class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight

    def getweight(self):
        self.weight = input('Enter weight')

    def displayweight(self):
        print('Weight is: ' + self.weight)


comp = Laptop('');
comp.getspecs()
comp.getweight()
comp.displayspecs()
comp.displayweight()


# Coding Challenge 13
class Multiply:

    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        x = self.x + other.x
        return x


number_a = Multiply(3)
number_b = Multiply(4)

print(number_a * number_b)

# Regular expressions
import re
pattern = r"eggs"

if re.match(pattern, "eggs omelet"):
    print("Match found!")
else:
    print("No match found.")

if re.match(pattern, "omelet with eggs"):
    print("Match found!")
else:
    print("No match found.")

# The search function instead
if re.search(pattern, "omelet with eggs"):
    print("Match found!")
else:
    print("No match found.")

if re.findall(pattern, "omelet with eggs and more eggs"):
    print("Match found!")
    print(re.findall(pattern, "omelet with eggs and more eggs"))
else:
    print("No match found.")

# Find and Replace
string = "My name is John. Hi! I'm John."
pattern = r"John"

if re.search(pattern, string):
    print("Match found!")
    new_string = re.sub(pattern, "James", string)
    print(new_string)
else:
    print("Match not found.")

# The dot meta-character
pattern = r"gr.y"

if re.match(pattern, "gray"):
    print("Match found!")

# Caret and dollar signs
pattern = r"^Greece$"
if re.match(pattern, "IGreece"):
    print("Match found!")
else:
    print("Match not found.")

if re.match(pattern, "Greece"):
    print("Match found!")
else:
    print("Match not found.")

if re.match(pattern, "Greece4"):
    print("Match found!")
else:
    print("Match not found.")

# Character Class
# AA1
pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "AA1"):
    print("Match found!")
else:
    print("Match not found.")

if re.search(pattern, "A1"):
    print("Match found!")
else:
    print("Match not found.")

if re.search(pattern, "A21"):
    print("Match found!")
else:
    print("Match not found.")

if re.search(pattern, "AAB"):
    print("Match found!")
else:
    print("Match not found.")

if re.search(pattern, "AC1"):
    print("Match found!")
else:
    print("Match not found.")

# Star meta-character
pattern = r"eggs(bacon)*"

if re.match(pattern, "eggs"):
    print("Match found!")
else:
    print("Match not found.")

if re.match(pattern, "eggsbacon"):
    print("Match found!")
else:
    print("Match not found.")

if re.match(pattern, "eggsbaconbacon"):
    print("Match found!")
else:
    print("Match not found.")

if re.match(pattern, "eggscheese"):
    print("Match found!")
else:
    print("Match not found.")

if re.match(pattern, "bacon"):
    print("Match found!")
else:
    print("Match not found.")

# Group
pattern = r"bread(eggs)*bread"

if re.match(pattern, "bread"):
    print("Match found!")
else:
    print("Match not found.")

if re.match(pattern, "breadbread"):
    print("Match found!")
else:
    print("Match not found.")

if re.match(pattern, "breadeggsbread"):
    print("Match found!")
else:
    print("Match not found.")
