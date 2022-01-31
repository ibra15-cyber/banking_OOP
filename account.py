from tabnanny import check


class Account:

    #field or variable property
    class_var= "testing"

    #constructor
    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, "r+") as file:
            self.balance = int(file.read())

    #methods
    def withdraw(self, amount):
        self.balance=self.balance-amount

    def deposit(self, amount):
        self.balance+=amount

    #this fn writes back to the file
    #it first converts self.balance a property of our class that can be seen anywhere into string again
    #bc write knows string and not int
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


#another class inheriting
class Checking(Account): #inheriting everything class A extends b

    """ A docstring """

    def __init__(self, filepath, charges):
        Account.__init__(self, filepath) #inheriting the init of the Account: java = super(items,)
        self.charges = charges

    def transfer(self, amount): #adding to our instance 
        self.balance=self.balance-(amount+self.charges)


#object of our first class
account=Account("balance.txt")
print(account.class_var)
print(account.balance)
account.deposit(100)
account.commit()
print(account.balance)

#object instance of the second class
john_checking=Checking("john.txt", 1)
print(john_checking.class_var)
john_checking.transfer(100)
john_checking.commit()
print(john_checking.balance)
print(john_checking.__doc__)

#object instance of the second class
jack_checking=Checking("jack.txt", 1)
print(jack_checking.class_var) #it can inherit an instance variable of the main class
jack_checking.transfer(100)
jack_checking.commit()
print(jack_checking.balance)
print(john_checking.__doc__)
