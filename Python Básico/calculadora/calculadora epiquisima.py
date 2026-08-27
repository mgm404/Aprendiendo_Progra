import os
import time

#### ** LOS PROCESOS MATEMÁTICOS

def sum_nums(num1, select, calculated):
    calculated=True
    final_sum=0
    print(f"+++   Ingrese un número a sumar con {num1}")

    try:
        num2=int(input("+++  "))
    except ValueError as error:
        print(f"------------  ERROR ------------- \n-- El valor ingresado no cuenta como número --- \n---  DETALLES: {error} \n---  Reiniciando la calculadora")
        time.sleep(5)
        errase_result(select, final_sum)
        main(calculated, final_sum, select)

    final_sum=num1+num2
    return final_sum

def subtract_num(num1, select, calculated):
    calculated=True
    final_subtraction=0
    print(f"+++   Ingrese la cantidad a restar de {num1}")
    
    try:
        num2=int(input("+++  "))
    except ValueError as error:
        print(f"------------  ERROR ------------- \n-- El valor ingresado no cuenta como número --- \n---  DETALLES: {error} \n---  Reiniciando la calculadora")
        time.sleep(5)
        errase_result(select, final_subtraction)
        main(calculated, final_subtraction, select)

    final_subtraction=num1-num2

    return final_subtraction

def mult_nums(num1, select, calculated):
    calculated=True
    final_mult=0
    print(f"+++   Ingrese el número a multiplicar con {num1}")

    try:
        num2=int(input("+++  "))
    except ValueError as error:
        print(f"------------  ERROR ------------- \n-- El valor ingresado no cuenta como número --- \n---  DETALLES: {error} \n---  Reiniciando la calculadora")
        time.sleep(5)
        errase_result(select, final_mult)
        main(calculated, final_mult, select)
    
    final_mult=num1*num2
    return final_mult

def divide_nums(num1, select, calculated):
    calculated=True
    final_div=0
    print(f"+++   Ingrese el divisor de {num1}")

    try:
        num2=int(input("+++  "))

        if num2 ==0:
            raise ZeroDivisionError()
    except ValueError as error:
        print(f"---  ERROR --- \n-- El valor ingresado no cuenta como número --- \n---  DETALLES: {error} \n---  Reiniciando la calculadora")
        time.sleep(5)
        errase_result(select, final_div)
        main(calculated, final_div, select)
    except ZeroDivisionError as err:
        print(f"---  ERROR --- \n---  DETALLES: No se puede dividir por 0, ingreso: {num2} \n---  Reiniciando la calculadora")
        time.sleep(5)
        errase_result(select, final_div)
        main(calculated, final_div, select)
    
    final_div=num1/num2
    return final_div

def errase_result(select, result):
    result= 10
    select= 0
    os.system('cls' if os.name == 'nt' else 'clear') #** Borra la terminal cuando se inicia
    return result, select


### ** LOS PROCESOS DE SELECCIÓN
def process_selection(select, calculated, result):
    match select:
                case 1:
                    result=sum_nums(result, select, calculated)
                    print(f"+++   Su suma da: {result}")
                    reselect(select, result, calculated)
                case 2:
                    result=subtract_num(result, select, calculated)
                    print(f"+++   Su resta da: {result}")
                    reselect(select, result, calculated)
                case 3:
                    result=mult_nums(result, select, calculated)
                    print(f"+++   Su multiplicación da: {result}")
                    reselect(select, result, calculated)
                case 4:
                    result=divide_nums(result, select, calculated)
                    print(f"+++   Su división da: {result}")
                    reselect(select, result, calculated)
                case 5:
                    errase_result(select, result)
                    calculated=False
                    main(calculated, result, select)
                case _:
                    print("--- ERROR --- \n-- El número escogido no existe entre las opciones de la calculadora --- \n--- Devolviendo al menú principal")
                    time.sleep(5)
                    errase_result(select, result)
                    main(calculated, result, select)


def reselect(select, result, calculated):  #En esta no se cambian valores de select ni result
    print("+++   ¿Quiere realizar otro calculo?")
    re_do=input("+++   (S/N): ").lower()
    try:
        if re_do=="si" or re_do=="s" or re_do=="sí":
            main(calculated, result, select)
        elif re_do=="no" or re_do=="n":
            exit()
        else:
            raise ValueError()
    except ValueError as error:
        print(f"---  ERROR --- \n-- La opción escojida no es válida; el programa se reiniciará --- \n---  DETALLES: Solo se puede escojer si o no")
        errase_result(select, result)
        main(calculated, result, select)

#### LA CALC EN SÍ

def main(calculated, result, select):
    
    

    if calculated==False:
        print(f"++++++++ Bienvenido a La Calculadora ++++++++ \n+++     El número dado para sus calculos es {result}")
    else:
        print(f"+++   El número que tiene para los cálculos es {result}")
    print(f"+++     Ingrese el número de la acción a realizar: \n+++     1. Sumar \n+++     2. Restar \n+++     3. Multiplicar \n+++     4. Dividir \n+++     5. Resetear la calculadora")
    try:
        select=int(input("+++  "))
    except ValueError as error:
        print(f"------------  ERROR ------------- \n-- El valor ingresado no cuenta como número --- \n---  DETALLES: {error} \n---  Reiniciando la calculadora")
        time.sleep(5)
        errase_result(select, result)
        main(calculated, result, select)

    process_selection(select, calculated, result)




if __name__=='__main__':
    result=10
    select= 0
    calculated=False #* para saber si ya calculo o no; cambiando el texto
    main(calculated, result, select)