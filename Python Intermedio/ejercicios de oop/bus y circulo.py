#circulo cn  atributo radio y get area (funcion)

class circle:
    def __init__(self, radius):
        self.radius= radius

    def get_area(self):
        area= 3.14 * (self.radius**2)
        self.area = area

##############

circle1= circle(8)
circle1.get_area()
print(f"{circle1.radius} {circle1.area}")



#bus atributo de max passangers, metodo de agregar gente al bus mientras hayan menos del max y mostrar mensaje de lleno, metodo de bajar pasajeros a random

class bus:
    def __init__(self):
        self.max_passangers= 15
    passangers=[]

    def get_passangers(self, passanger):
        if len(self.passangers) >= self.max_passangers:
            print("El bus ya esta lleno!!")
            return
        self.passangers.append(passanger)

    def leave_passanger(self):
        print(f"Hay {len(self.passangers)} pasajeros en el bus, escoja el número de 1 de los pasajeros para que salga")
        leave= int(input("Pasajero número: "))-1
        self.passangers.pop(leave)
        print(f"Se bajo el pasajero número {leave+1}!")

#####################

class Person():
	def __init__(self, name):
		print(f"Ha aparecido un pasajero {name}!")
		self.name = name
		self.age = 25

#################

person1= Person("Juan carlos Bodoque")
person2= Person("Tulio Triviño")

thirty_one_minutes_bus= bus()
thirty_one_minutes_bus.get_passangers(person1)
thirty_one_minutes_bus.get_passangers(person2)

print("Quedan los pasajeros:")
for passanger in thirty_one_minutes_bus.passangers:
    print(f" - {passanger.name}")
    
thirty_one_minutes_bus.leave_passanger()

print("Quedan los pasajeros:")
for passanger in thirty_one_minutes_bus.passangers:
    print(f" - {passanger.name}")