import os
import random

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start="si"

while start=="si" or start=="s" or start=="sí":

    os.system('cls' if os.name == 'nt' else 'clear') #** Borra la terminal cuando se inicia

    random.shuffle(numbers) #* Intercambia los numeros de lugar en la lista

    rand_num=random.choice(numbers) #* Esccoje al azar de la lista
    guess=0
    guesses=[]

    print(" +++ Adivinando números secretos +++")
    print(" +++   Ya hay un número secreto  +++")
    while guess!=rand_num:
        if guess!=0:
            guesses.append(guess)
            print("\n\n ++ Ese no es!")
            print(f" ++ Números que no son: \n    {guesses}")
        guess=int(input(" ++ ¿Cual crees que es? (del 1 al 10) \n ++ "))
    
    print(" +++++++++++++++++++++++++++++++++++ \n +++          ¡Correcto !        +++")
    print(f" ++ La respuesta era: {rand_num} y adivinaste {guess}! \n ++ Tus intentos fallidos fueron: \n    {guesses}")

    start=input(" +++++++++++++++++++++++++++++++++++ \n ++ ¿Desea volver a jugar?(s/n) \n ++ ").lower()
