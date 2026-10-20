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
    def __init__(self, min_balance):
        self.min_balance = min_balance
        super().__init__(self.min_balance)

    def take_away_money(self, ammount):
        try: 
            if (self.balance - ammount)>=self.min_balance:
                return super().take_away_money(ammount)
            else:
                raise ValueError()
        except ValueError:
            print(f"No se puede retirar esa cantidad de dinero! La cuenta quedaría en menos de {self.min_balance}!")
            return

saving=SavingsAccount(500)

saving.add_money(250)
saving.take_away_money(500)
saving.take_away_money(15)