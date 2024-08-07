# This is just to help me learn.
# I love to learn linux
# Hello World
# Hello from Fleet!
print("Hello, World!")

# Variables and Data Types
x = 5
a_string = "Hello"
an_integer = 42
a_float = 3.14
a_boolean = True

# Basic Math Operations
result = 5 + 3
result = 10 - 4
result = 6 * 7
result = 20 / 4
result = 2 ** 3

# Conditional Statements
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# Loops
for i in range(5):
    print(i)
count = 0
while count < 5:
    print(count)
    count += 1

# Lists
my_list = [1, 2, 3, 4, 5]
print(my_list[0])
my_list[0] = 6
my_list.append(7)
my_list.remove(3)
for item in my_list:
    print(item)

# Dictionaries
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
print(my_dict["apple"])
my_dict["banana"] = 4
my_dict["date"] = 6
del my_dict["cherry"]
for key, value in my_dict.items():
    print(key, value)

# Functions
def greet(name):
    print("Hello,", name)
greet("Alice")

# Classes and Objects
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(self.name, "says Woof!")
my_dog = Dog("Buddy")
print(my_dog.name)
my_dog.bark()

# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
