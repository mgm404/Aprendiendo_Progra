import data
import time
import os


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
    #blablablablabla
    for i in amount_of_students:
        i #TODO Codigo al chile
