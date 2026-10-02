#Attributes: Attributes in the class are define according to object and store the data of the different object under particular object name.
#Method : Function which are defined in the class to perfoem the a particular task and object and use it is called Method

class Bank:
    def __init__(self,name,balanace):
        self.name=name
        self.balance=balanace
    
    def credit(self,credit):
        self.balance+=credit
        print("Amount after credit : ",self.balance)

    def withdraw(self,debit):
        if self.balance<debit:
            print("Sorry insuffcient balance!")
            return
        self.balance-=debit
        print("Remaining amount after debit : ",self.balance)

customer1=Bank("Ashutosh",1000)
print(customer1.name)
print("Available balance : ",customer1.balance)
customer1.credit(1000)
customer1.withdraw(500)

