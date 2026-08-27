import actions
import data
import os
import time

def menu():
    student_data= data.read_student_data
    select=0

    os.system('cls' if os.name == 'nt' else 'clear')
    #El titulo/bienvenida
    print("++++++++++++++++++++++++++++++++++++++++++++++ \n+++++++++++ Control de estudiantes +++++++++++ \n++++++++++++++++++++++++++++++++++++++++++++++ \n++++++++++                          ++++++++++ \n+++         ¿Que quiere hacer hoy?         +++")


    if student_data==None:
        print("\n+ 1. Ingresar información de los estudiantes \n+ *2. Ver información de los estudiantes \n+ *3. Ver las top 3 notas promedio  \n+ *4. Ver las notas promedio generales")
        print("\n++ OPCIÓNES 2-4 INVÁLIDAS  \n+ (no hay registro de estudiantes previo)")
    else:
        print("\n+ 1. Ingresar información de los estudiantes \n+ 2. Ver información de los estudiantes \n+ 3. Ver las top 3 notas promedio  \n+ 4. Ver las notas promedio generales")

    try:
        select=int(input("++++ Selección: "))

        if student_data==None and select!=1:
            raise ValueError()
        elif select<1 or select>4:
            raise ValueError()
        
    except ValueError as error:
        print("+ Selección invalida")
        time.sleep(3)
        menu()

    match select:
        case 1: #Ingresar info de estudiantes
            actions.student_info
        case 2: #Ver info de estudiantes (si hay)
            actions.view_student_info
        case 3: #Top 3 mejores notas
            actions.top_three_students
        case 4: #Ver promedios
            actions.view_averages
        case _:
            print("+ Selección invalida")
            time.sleep(3)
            menu()