class BankAccount():
    def __init__(self, balance=0):
        self.balance = balance

    def add_money(self, amount):
        if amount<0:
            amount=amount*-1
        elif amount==0:
            print("Se intentó añadir un monto nulo a la cuenta, no se pueden añadir valores nulos")
            return
        
        self.balance= self.balance + amount

    def take_away_money(self, amount):
        if amount<0:
            amount=amount*-1
        elif amount==0:
            print("Se intentó retirar un monto nulo a la cuenta, no se pueden retirar valores nulos")
            return
        
        self.balance= self.balance - amount


class SavingsAccount(BankAccount):
    def __init__(self, min_balance, balance):
        self.min_balance = min_balance
        super().__init__(balance)

    def take_away_money(self, amount):
        return super().take_away_money(amount)

starting_balance=0
min_balance=1

while starting_balance<min_balance:
    min_balance=int(input("¿Cuanto quiere que sea el monto mínimo de la cuenta?"))
    starting_balance=int(input(f"¿Con cuanto dinero desea iniciar la cuenta la cuenta? (mínimo: {min_balance})"))
    try: 
        if starting_balance>=min_balance:
            saving=SavingsAccount(min_balance, starting_balance)
        else:
            raise ValueError()

    except ValueError:
        print(f"No se puede iniciar la cuenta con menos del monto mínimo, el mínimo es: {min_balance}. Intento ponerle: {starting_balance}")

print("Le añaden 250")
saving.add_money(250)
print(f"Ahora tu cuenta tiene: {saving.balance}!")

retrive_money=False
while retrive_money==False:
    amount=int(input("¿Cuanto quiere retirar de la cuenta?"))
    try: 
        if (saving.balance - amount)>=saving.min_balance:
            saving.take_away_money(amount)
            retrive_money=True
        else:
            raise ValueError()

    except ValueError:
        print(f"No se puede retirar {amount} ! La cuenta quedaría en menos del monto mínimo!\n Monto mínimo: {saving.min_balance}")
print(f"Ahora tu cuenta tiene: {saving.balance}!")