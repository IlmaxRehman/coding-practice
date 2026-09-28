class Employee:
    def __init__(self,name,salary,age):
        self.name = name
        self.__salary = salary
        self._age = age


class SubEmployee(Employee):
    def show_age(self):
        print("Age :",self._age)

emp = SubEmployee("akshat",10000,22)
print(emp.name)
emp.show_age()

# python achieves encapsulation by name conventions method

class BankAccount:
    def __init__(self):
        self.balance = 1000

    def _show_balance(self): #protected method
        print(f"Balance : ${self.balance}")

    def __update_balance(self,amount): #private method 
        self.balance += amount

    def deposit(self,amount):
        if amount > 0:
            self.__update_balance(amount) #accessing private method

            self._show_balance() # accessing protected method
        else:
            print("invalid deposit amount")

account = BankAccount()
account._show_balance()
account.deposit(400)

# getter and setter method , read data - getter, update data - setter

class Intern :
    def __init__(self):
        self.__salary = 10000

    def get_salary(self):
        return self.__salary

    def set_salary(self,amount):
        if amount> 0:
            self.__salary = amount
        else:
            print("Invalid amount!")

inter = Intern()
print(inter.get_salary())

inter.set_salary(15000)

print(inter.get_salary())