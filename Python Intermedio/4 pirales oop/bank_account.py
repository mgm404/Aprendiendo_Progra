class BankAccount():
    def __init__(self, balance=0):
        self.balance = balance

    def add_money(self, amount):
        if amount<=0:
            raise ValueError()

        
        self.balance= self.balance + amount

    def take_away_money(self, amount):
        if amount<=0:
            raise ValueError()
        
        self.balance= self.balance - amount


class SavingsAccount(BankAccount):
    def __init__(self, min_balance, balance):
        if starting_balance<min_balance:
            raise ValueError()
        
        self.min_balance = min_balance
        super().__init__(balance)

    def take_away_money(self, amount):
        if (self.balance - amount)>=self.min_balance:
            return super().take_away_money(amount)
        else:
            raise ValueError()

starting_balance=0
min_balance=1

while starting_balance<min_balance:
    try: 
        min_balance=int(input("¿Cuanto quiere que sea el monto mínimo de la cuenta?"))
        starting_balance=int(input(f"¿Con cuanto dinero desea iniciar la cuenta? (mínimo: {min_balance})"))
        saving=SavingsAccount(min_balance, starting_balance)

    except ValueError:
        print(f"No se puede iniciar la cuenta con menos del monto mínimo, el mínimo es: {min_balance}. Intento ponerle: {starting_balance}")


try:
    print("Le añaden 250")
    saving.add_money(250)
    print(f"Ahora tu cuenta tiene: {saving.balance}!")
except ValueError:
    print("El valor es igual o menor que 0, el monto tiene que ser positivo (ej. 100) y mayor que 0.")


retrive_money=False
while retrive_money==False:
    amount=int(input("¿Cuanto quiere retirar de la cuenta?"))
    try: 
        saving.take_away_money(amount)
        retrive_money=True
        print(f"Ahora tu cuenta tiene: {saving.balance}!")

    except ValueError:
        print(f"No se puede retirar {amount} ! La cuenta quedaría en menos del monto mínimo!\n Monto mínimo: {saving.min_balance}")
