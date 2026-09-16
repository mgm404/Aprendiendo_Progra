import actions, data, os, time


def menu(students):
    student_data=bool(students) #import student info (if false(empty), blocks out options)
    select=0
    one_or_five=False #To verify if the option is 1 or 5 when there's no student data

    os.system('cls' if os.name == 'nt' else 'clear')
    #The title/welcome
    print("++++++++++++++++++++++++++++++++++++++++++++++ \n+++++++++++ Control de estudiantes +++++++++++ \n++++++++++++++++++++++++++++++++++++++++++++++ \n++++++++++                          ++++++++++ \n+++         ¿Que quiere hacer hoy?         +++")


    if student_data==False: #Changes text depending on if there's student information
        print("\n+ 1. Ingresar información de los estudiantes \n+ *2. Ver información de los estudiantes \n+ *3. Ver las top 3 notas promedio  \n+ *4. Ver las notas promedio generales \n+ 5. Importar registros anteriores \n+ *6. Exportar información de estudiantes")
        print("\n++ OPCIÓNES 2-4 y 6 INVÁLIDAS  \n+ (no hay registro de estudiantes en uso)")
    else:
        print("\n+ 1. Ingresar información de los estudiantes \n+ 2. Ver información de los estudiantes \n+ 3. Ver las top 3 notas promedio  \n+ 4. Ver las notas promedio generales \n+ 5. Importar registros anteriores \n+ 6. Exportar información de estudiantes")

    try:
        select=int(input("++++ Selección: "))

        if select==1: #Verifying if selection is 1 or 5, not used if all options available
            one_or_five=True
        elif select==5:
            one_or_five=True
        else:
            one_or_five=False

        if student_data==False and one_or_five==False: #Without information only option 1 and 5 are available
            raise ValueError()
        elif select<1 or select>6:
            raise ValueError()
        
    except ValueError as error:
        print("+++++++++++++++++++ ERROR ++++++++++++++++++++ \n+   	     Selección invalida        	     + \n+    Por favor seleccione una opción valida  + \n++++++++++++++++++++++++++++++++++++++++++++++")
        time.sleep(10)
        menu(students)
        return

    match select:
        case 1: #Input student information
            actions.input_students(students)
        case 2: #View student info (if there's any)
            actions.view_student_info(students)
        case 3: #Top 3 best grades
            actions.top_three_students(students)
        case 4: #View averages
            actions.view_averages(students)
        case 5: #Import the csv
            actions.import_students(students)
        case 6: #Export the csv
            data.save_student_data(students)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n+ Se guardó la información correctamente!\n+ Borrando del programa la información...")
            students=[]
            time.sleep(7)
            go_back_menu(students)
        case _: 
            #Empty case, in case the earlier checker didn't work
            print("+++++++++++++++++++ ERROR ++++++++++++++++++++ \n+   	     Selección invalida        	     + \n+    Por favor seleccione una opción valida  + \n++++++++++++++++++++++++++++++++++++++++++++++")
            time.sleep(10)
            menu(students)
            return


## Mini menu of exit or come back to the main menu
def go_back_menu(students):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n++++++++++++++++++++++++++++++++++++++++++++++\n\n+++   ¿Quiere volver al menú principal?     ++")
    re_do=input("\n+ (S/N): ").lower()
    try:
        if re_do=="si" or re_do=="s" or re_do=="sí":
            menu(students)
        elif re_do=="no" or re_do=="n":
            exit()
        else:
            raise ValueError()
    except ValueError as error:
        print(f"\n+++++++++++++++++++ ERROR ++++++++++++++++++++ \n+    La opción ingresada no es Sí o No       + \n+            Ingreso: {re_do}                + \n+        Ingrese una opción valida           + \n++++++++++++++++++++++++++++++++++++++++++++++ \n+ (si desea salir del programa escoja que no)")
        time.sleep(5)
        go_back_menu(students)