#POLYMORPHISM : Let's divide it in two parts i.e pOly --> many and Morph -->Form 
""" That Means a single interface can have different behaivours/Forms. Similarly here we can relate it to the the Methods Same method same or common method name peerform different task.
-- We can use polymorphics in Inheritance as we can define a method in the parent class and same method in the child class performing different task.For example we make two classes dog and cat there we can define the sound() method which perform different tast but in normal programing two function with same name will replace the last function or last function will execute .

ABSTRACTION : Simple words , Abstraction means Hiding the implementation / unnecessay part and exposing the functionality part.

For ex: If we drive the car , We know the function of the steering , we know horn but we don't know the implmentation ..How they work we don't know this abstaction proving the functions to use and hiding the details.

Abstraction is very important when we want to use the function without knowing the deatils of the function.
For eg: we made a parent class car in which we define the method of starting the function , stopping the method. we can use these methods in the the particular car .

For abstraction , we need to import the abc module (abstraction base classes module) which provide the ABC and @abstractionethod.
ABC--> It is basically base class which is used to make the class to abstract base class.
@abstractmethod --> It is used mainly with the method making compulsory for the children class.It child class do not include that methods and don't complete it then it will show eeror.
"""

from abc import ABC , abstractmethod
class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    def greet(self):
        print("Congratulation You are going to drive the car")
class Kia(Car):
    def greet(self):
        super().greet()  #Inheritance access of method.
    def start(self):
        print("You are going to ride kia seltos")
class Bmw(Car):
    def greet(self):
        super().greet()  #Inheritance access of method.
    def start(self):
        print("You are going to ride BMW ")

c1=[Kia(),Bmw()]

for car in c1:
    car.greet()
    car.start()