from pathlib import Path 
import csv

def read_student_data():
    student_data_original=Path(__file__).parent / 'student_data.csv'
    try:
        with open(student_data_original, 'r', encoding='utf-8') as file:
            student_data= csv.DictReader(file)
    except FileNotFoundError:
        student_data=None
    return student_data