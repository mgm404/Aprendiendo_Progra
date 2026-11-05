#Cree un decorador que se encargue de revisar si todos 
#los parámetros de la función que decore son números, y arroje una excepción de no ser así.
import math
def is_num(func):
    def wrapper(*args):
        for num, arg in enumerate(args):
            if isinstance(arg, (float, int)):
                pass
            else:
                raise ValueError(
                    "Solo se permiten números"
                    )
        return func(*args)
    return wrapper


@is_num
def calculate_perimeter(radius):
    perimeter=2*math.pi*radius
    return perimeter





try:
    perimeter= calculate_perimeter(5)
    print (perimeter)
except ValueError as error:
    print(error)
