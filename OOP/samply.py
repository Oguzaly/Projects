#Parent Class

class User():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender


    def show_details(self):     #buraya self yazınca bu methot self geçen her objeye erişebliyor
        print("personal details")
        print("")
        print("name",self.name,"age",self.age,"gender", self.gender)

#Child Class : Parent chilasın her bir objesini burada kullandığımız için child class dedik (inheritance)


class Banks(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0

    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print("Account Balance has been updated",self.balance)

    def withdraw(self,amount):
        self.amount=amount
        if(self.amount>self.balance):
            print("Insufficient funds : Balance Available : ", self.balance )
        else:
            self.balance = self.balance -self.amount
            print("Account balance has been updated")

    def show_balance(self):

        self.show_details()
        print("Account balance has been updated")
