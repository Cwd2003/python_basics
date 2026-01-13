# Variables
#Definition -> A variable is a container used to store data values in memory

#Syntax-> variable_name = value

#Example -> Box name = age

#Inside value = 21

#Example With Code->

age = 22
name= "Deepak"
marks = 85.5 

print(age)
print(name)
print(marks)


# Conditions(if, else, elif)

#Definition-> Conditions are used to make decisions based on true or false situations.

#Syntax -> if condition: statement
# elif condition:statement
# else: statement

#Example->
marks = 55

if marks >= 40:
    print("Pass")
else:
    print("Fail")

#Loops->
# Definition->Loops are used to repeat a block of code multiple times

#1. For Loop
#Syntax for variable in sequence: statement
#Example -> Calling roll numbers in a class.
for i in range(1,6):
    print(i)
#2. While Loop
# Syntax -> while condition: statement 
# Real-Life Example -> Charging phone until battery is 100%
battery =20

while battery <100:
    print("Charging...",battery)
    battery +=20

#Functions-> A function is a block of reusable code that performs a specific task.
#Syntax def function_name(parameters):
#           statements
#           return value
# Example->A coffee machine: Input: coffee powder, water ,Output: coffee

def add(a, b):
    return a + b

result = add(5, 3)
print(result)        

#Lists->A list stores multiple values in a single variable
#Ordered  and Changeable (mutable)
# Syntax-> list_name = [value1, value2, value3]
# Example-> Shopping List
fruits = ["apple", "banana", "mango"]

print(fruits)
print(fruits[0])      # apple

fruits.append("orange")
print(fruits)

#Tuples-> A tuple is like a list but:Ordered Unchangeable (immutable)
#Syntax->tuple_name = (value1, value2)
#Example-> Coordinates on a map (fixed values)
location = (28.61, 77.20)
print(location)

# Sets->A set stores unique values only.Unordered ,No duplicates
#Syntax ->set_name = {value1, value2}
#Example ->Roll numbers in a class (no duplicates)
numbers = {1, 2, 3, 3, 4}
print(numbers)   # duplicates removed

#Dictionaries->A dictionary stores data in key : value pairs.
#Syntax->dict_name = { key1: value1, key2: value2}

#Example->Student record Name → Marks Roll No → Details
student = {
    "name": "Deepak",
    "age": 21,
    "marks": 85
}

print(student["name"])
print(student["marks"])

# Combined allconcepts example
students = {
    "Amit": 78,
    "Riya": 35,
    "Kunal": 90
}

for name, marks in students.items():
    if marks >= 40:
        print(name, "Pass")
    else:
        print(name, "Fail")


