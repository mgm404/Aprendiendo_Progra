class BankAccount():
    def __init__(self, balance=0):
        self.balance = balance

    def add_money(self, ammount):
        self.balance= self.balance + ammount
        print(f"Ahora tu cuenta tiene: {self.balance}!")

    def take_away_money(self, ammount):
        self.balance= self.balance - ammount
        print(f"Ahora tu cuenta tiene: {self.balance}!")

class SavingsAccount(BankAccount):
    def __init__(self):
        self.min_balance = 500
        super().__init__(self.min_balance)

    def take_away_money(self, ammount):
        if (self.balance - ammount)>=self.min_balance:
            return super().take_away_money(ammount)
        else:
            print("No se puede retirar esa cantidad de dinero! La cuenta quedaría en menos de 500!")
            return

saving=SavingsAccount()

saving.add_money(250)
saving.take_away_money(500)
saving.take_away_money(15)