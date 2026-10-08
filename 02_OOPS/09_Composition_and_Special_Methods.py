#COMPOSITION: Composition is mainly use where there is a relation of --> HAS A.
"""IN COMPOSITION , we use a object inside the class the object is made from another class. Here we don't inherit the class but use its object.
More flexible,Reuse through Objects. 
For eg : Assume engine is a class then in another class we are using it as self.engine=engine()

Special Methods: They are used with the dunder representation.It allow to use The function simply on the classes..From here the concept of Operator overloading came.
Eg: + Has different fucntion with with different operand like with string concatenate,number sum,list add..To make the use of + we use __add__ which tells what operation occus when we use + with objects.
"""
class Class:
    def strength(self):
        print("Maximum strength in class is : 60")

class School:
    def __init__(self, school,total):
        self.school=school 
        self.total=total
        self.Class=Class()
    def __str__(self):
        return f"School(Name of school{self.school})"
    def __len__(self):
        return len(self.school)
    def __add__(self,n2):
        return self.total + n2.total
sc=School("APS,Bly",1500)
sc2=School("Kv",1000)
sc.Class.strength()
print(sc)
print("Length of school name :",len(sc))
print("Toatal student in both the class :",sc+sc2)