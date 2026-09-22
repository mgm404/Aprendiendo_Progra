from pathlib import Path 
import csv
import operator
import actions

def existing_student_data():
    student_data_original=Path(__file__).parent / 'student_data.csv'
    try:
        with open(student_data_original, 'r', encoding='utf-8') as file:
            student_data= csv.DictReader(file, delimiter='\t')
    except FileNotFoundError:
        student_data=None
    return student_data

def save_student_data(student_list):
    file_exists=existing_student_data() #Confirms if it exists or not

    student_data=Path(__file__).parent / 'student_data.csv'

    students=object_to_dict(student_list)

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


def object_to_dict(student_list): #Makes the student objects into a dictionary in order to save them correctly
    student_data=[]
    
    for student in student_list.students:
        one_student={}
        one_student['name']=student.name
        one_student['student_class']=student.student_class
        
        one_student['spanish_grade']=student.spanish_grade
        one_student['english_grade']=student.english_grade
        one_student['social_studies_grade']=student.social_studies_grade
        one_student['science_grade']=student.science_grade
        one_student['general_average']=student.general_average
        
        student_data.append(one_student)
    return student_data




def print_full_data(student_list): #prints all the student information 

    student_number=0 #Used to give students a number

    for student in student_list.students:
        student_number+=1
        print(f"\n#{student_number}\n   Nombre: {student.name}\n   Clase: {student.student_class}\n   Nota de Español: {student.spanish_grade}\n   Nota de Ingles: {student.english_grade}\n   Nota de Estudios sociales: {student.social_studies_grade}\n   Nota de Ciencias: {student.science_grade}\n   Promedio: {student.general_average}")



def read_student_averages(student_list):
    student_data=student_list.students

    sorted_student_data = sorted(student_data, key=lambda x: x.general_average, reverse=True)
    #sorted(student_data, key=operator.itemgetter('general_average'), reverse=True)

    students_names=[]
    students_class=[]
    students_average=[]
        
    for student in sorted_student_data:
        students_names.append(student.name)
        students_class.append(student.student_class)
        students_average.append(student.general_average)


    return students_average, students_names, students_class


def import_data():
    student_data_original=Path(__file__).parent / 'student_data.csv'
    
    with open(student_data_original, 'r', encoding='utf-8') as file:
        student_data= csv.DictReader(file, delimiter='\t')
        imported_data=[]
        for student in student_data:
            imported_data.append(student)

    student_list=actions.Student_list()
    for student in imported_data:
            st_name=student['name']
            st_class=student['student_class']
            
            spanish_grade=student['spanish_grade']
            english_grade=student['english_grade']
            social_studies_grade=student['social_studies_grade']
            science_grade=student['science_grade']
            general_average=student['general_average']
            
            one_student= actions.Student(st_name, st_class, spanish_grade, english_grade, social_studies_grade, science_grade, general_average)
            
            student_list.get_student(one_student)

    return student_list