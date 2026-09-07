import actions
import data
import os
import time

def menu():
    student_data= data.read_student_data() #importa la info de estudiantes (si no existe bloquea opciones)
    select=0

    os.system('cls' if os.name == 'nt' else 'clear')
    #El titulo/bienvenida
    print("++++++++++++++++++++++++++++++++++++++++++++++ \n+++++++++++ Control de estudiantes +++++++++++ \n++++++++++++++++++++++++++++++++++++++++++++++ \n++++++++++                          ++++++++++ \n+++         ¿Que quiere hacer hoy?         +++")


    if student_data==None: #Cambia el texto dependiendo de si hay registro o no
        print("\n+ 1. Ingresar información de los estudiantes \n+ *2. Ver información de los estudiantes \n+ *3. Ver las top 3 notas promedio  \n+ *4. Ver las notas promedio generales")
        print("\n++ OPCIÓNES 2-4 INVÁLIDAS  \n+ (no hay registro de estudiantes previo)")
    else:
        print("\n+ 1. Ingresar información de los estudiantes \n+ 2. Ver información de los estudiantes \n+ 3. Ver las top 3 notas promedio  \n+ 4. Ver las notas promedio generales")

    try:
        select=int(input("++++ Selección: "))

        if student_data==None and select!=1: #Sin registro solo queda la opción 1
            raise ValueError()
        elif select<1 or select>4:
            raise ValueError()
        
    except ValueError as error:
        print("+++++++++++++++++++ ERROR ++++++++++++++++++++ \n+   	     Selección invalida        	     + \n+    Por favor seleccione una opción valida  + \n++++++++++++++++++++++++++++++++++++++++++++++")
        time.sleep(10)
        menu()

    match select:
        case 1: #Ingresar info de estudiantes
            actions.input_students()
        case 2: #Ver info de estudiantes (si hay)
            actions.view_student_info()
        case 3: #Top 3 mejores notas
            actions.top_three_students()
        case 4: #Ver promedios
            actions.view_averages()
        case _: 
            #Caso vacío por si arriba no funciona el delimitador
            print("+++++++++++++++++++ ERROR ++++++++++++++++++++ \n+   	     Selección invalida        	     + \n+    Por favor seleccione una opción valida  + \n++++++++++++++++++++++++++++++++++++++++++++++")
            time.sleep(10)
            menu()



## Mini menú de salir o volver al menú principal
def go_back_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n++++++++++++++++++++++++++++++++++++++++++++++\n\n+++   ¿Quiere volver al menú principal?     ++")
    re_do=input("\n+ (S/N): ").lower()
    try:
        if re_do=="si" or re_do=="s" or re_do=="sí":
            menu()
        elif re_do=="no" or re_do=="n":
            exit()
        else:
            raise ValueError()
    except ValueError as error:
        print(f"\n+++++++++++++++++++ ERROR ++++++++++++++++++++ \n+    La opción ingresada no es Sí o No       + \n+            Ingreso: {re_do}                + \n+        Ingrese una opción valida           + \n++++++++++++++++++++++++++++++++++++++++++++++ \n+ (si desea salir del programa escoja que no)")
        time.sleep(5)
        go_back_menu()