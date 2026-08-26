def is_prime_number(num):
    divide=1 #* El divisor
    divisible=0 #*Cantidad de números x la que es divisible
    is_prime=True #*Si es primo o no

    while divide<num:
        
        if divisible>=3: #*Si el num tiene 3 o más divisores que den enteros NO es primo
            is_prime=False
            break #* Se sale del ciclo
        
        elif num%divide==0: #*El residuo de dividir a num con el divisor
            divisible+=1

        divide+=1
    
    return is_prime


def organize_list(epic_list):
    prime_numbers=[] #*La lista de numeros primos

    for num in epic_list:
        
        prime=is_prime_number(num)

        if prime==True:
            prime_numbers.append(num) #*Añade splo los primos

    print(f"Lista: {epic_list}; sus números primos: {prime_numbers}")




list1=[1, 5, 98, 46, 71, 16, 85, 83, 23, 65, 89]
organize_list(list1)