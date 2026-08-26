#Cree un programa que le pida tres números al usuario y muestre el mayor.

import os

start="si"

while start=="si" or start=="s" or start=="sí":

    os.system('cls' if os.name == 'nt' else 'clear') #** Borra la terminal cuando se inicia

    print("---- Verificación número mayor ----")
    num1=int(input("-- Primer número: "))
    num2=int(input("-- Segundo número: "))
    num3=int(input("-- Tercer número: "))

    big=""

    #* Verificaciones
    if num1>num2 and num1>num3:
        big=num1
    elif num2>num3 and num2>num1:
        big=num2
    elif num3>num2 and num3>num1:
        big=num3
    else:
        big="ninguno"

    print(f"-- ¡El mayor entre esos números es {big}!")
    start=input("-- ¿Desea volver a verificar?(s/n) \n-- ").lower() #** El .lower() hace que el input se vuelva lowercase