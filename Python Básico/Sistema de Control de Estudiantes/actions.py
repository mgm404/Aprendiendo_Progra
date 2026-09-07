import data
import time
import os
import menu


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
        null_grade=-1 #Base de los grados, hace posible guardar después un valor

        spanish_grade=student_grades(null_grade, "Español")
        english_grade=student_grades(null_grade, "Ingles")
        social_studies_grade=student_grades(null_grade, "Estudios sociales")
        science_grade=student_grades(null_grade, "Ciencias")

        general_average=(spanish_grade+english_grade+social_studies_grade+science_grade)/4

        one_student['spanish_grade']=spanish_grade
        one_student['english_grade']=english_grade
        one_student['social_studies_grade']=social_studies_grade
        one_student['science_grade']=science_grade
        one_student['general_average']=general_average

        students.append(one_student)

    data.save_student_data(students)
    print("\n+ Se guardo la información de los estudiantes \n	       correctamente!")
    time.sleep(7)
    menu.go_back_menu()

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
    exit_info="" #Es lo que hace posible salir de la información e ir a el go_back_menu

    while exit_info!="q":#Como exit_info no es q, hace posible esperar hasta que el usuario decida salir :3
        os.system('cls' if os.name == 'nt' else 'clear')

        print("++++++++++++++++++++++++++++++++++++++++++++++ \n+++++++++++ Control de estudiantes +++++++++++ \n++++++++++++++++++++++++++++++++++++++++++++++ \n++++++++++                          ++++++++++ \n+++        Registro de estudiantes         +++")

        data.print_full_data()

        print("\n++ para salir presione q ")
        exit_info=input("+ ")

    menu.go_back_menu()



## Acciones de ver los top 3 promedios
def top_three_students():
    exit_info="" #Es lo que hace posible salir de la información e ir a el go_back_menu

    students_average, students_names, students_class= data.read_student_averages()


    while exit_info!="q":#Como exit_info no es q, hace posible esperar hasta que el usuario decida salir :3
        os.system('cls' if os.name == 'nt' else 'clear')
        print("++++++++++++++++++++++++++++++++++++++++++++++ \n+++++++++++ Control de estudiantes +++++++++++ \n++++++++++++++++++++++++++++++++++++++++++++++ \n++++++++++                          ++++++++++ \n+++            Top 3 Promedios             +++")

        print(f"\n+ #1. \n   Estudiante: {students_names[0]} \n   Clase: {students_class[0]}\n   Promedio: {students_average[0]}")
        print(f"+ #2. \n   Estudiante: {students_names[1]} \n   Clase: {students_class[1]}\n   Promedio: {students_average[1]}")
        print(f"+ #3. \n   Estudiante: {students_names[2]} \n   Clase: {students_class[2]}\n   Promedio: {students_average[2]}")

        print("\n++ para salir presione q ")
        exit_info=input("+ ")

    menu.go_back_menu()


## Acciones de ver todos los promedios
def view_averages():
    exit_info="" #Es lo que hace posible salir de la información e ir a el go_back_menu

    students_average, students_names, students_class= data.read_student_averages()

    while exit_info!="q":#Como exit_info no es q, hace posible esperar hasta que el usuario decida salir :3
        student_number=0
        os.system('cls' if os.name == 'nt' else 'clear')
        print("++++++++++++++++++++++++++++++++++++++++++++++ \n+++++++++++ Control de estudiantes +++++++++++ \n++++++++++++++++++++++++++++++++++++++++++++++ \n++++++++++                          ++++++++++ \n+++          Promedios Generales           +++")

        for index in range(0, len(students_class)):
            student_number+=1
            print(f"\n+ #{student_number}. \n   Estudiante: {students_names[index]} \n   Clase: {students_class[index]}\n   Promedio: {students_average[index]}")

        print("\n++ para salir presione q ")
        exit_info=input("+ ")
        
    menu.go_back_menu()
