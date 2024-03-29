#!/bin/python3

class Person(object):
    # Class variables shared by all objects.
    shared = {}
    
    # Constructor method with instance variables.
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.todo = {}
        
        # Call its own methos.
        self.addTodo('12PM', 'Call own methods')
    
    def addTodo(self, key, value):
        self.todo[key] = value

    def addShared(self, key, value):
        self.shared[key] = value
        
    def __privateMethod(self):
        print("Access __privateMethod()")
    
    def callPrivateMethod(self):
        self.__privateMethod()
    
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

print("================")
kate.callPrivateMethod()

#~ John
#~ {'12PM': 'Call own methods', '5PM': 'play', '6PM': 'souper'}
#~ {'5': 'from john'}
#~ ================
#~ Kate
#~ {'12PM': 'Call own methods', '7PM': 'read', '9PM': 'sleep'}
#~ {'5': 'from john', '9': 'from kate'}

