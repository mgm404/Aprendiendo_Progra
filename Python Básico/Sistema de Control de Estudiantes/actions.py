import data
import time
import os
import menu
import operator
import csv

## Acciones de guardar info de estudiantes

def input_students():
    os.system('cls' if os.name == 'nt' else 'clear')
    amount_of_students=0
    #Titulo
    print("++++++++++++++++++++++++++++++++++++++++++++++ \n+++++++++++ Control de estudiantes +++++++++++ \n++++++++++++++++++++++++++++++++++++++++++++++ \n++++++++++                          ++++++++++ \n+++         Ingreso de información         +++")

    print("\n+++ Primero,  \n+ ¿Cuántos estudiantes se van a registrar?")
    try:
        amount_of_students=int(input("+ "))
    except ValueError as err:
        print(f"++++++++++++++++++ ERROR +++++++++++++++++++++ \n+ El valor ingresado tiene que ser un número + \n+ Ingreso: {amount_of_students}              +")
        time.sleep(7)
        input_students() #! Reinicia la sección por el error

    student_info(amount_of_students) #Va a guardar info

def student_info(amount_of_students):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("++++++++++++++++++++++++++++++++++++++++++++++ \n+++++++++++ Control de estudiantes +++++++++++ \n++++++++++++++++++++++++++++++++++++++++++++++ \n++++++++++                          ++++++++++ \n+++         Ingreso de información         +++")

    students=[]

    for i in range(amount_of_students):
        one_student={}
        print(f"\n+++ Estudiante #{i+1}")
        one_student['name']=input("+ Nombre y apellidos: ")
        one_student['student_class']=input("+ Sección (ej. 11B):")

        print("+")

        spanish_grade=student_grades(spanish_grade, "Español")
        english_grade=student_grades(english_grade, "Ingles")
        social_studies_grade=student_grades(social_studies_grade, "Estudios sociales")
        science_grade=student_grades(science_grade, "Ciencias")

        general_average=spanish_grade+english_grade+social_studies_grade+science_grade/4
        one_student['spanish_grade']=spanish_grade
        one_student['english_grade']=english_grade
        one_student['social_studies_grade']=social_studies_grade
        one_student['science_grade']=science_grade
        one_student['general_average']=general_average

        students.append(one_student)

    data.save_student_data(students)
    print("\n+ Se guardo la información de los estudiantes \n	       correctamente!")
    time.sleep(7)
    go_back_menu()

def student_grades(grade, class_of_grade):
    while grade<0 or grade>100:
        try:
            grade=int(input(f"\n+ Nota total de {class_of_grade}:"))

            if grade<0 or grade>100:
                raise ValueError()
        except ValueError:
            print("+++++++++++++++++++ ERROR ++++++++++++++++++++ \n+    El valor ingresado tiene que ser un     + \n+	   número entre 0 y 100              + \n+            Ingreso: {grade}                + \n+        Ingrese el valor correcto           + \n++++++++++++++++++++++++++++++++++++++++++++++")

    return grade


## Acciones de ver info de estudiantes

def view_student_info():
    students_data=data.read_student_data() #Agarra la información de los estudiantes
    student_number=0 #Usado para enumerar los estudiantes
    exit_info="" #Es lo que hace posible salir de la información e ir a el go_back_menu

    print("++++++++++++++++++++++++++++++++++++++++++++++ \n+++++++++++ Control de estudiantes +++++++++++ \n++++++++++++++++++++++++++++++++++++++++++++++ \n++++++++++                          ++++++++++ \n+++        Registro de estudiantes         +++")

    for student in students_data:
        student_number+=1
        print(f"\n+ #{student_number}.\n	Nombre: {student['name']}\n	Clase: {student['student_class']}\n	Nota de Español: {student['spanish_grade']}\n	Nota de Ingles: {student['english_grade']}\n	Nota de Estudios sociales: {student['social_studies_grade']}\n	Nota de Ciencias: {student['science_grade']}\n	Promedio: {student['general_average']}")

    print("\n++ para salir presione q \n+ ")

    while exit_info!="q": #Como exit_info no es q, hace posible esperar hasta que el usuario decida salir :3
        exit_info=input()

    go_back_menu()



## Acciones de ver los top 3 promedios
def top_three_students():
    students_data=data.read_student_data() #Agarra la información de los estudiantes
    student_number=0 #Usado para enumerar los estudiantes
    exit_info="" #Es lo que hace posible salir de la información e ir a el go_back_menu

    



## Mini menú de salir o volver al menú principal

def go_back_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n++++++++++++++++++++++++++++++++++++++++++++++\n\n+++   ¿Quiere volver al menú principal?     ++")
    re_do=input("\n+ (S/N): ").lower()
    try:
        if re_do=="si" or re_do=="s" or re_do=="sí":
            menu.menu()
        elif re_do=="no" or re_do=="n":
            exit()
        else:
            raise ValueError()
    except ValueError as error:
        print(f"\n+++++++++++++++++++ ERROR ++++++++++++++++++++ \n+    La opción ingresada no es Sí o No       + \n+            Ingreso: {re_do}                + \n+        Ingrese una opción valida           + \n++++++++++++++++++++++++++++++++++++++++++++++ \n+ (si desea salir del programa escoja que no)")
        time.sleep(5)
        go_back_menu()