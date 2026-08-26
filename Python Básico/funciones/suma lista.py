def sum_list(list1):
    final_sum=0
    for num in list1:  #**Sin el +1 por alguna razón no cuenta el último número de la lista
        final_sum= final_sum+num
    return final_sum

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

final_sum=sum_list(numbers)

print(final_sum)