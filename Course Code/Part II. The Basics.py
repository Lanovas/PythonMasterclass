# Error handling
def function_add(a,b):
    print(a/b)

# We need to handle the error, otherwise the code will not run
alpha = 20
beta = 0

try:
    function_add(a=alpha, b=beta)
except ZeroDivisionError:
    print("There is a divide by 0 error")
finally:
    print("This is going to execute no matter what!")

print("Hello!")

alpha = 20
beta = 4

try:
    function_add(a=alpha, b=beta)
except ZeroDivisionError:
    print("There is a divide by 0 error")
finally:
    print("This is going to execute no matter what!")

# File Handling
file_to_open = open(file="demo.txt", mode="r")
# do something with the file
file_content = file_to_open.read()
print(file_content)
file_to_open.close()

file_to_open = open(file="demo.txt", mode="r")
file_content = file_to_open.readline()
print(file_content)
file_to_open.close()

# Write content to the file
file_to_open = open(file="demo.txt", mode="w")
file_content = file_to_open.write("This is the first line written from Python")
file_to_open.close()

file_to_open = open(file="demo.txt", mode="r")
file_content = file_to_open.read()
print(file_content)
file_to_open.close()

# Write however overwrites the content in the file,
# append makes more sense if you want to preserve that
file_to_open = open(file="demo.txt", mode="a")
file_content = file_to_open.write("This is new line, which got appended!")
file_to_open.close()

file_to_open = open(file="demo.txt", mode="r")
file_content = file_to_open.read()
print(file_content)
file_to_open.close()

def divide_numbers(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        print("Please insert a non-zero value for b!")
        return 0

final = divide_numbers(a=10,b=0)
print(final)

# More types, like dictionary and tuples
# Dictionaries
people_ages = {"James": 27,
               "Alan": 40,
               "Johnny": 55}

print(people_ages["James"])
print(people_ages.keys())

numbers = {1: "Maria",
           2: "Woody",
           3: "Mourmoura"}

print(1 in numbers)
print("Maria" in numbers)
print(numbers.get(1))
print(numbers.get(5))
print(numbers.get(5, "Key not found!"))

# Tuples
fruits = ("Apple", "Banana", "Mango")
print(fruits)
print(fruits[1])

fruits[1] = "Orange"

# It can be defined as well like this
fruits = "Apple", "Banana", "Mango"
print(fruits)

# List slicing
numbers = [0, 100, 200, 300, 400, 500, 600]
print(numbers[0:3])
print(numbers[:3])
print(numbers[4:])
print(numbers[0:4:2])
print(numbers[1:6:3])

# List comprehension
square_list = [x**2 for x in range(5)]
print(square_list)

even_list = [x**2 for x in range(10) if x**2 % 2 == 0]
print(even_list)

# String formatting
numbers = [4, 5, 6]
new_string = "Numbers: {0}, {1}, {2}".format(numbers[0], numbers[1], numbers[2])
print(new_string)

date_list = [12, 12, 2016]
new_string = "Date: {0}/{1}/{2}".format(date_list[0], date_list[1], date_list[2])
print(new_string)

a = "{x}/{y}".format(x=100, y=200)
print(a)

# String functions
print(", ".join(fruits))
print("Hello there".replace("there", "World!"))

new_string = "This is a string"
print(new_string.startswith("This"))
print(new_string.isalnum())
print(new_string.endswith("string"))
print(new_string.upper())
print(new_string.lower())

# Numeric functions
print(min(1, 2, 100))
print(max(1, 2, 100))
print(abs(-1))

# Coding Challenge 7
products = {"Laptop": 1200,
            "Mouse": 80,
            "Monitor": 160,
            "Chair": 360,
            "Tablet": 600}
print(len(products))
print(str(products))
print(type(products))

choice = input("Please enter the product that you want the price for: ")
if choice in products:
    print("The price of the product {0} is {1} Euros.".format(choice, products.get(choice)))
else:
    print("Product not found...")

# Coding Challenge 8
new_list = list(range(1, 101))
for x in new_list:
    if x % 2 != 0:
        print(x)
# Or
odd_numbers = [x for x in range(1, 101) if x % 2 != 0]
print(odd_numbers)