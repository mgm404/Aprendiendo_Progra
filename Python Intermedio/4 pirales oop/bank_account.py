class BankAccount():
    def __init__(self, balance=0):
        self.balance = balance

    def add_money(self, amount):
        self.check_if_positive_amount(amount)
        
        self.balance= self.balance + amount

    def take_away_money(self, amount):
        self.check_if_positive_amount(amount)
        
        self.balance= self.balance - amount

    def check_if_positive_amount(self, amount):
        if amount<=0:
            raise ValueError("El valor es igual o menor(negativo) que 0, el monto tiene que ser positivo (ej. 100) y mayor que 0.")


class SavingsAccount(BankAccount):
    def __init__(self, min_balance, balance):
        if balance<min_balance:
            raise ValueError(f"No se puede iniciar la cuenta con menos del monto mínimo, el mínimo es: {min_balance}. Intento ponerle: {balance}")
        
        self.min_balance = min_balance
        super().__init__(balance)

    def take_away_money(self, amount):
        if (self.balance - amount)>=self.min_balance:
            return super().take_away_money(amount)
        else:
            raise ValueError(f"No se puede retirar {amount} ! La cuenta quedaría en menos del monto mínimo!\n Monto mínimo: {self.min_balance}")

starting_balance=0
min_balance=1

while starting_balance<min_balance:
    try: 
        min_balance=int(input("¿Cuanto quiere que sea el monto mínimo de la cuenta?"))
        starting_balance=int(input(f"¿Con cuanto dinero desea iniciar la cuenta? (mínimo: {min_balance})"))
        saving=SavingsAccount(min_balance, starting_balance)

    except ValueError as err:
        print(err)


try:
    print("Le añaden 250")
    saving.add_money(250)
    print(f"Ahora tu cuenta tiene: {saving.balance}!")
except ValueError as e:
    print(e)


retrive_money=False
while retrive_money==False:
    try: 
        amount=int(input("¿Cuanto quiere retirar de la cuenta?"))
        saving.take_away_money(amount)
        retrive_money=True
        print(f"Ahora tu cuenta tiene: {saving.balance}!")

    except ValueError as error:
        print(error)
