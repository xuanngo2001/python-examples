#!/bin/python3

class Person(object):
    # Class variables shared by all objects.
    shared = {}
    
    # Constructor method with instance variables.
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.todo = {}
    
    def addTodo(self, key, value):
        self.todo[key] = value

    def addShared(self, key, value):
        self.shared[key] = value

john = Person('John', 11)
john.addTodo('5PM', 'play')
john.addTodo('6PM', 'souper')
john.addShared('5', 'from john')
print(john.name)
print(john.todo)
print(john.shared)

print("================")
kate = Person('Kate', 22)
kate.addTodo('7PM', 'read')
kate.addTodo('9PM', 'sleep')
kate.addShared('9', 'from kate')
print(kate.name)
print(kate.todo)
print(kate.shared)


#~ John
#~ {'5PM': 'play', '6PM': 'souper'}
#~ {'5': 'from john'}
#~ ================
#~ Kate
#~ {'7PM': 'read', '9PM': 'sleep'}
#~ {'5': 'from john', '9': 'from kate'}

