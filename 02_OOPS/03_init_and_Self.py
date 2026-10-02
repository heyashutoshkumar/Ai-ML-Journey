# __init__ is a speacial python function used to intialize the object after it has been created.
"""Important:
- __init__ is not used for creating the object , in creation of object __new__ is used.
- It provides the space to intitialize the each object attributes."""

#self is used for reference each object. Basically , self is the reference given to the object so that different object can use the class.
"""Important:
- It is not important to use the self variable to identify the the object , we can use any word but overall it is considered as general name for that field.
- self is usefull in creating the simple variable to the attributes so that each object can store the data in attributes in particular object.
- There is a single self  in the class which is used for different object accordung to the object/object name."""

# self.name -->Important It is used to make the variable as attribute, which is used by different object.

class Student:
    def __init__(self,name,section,branch):
        self.name=name
        self.section=section
        self.branch=branch
    def get_Section(self):
        print(self.name,"'s section is :",self.section)
    def get_Brach(self):
        print(self.name,"'s branch is :",self.branch)

#Creating objects
st1=Student("Ashutosh","CS-AI-2B","CS-AI")
st2=Student("Mahii","Ece-2b","ECE")
st1.get_Section()
st1.get_Brach()

print(st2.name)
st2.get_Section()
st2.get_Brach()
