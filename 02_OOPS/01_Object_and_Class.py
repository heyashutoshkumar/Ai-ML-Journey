#CLASS: It is the Blue-Print which is made for the object.
#Object: Object is the instances created on the basis of the class.Object has its on state(data/attributes) and uses the methids defind in the class
"""Advantages of OOPS:
Encapculation:It means keeping the related data and behaviour together
Inheritance:Helps in using the classes in another class
Polymorphism:It is helps in using the same variable name for different things.
Abstraction:Abstraction means Not knowing the actual process just know thw method  that can be used by the user
"""

#Creating the simple CLASS:
class Student:
    def __init__(self,name): #Initializer method:When the object is created this initilizer is created by default/by user.
        self.name=name       #self.name is the attribute and name on right side is the parameter.
#Object
s1=Student("Ashutosh")
s2=Student("Ram")
print("Name of the student :",s1.name)
print("Name of the second student :",s2.name)