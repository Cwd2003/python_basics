#File handling-> File handling means reading, writing, and updating data stored in files so that data is saved permanently.
# Data stored in variables is temporary Data stored in files is permanent
#Example->Student register book
# Write student data Read student data later
#File Modes
#Mode	Meaning
#r	Read
#w	Write (overwrite)
#a	Append
#x	Create new file

#Basic Syntax-> 
#file = open("filename.txt", "mode")
#file.read() / file.write()  file.close()

#writing to a file 
file= open("data.txt","w")
file.write("Hello Python\n")
file.write("File handling example")
file.close()

# Reading to a file
file=open("data.txt","r")
content=file.read()
print(content)
file.close()

# Best method-> with open("data.txt","r") as file:
#                     print(file.read())

def save_student(name, marks):
    with open("students.txt", "a") as file:
        file.write(f"{name} - {marks}\n")

save_student("Deepak", 85)
save_student("Riya", 78)

# OOP Concept->OOP is a programming approach where we represent real-world entities using classes and objects.
#Example-> properties- color,brand actions-drive,stop
#Syntax->class ClassName: 
#        def method(self):
#         pass
#object_name = ClassName()

class Student:
    def show(self):
        print("I am a student")

s1 = Student()
s1.show()

#Cosntructor(_init_)-> Constructor initializes object data

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)

s1 = Student("Deepak", 85)
s1.display()

# self keyword refers to the current object
# 4 Pillars of OOP-> 
#Encapsulation-> Wrapping data and methods together
#Example->
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print(self.balance)

# Inheritance-> Child class uses parent class features
#Example->
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()

#Polymorphism->Same function name, different behaviour.
class Bird:
    def fly(self):
        print("Some birds fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies")

b = Sparrow()
b.fly()

#Abstraction->
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        print("Area = side * side")

#Mini Project->

class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show(self):
        print(self.name, self.balance)

acc = Bank("Deepak", 5000)
acc.deposit(2000)
acc.withdraw(1000)
acc.show()

#WHY THESE ARE IMPORTANT FOR AI
#Concept	    Usage
#File Handling	Dataset storage
#OOP	        ML models & pipelines
#Classes	    Model creation
#Methods	    Training & prediction



