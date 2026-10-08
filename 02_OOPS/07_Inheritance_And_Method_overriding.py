#Inheritance: It is a usefull way of using the paresnt class into the child class.It allows to use the parent class method,attributes to store the data.
"""Types :
-- Single-Level Inheritance  Eg: class engineer(employee)
-- Multi-Level Inheritance   Eg: class engineer(employee) then class AI(engineer)
-- Multi Inheritance         Eg: class engineer(employee,expert)

Super()-->super() is used to access the next class in the inheritance hierarchy, commonly to call parent-class methods or the parent initializer.
           We can also use it to initialize the child class data to the parent class attribute under intializer block.
           Should be inside the child method to call the parent method or attribute.

Eg: We can do  super().__init__(age)

Method Overriding : It tells that if we use the same name for the method in the child class which is same in the parent class then The output depenf upon which class is used to access the method..
                    By the parent class we will get the parent class method output and Child class will child method output.
                    With super.method_name this will give different thing .. This will provide the parent class method output.

"""

class School:
    school="Army Public School"
    def __init__(self,total):
        self.total=total
    def greet(self):
        print("WELCOME TO OUR SCHOOL")
class Class(School):
    def __init__(self,strength,total):
        self.strength=strength
        super().__init__(total)        #Here we are using the Parent Instance Attribute Because of the Inheritance of that class in present class.
    
    def greet(self):
        super().greet()
        print("Welcome to our class")
    
cls1=Class(60,1000)
cls1.greet()
print(cls1.total)



""" Important Question : 
                            If we not define the __Init__ in the child class then it will automatically access the parent.__init__().
"""
