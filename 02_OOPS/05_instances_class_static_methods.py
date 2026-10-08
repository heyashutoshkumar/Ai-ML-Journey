#Method : Methods are the function written in the class. They are used by the object to perform a particular task.
"""
Types of the Methods:
1.Instances Method
2.Class Method
3.Static Method

Instances Method: In these type of method , The method is accessed by the oject.
~First parameter is the self used by object reference.

Class Method : In this type of the method , Mainly class interfence is there.
~cls is used as reference for the class under which the method is written
Static Method : In this type of method , usually we do not need a class and object.
~These methods do not start with self or cls parameter they are executed directly whenever they are called.

"""
class car:
    car_name="Mahindra"
    def __init__(self,name,price,model):  
        self.name=name
        self.price=price
        self.model=model
    
    @classmethod
    def get_company(cls):      #This is class method
        print("Name of the company of the car is :",cls.car_name)

    @staticmethod
    def greet():
        print("We welcome You in our car showroom.")   #static method

    def get_car(self):
        print("Name of the car is :",self.name)   #instances method

car1=car("Thar",1500,2026)
car.greet()
car.get_company()
car1.get_car()

    