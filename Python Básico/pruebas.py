import time

start = time.time()
print(f'Start time: {start}')
time.sleep(5) #! El código solo continua después de ese tiempo (en segundos)
print("hola mundo")
print(1234567)
print(1234567789)
end = time.time()
print(f'Elapsed: {end - start:.2f} seconds')


#** Como agarrar cierta info desde un csv
#with open(student_data_original, 'r', encoding='utf-8') as file:
#    student_data= csv.DictReader(file, delimiter='\t')
#    sorted_student_data = sorted(student_data, key=operator.itemgetter('general_average'), reverse=True)
#        
#    students_names=[]
#    students_class=[]
#    students_average=[]
#        
#    for row in sorted_student_data:
#        students_names.append(row['name'])
#        students_class.append(row['student_class'])
#        students_average.append(row['general_average'])