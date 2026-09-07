from pathlib import Path 
import csv
import operator

def read_student_data():
    student_data_original=Path(__file__).parent / 'student_data.csv'
    try:
        with open(student_data_original, 'r', encoding='utf-8') as file:
            student_data= csv.DictReader(file, delimiter='\t')
    except FileNotFoundError:
        student_data=None
    return student_data

def save_student_data(students):
    file_exists=read_student_data() #Confirma si ya existe o no 

    student_data=Path(__file__).parent / 'student_data.csv'

    if file_exists==None:
        with open(student_data, 'w', encoding='utf-8', newline='') as csvfile:
            headers = students[0].keys()

            writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter='\t') #**\t es tab

            writer.writeheader()

            writer.writerows(students)

    else:
        with open(student_data, 'a', encoding='utf-8', newline='') as csvfile:
            headers = students[0].keys()
        
            writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter='\t') #**\t es tab
        
            writer.writerows(students)



def print_full_data(): #imprime la información de todos los estudiantes
    student_data_original=Path(__file__).parent / 'student_data.csv'
    student_number=0 #Usado para enumerar los estudiantes
    with open(student_data_original, 'r', encoding='utf-8') as file:
        student_data= csv.DictReader(file, delimiter='\t')
        for student in student_data:
            student_number+=1
            print(f"\n#{student_number}\n   Nombre: {student['name']}\n   Clase: {student['student_class']}\n   Nota de Español: {student['spanish_grade']}\n   Nota de Ingles: {student['english_grade']}\n   Nota de Estudios sociales: {student['social_studies_grade']}\n   Nota de Ciencias: {student['science_grade']}\n   Promedio: {student['general_average']}")



def read_student_averages():
    student_data_original=Path(__file__).parent / 'student_data.csv'

    with open(student_data_original, 'r', encoding='utf-8') as file:
        student_data= csv.DictReader(file, delimiter='\t')
        sorted_student_data = sorted(student_data, key=operator.itemgetter('general_average'), reverse=True)
        
        students_names=[]
        students_class=[]
        students_average=[]
        
        for row in sorted_student_data:
            students_names.append(row['name'])
            students_class.append(row['student_class'])
            students_average.append(row['general_average'])

    return students_average, students_names, students_class