import data, time, os, menu

#Objects used
class Student_list():

    students = []

    def get_student(self, student):
        self.students.append(student)


class Student:
    def __init__(self, name, student_class, spanish_grade, english_grade, social_studies_grade, science_grade, general_average):
        self.name= name
        self.student_class=student_class
        self.spanish_grade=spanish_grade
        self.english_grade=english_grade
        self.social_studies_grade=social_studies_grade
        self.science_grade=science_grade
        self.general_average=general_average

## Actions of saving/inputing student data


def input_students(student_list):
    os.system('cls' if os.name == 'nt' else 'clear')
    students=[]
    amount_of_students=0
    #Title
    print("++++++++++++++++++++++++++++++++++++++++++++++ \n+++++++++++ Control de estudiantes +++++++++++ \n++++++++++++++++++++++++++++++++++++++++++++++ \n++++++++++                          ++++++++++ \n+++         Ingreso de información         +++")

    print("\n+++ Primero,  \n+ ¿Cuántos estudiantes se van a registrar?")
    try:
        amount_of_students=int(input("+ "))
    except ValueError as err:
        print(f"++++++++++++++++++ ERROR +++++++++++++++++++++ \n+ El valor ingresado tiene que ser un número + \n+ Ingreso: {amount_of_students}              +")
        time.sleep(7)
        input_students(student_list)
        return #! Restarts section due to error

    student_info(amount_of_students, students) #Goes to save info

def student_info(amount_of_students, student_list):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("++++++++++++++++++++++++++++++++++++++++++++++ \n+++++++++++ Control de estudiantes +++++++++++ \n++++++++++++++++++++++++++++++++++++++++++++++ \n++++++++++                          ++++++++++ \n+++         Ingreso de información         +++")
    student_list=Student_list()

    for i in range(amount_of_students):
        print(f"\n+++ Estudiante #{i+1}")
        st_name=input("+ Nombre y apellidos: ")
        st_class=input("+ Sección (ej. 11B):")

        print("+")
        null_grade=-1 #Placeholder grade, makes it able to input an actual grade

        spanish_grade=student_grades(null_grade, "Español")
        english_grade=student_grades(null_grade, "Ingles")
        social_studies_grade=student_grades(null_grade, "Estudios sociales")
        science_grade=student_grades(null_grade, "Ciencias")

        general_average=(spanish_grade+english_grade+social_studies_grade+science_grade)/4

        one_student= Student(st_name, st_class, spanish_grade, english_grade, social_studies_grade, science_grade, general_average)

        student_list.get_student(one_student)

    print("\n+ La información esta guardada! \n \n++ Para guardar la información permanentemente \n en el registro de estudiantes use la opción 6 \n en el menú principal")


    time.sleep(10)
    menu.go_back_menu(student_list)

def student_grades(grade, class_of_grade):
    while grade<0 or grade>100:
        try:
            grade=int(input(f"\n+ Nota total de {class_of_grade}:"))

            if grade<0 or grade>100:
                raise ValueError()
        except ValueError:
            print("+++++++++++++++++++ ERROR ++++++++++++++++++++ \n+    El valor ingresado tiene que ser un     + \n+	   número entre 0 y 100              + \n+            Ingreso: {grade}                + \n+        Ingrese el valor correcto           + \n++++++++++++++++++++++++++++++++++++++++++++++")

    return grade


## Action of viewing student grades
def view_student_info(student_list):
    exit_info="" #Is what makes it possible to get out of the information screen

    while exit_info!="q":#Since exit info isn't q, makes it possible for the user to choose when to quit the screen :p
        os.system('cls' if os.name == 'nt' else 'clear')

        print("++++++++++++++++++++++++++++++++++++++++++++++ \n+++++++++++ Control de estudiantes +++++++++++ \n++++++++++++++++++++++++++++++++++++++++++++++ \n++++++++++                          ++++++++++ \n+++        Registro de estudiantes         +++")

        data.print_full_data(student_list)

        print("\n++ para salir presione q ")
        exit_info=input("+ ")

    menu.go_back_menu(student_list)



## Actions to view the top 3 students
def top_three_students(student_list):
    exit_info="" #Is what makes it possible to get out of the information screen

    students_average, students_names, students_class= data.read_student_averages(student_list)
    students_ammount=int(len(students_average))
    student_number=0


    while exit_info!="q":#Since exit info isn't q, makes it possible for the user to choose when to quit the screen :p
        os.system('cls' if os.name == 'nt' else 'clear')
        print("++++++++++++++++++++++++++++++++++++++++++++++ \n+++++++++++ Control de estudiantes +++++++++++ \n++++++++++++++++++++++++++++++++++++++++++++++ \n++++++++++                          ++++++++++ \n+++            Top 3 Promedios             +++")

        if students_ammount>=3:
            print(f"\n+ #1. \n   Estudiante: {students_names[0]} \n   Clase: {students_class[0]}\n   Promedio: {students_average[0]}")
            print(f"+ #2. \n   Estudiante: {students_names[1]} \n   Clase: {students_class[1]}\n   Promedio: {students_average[1]}")
            print(f"+ #3. \n   Estudiante: {students_names[2]} \n   Clase: {students_class[2]}\n   Promedio: {students_average[2]}")
        else:
            for index in range(0, len(students_average)):
                student_number+=1
                print(f"\n+ #{student_number}. \n   Estudiante: {students_names[index]} \n   Clase: {students_class[index]}\n   Promedio: {students_average[index]}")

        print("\n++ para salir presione q ")
        exit_info=input("+ ")

    menu.go_back_menu(student_list)


## Actions to see only the averages
def view_averages(student_list):
    exit_info="" #Is what makes it possible to get out of the information screen

    students_average, students_names, students_class= data.read_student_averages(student_list)

    while exit_info!="q":#Since exit info isn't q, makes it possible for the user to choose when to quit the screen :p
        student_number=0
        os.system('cls' if os.name == 'nt' else 'clear')
        print("++++++++++++++++++++++++++++++++++++++++++++++ \n+++++++++++ Control de estudiantes +++++++++++ \n++++++++++++++++++++++++++++++++++++++++++++++ \n++++++++++                          ++++++++++ \n+++          Promedios Generales           +++")

        for index in range(0, len(students_class)):
            student_number+=1
            print(f"\n+ #{student_number}. \n   Estudiante: {students_names[index]} \n   Clase: {students_class[index]}\n   Promedio: {students_average[index]}")

        print("\n++ para salir presione q ")
        exit_info=input("+ ")
        
    menu.go_back_menu(student_list)


## Actions to import student data
def import_students(student_list):
    os.system('cls' if os.name == 'nt' else 'clear')
    file_exists=data.existing_student_data()
    if file_exists==None: #If it doesn't exist
        print("+++++++++++++++++++ ERROR ++++++++++++++++++++ \n+                                            + \n+               No existe un                 + \n+       registro previo de estudiantes.      + \n+                                            + \n+  Primero registre y guarde la información  + \n+  de los estudiantes para poder importarla  + \n+                                            + \n++++++++++++++++++++++++++++++++++++++++++++++")
        time.sleep(10)
        menu.go_back_menu(student_list)
    else:
        print("+     +      +ADVERTENCIA+             +     + \n \n++ Al usar información previa, cualquier dato \n ingresado en esta sesión, SIN guardar se va a \n perder para siempre. \n+ La información importada se va a utilizar \n para todos los procesos a menos que ingrese \n nueva información desde la opción 1 del menú")
        print("++ ¿Esta segur@ que quiere continuar? (S/N)")
        import_info=input("+ ").lower()

        try:
            if import_info=="si" or import_info=="s" or import_info=="sí": #Imports the students
                students=data.import_data()
                print("\n+ Se importo la información de los estudiantes \n	       correctamente!")
                time.sleep(7)
                menu.go_back_menu(student_list)

            elif import_info=="no" or import_info=="n": #Cancels operation
                menu.go_back_menu(student_list)
            else:
                raise ValueError()
        except ValueError as error: #Restarts operation
            print(f"\n+++++++++++++++++++ ERROR ++++++++++++++++++++ \n+    La opción ingresada no es Sí o No       + \n+            Ingreso: {import_info}                + \n+        Ingrese una opción valida           + \n++++++++++++++++++++++++++++++++++++++++++++++ \n+ (si desea salir del programa escoja que no)")
            time.sleep(5)
            import_students(student_list)
            return
