def reverse_str(str1):
    str1_reverse=""
    for i in range(len(str1)-1, -1, -1): #El -1 del len es para que no de error
        str1_reverse+=str1[i]
    return str1_reverse


string="Tulio Triviño de 31 minutos" 
print(string)
string2=reverse_str(string)
print(string2)