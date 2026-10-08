#Encapsulation : It is way of keeping the related data together and methods under the a class , which can be accessed by data of the class.
# It also controls the access of the data.

"""Pyhton uses the name convention for controlling the data access.
Majorly there are three conventions:
1.Public data access
2.Protected
3.Private (Private-style)

Public :
- It is the most common way of accessing the class data and the methods from external like object.

Protected :
- This way of the accessing data is with the help of the single _attribute.
- This is intended for class/subclass usesage.
- Pyhton does not strictly prevent outside access.

Private :
- It is the private -style name mangling way of accessing the class data.
- It is way of preventing the outside access of the data.
- __attribute_name this format is used for making the private attribute.
- Name mangling means converting the attribute name to the _class_name__attribute. It is usefull for treating the simple attribute to protected attribute.
"""

class Bank:
    bank_name="State Bank of India" #This is Class Attribute.
    
    def __init__(self,acc,passd,bal):
        self.acc=acc             #This is Public
        self.__passd=passd       #This is private 
        self._bal=bal            #This is protected
    def show_balance(self):
        print("Current balance :", self._bal)
    def credit(self,amount):
        self._bal+=amount
        self.show_balance()
    
    def reset_Password(self):
        print("Your current password is :",self.__passd)

cust1=Bank(10,"Ashu12",1000)
cust1.credit(50)
#print("Password :",cust1.__passd) ->This will show error
cust1.reset_Password()
print("Balance of account is :",cust1._bal)