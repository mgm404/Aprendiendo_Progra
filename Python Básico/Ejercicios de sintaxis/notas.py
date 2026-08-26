import os

start="si"


while start=="si" or start=="s" or start=="sí":

    #** Variables, para que se reseteen al iniciar
    not_passed=0
    passed=0
    sum_not_pased=0
    sum_passed=0
    sum_grades=0
    average_not_passed=0
    average_passed=0
    average_grades=0
    grade_counter=0

    os.system('cls' if os.name == 'nt' else 'clear') #** Borra la terminal cuando se inicia
    
    print("///// Calculadora de promedios de notas /////")
    ammount_grades=int(input("// ¿Cual es la cantidad de notas que desea ingresar? \n// "))
    for i in range(ammount_grades):
        grade_counter=grade_counter+1 #cantidad de notas ingresadas
        grade=int(input(f"\n// Ingresa la nota #{grade_counter}: "))
        if grade<70:
            not_passed=not_passed+1
            sum_not_pased=sum_not_pased+grade
        else:
            passed=passed+1
            sum_passed=sum_passed+grade
        sum_grades=sum_grades+grade
    if not_passed>0:
        average_not_passed=sum_not_pased/not_passed
    else:
        average_not_passed=0
    if passed>0:
        average_passed=sum_passed/passed
    else:
        average_passed=0
    average_grades=sum_grades/grade_counter
    print(f"\n///////////////////////////////////////////// \n// Sus promedios son: \n// Aprovadas: {average_passed:.2f}, con {passed} notas aprovadas \n// Desaprovadas: {average_not_passed:.2f}, con {not_passed} desaprovadas \n Total: {average_grades:.2f}, con {grade_counter} notas \n")
    start=input("// ¿Desea calcular más promedios?(s/n) \n -- ").lower() #** El .lower() hace que el input se vuelva lowercase
    #** el "":.2f" en una variable hace que tenga 2 decimales