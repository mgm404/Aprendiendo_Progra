class LeggedAnimal():
    def body_info(self):
        print("Tengo piernas!")

class NonLeggedAnimal():
    def body_info(self):
        print("No tengo piernas!")

class Mammal():
    def animal_info(self):
        print("Soy un mamífero!")

class Reptile():
    def animal_info(self):
        print("Soy un reptil!")

class Fox(LeggedAnimal, Mammal):
    def speak(self):
        print("Los zorros no dicen \"ninininini\" como en la canción")

class OldSnake(LeggedAnimal, Reptile):
    def speak(self):
        print("Las serpientes antes tenian piernas, mayoría las dejaron en el pasado")

class Snake(NonLeggedAnimal, Reptile):
    def speak(self):
        print("Las serpientes ahora no tienen piernas, pero algunas aún tienen la estructura génetica para crecer piernas(solo que no se usa)")


fox_facts=Fox()
snake_facts1=OldSnake()
snake_facts2=Snake()

fox_facts.body_info(), fox_facts.animal_info(), fox_facts.speak()

snake_facts1.body_info(), snake_facts1.animal_info(), snake_facts1.speak()

snake_facts2.body_info(), snake_facts2.animal_info(), snake_facts2.speak()