# FTPY_19_Code

#class Person:
    # constructor or initializer
#    def __init__(self, name):
#        self.name = name

    # method which prints a string
#    def you_are(self):
#        print('You are', self.name)

# Default constructor
class DemoClass:
    def __init__(self):
        self.num = 101

    def print_number(self):
        print(self.num)
    
class DemoClass2:
    num = 101
    
    def print_number(self):
        print(self.num)


class Shark:
    # class variables
    location = 'Atlantic ocean'

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_location(self):
        return self.location
    
    def set_location(self, newLocation):
        self.location = newLocation

    def message(self):
        print(self.name, 'is a', self.gender, 'shark')
        print(self.name, 'is located in the', self.get_location())


class House:
    def __init__(self, location, owner):
        self.location = location
        self.owner = owner

    def where(self):
        print('The house of', self.owner, 'is located in', self.location)

a = House('Athens', 'Anna')
b = House('Amsterdam', 'Samy')

annas_location = a.location
samys_location = b.location

print('Anna lives in', annas_location, 'and Samy lives in', samys_location)



print(a.location)

# Anna moved so let's change the location
a.location = 'Paris'
a.where()

# class exercise

class Summarize:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def sum(self):
        sum = self.a + self.b
        return sum * 10

first_sum = Summarize(4, 6)
result = first_sum.sum()
print(result)



# object inspection

import inspect

class Sample:
    """ This is a Sample class"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def printing(self):
        print('This is', self.name, self.surname)

diana = Sample('Diana', 'Joobs')

# print the docstring of a class
print(inspect.getdoc(Sample))

# Getting the signature of a single method 
print(inspect.signature(diana.__init__))

# Get the source code of a single method only
print(inspect.getsource(diana.printing))

# Get the source code of a class
print(inspect.getsource(Sample))

# Get the members of an object
print(inspect.getmembers(diana))

# type
print(type(diana))
print(type(diana.name))

# dir
print(dir(diana))


# Override magic methods
class Number:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        self.x += other*100
        
num = Number(2)
print('Before addition:', num.x)

# note that you are adding to num
# and not to num.x
num + 10
print('After addition:', num.x)

# class exercise
class Money:
    '''Money class contains a method to allot a money amount
    among the defined number of people in three decimal points precision'''
    
    def __init__(self, amount):
        self.amount = amount

    def __truediv__(self, parts):
        self.amount /= parts
        self.amount = float('{:.3f}'.format(self.amount))

amount1 = Money(10)
amount1 / 3
print('Each person should get:', amount1.amount)


# Subclasses

# Create the parent class
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def print_name(self):
        print(self.firstname, self.lastname)

x = Person('Matthew', 'Smith')
x.print_name()

# Create the child class
class Student(Person):
    def __init__(self, firstname, lastname, graduation):
        super().__init__(firstname, lastname)
        self.graduation = graduation
    
    def welcome(self):
        print('Welcome', self.firstname, self.lastname, 'to the class of', self.graduation)

y = Student('Lilian', 'Rose', 2022)
y.welcome()

# class exercise 
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def print_info(self):
        print(self.name, 'is an employee whose salary is:', self.salary)
    
class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)  # or Employee.__init__(name, salary)

    def calculate_salary(self):
        self.salary *= 2
    
    def print_info(self):
        print(self.name, 'is a developer whose salary is:', self.salary)

mark_emp = Employee('Mark Johnes', 1560)
mark_emp.print_info()

ariadna_dev = Developer('Ariadna Woods', 1560)
ariadna_dev.calculate_salary()
ariadna_dev.print_info()

