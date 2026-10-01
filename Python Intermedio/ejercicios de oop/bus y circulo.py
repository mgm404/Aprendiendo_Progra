#circulo cn  atributo radio y get area (funcion)
import math

class Circle:
    def __init__(self, radius):
        self.radius= radius
        self.area = 0

    def get_area(self):
        area= math.pi * (self.radius**2)
        self.area = area
        return area

##############

circle1= Circle(8)
circle1.get_area()
print(f"{circle1.radius} {circle1.area}")



#bus atributo de max passangers, metodo de agregar gente al bus mientras hayan menos del max y mostrar mensaje de lleno, metodo de bajar pasajeros a random

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers= max_passengers
        self.passengers=[]

    def add_passengers(self, passenger):
        if len(self.passengers) >= self.max_passangers:
            print("El bus ya esta lleno!!")
            return
        self.passangers.append(passenger)

    def leave_passenger(self):
        if self.passengers<0:
            print(f"Hay {len(self.passengers)} pasajeros en el bus, escoja el número de 1 de los pasajeros para que salga")
            leave=-1
            try:
                leave= int(input("Pasajero número: "))-1
                if leave>len(self.passengers):
                    raise ValueError
            except ValueError:
                print("Ese pasajero no esta, pruebe con otro número")

            left=self.passengers.pop(leave)
            print(f"Se bajo el pasajero {left}!")
        else:
            print("El bus esta vacío, no hay nadie que se pueda bajar")

#####################

class Person():
	def __init__(self, name):
		print(f"Ha aparecido un pasajero {name}!")
		self.name = name
		self.age = 25

#################

person1= Person("Juan carlos Bodoque")
person2= Person("Tulio Triviño")

thirty_one_minutes_bus= Bus(15)
thirty_one_minutes_bus.add_passengers(person1)
thirty_one_minutes_bus.add_passengers(person2)

print("Quedan los pasajeros:")
passenger_number=0
for passenger in thirty_one_minutes_bus.passengers:
    passanger_number+=1
    print(f" {passenger_number}- {passenger.name}")
    
thirty_one_minutes_bus.leave_passenger()

print("Quedan los pasajeros:")
for passenger in thirty_one_minutes_bus.passengers:
    print(f" - {passenger.name}")