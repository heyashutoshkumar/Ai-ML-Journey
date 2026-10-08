#Attributes are defined inside the class to store the data may predefined or data of each object inside the object.
"""Types of Attributes:
1.Class Attributes
2.Instances Attributes

Class Attributes:
- Class attributes are defined inside the class and object cannot store data in the class attribute if thry forcely store the value then the orignal class value is not change., 
- Due to which each and very object have the same value for class object.
- Majorly ,it is used when we have that value which is common for all the object.

Instances Attributes:
- Instances attribute also defined in the class but the object data is stored in these attributes.
- Object have the access on the Insatances Attributes.
"""

class Bank:
    bank_name="State bank of India"   #This class attribute
    def __init__(self,acc,balance):
        self.acc=acc
        self.balance=balance    #These are instances attributes
    def print_balace(self):
        print("Balance of the account is :",self.balance)

customer1=Bank("121",100)
print(Bank.bank_name)
print(customer1.acc)
